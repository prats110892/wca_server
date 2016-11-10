import os, sys

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIRECTORY)

from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from tables import parseAndInsertData, updateIdTableWithNewCSVFile, parseAndInsertCalculations
from tables.categories import DataCategories
from tables.output.base_output_table import Base_Output_Table
from tables.demographics import getTableObject
from tables.calculations import getCalculationsTableObject
from upload_response import getReponseBody


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

@app.route("/upload_data", methods=["GET", "POST"])
def upload_data_file() :
	if request.method == "POST" :
		file = request.files['data-file']
		if 'data-file' not in request.files or file.filename == '':
			getReponseBody("File is missing")
			return render_template("upload_response.html")
		if request.form.get("category") is "" :
			getReponseBody("Category is missing")
			return render_template("upload_response.html")
		if request.form.get("table-name") is "" :
			getReponseBody("Category is missing")
			return render_template("upload_response.html")
		if request.form.get("from-date") is "" :
			getReponseBody("From Date is missing")
			return render_template("upload_response.html")
		if request.form.get("to-date") is "":
			getReponseBody("To Date is missing")
			return render_template("upload_response.html")

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(upload_file_path)
			insertDataIntoDatabase(upload_file_path, request)
			getReponseBody("File " + filename + " Successfully Uploaded")
			return render_template("upload_response.html")
	return render_template("upload_scrolling.html")

@app.route('/upload_calc', methods=["GET", "POST"])
def upload_calc_file() :
	if request.method == "POST" :
		file = request.files['calc-file']
		if 'calc-file' not in request.files or file.filename == '':
			getReponseBody("File is missing")
			return render_template("upload_response.html")
		if request.form.get("table-name") is "" :
			getReponseBody("Category is missing")
			return render_template("upload_response.html")
		if request.form.get("from-date") is "" :
			getReponseBody("From Date is missing")
			return render_template("upload_response.html")

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(upload_file_path)
			insertCalculationsIntoDatabase(upload_file_path, request)
			getReponseBody("File " + filename + " Successfully Uploaded")
			return render_template("upload_response.html")
	return render_template("geographic_calculation.html")

@app.route("/download_data", methods=["GET", "POST"])
def download_data() :
	# if request.method == "POST" :
	# 	if request.form.get("category") is "" :
	# 		getReponseBody("Category is missing")
	# 		return render_template("upload_response.html")
	# 	if request.form.get("table_name") is "" :
	# 		getReponseBody("Detail is missing")
	# 		return render_template("upload_response.html")
	# 	if request.form.get("for_year") is "" :
	# 		getReponseBody("Date is missing")
	# 		return render_template("upload_response.html")
	# 	if request.form.get("region") is "" :
	# 		getReponseBody("Output region is missing")
	# 		return render_template("upload_response.html")
	#
	# 	category = request.form.get("category")
	# 	table_name = request.form.get("table_name")
	# 	forYear = int(request.form.get("for_year"))
	# 	region = request.form.get("region")
	#
	#
	# 	base_output_table = Base_Output_Table()
	# 	base_output_table.initalize(forYear, getTableObject(table_name), getCalculationsTableObject(region))
	# 	outputFileLocation = secure_filename(base_output_table.getOutputCSVPath())
	#
	return render_template("download.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],
								filename)

class GetCSVFile(Resource) :
	def get(self) :
		baseOutputTable = Base_Output_Table()
		baseOutputTable.initalize(2011, getTableObject("Relationship_Children"), getCalculationsTableObject("NPU"))
		outputFileLocation = baseOutputTable.getOutputCSVPath()
		return {
			"name" : "some_name_here",
			"fromYear" : 1993,
			"toYear" : 1997,
			"downloadLink" : outputFileLocation
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
