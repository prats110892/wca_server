from tables.base_table_class import Base_Table
import csv

class RACE_Table(Base_Table):
	"The definition of the Race Table in the database"

	num_of_rows_to_leave = 2
	table_name = "RACE"
	columns = 	Base_Table.columns + ["Total Population", "White alone",
	 			"Black or African American alone",
				"American Indian and Alaska Native alone", "Asian alone",
				"Native Hawaiian and Other Pacific Islander alone",
				"Some other race alone",
				"Two or more races"]

	def __init__(self) :
		Base_Table.__init__()

	def getInsertQueryForCSV(self, csvReader, fromYear, toYear) :
		skipCount = 0
		insertDataQuery = "INSERT INTO " + table_name + " VALUES "
		for row in csvReader:
			if (skipCount < num_of_rows_to_leave) :
				skipCount += 1
				continue

			defaultQuery = Base_Table().getIDAndYearQueryForRow(row, fromYear, toYear)
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
															int(row[4]), #C
															int(row[5]), #D
															int(row[6]), #E
															int(row[7]), #F
															int(row[8]), #G
															int(row[9]), #H
															int(row[10])) #I
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
