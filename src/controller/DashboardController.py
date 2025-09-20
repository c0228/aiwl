from flask import Blueprint, render_template
from src.utils.logger import log_message, HTTP_LOG_ID

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def hello():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return "Hello, World!"

@dashboard_bp.route("/auth/init")
def authenticate():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return render_template("auth-reg-login.html")

@dashboard_bp.route("/index")
def index():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Index")
    return render_template("index.html")
