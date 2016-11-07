from tables.base_table_class import Base_Table

class TENURE_UNITS_STRUCTURE_Table(Base_Table):

	table_name = "TENURE_UNITS_STRUCTURE"

	def __init__(self) :
		self.table_name = TENURE_UNITS_STRUCTURE_Table.table_name
		self.columns = Base_Table.columns + ["Owner-occupied housing units","1, detached","1, attached","2","3 or 4","5 to 9","10 to 19","20 to 49","50 or more","Mobile home","Boat, RV, van, etc.","Estimate; Renter-occupied housing units:","1, detached","1, attached","2","3 or 4","5 to 9","10 to 19","20 to 49","50 or more","Mobile home","Boat, RV, van, etc.","Total occupied housing units","1, detached","1, attached","2","3 or 4","5 to 9","10 to 19","20 to 49","50 or more","Mobile home","Boat, RV, van, etc."]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
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
										int(row[18]), #P
                                                         int(row[19]), #Q
										int(row[20]), #R
                                                         int(row[21]), #S
										int(row[22]), #T
                                                         int(row[23]), #U
										int(row[24]), #V
                                                         int(row[25]), #W
										int(row[3]), #X
                                                         int(row[5])+int(row[16]), #Y
										int(row[6])+int(row[17]), #Z
                                                         int(row[7])+int(row[18]), #AA
										int(row[8])+int(row[19]), #AB
                                                         int(row[9])+int(row[20]), #AC	
										int(row[10])+int(row[21]), #AD
                                                         int(row[11])+int(row[22]), #AE
										int(row[12])+int(row[23]), #AF
                                                         int(row[13])+int(row[24]), #AG
										int(row[14])+int(row[25])) #AH                                                       
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
