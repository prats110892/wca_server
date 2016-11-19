from tables.base_table_class import Base_Table

class TENURE_VEHICLES_AVAILABLE_Table(Base_Table):

	table_name = "TENURE_VEHICLES_AVAILABLE"

	def __init__(self) :
		self.table_name = TENURE_VEHICLES_AVAILABLE_Table.table_name
		self.columns = Base_Table.columns + ["Total occupied housing units","No vehicle 1","1 vehicle 1","2 vehicles 1","3 vehicles 1","4 vehicles 1","5 or more 1","Owner occupied","No vehicle 2","1 vehicle 2","2 vehicles 2","3 vehicles 2","4 vehicles 2","5 or more 2","Renter occupied","No vehicle 3","1 vehicle 3","2 vehicles 3","3 vehicles 3","4 vehicles 3","5 or more 3"]
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
                       %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[5])+int(row[12]), #C
										int(row[6])+int(row[13]), #D
                                                         int(row[7])+int(row[14]), #E
										int(row[8])+int(row[15]), #F
                                                         int(row[9])+int(row[16]), #G
										int(row[10]+int(row[17])), #H
                                                         int(row[4]), #I
										int(row[5]), #J
                                                         int(row[6]), #K
										int(row[7]), #L
                                                         int(row[8]), #M
										int(row[9]), #N
                                                         int(row[10]), #O
										int(row[11]), #P
                                                         int(row[12]), #Q
										int(row[13]), #R
                                                         int(row[14]), #S
										int(row[15]), #T
                                                         int(row[16]), #U
										int(row[17])) #V
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"
		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
