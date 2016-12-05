from tables.base_table_class import Base_Table

class TENURE_YEAR_STRUCTURE_BUILT_Table(Base_Table):

	table_name = "TENURE_YEAR_STRUCTURE_BUILT"

	def __init__(self) :
		self.table_name = TENURE_YEAR_STRUCTURE_BUILT_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied","2010 or later 1","2000 to 2009 1","1990 to 1999 1","1980 to 1989 1","1970 to 1979 1","1960 to 1969 1","1950 to 1959 1","1940 to 1949 1","1939 or earlier 1","Renter occupied","2010 or later 2","2000 to 2009 2","1990 to 1999 2","1980 to 1989 2","1970 to 1979 2","1960 to 1969 2","1950 to 1959 2","1940 to 1949 2","1939 or earlier 2","Total occuiped housing units","2010 or later 3","2000 to 2009 3","1990 to 1999 3","1980 to 1989 3","1970 to 1979 3","1960 to 1969 3","1950 to 1959 3","1940 to 1949 3","1939 or earlier 3"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, \
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[4]), #B
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
                                                         int(row[15]), #M
										int(row[16]), #N
                                                         int(row[17]), #O
										int(row[18]), #P
                                                         int(row[19]), #Q
										int(row[20]), #R
                                                         int(row[21]), #S
										int(row[22]), #T
                                                         int(row[23]), #U
										int(row[3]), #V
                                                         int(row[5])+int(row[15]), #W
										int(row[6])+int(row[16]), #X
                                                         int(row[7])+int(row[17]), #Y
										int(row[8])+int(row[18]), #Z
                                                         int(row[9])+int(row[19]), #AA
										int(row[10])+int(row[20]), #AB
                                                         int(row[11])+int(row[21]), #AC	
										int(row[12])+int(row[22]), #AD
                                                         int(row[13])+int(row[23])) #AE
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
