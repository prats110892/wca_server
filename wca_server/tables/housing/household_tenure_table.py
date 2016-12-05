from tables.base_table_class import Base_Table

class HOUSEHOLD_TENURE_Table(Base_Table):

	table_name = "HOUSEHOLD_TENURE"

	def __init__(self) :
		self.table_name = HOUSEHOLD_TENURE_Table.table_name
		self.columns = Base_Table.columns + ["Married-couple family","Owner-occupied 1","Renter-occupied 1","Male householder, no wife present","Owner-occupied 2","Renter-occupied 2","Female householder, no husband present","Owner-occupied 3","Renter-occupied 3","Nonfamily households","Owner-occupied 4","Renter-occupied 4"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[5]), #B
										int(row[6]), #C
										int(row[7]), #D
                                                         int(row[9]), #E
										int(row[10]), #F
                                                         int(row[11]), #G
										int(row[12]), #H
                                                         int(row[13]), #I
										int(row[14]), #J
                                                         int(row[15]), #K
										int(row[16]), #L
                                                         int(row[17])) #M
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
