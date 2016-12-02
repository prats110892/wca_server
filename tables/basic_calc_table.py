from Dbhelper import Dbhelper
from id_table import ID_Table

class Base_Calc_Table(object):
	"This is the base class table class that all other calc table classes will extend"

	columns = ["From Year", "Id"] # Just a default definition. You still have to add to all the others
	column_data_types = ["INT", "VARCHAR(50) NOT NULL", "FLOAT"] # If all the columns other than id are the same datatype then just 2 entries needed
	table_extra_meta_data = "FOREIGN KEY(" + columns[1] + ") REFERENCES " + ID_Table.table_name + "(" + ID_Table.columns[0] + "), "
	table_extra_meta_data += "PRIMARY KEY(`" + columns[0] + "`, `" + columns[1] + "`)"
	num_of_rows_to_leave = 1

	def initalize(self) :
		self.dbHelper = Dbhelper()
		if self.dbHelper.checkIfTableExists(self.table_name) is False:
			self.createTable()

	def createTable(self) :
		return self.dbHelper.createTable(self.table_name, self.columns, Base_Calc_Table.column_data_types, Base_Calc_Table.table_extra_meta_data)

	def deleteTable(self) :
		return self.dbHelper.deleteTable(self.table_name)

	def insertDataFromCSVFile(self, csvFileName, fromYear) :
		csvFile = open(csvFileName, 'rU')
		insertDataQuery = self.getInsertQueryForCSV(csvFile, fromYear)
		return self.dbHelper.executeQuery(insertDataQuery)

	def getInsertQueryForCSV(self, csvFile, fromYear) :
		skipCount = 0
		insertDataQuery = """INSERT INTO `{0}` VALUES """.format(self.table_name)
		for line in csvFile:
			row = line.split(",")
			if (skipCount < Base_Calc_Table.num_of_rows_to_leave) :
				skipCount += 1
				continue

			defaultQuery = self.getIDAndYearQueryForRow(row, fromYear)
			dataQuery = ""
			for i in range(1, len(row)) :
				dataQuery += "%f," %(float(row[i]))
			dataQuery = dataQuery[:-1]
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"
		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery

	def getIDAndYearQueryForRow(self, row, fromYear) :
		return "%d, '%s'," %(int(fromYear), row[0])
