from Dbhelper import Dbhelper
import csv

class ID_Table(object):
	"The definition of the ID table in the database"

	table_name = "GEO_ID"
	columns = ["Id", "Id2", "Geography"]
	column_data_types = ["VARCHAR(50) NOT NULL", "BIGINT", "VARCHAR(200)"]
	table_extra_meta_data = "PRIMARY KEY(" + columns[0] + ")"
	num_of_rows_to_leave = 2

	Dbhelper = NULL

	def __init__ () :
		Dbhelper = Dbhelper()

	def createTable() :
		return Dbhelper.createTable(table_name, columns, column_data_types, table_extra_meta_data)

	def deleteTable() :
		return Dbhelper.deleteTable(table_name)

	def insertDataFromCSVFile(csvFileName) :
		if Dbhelper.checkIfTableExists(table_name) is True:
			deleteTable() # Delete existing primary id mappings because new ones are being provided

		createTable()	#Create a new Primary Mappings table as it seems to have been updates
		csvFile = open(csvFileName)
		csvReader = csv.reader(csvFile)
		insertDataQuery = getInsertQueryForCSV(csvReader)
		return Dbhelper.executeQuery(insertDataQuery)

	def getInsertQueryForCSV(csvReader) :
		skipCount = 0
		insertDataQuery = "INSERT INTO " + table_name + " VALUES "
		for row in csvReader:
			if (skipCount < num_of_rows_to_leave) :
				skipCount += 1
				continue

			insertDataQuery += "('%s', %d, '%s')," % (row[0], 0 if row[1] == '' else int(row[1]), row[2])

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
