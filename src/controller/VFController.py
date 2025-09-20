from flask import Blueprint, Flask, request, send_from_directory, render_template, jsonify
from src.utils.logger import log_message, HTTP_LOG_ID
from src.utils.VFUtils import convert_webm_to_mp4, convert_mp4_to_wav
import os
import uuid

vf_bp = Blueprint("vf", __name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@vf_bp.route("/auth/footage-reference")
def footageReference():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return render_template("auth-ref-footage.html")

@vf_bp.route("/vf/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    # Save temporary WebM
    temp_webm = f"{uuid.uuid4()}.webm"
    temp_webm_path = os.path.join(UPLOAD_FOLDER, temp_webm)
    file.save(temp_webm_path)

    # Convert WebM → MP4
    mp4_filename = f"{uuid.uuid4()}.mp4"
    mp4_path = os.path.join(UPLOAD_FOLDER, mp4_filename)
    convert_webm_to_mp4(temp_webm_path, mp4_path)

    # Convert MP4 → WAV
    wav_filename = f"{uuid.uuid4()}.wav"
    wav_path = os.path.join(UPLOAD_FOLDER, wav_filename)
    convert_mp4_to_wav(mp4_path, wav_path)

    # Remove temporary WebM
    os.remove(temp_webm_path)

    # Return filenames to frontend
    return jsonify({
        "message": "Upload successful",
        "mp4_file": mp4_filename,
        "wav_file": wav_filename
    }), 200

@vf_bp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)