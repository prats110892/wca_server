from tables.base_table_class import Base_Table

class ROOMS_Table(Base_Table):

	table_name = "ROOMS"

	def __init__(self) :
		self.table_name = ROOMS_Table.table_name
		self.columns = Base_Table.columns + ["Total housing units","1 room","2 rooms","3 rooms","4 rooms","5 rooms","6 rooms","7 rooms","8 rooms","9 or more rooms"]
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
										int(row[4]), #C
										int(row[5]), #D
                                                         int(row[6]), #E
										int(row[7]), #F
                                                         int(row[8]), #G
										int(row[9]), #H
                                                         int(row[10]), #I
										int(row[11]), #J
                                                         int(row[12])) #K
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
