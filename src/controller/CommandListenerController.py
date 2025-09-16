from flask import Blueprint, jsonify
from src.utils.logger import log_message, HTTP_LOG_ID
from src.routes.CommandRoutes import start_server, stop_server

commandListener_bp = Blueprint("commandListener", __name__)

@commandListener_bp.route("/command/listen/start", methods=["POST", "GET"])
def command_listen_start():
    try:
        started = start_server()
        msg = f"Speech listener started in background" if started else "Speech listener already running"
        log_message(HTTP_LOG_ID, msg)
        return jsonify({"status": msg})
    except Exception as e:
        log_message(HTTP_LOG_ID, f"Failed to start listener: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@commandListener_bp.route("/command/listen/stop", methods=["POST", "GET"])
def command_listen_stop():
    try:
        stopped = stop_server()
        msg = "Stopped speech listener" if stopped else "Nothing to stop"
        log_message(HTTP_LOG_ID, msg)
        return jsonify({"status": msg})
    except Exception as e:
        log_message(HTTP_LOG_ID, f"Failed to stop listener: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500