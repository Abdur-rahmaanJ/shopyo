from typing import Any
import os
import json

from flask import Flask
from shopyo_base.view import module_blueprint

__version__ = "1.1.0"


info = {}
with open(os.path.dirname(os.path.abspath(__file__)) + os.sep + "info.json") as f:
    info = json.load(f)


class ShopyoBase:
    def __init__(self, app: Any = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions["shopyo_base"] = self
        bp = module_blueprint
        app.register_blueprint(bp)

    def get_info(self):
        return info
