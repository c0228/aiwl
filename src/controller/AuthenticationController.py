from flask import Blueprint, render_template
from src.utils.Logger import log_message, HTTP_LOG_ID

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth/init")
def authenticate():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return render_template("auth-manage-init.html")

@auth_bp.route("/auth/profiles/manage")
def manageProfile():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return render_template("auth-profile-manage.html")

@auth_bp.route("/auth/profile/create")
def createProfile():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return render_template("auth-profile-create.html")

@auth_bp.route("/auth/manage/footage")
def manageFootage():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return render_template("auth-manage-footage.html")