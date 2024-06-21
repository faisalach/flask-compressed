import os
import time
import random
from flask import Flask, request,jsonify,send_from_directory
from werkzeug.utils import secure_filename

from audio.mp3 import compress_audio_mp3
from audio.ogg import compress_audio_ogg
from gambar.webp import compress_gambar_webp
from gambar.jpeg import compress_gambar_jpeg
from video.h264 import compress_video_h264
from video.h265 import compress_video_h265

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp4', 'jpg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
