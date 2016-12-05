from tables.base_table_class import Base_Table

class RELATIONSHIP_CHILDREN_Table(Base_Table):
	"The definition of the Relationship Children Table in the database"

	table_name = "RELATIONSHIP_CHILDREN"

	def __init__(self) :
		self.table_name = RELATIONSHIP_CHILDREN_Table.table_name
		self.columns = Base_Table.columns + ["Estimate: Total",
					"Estimate: Own child - Biological child",
		 			"Estimate: Own child - Adopted child",
					"Estimate: Own child - Stepchild",
					"Estimate: Grandchild",
					"Estimate: Other relatives",
					"Estimate: Foster child or Other Unrelated child"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d" %(int(row[3]),
														int(row[5]),
														int(row[6]),
														int(row[7]),
														int(row[8]),
														int(row[9]),
														int(row[10]))
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
