from tables.base_table_class import Base_Table

class AGGREGATE_HOUSEHOLD_INCOME_Table(Base_Table):

	table_name = "AGGREGATE_HOUSEHOLD_INCOME"

	def __init__(self) :
		self.table_name = AGGREGATE_HOUSEHOLD_INCOME_Table.table_name
		self.columns = Base_Table.columns + ["Aggregate household income past 12 months (2014 Inflation-adjusted)"]
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
			dataQuery = "%d" %(int(row[3])) #B
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
