##############################################################################################################################
##                                                                                                                          ##
##      ------------------------------------------------                                                                    ##
##      DashboardController.py:                                                                                             ##
##      ------------------------------------------------                                                                    ##
##          1) Creates a HTTP Server based web app.                                                                         ##
##          2) Logs each visit to the root URL.                                                                             ##
##          3) Serves it through Waitress on port 5999, accessible from any machine on the network.                         ##                         ##
##                                                                                                                          ##
##############################################################################################################################

import sys # to read command-line arguments (sys.argv).
import os # general OS utilities (checking/removing files).

from src.utils.logger import HTTP_LOG_ID, log_message
from flask import Flask # a lightweight Python web framework for defining routes and handling HTTP requests.
import waitress # a production-ready WSGI server that actually serves the Flask application to the network.

# Create Flask app - Initializes a Flask application object.
# __name__ tells Flask where to look for templates, static files, etc.
app = Flask(__name__)

# Define route for homepage
# @app.route("/") maps the root URL (/) to the hello function.
# When a browser requests http://<host>:5999/, Flask runs hello().
# Inside:
#   1) Logs the visit using your logger with the HTTP log ID.
#   2) Returns a simple text response "Hello, World!".
@app.route("/")
def hello():
    log_message(HTTP_LOG_ID, "Triggered Basic Route - Hello World")
    return "Hello, World!"

# Run server
if __name__ == "__main__":
    # Bind to 0.0.0.0 so it’s accessible in browser
    waitress.serve(app, host="0.0.0.0", port=5999)
