import os
import time
import random
from flask import Flask, request,jsonify,send_from_directory
from werkzeug.utils import secure_filename
#from pydub import AudioSegment

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
    return "<p>Hello, World dedede!</p>"

@app.route("/download_file/<filename>")
def download_file(filename):
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(full_path, filename)