from tables.base_table_class import Base_Table

class EMPLOYMENT_Table(Base_Table):

	table_name = "EMPLOYMENT"

	def __init__(self) :
		self.table_name = EMPLOYMENT_Table.table_name
		self.columns = Base_Table.columns + ["Total population 16 years and over","Employed","Unemployed","Armed Forces","Not in labor force"]
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
			dataQuery = "%d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[6]), #C
										int(row[7]), #D
                                                         int(row[8]), #E
										int(row[9])) #F
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
