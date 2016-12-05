from tables.base_table_class import Base_Table

class TIME_LEAVING_WORK_Table(Base_Table):

	table_name = "TIME_LEAVING_WORK"

	def __init__(self) :
		self.table_name = TIME_LEAVING_WORK_Table.table_name
		self.columns = Base_Table.columns + ["Total workers 16 years and over who did not work at home","12:00 a.m. to 4:59 a.m.","5:00 a.m. to 5:59 a.m.","6:00 a.m. to 6:59 a.m.","7:00 a.m. to 7:59 a.m.","8:00 a.m. to 8:59 a.m.","9:00 a.m. to 9:59 a.m.","10:00 a.m. to 10:59 a.m.","11:00 a.m. to 11:59 a.m.","12:00 p.m. to 3:59 p.m.","4:00 p.m. to 11:59 p.m."]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[5])+int(row[6]), #D
                                                         int(row[7])+int(row[8]), #E
										int(row[9])+int(row[10]), #F
                                                         int(row[11])+int(row[12]), #G
										int(row[11])+int(row[12]), #H
                                                         int(row[14]), #I
										int(row[15]), #J
                                                         int(row[16]), #K
										int(row[17])) #L
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
