from tables.base_table_class import Base_Table
import csv

class SEX_MARITAL_STATUS_Table(Base_Table):
	"The definition of the Sex Marital Status Table in the database"

	table_name = "SEX_MARITAL_STATUS"
	columns = 	Base_Table.columns +
				["Total Population 15 years and over",
				"Never married", "Now married",
	 			"Separated but still married",
				"Divorced",
				"Widowed",
				"Now married",
				"Married, spouse present",
				"Married, spouse absent"]

	def __init__(self) :
		Base_Table.__init__()

	def getInsertQueryForCSV(self, csvReader) :
		skipCount = 0
		insertDataQuery = "INSERT INTO " + table_name + " VALUES "
		for row in csvReader:
			if (skipCount < num_of_rows_to_leave) :
				skipCount += 1
				continue
			insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d)," %(row[0],
																	int(row[3]), #B
																	int(row[5]+row[14]), #C
																	int(row[6]+row[15]), #D
																	int(row[9]+row[18]), #E
																	int(row[12]+row[21]), #F
																	int(row[11]+row[20]), #G
																	int(row[6]+row[15]), #H
																	int(row[7]+row[16]), #I
																	int(row[8]+row[17])) #J
		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
