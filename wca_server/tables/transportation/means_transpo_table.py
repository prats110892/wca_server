from tables.base_table_class import Base_Table

class MEANS_TRANSPO_Table(Base_Table):

	table_name = "MEANS_TRANSPO"

	def __init__(self) :
		self.table_name = MEANS_TRANSPO_Table.table_name
		self.columns = Base_Table.columns + ["Total workers 16 years and over","Drove alone","Carpooled","Public transportation (excluding taxicab)","Taxicab","Motorcycle","Bicycle","Walked","Other means","Worked at home"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[5]), #C
										int(row[6]), #D
                                                         int(row[12]), #E
										int(row[18]), #F
                                                         int(row[19]), #G
										int(row[20]), #H
                                                         int(row[21]), #I
										int(row[22]), #J
                                                         int(row[23])) #K
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
