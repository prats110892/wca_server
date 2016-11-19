from Dbhelper import Dbhelper
from id_table import ID_Table

class Base_Table(object):
	"This is the base table class that all other table classes will extend"

	num_of_rows_to_leave = 2
	columns = ["From Year", "To Year", "Id"] # Just a default definition. You still have to add to all the others
	column_data_types = ["INT", "INT", "VARCHAR(50) NOT NULL", "BIGINT"] # If all the columns other than id are the same datatype then just 2 entries needed
	table_extra_meta_data = "FOREIGN KEY(" + columns[2] + ") REFERENCES " + ID_Table.table_name + "(" + ID_Table.columns[0] + ")"

	def initalize(self) :
		self.dbHelper = Dbhelper()
		if self.dbHelper.checkIfTableExists(self.table_name) is False:
			self.createTable()

	def createTable(self) :
		return self.dbHelper.createTable(self.table_name, self.columns, Base_Table.column_data_types, self.table_extra_meta_data)

	def deleteTable(self) :
		return self.dbHelper.deleteTable(self.table_name)

	def insertDataFromCSVFile(self, csvFileName, fromYear, toYear) :
		csvFile = open(csvFileName, 'rU')
		insertDataQuery = self.getInsertQueryForCSV(csvFile, fromYear, toYear)
		return self.dbHelper.executeQuery(insertDataQuery)

	def getInsertQueryForCSV(self, csvFile, fromYear, toYear) :
		raise ("Function Not Implemented Error")

	def getIDAndYearQueryForRow(self, row, fromYear, toYear) :
		return "%d, %d, '%s'," %(int(fromYear), int(toYear), row[0])
