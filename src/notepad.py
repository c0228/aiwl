from pywinauto import Application, keyboard
import time

def open_run_dialog():
    """Opens the Windows Run dialog (Win + R)."""
    keyboard.send_keys("{VK_LWIN down}r{VK_LWIN up}")
    time.sleep(1)  # small delay for Run dialog

def launch_application(app_name, char_delay=0.1):
    """Launches an application via Run dialog with optional typing delay."""
    for char in app_name:
        keyboard.send_keys(char)
        time.sleep(char_delay)
    keyboard.send_keys("{ENTER}")

def wait_for_window(title_regex, timeout=10, interval=1.4, backend="win32"):
    """Waits until a window matching the title regex exists."""
    elapsed = 0
    dlg = None
    while elapsed < timeout:
        try:
            app = Application(backend=backend).connect(title_re=title_regex)
            dlg = app.window(title_re=title_regex)
            if dlg.exists():
                return dlg
        except Exception:
            pass
        time.sleep(interval)
        elapsed += interval
    raise Exception(f"Window with title '{title_regex}' not found!")

def type_text(dlg, text, key_delay=0.1):
    """Types text into the given window/dialog with optional key delay."""
    for char in text:
        dlg.type_keys(char, with_spaces=True)
        time.sleep(key_delay)

def main():
    open_run_dialog()
    launch_application("notepad", char_delay=0.1)
    dlg = wait_for_window(".*Notepad", timeout=10)
    dlg.wait("visible enabled ready", timeout=10)
    type_text(dlg, "Hello, I am assistant!", key_delay=0.1)
    print("Text typed successfully!")

if __name__ == "__main__":
    main()
