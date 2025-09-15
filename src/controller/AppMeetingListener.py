##############################################################################################################################
##                                                                                                                          ##
##      ------------------------------------------------                                                                    ##
##      AppMeetingListener.py:                                                                                              ##
##      ------------------------------------------------                                                                    ##
##          1) Captures live audio from a system or microphone.                                                             ##
##          2) Queues audio frames from the sounddevice callback.                                                           ##
##          3) Feeds them to Vosk for real-time transcription.                                                              ##
##          4) Logs recognized text through your own log_message system.                                                    ##
##                                                                                                                          ##
##############################################################################################################################

import sys # to read command-line arguments (sys.argv).
import os # general OS utilities (checking/removing files).
import queue # a thread-safe queue to move audio data from the sound callback to the recognizer loop.
import threading # you create and control threads—independent lines of execution inside a single Python process.
import sounddevice as sd # records live audio from any input device.
import vosk # offline speech-to-text engine.
import json # parse recognizer output.
import numpy as np # audio arrays from sounddevice.
from src.utils.logger import STT_LOG_ID, log_message # Our own helper to write logs (tagged with STT_LOG_ID).


class AppMeetingListener:
    # Holds all logic for capturing audio and recognizing speech.
    # model_path – folder containing the Vosk model files.
    # sample_rate – audio sampling rate (16 kHz is standard for speech)
    # self.q – a queue.Queue() for passing audio chunks from the audio callback to the recognizer.
    def __init__(self, model_path, sample_rate=16000):
        self.model_path = model_path
        self.sample_rate = sample_rate
        self.q = queue.Queue()

        try:
            # Loads the acoustic/language model.
            self.model = vosk.Model(model_path)
        except Exception as e:
            # Throws a descriptive error if the model folder is missing or corrupt.
            raise RuntimeError(f"❌ Could not load Vosk model from {model_path}: {e}")

        # Creates a Kaldi-based recognizer that will accept audio frames and output text.
        self.recognizer = vosk.KaldiRecognizer(self.model, self.sample_rate)

    # This is automatically called by sounddevice.InputStream whenever a new block of audio arrives.
    def _callback(self, indata, frames, time, status):
        """Collect audio data in a queue (force mono if multi-channel)"""
        if status:
            # Logs any driver/stream status messages.
            log_message(STT_LOG_ID, f" Status: {status}")
        # Ensures mono audio (speech recognizer expects 1 channel).
        # Take only the first channel
        if indata.ndim > 1:
            indata = indata[:, 0]
        # Places raw bytes of audio into the queue for the recognizer loop.
        self.q.put(bytes(indata))

    # -------------------------------------
    # _recognize_loop runs forever:
    # -------------------------------------
    #   1. Pulls audio chunks from the queue.
    #   2. Feeds them to the recognizer.
    #   3. When Vosk thinks it has a complete utterance (AcceptWaveform returns True), it parses 
    #       the JSON and logs the recognized text.
    def _recognize_loop(self):
        """Internal recognition loop"""
        while True:
            data = self.q.get()
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get("text")
                if text:
                    log_message(STT_LOG_ID, f" Recognized:"+ str(text))

    # ------------------------------------
    # list_input_devices:
    # ------------------------------------
    #   1) Uses sd.query_devices() to find all available audio input devices (microphones, virtual 
    #       cables, stereo mix, etc.).
    #   2) Returns a list of dictionaries with id, name, and channels.
    def list_input_devices(self):
        """List all input devices with at least 1 input channel"""
        devices = sd.query_devices()
        input_devices = []
        for idx, dev in enumerate(devices):
            if dev["max_input_channels"] > 0:
                input_devices.append({
                    "id": idx,
                    "name": dev["name"],
                    "channels": dev["max_input_channels"]
                })
        return input_devices

    # ------------------------------------------
    # auto_select_stereo_mix:
    # ------------------------------------------
    #   1) Searches that list for a device whose name contains “stereo mix” (case-insensitive).
    #   2) Logs and returns its device ID if found, else returns None.
    #   3) Stereo Mix is a Windows feature that captures system audio—perfect for meeting transcription.
    def auto_select_stereo_mix(self):
        """Try to find Stereo Mix automatically"""
        devices = self.list_input_devices()
        for d in devices:
            if "stereo mix" in d["name"].lower():
                log_message(STT_LOG_ID, f"Auto-selected Stereo Mix: {d['name']} (id: {d['id']})")
                return d["id"]
        # If not found, return None
        return None

    def listen_from_device(self, device_id):
        """Listen from a chosen input device"""
        try:
            device_info = sd.query_devices(device_id)
            # Checks the chosen device and forces it to 1 channel.
            channels = min(device_info["max_input_channels"], 1)  # Force mono
            if channels < 1:
                raise RuntimeError(f"Device {device_id} does not have input channels.")

            log_message(STT_LOG_ID, f" Listening to device {device_id} ({device_info['name']}) with {channels} channel(s)")

            # Opens a live input stream:
            #   1) 16 kHz sample rate.
            #   2) blocksize=8000 means it hands over roughly 0.5 s chunks at a time.
            #   3) dtype="int16" keeps it compatible with Vosk.
            #   4) Calls _callback each time audio arrives.
            # While the stream is open, _recognize_loop() continuously processes and logs text.
            with sd.InputStream(
                samplerate=self.sample_rate,
                blocksize=8000,
                device=device_id,
                channels=channels,
                dtype="int16",
                latency="low",
                callback=self._callback
            ):
                self._recognize_loop()

        except Exception as e:
            # Graceful error handling if the stream can’t open.
            log_message(STT_LOG_ID, f" Could not start listening: {e}")


if __name__ == "__main__":
    # When run directly, creates a listener using a specific Vosk model folder.
    listener = AppMeetingListener("model/vosk-model-small-en-us-0.15")

    # Try auto-select Stereo Mix
    # First tries to grab “Stereo Mix” automatically for system-wide audio.
    stereo_mix_id = listener.auto_select_stereo_mix()
    if stereo_mix_id is not None:
        listener.listen_from_device(stereo_mix_id)
    else:
        # If Stereo Mix not found, list devices and let user choose
        # Prompts the user to type the numeric device ID.
        # Starts listening on the chosen device.
        devices = listener.list_input_devices()
        log_message(STT_LOG_ID, f" Available devices to capture meeting audio:")
        for d in devices:
            log_message(STT_LOG_ID, f"   [{d['id']}] {d['name']} (channels: {d['channels']})")
        choice = int(input("👉 Enter the device ID to capture meeting audio from: "))
        listener.listen_from_device(choice)
