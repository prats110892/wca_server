from tables.base_table_class import Base_Table

class AGE_MEALS_RENT_Table(Base_Table):

	table_name = "AGE_MEALS_RENT"

	def __init__(self) :
		self.table_name = AGE_MEALS_RENT_Table.table_name
		self.columns = Base_Table.columns + ["Householder 15 to 54 years","Meals included in rent 1","No meals included in rent 1","Householder 55 to 64 years","Meals included in rent 2","No meals included in rent 2","Householder 65 to 74 years","Meals included in rent 3","No meals included in rent 3","Householder 75 years and over","Meals included in rent 4","No meals included in rent 4"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[4]), #B
										int(row[5]), #C
										int(row[6]), #D
                                                         int(row[7]), #E
										int(row[8]), #F
                                                         int(row[9]), #G
										int(row[10]), #H
                                                         int(row[11]), #I
										int(row[12]), #J
                                                         int(row[13]), #K
										int(row[14]), #L
                                                         int(row[15])) #M
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
