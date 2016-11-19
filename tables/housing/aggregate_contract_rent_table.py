from tables.base_table_class import Base_Table

class AGGREGATE_CONTRACT_RENT_Table(Base_Table):

	table_name = "AGGREGATE_CONTRACT_RENT"

	def __init__(self) :
		self.table_name = AGGREGATE_CONTRACT_RENT_Table.table_name
		self.columns = Base_Table.columns + ["Aggregate contract rent for renter-occupied housing units paying cash rent"]
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
			dataQuery = "%d" %(int(row[3])) #B
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
