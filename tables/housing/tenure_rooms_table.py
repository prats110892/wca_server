from tables.base_table_class import Base_Table

class TENURE_ROOMS_Table(Base_Table):

	table_name = "TENURE_ROOMS"

	def __init__(self) :
		self.table_name = TENURE_ROOMS_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied","1 room 1","2 rooms 1","3 rooms 1","4 rooms 1","5 rooms 1","6 rooms 1","7 rooms 1","8 rooms 1","9 or more rooms 1","Renter occupied","1 room 2","2 rooms 2","3 rooms 2","4 rooms 2","5 rooms 2","6 rooms 2","7 rooms 2","8 rooms 2","9 or more rooms 2","Total occupied housing units","1 room 3","2 rooms 3","3 rooms 3","4 rooms 3","5 rooms 3","6 rooms 3","7 rooms 3","8 rooms 3","9 or more rooms 3"]
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
