from tables.base_table_class import Base_Table
import csv

class HISPANIC_ORIGIN_Table(Base_Table):
	"The definition of the Hispanic Origin Table in the database"

	table_name = "HISPANIC_ORIGIN"
	columns = 	Base_Table.columns + ["Total Population",
				"Not Hispanic or Latino",
	 			"Hispanic or Latino"]

	def __init__(self) :
		Base_Table.__init__()

	def getInsertQueryForCSV(self, csvReader) :
		skipCount = 0
		insertDataQuery = "INSERT INTO " + table_name + " VALUES "
		for row in csvReader:
			if (skipCount < num_of_rows_to_leave) :
				skipCount += 1
				continue
			insertDataQuery += "('%s', %d, %d, %d)," %(row[0],
																	int(row[3]), #B
																	int(row[4]), #C
																	int(row[5])) #D

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
