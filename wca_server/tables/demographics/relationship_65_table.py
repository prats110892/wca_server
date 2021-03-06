from tables.base_table_class import Base_Table

class RELATIONSHIP_65_Table(Base_Table):
	"The definition of the Relationship 65 Table in the database"

	table_name = "RELATIONSHIP_65"
	def __init__(self) :
		self.table_name = RELATIONSHIP_65_Table.table_name
		self.columns = Base_Table.columns + ["Total Population in 65 years and over",
					"In households", "In group quarters",
		 			"Householder",
					"Male householder (in family and nonfamily households)",
					"Female householder (in family and nonfamily households)",
					"In Households For Details", "Householder For Details", "Spouse", "Parent",
					"Parent-in-law", "Other relatives", "Other nonrelatives",
					"In Households For Male vs Female", "Male living alone", "Female living alone"]
		self.table_extra_meta_data = Base_Table.table_extra_meta_data
		self.initalize()

	def getInsertQueryForCSV(self, csvFile, fromYear, toYear) :
		skipCount = 0
		insertDataQuery = """REPLACE INTO `{0}` VALUES """.format(self.table_name)
		for line in csvFile:
			row = line.split(",")
			if (skipCount < Base_Table.num_of_rows_to_leave) :
				skipCount += 1
				continue

			defaultQuery = self.getIDAndYearQueryForRow(row, fromYear, toYear)
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
	                  %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
					  int(row[4]), #C
					  int(row[23]), #D
					  int(row[7])+int(row[16])+int(row[8])+int(row[19]), #E
					  int(row[7])+int(row[16]), #F
					  int(row[8])+int(row[19]), #G
					  int(row[4]), #H
					  int(row[7])+int(row[16])+int(row[8])+int(row[19]), #I
					  int(row[9]), #J
					  int(row[10]), #K
					  int(row[11]), #L
					  int(row[12]), #M
					  int(row[4])-int(row[7])-int(row[16])-int(row[8])-int(row[19])-int(row[9])-int(row[10])-int(row[11])-int(row[12]), #N
					  int(row[4]), #O
					  int(row[17]), #P
					  int(row[19])) #Q
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
