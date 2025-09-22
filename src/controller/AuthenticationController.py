from flask import Blueprint, request, jsonify, render_template
from src.utils.Logger import log_message, HTTP_LOG_ID

auth_bp = Blueprint("auth", __name__)

# ------------------ SCREEN #1 --------------------------------------
@auth_bp.route("/auth/init")
def authenticate():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return render_template("auth-manage-init.html")

@auth_bp.route("/auth/create-account", methods=['POST'])
def createAccount():
    # Get data from POST request
    data = request.get_json()  # expects JSON body
    name = data.get('name')
    country = data.get('country')
    state = data.get('state')
    mobile = data.get("mobile")

    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")

    #  Create an Account at [data/account.enc.iwl]

    # Add this Account at [PHP/Apache Server]
    #   - Credentials - pick from Environmental Variables

    result = {
        "message": f"Created Account Successfully",
        "data": {
            "name" : name,
            "country" : country,
            "state" : state,
            "mobile": mobile
        }
    }
    return jsonify(result), 200   # Return JSON with status code 200

@auth_bp.route("/auth/login-account", methods=['POST'])
def loginAccount():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return jsonify({}), 200   # Return JSON with status code 200

@auth_bp.route("/auth/export-account", methods=['POST'])
def exportAccount():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return jsonify({}), 200   # Return JSON with status code 200
# -----------------------------------------------------------------

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