from tables.base_table_class import Base_Table

class YEAR_STRUCTURE_BUILT_Table(Base_Table):

	table_name = "YEAR_STRUCTURE_BUILT"

	def __init__(self) :
		self.table_name = YEAR_STRUCTURE_BUILT_Table.table_name
		self.columns = Base_Table.columns + ["Total housing units","2010 or later","2000 to 2009","1990 to 1999","1980 to 1989","1970 to 1979","1960 to 1969","1950 to 1959","1940 to 1949","1939 or earlier"]
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
