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

from src.settings.constants import APP_ID, APP_NAME, APP_VERSION, PROJECT_ROOT, CONTROLLER_ROOT, RPI_ROOT
from src.utils.logger import HTTP_LOG_ID, STT_LOG_ID, LOG_FILES

# Initializes colorama so Windows & Unix terminals handle color codes.
# autoreset=True means you don’t need to manually reset the color each time.
init(autoreset=True)

# Scripts & PID files for HTTP Web Server and Speech Listener Servers
DASHBOARD_PATH = CONTROLLER_ROOT / "DashboardController.py"
PID_FILE = RPI_ROOT / f"{APP_ID}-server.pid"

SPEECH_PATH = CONTROLLER_ROOT / "AppMeetingListener.py"
SPEECH_PID_FILE = RPI_ROOT / f"{APP_ID}-speech.pid"

# ---------------- Command Definition ----------------
# Prints a simple CLI help message with colored separators and usage instructions.
def definition():
    print("==============")
    print("Command Usage:")
    print("==============")
    print(f"{APP_ID} --version              : To view the App Version")
    print(f"{APP_ID} automate --start       : Start {APP_NAME} Server & Speech Listener")
    print(f"{APP_ID} automate --stop        : Stop {APP_NAME} Server & Speech Listener")

# ---------------- Generic Process Stop ----------------
def stop_process(pid_file, name):

    # If the PID file doesn’t exist, assumes the process isn’t running.
    if not os.path.exists(pid_file):
        print(Fore.YELLOW + f"No running {name} found (no PID file).")
        return
    
    # Reads the stored PID.
    with open(pid_file, "r") as f:
        pid_str = f.read().strip()
    
    # Sanity check: PID must be numeric; cleans up if not.
    if not pid_str.isdigit():
        print(Fore.RED + f"Invalid PID in {name} PID file. Cleaning up.")
        os.remove(pid_file)
        return

    # If PID exists, tries to terminate gracefully, waits up to 5 s.
    # Reports if already dead.
    pid = int(pid_str)
    if psutil.pid_exists(pid):
        try:
            p = psutil.Process(pid)
            p.terminate()       # send terminate signal
            p.wait(timeout=5)   # wait until process exits
            print(Fore.RED + f"{name} with PID {pid} stopped.")
        except Exception as e:
            print(Fore.RED + f"Could not stop {name}: {e}")
    else:
        print(Fore.YELLOW + f"{name} PID {pid} not found. Already stopped.")
    
    # Finally removes the stale PID file.
    if os.path.exists(pid_file):
        os.remove(pid_file)

# ---------------- Start Server ----------------
def start_server():
    # ---- HTTP Server -----
    # If no PID file, launches the HTTP Server dashboard:
    if os.path.exists(PID_FILE):
        print(Fore.GREEN + f"{APP_NAME} Server already running. Stop it first with `{APP_ID} automate --stop`.")
    else:
        with open(LOG_FILES[HTTP_LOG_ID], "a") as log_file:
            # subprocess.Popen runs it detached so it survives terminal close.
            # Stdout/stderr redirected to the HTTP log.
            # Records the child PID in a file for future stopping.
            process = subprocess.Popen(
                ["python", str(DASHBOARD_PATH)],
                stdout=log_file,
                stderr=subprocess.STDOUT,
                creationflags=subprocess.DETACHED_PROCESS
            )
            with open(PID_FILE, "w") as f:
                f.write(str(process.pid))
            print(Fore.GREEN + f"{APP_NAME} Server started with PID {process.pid} at http://localhost:5999")

    # ---- Speech Listener ----
    if os.path.exists(SPEECH_PID_FILE):
        print(Fore.GREEN + f"SpeechListener already running. Stop it first with `{APP_ID} automate --stop`.")
    else:
        # Clear previous speech log
        with open(LOG_FILES[STT_LOG_ID], "a") as log_file:
            # subprocess.Popen runs it detached so it survives terminal close.
            # Stdout/stderr redirected to the HTTP log.
            # Records the child PID in a file for future stopping.
            process_speech = subprocess.Popen(
                ["python", str(SPEECH_PATH)],
                stdout=log_file,
                stderr=subprocess.STDOUT,
                creationflags=subprocess.DETACHED_PROCESS
            )
            with open(SPEECH_PID_FILE, "w") as f:
                f.write(str(process_speech.pid))
            print(Fore.GREEN + f"Speech Recognition started in background with PID {process_speech.pid}")

    print(Fore.CYAN + "You can safely close the terminal. Both processes run in the background.")

# ---------------- Stop Server ----------------
def stop_server():
    # Simply calls the generic stopper for each service.
    stop_process(PID_FILE, f"{APP_NAME} Server")
    stop_process(SPEECH_PID_FILE, "SpeechListener")

# ---------------- Command Dispatcher ----------------
def commands():
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print( APP_VERSION )
    elif len(sys.argv) > 2 and sys.argv[1] == "automate" and sys.argv[2] == "--start":
        start_server()
    elif len(sys.argv) > 2 and sys.argv[1] == "automate" and sys.argv[2] == "--stop":
        stop_server()
    else:
        definition()

# ---------------- Main ----------------
if __name__ == "__main__":
    # run commands() only when executed directly, not when imported.
    commands()
