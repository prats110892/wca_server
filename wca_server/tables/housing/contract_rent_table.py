from tables.base_table_class import Base_Table

class CONTRACT_RENT_Table(Base_Table):

	table_name = "CONTRACT_RENT"

	def __init__(self) :
		self.table_name = CONTRACT_RENT_Table.table_name
		self.columns = Base_Table.columns + ["Total renter-occupied housing units","Estimate; With cash rent: 1","Estimate; No cash rent","Estimate; With cash rent: 2","Less than $100","$100 to $149","Estimate; With cash rent:","$200 to $249","$250 to $299","$300 to $349","$350 to $399","$400 to $449","$450 to $499","$500 to $549","$550 to $599","$600 to $649","$650 to $699","$700 to $749","$750 to $799","$800 to $899","$900 to $999","$1,000 to $1,249","$1,250 to $1,499","$1,500 to $1,999","$2,000 or more"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[26]), #D
                                                         int(row[4]), #E
										int(row[5]), #F
                                                         int(row[6]), #G
										int(row[7]), #H
                                                         int(row[8]), #I
										int(row[9]), #J
                                                         int(row[10]), #K
										int(row[11]), #L
                                                         int(row[12]), #M
										int(row[13]), #N
                                                         int(row[14]), #O
										int(row[15]), #P
                                                         int(row[16]), #Q
										int(row[17]), #R
                                                         int(row[18]), #S
										int(row[19]), #T
                                                         int(row[20]), #U
										int(row[21]), #V
                                                         int(row[22]), #W
										int(row[23]), #X
                                                         int(row[24]), #Y
										int(row[25])) #Z
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
