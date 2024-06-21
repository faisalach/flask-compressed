import os
import time
import random
from flask import Flask, request,jsonify,send_from_directory
from werkzeug.utils import secure_filename

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
