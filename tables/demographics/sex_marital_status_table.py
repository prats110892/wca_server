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

		self.table_extra_meta_data = Base_Table.table_extra_meta_data +
									", FOREIGN KEY(" + self.columns[6 + len(Base_Table.columns)] + ") REFERENCES " + self.table_name + "(" + self.columns[len(Base_Table.columns) + 2] + ")"
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
																int(row[5]+row[14]), #C
																int(row[6]+row[15]), #D
																int(row[9]+row[18]), #E
																int(row[12]+row[21]), #F
																int(row[11]+row[20]), #G
																int(row[6]+row[15]), #H
																int(row[7]+row[16]), #I
																int(row[8]+row[17])) #J
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery