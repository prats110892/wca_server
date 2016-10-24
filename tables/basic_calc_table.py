from Dbhelper import Dbhelper
import csv

class Base_Calc_Table(object):
	"This is the base class table class that all other calc table classes will extend"

		columns = ["From Year", "To Year", "Id"] # Just a default definition. You still have to add to all the others
		column_data_types = ["INT", "INT", "VARCHAR(50) NOT NULL", "FLOAT"] # If all the columns other than id are the same datatype then just 2 entries needed
		table_extr]a_meta_data = "FOREIGN KEY(" + columns[2] + ") REFERENCES " + ID_Table.table_name + "(" + ID_Table.columns[0] + ")"

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

		def getInsertQueryForCSV(self, csvReader, fromYear, toYear) :
			skipCount = 0
			insertDataQuery = "INSERT INTO " + table_name + " VALUES "
			for row in csvReader:
				if (skipCount < num_of_rows_to_leave) :
					skipCount += 1
					continue

				defaultQuery = getIDAndYearQueryForRow(row, fromYear, toYear)
				dataQuery = ""
				for i in range(1, len(row)) :
					dataQuery += "%f," %(float(row[i]))
				dataQuery = dataQuery[:-1]
				insertDataQuery += "(" + defaultQuery + dataQuery + "),"

			insertDataQuery = insertDataQuery[:-1]
			insertDataQuery += ";"
			return insertDataQuery

		def getIDAndYearQueryForRow(row, fromYear, toYear) :
			return "%d, %d, '%s'," %(fromYear, toYear, row[0])
