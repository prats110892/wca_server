from Dbhelper import Dbhelper
import csv

class ID_Table(object):
	"The definition of the ID table in the database"

	table_name = "GEO_ID"
	columns = ["Id", "Id2", "Geography"]
	column_data_types = ["VARCHAR(50) NOT NULL", "VARCHAR(50)", "VARCHAR(200)"]
	table_extra_meta_data = "PRIMARY KEY(" + columns[0] + ")"
	num_of_rows_to_leave = 2

	def __init__ (self) :
		self.dbHelper = Dbhelper()
		if self.dbHelper.checkIfTableExists(ID_Table.table_name) is False:
			self.createTable()

	def createTable(self) :
		return self.dbHelper.createTable(ID_Table.table_name, ID_Table.columns, ID_Table.column_data_types, ID_Table.table_extra_meta_data)

	def deleteTable(self) :
		return self.dbHelper.deleteTable(table_name)

	def insertDataFromCSVFile(self, csvFileName) :
		csvFile = open(csvFileName, 'rU')
		csvReader = csv.reader(csvFile)
		insertDataQuery = self.getInsertQueryForCSV(csvReader)
		return self.dbHelper.executeQuery(insertDataQuery)

	def getInsertQueryForCSV(self, csvReader) :
		skipCount = 0
		insertDataQuery = "INSERT INTO " + ID_Table.table_name + " VALUES "
		for row in csvReader:
			if (skipCount < ID_Table.num_of_rows_to_leave) :
				skipCount += 1
				continue

			insertDataQuery += "('%s', %d, '%s')," % (row[0], 0 if row[1] == '' else int(row[1]), row[2])

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
