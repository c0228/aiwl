import os, time # general OS utilities (checking/removing files).
from flask import Flask
from waitress import serve
from src.settings.constants import PROJECT_ROOT
from src.controller.DashboardController import dashboard_bp
from src.controller.CommandListenerController import commandListener_bp
from src.controller.VFController import vf_bp

app = Flask(__name__,
            template_folder=os.path.join(PROJECT_ROOT, "templates"),
            static_folder=os.path.join(PROJECT_ROOT, "static"))

# register blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(commandListener_bp)
app.register_blueprint(vf_bp)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5999)
