from tables.base_table_class import Base_Table
import csv

class SEX_AGE_VETERAN_Table(Base_Table):
	"The definition of the Sex Age Veteran Table in the database"

	num_of_rows_to_leave = 2
	table_name = "SEX_AGE_VETERAN"
	columns = 	Base_Table.columns +
				["Total Civilian Population 18 Years and over",
				"Veteran", "Nonveteran"]

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
						dataQuery = "%d, %d, %d, %d" %(int(row[3]), #B
														int(row[4]), #C
														int(row[5])) #D
						insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
