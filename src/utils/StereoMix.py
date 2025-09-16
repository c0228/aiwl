# pip install comtypes
import comtypes.client

DEVICE_STATE_ACTIVE = 0x1
DEVICE_STATEMASK_ALL = 0x0F
eCapture = 1   # recording devices

def stereo_mix_enabled() -> bool:
    # Use the canonical ProgID – just "MMDeviceEnumerator"
    enumerator = comtypes.client.CreateObject("MMDeviceEnumerator", dynamic=True)
    devices = enumerator.EnumAudioEndpoints(eCapture, DEVICE_STATEMASK_ALL)

    for i in range(devices.GetCount()):
        dev = devices.Item(i)
        if "stereo mix" in dev.FriendlyName.lower():
            return bool(dev.GetState() & DEVICE_STATE_ACTIVE)
    return False

if __name__ == "__main__":
    print("Stereo Mix is ENABLED" if stereo_mix_enabled()
          else "Stereo Mix is DISABLED")
