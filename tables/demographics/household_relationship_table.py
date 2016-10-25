from tables.base_table_class import Base_Table

class HOUSEHOLD_RELATIONSHIP_Table(Base_Table):
	"The definition of the Household Relationship Table in the database"
	table_name = "HOUSEHOLD_RELATIONSHIP"

	def __init__(self) :
		self.table_name = HOUSEHOLD_RELATIONSHIP_Table.table_name
		self.columns = Base_Table.columns + ["Total Population",
					"In households", "In group quarters",
		 			"Householder",
					"Male householder (in family and nonfamily households)",
					"Female householder (in family and nonfamily households)",
					"In Households For Details", "Householder For Details", "Spouse", "Child", "Grandchild",
					"Brother or sister", "Parent", "Parent-in-law",
					"Son-in-law or daughter-in-law", "Other relatives",
					"Roomer or boarder", "Housemate or roommate",
					"Unmarried partner", "Foster child", "Other nonrelatives",
					"In Households For Male vs Females", "Male living alone", "Female living alone"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
	                     %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
	                     %d, %d" %(int(row[3]), #B
								   int(row[4]), #C
								   int(row[40]), #D
								   int(row[6]+row[27]), #E
								   int(row[7]+row[28]), #F
								   int(row[8]+row[29]), #G
								   int(row[4]), #H
								   int(row[6]+row[27]), #I
								   int(row[9]), #J
								   int(row[10]), #K
								   int(row[14]), #L
								   int(row[15]), #M
								   int(row[16]), #N
								   int(row[17]), #O
								   int(row[18]), #P
								   int(row[19]), #Q
								   int(row[21]+row[35]), #R
								   int(row[22]+row[36]), #S
								   int(row[23]+row[37]), #T
								   int(row[24]+row[38]), #U
								   int(row[25]+row[39]), #V
								   int(row[4]), #W
								   int(row[29]), #X
								   int(row[32]))
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
