import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/uploads"
ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename) :
	return "." in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def root_path() :
	return "Something else will come here"

@app.route("/upload_file")
def upload_a_new_file() :
	return render_template("upload.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file() :
	if request.method == "POST" :
		# check if the post request has the file part
		if 'file' not in request.files:
				flash('No file part')
				return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return "File " + filename + " Uploaded"
	return "Invalid argument. Can't come to this page directly"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],
								filename)
