from tables.base_table_class import Base_Table

class HISPANIC_ORIGIN_Table(Base_Table):
	"The definition of the Hispanic Origin Table in the database"

	table_name = "HISPANIC_ORIGIN"

	def __init__(self) :
		self.table_name = HISPANIC_ORIGIN_Table.table_name
		self.columns = Base_Table.columns + ["Total Population",
					"Not Hispanic or Latino",
		 			"Hispanic or Latino"]
		self.table_extra_meta_data = Base_Table.table_extra_meta_data
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
			dataQuery = "%d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[5]))
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
