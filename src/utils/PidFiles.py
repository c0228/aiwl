from pathlib import Path # convenient, cross-platform path handling.
from colorama import Fore, init # adds colored text to terminal output.
import psutil # process utilities (checking PIDs, terminating processes).
import sys # to read command-line arguments (sys.argv).
import subprocess # to spawn new processes (starting server/listener).
import os # general OS utilities (checking/removing files).

from src.settings.constants import APP_ID, APP_NAME, APP_VERSION, PROJECT_ROOT, ROUTE_ROOT, CONTROLLER_ROOT, RPI_ROOT
from src.utils.logger import HTTP_LOG_ID, STT_LOG_ID, LOG_FILES

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
