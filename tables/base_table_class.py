from Dbhelper import Dbhelper
import csv

class Base_Table(object):
	"This is the base table class that all other table classes will extend"

		columns = ["From Year", "To Year", "Id"] # Just a default definition. You still have to add to all the others
		column_data_types = ["INT", "INT", "VARCHAR(50) NOT NULL", "INT"] # If all the columns other than id are the same datatype then just 2 entries needed
		table_extra_meta_data = "FOREIGN KEY(" + columns[2] + ") REFERENCES " + ID_Table.table_name + "(" + ID_Table.columns[0] + ")"

		Dbhelper = NULL

		def __init__ (self) :
			Dbhelper = Dbhelper()
			if Dbhelper.checkIfTableExists(table_name) is False:
				createTable()

		def createTable(self) :
			return Dbhelper.createTable(table_name, columns, column_data_types, table_extra_meta_data)

		def deleteTable(self) :
			return Dbhelper.deleteTable(table_name)

		def insertDataFromCSVFile(self, csvFileName, fromYear, toYear) :
			csvFile = open(csvFileName)
			csvReader = csv.reader(csvFile)
			insertDataQuery = getInsertQueryForCSV(csvReader, fromYear, toYear)
			return Dbhelper.executeQuery(insertDataQuery)

		def getIDAndYearQueryForRow(row, fromYear, toYear) :
			return "%d, %d, '%s'," %(fromYear, toYear, row[0])
