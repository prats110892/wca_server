from tables.base_table_class import Base_Table

class TRAVEL_TIME_Table(Base_Table):

	table_name = "TRAVEL_TIME"

	def __init__(self) :
		self.table_name = TRAVEL_TIME_Table.table_name
		self.columns = Base_Table.columns + ["Total workers 16 years and over who did not work at home","14 minutes and under","15 to 29 minutes","30 to 44 minutes","45 to 59 minutes","60 to 89 minutes","More than 90 minutes"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4])+int(row[5])+int(row[6]), #C
										int(row[7])+int(row[8])+int(row[9]), #D
                                                         int(row[10])+int(row[11])+int(row[12]), #E
										int(row[13]), #F
                                                         int(row[14]), #E
                                                         int(row[15])) #E
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
