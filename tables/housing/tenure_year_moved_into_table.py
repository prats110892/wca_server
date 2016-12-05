from tables.base_table_class import Base_Table

class TENURE_YEAR_MOVED_INTO_Table(Base_Table):

	table_name = "TENURE_YEAR_MOVED_INTO"

	def __init__(self) :
		self.table_name = TENURE_YEAR_MOVED_INTO_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied","2010 or later 1","2000 to 2009 1","1990 to 1999 1","1980 to 1989 1","1970 to 1979 1","1969 or earlier 1","Renter occupied","2010 or later 2","2000 to 2009 2","1990 to 1999 2","1980 to 1989 2","1970 to 1979 2","1969 or earlier 2","Total occupied housing units","2010 or later 3","2000 to 2009 3","1990 to 1999 3","1980 to 1989 3","1970 to 1979 3","1969 or earlier 3"]
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
                       %d, %d, %d, %d, %d" %(int(row[4]), #B
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
										int(row[3]), #P
                                                         int(row[5])+int(row[12]), #Q
										int(row[6])+int(row[13]), #R
                                                         int(row[7])+int(row[14]), #S
										int(row[8])+int(row[15]), #T
                                                         int(row[9])+int(row[16]), #U
										int(row[10])+int(row[17])) #V
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
