##############################################################################################################################
##                                                                                                                          ##
##      ------------------------------------------------                                                                    ##
##      constants.py:                                                                                                       ##
##      ------------------------------------------------                                                                    ##
##        Centralized module for defining and managing all project-wide constant values (paths, IDs, configuration          ##
##        settings) used throughout the application.                                                                        ##                ##
##                                                                                                                          ##
##############################################################################################################################

import os # general OS utilities (checking/removing files).
from pathlib import Path # convenient, cross-platform path handling.

APP_ID = "iwlab"
APP_NAME = "IWLab"
APP_VERSION = "1.0.0"

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PYCACHE_DIR = PROJECT_ROOT / "__pycache__"
ROUTE_ROOT = PROJECT_ROOT / "src" / "routes"
CONTROLLER_ROOT = PROJECT_ROOT / "src" / "controller"
SERVICES_ROOT = PROJECT_ROOT / "src" / "services"
RPI_ROOT = PROJECT_ROOT / "rpi"
LOG_DIR = PROJECT_ROOT / "logs"