##############################################################################################################################
##                                                                                                                          ##
##      ------------------------------------------------                                                                    ##
##      logger.py:                                                                                                          ##
##      ------------------------------------------------                                                                    ##
##         1) It defines unique log identifiers for different application areas (HTTP/server and speech-to-text) and maps   ##
##            them to log file paths inside the project’s logs directory, using the current APP_ID.                         ##
##         2) The log_message function appends a timestamped message to the appropriate log file, creating the file if it   ##
##            does not yet exist.                                                                                           ##
##         3) This allows other parts of the application to record events and debug information in a consistent,            ##
##            centralized manner.                                                                                           ##
##                                                                                                                          ##
##############################################################################################################################

from datetime import datetime # Imports the datetime class so you can get the current date/time for timestamps.
import threading  # you create and control threads—independent lines of execution inside a single Python process.   
import os # general OS utilities (checking/removing files).
from src.settings.constants import PROJECT_ROOT, APP_ID

HTTP_LOG_ID = "httpId"
STT_LOG_ID = "sttId"

LOG_FILES = {
  HTTP_LOG_ID: os.path.join( PROJECT_ROOT / "logs" / f"{APP_ID}-server.log" ),
  STT_LOG_ID: os.path.join( PROJECT_ROOT / "logs" / f"{APP_ID}-stt.log" )
}

# ---------- Thread-safe utility logging ----------
_log_lock = threading.Lock()                # <-- NEW: global lock

# ---------------- Utility Logging ----------------
def log_message(logId: str, message: str):
    """Append a message to the chosen log file with a timestamp."""
    logPath = LOG_FILES[logId]

    # Make sure parent directory exists
    os.makedirs(logPath.parent, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}\n"

    # Only one thread at a time can write
    with _log_lock:
        with open(logPath, "a", encoding="utf-8") as f:
            f.write(line)