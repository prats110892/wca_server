from tables.base_table_class import Base_Table

class TOTAL_POP_TENURE_UNITS_Table(Base_Table):

	table_name = "TOTAL_POP_TENURE_UNITS"

	def __init__(self) :
		self.table_name = TOTAL_POP_TENURE_UNITS_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied","1, detached or attached (1)","2 to 4 (1)","5 or more (1)","Mobile home (1)","Boat, RV, van, etc. (1)","Estimate; Renter occupied:","1, detached or attached (2)","2 to 4 (2)","5 or more (2)","Mobile home (2)","Boat, RV, van, etc. (2)","Total population in occupied housing units by tenure by units in structure","1, detached or attached (3)","2 to 4 (3)","5 or more (3)","Mobile home (3)","Boat, RV, van, etc. (3)"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, \
                       %d, %d" %(int(row[4]), #B
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
										int(row[3]), #N
                                                         int(row[5])+int(row[11]), #O
										int(row[6])+int(row[12]), #P
                                                         int(row[7])+int(row[13]), #Q
										int(row[8])+int(row[14]), #R
                                                         int(row[9])+int(row[15])) #S
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
