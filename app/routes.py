from app import app, render_template, request, url_for, flash, redirect, session
import os
from app.licence import detection
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = '/Users/aayush/Downloads/licence-aa'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
    error = request.args.get('error')
    return render_template("home.html",error = error)

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template("numplate.html",a = a)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f != None:
            if 'file' not in request.files:
                return redirect(url_for('home',error = 'No file part'))
            if f.filename == '':
                return redirect(url_for('home',error = "No selected file"))
            if f and allowed_file(f.filename):
                f = request.files['file']
                fname = f.filename
                f.save(secure_filename(fname))
                d = detection()
                a = d.licence_plate(fname)
                #a = licence_plate(fname)
                return render_template("numplate.html",a = a)
            else:
                return redirect(url_for('home',error = "Invalid File"))

    return redirect(url_for('home'))
