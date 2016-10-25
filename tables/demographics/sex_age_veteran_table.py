from tables.base_table_class import Base_Table

class SEX_AGE_VETERAN_Table(Base_Table):
	"The definition of the Sex Age Veteran Table in the database"

	table_name = "SEX_AGE_VETERAN"

	def __init__(self) :
		self.table_name = SEX_AGE_VETERAN_Table.table_name
		self.columns = Base_Table.columns + ["Total Civilian Population 18 Years and over",
					"Veteran", "Nonveteran"]
		self.initalize()

	def getInsertQueryForCSV(self, csvFile, fromYear, toYear) :
		skipCount = 0
		insertDataQuery = """INSERT INTO `{0}` VALUES """.format(self.table_name)
		for line in csvFile:
			row = line.split(",")
			if (skipCount < Base_Table.num_of_rows_to_leave) :
				skipCount += 1
				continue

			defaultQuery = self.getIDAndYearQueryForRow(row, fromYear, toYear)
			dataQuery = "%d, %d, %d, %d" %(int(row[3]), #B
											int(row[4]), #C
											int(row[5])) #D
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
