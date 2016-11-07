import os, sys

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIRECTORY)

from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from tables import parseAndInsertData, updateIdTableWithNewCSVFile, parseAndInsertCalculations
from tables.categories import DataCategories


app = Flask(__name__)
api = Api(app)


UPLOAD_FOLDER = CURRENT_DIRECTORY + "/uploads"
ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename) :
	return "." in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def root_path() :
	return "Something else will come here"

@app.route("/upload")
def upload_a_new_file() :
	return upload_data_file()

@app.route("/download")
def download_data() :
	return render_template("download.html")

@app.route("/upload_data", methods=["GET", "POST"])
def upload_data_file() :
	if request.method == "POST" :
		file = request.files['data-file']
		if 'data-file' not in request.files or file.filename == '':
			return "File is missing"
		if request.form.get("category") is "" :
			return "Category is missing"
		if request.form.get("table-name") is "" :
			return "Category is missing"
		if request.form.get("from-date") is "" :
			return "From Date is missing"
		if request.form.get("to-date") is "":
			return "To Date is missing"

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(upload_file_path)
			insertDataIntoDatabase(upload_file_path, request)
			return "File " + filename + " Successfully Uploaded"
	return render_template("upload_scrolling.html")

@app.route('/upload_calc', methods=["GET", "POST"])
def upload_calc_file() :
	if request.method == "POST" :
		file = request.files['calc-file']
		if 'calc-file' not in request.files or file.filename == '':
			return "File is missing"
		if request.form.get("table-name") is "" :
			return "Category is missing"
		if request.form.get("from-date") is "" :
			return "From Date is missing"

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(upload_file_path)
			insertCalculationsIntoDatabase(upload_file_path, request)
			return "File " + filename + " Successfully Uploaded"
	return render_template("geographic_calculation.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],
								filename)


class GetCSVFile(Resource) :
	def get(self) :
		return {
			"name" : "some_name_here",
			"fromYear" : 1993,
			"toYear" : 1997,
			"downloadLink" : "http://hello.fuckoff.com"
			}

api.add_resource(GetCSVFile, "/getcsvfile")

def insertCalculationsIntoDatabase(uploadFilePath, request) :
	tableName = request.form.get("table-name")
	fromDate = request.form.get("from-date")
	csvFileName = uploadFilePath
	print(tableName + " " + fromDate + " " + csvFileName)
	parseAndInsertCalculations(csvFileName, tableName, fromDate)

def insertDataIntoDatabase(uploadFilePath, request) :
	category = request.form.get("category").lower()
	tableName = request.form.get("table-name")
	fromDate = request.form.get("from-date")
	toDate = request.form.get("to-date")
	csvFileName = uploadFilePath
	print(category + " " + tableName + " " + fromDate + " "  + toDate + " " + csvFileName)
	parseAndInsertData(category, csvFileName, tableName, fromDate, toDate)

if __name__ == "__main__":
	app.run(debug=True)
