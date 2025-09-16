#################################################################################################################################
##                                                                                                                             ##
##   ----------------------------                                                                                              ##
##   main.py :                                                                                                                 ##
##   ----------------------------                                                                                              ##
##       1. Starts and stops two background processes (Dashboard Service & Speech listener Service).                           ##
##       2. Manages PID files for safe termination.                                                                            ##
##       3. Handles logs, sends output to rotating log files.                                                                  ##
##       4. Provides colored CLI feedback and a simple help message.                                                           ##
##                                                                                                                             ##
#################################################################################################################################

from pathlib import Path # convenient, cross-platform path handling.
from colorama import Fore, init # adds colored text to terminal output.
import psutil # process utilities (checking PIDs, terminating processes).
import sys # to read command-line arguments (sys.argv).
import subprocess # to spawn new processes (starting server/listener).
import os # general OS utilities (checking/removing files).

from src.utils.PidFiles import stop_process
from src.settings.constants import APP_ID, SERVICES_ROOT, RPI_ROOT
from src.utils.logger import HTTP_LOG_ID, STT_LOG_ID, LOG_FILES, log_message

# Initializes colorama so Windows & Unix terminals handle color codes.
# autoreset=True means you don’t need to manually reset the color each time.
init(autoreset=True)

# Scripts & PID files for Speech Listener Servers
SPEECH_PATH = SERVICES_ROOT / "CommandListenerService.py"
SPEECH_PID_FILE = RPI_ROOT / f"{APP_ID}-speech.pid"

# ---------------- Start Server ----------------
def start_server():
    # ---- Speech Listener ----
    if os.path.exists(SPEECH_PID_FILE):
        log_message( HTTP_LOG_ID, f"SpeechListener already running. Stop it first with `{APP_ID} automate --stop`.")
        return False  # Already running
    else:
        try:
            log_message(STT_LOG_ID, '------------- Started Speech Listener ----------------')
            # Clear previous speech log
            with open(LOG_FILES[STT_LOG_ID], "a") as log_file:
                # subprocess.Popen runs it detached so it survives terminal close.
                # Stdout/stderr redirected to the HTTP log.
                # Records the child PID in a file for future stopping.
                process_speech = subprocess.Popen(
                    [sys.executable, str(SPEECH_PATH)],
                    stdout=log_file,
                    stderr=subprocess.STDOUT,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP  # better for Windows
                )
                with open(SPEECH_PID_FILE, "w") as f:
                    f.write(str(process_speech.pid))
                log_message( HTTP_LOG_ID, f"Speech Recognition started in background with PID {process_speech.pid}")
                return True
        except Exception as e:
                return False

# ---------------- Stop Server ----------------
def stop_server():
    # Simply calls the generic stopper for each service.
    if os.path.exists(SPEECH_PID_FILE):
        stop_process(SPEECH_PID_FILE, "SpeechListener")
        log_message(STT_LOG_ID, '------------- Stopped Speech Listener ----------------')
        return True
    log_message(STT_LOG_ID, 'No Speech Listener is available to Stop')
    return False