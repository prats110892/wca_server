from tables.base_table_class import Base_Table

class SEX_MARITAL_STATUS_Table(Base_Table):
	"The definition of the Sex Marital Status Table in the database"

	table_name = "SEX_MARITAL_STATUS"
	def __init__(self) :
		self.table_name = SEX_MARITAL_STATUS_Table.table_name
		self.columns = Base_Table.columns + ["Total Population 15 years and over",
					"Never married", "Now married",
		 			"Separated but still married",
					"Divorced",
					"Widowed",
					"Now married For Spouse Presence",
					"Married, spouse present",
					"Married, spouse absent"]

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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
																int(row[5])+int(row[14]), #C
																int(row[6])+int(row[15]), #D
																int(row[9])+int(row[18]), #E
																int(row[12])+int(row[21]), #F
																int(row[11])+int(row[20]), #G
																int(row[6])+int(row[15]), #H
																int(row[7])+int(row[16]), #I
																int(row[8])+int(row[17])) #J
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
