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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file(request):
    if 'file' not in request.files:
        return {
            'status' : 200,
            'error' : "No file part"
        }

    file = request.files['file']
    if file.filename == '':
        return {
            'status' : 200,
            'error' : "No selected file"
        }
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        split   = filename.split('.')
        extension   = split[-1]
        
        new_filename = "uploads_"+str(time.time())+str(random.random())+"."+extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
        path = "./uploads/"+new_filename
        return path

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/download_file/<filename>")
def download_file(filename):
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(full_path, filename)

@app.route("/api/audio/mp3",methods=['POST'])
def audio_mp3():
    path    = validate_file(request)
    result  = compress_audio_mp3(path)
    return jsonify(result)

@app.route("/api/audio/ogg",methods=['POST'])
def audio_ogg():
    path    = validate_file(request)
    result  = compress_audio_ogg(path)
    return jsonify(result)

@app.route("/api/gambar/webp",methods=['POST'])
def gambar_webp():
    path    = validate_file(request)
    result  = compress_gambar_webp(path)
    return jsonify(result)

@app.route("/api/gambar/jpeg",methods=['POST'])
def gambar_jpeg():
    path    = validate_file(request)
    result  = compress_gambar_jpeg(path)
    return jsonify(result)

@app.route("/api/video/h264",methods=['POST'])
def video_h264():
    path    = validate_file(request)
    result  = compress_video_h264(path)
    return jsonify(result)

@app.route("/api/video/h265",methods=['POST'])
def video_h265():
    path    = validate_file(request)
    result  = compress_video_h265(path)
    return jsonify(result)
        