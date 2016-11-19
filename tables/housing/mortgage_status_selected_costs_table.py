from tables.base_table_class import Base_Table

class MORTGAGE_STATUS_SELECTED_COSTS_Table(Base_Table):

	table_name = "MORTGAGE_STATUS_SELECTED_COSTS"

	def __init__(self) :
		self.table_name = MORTGAGE_STATUS_SELECTED_COSTS_Table.table_name
		self.columns = Base_Table.columns + ["Housing units with a mortgage","Less than $200","$200 to $299","$300 to $399","$400 to $499 1","$500 to $599 2","$600 to $699 3","$700 to $799","$800 to $899","$900 to $999","$1,000 to $1,249","$1,250 to $1,499","$1,500 to $1,999","$2,000 to $2,499","$2,500 to $2,999","$3,000 or more","Housing units without a mortgage","Less than $100","$100 to $149","$150 to $199","$200 to $249","$250 to $299","$300 to $349","$350 to $399","$400 to $499","$500 to $599","$600 to $699","$700 or more"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[4]), #B
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
										int(row[26]), #X
                                                         int(row[27]), #Y
										int(row[28]), #Z
                                                         int(row[29]), #AA
										int(row[30]), #AB
                                                         int(row[31])) #AC	
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
