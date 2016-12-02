from tables.base_table_class import Base_Table

class HOUSEHOLD_INCOME_Table(Base_Table):

	table_name = "HOUSEHOLD_INCOME"

	def __init__(self) :
		self.table_name = HOUSEHOLD_INCOME_Table.table_name
		self.columns = Base_Table.columns + ["Estimate; Total:","Estimate; Total: - Less than $10,000","Estimate; Total: - $10,000 to $14,999","Estimate; Total: - $15,000 to $19,999","Estimate; Total: - $20,000 to $24,999","Estimate; Total: - $25,000 to $29,999","Estimate; Total: - $30,000 to $34,999","Estimate; Total: - $35,000 to $39,999","Estimate; Total: - $40,000 to $44,999","Estimate; Total: - $45,000 to $49,999","Estimate; Total: - $50,000 to $59,999","Estimate; Total: - $60,000 to $74,999","Estimate; Total: - $75,000 to $99,999","Estimate; Total: - $100,000 to $124,999","Estimate; Total: - $125,000 to $149,999	","Estimate; Total: - $150,000 to $199,999","Estimate; Total: - $200,000 or more"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[5]), #D
                                                         int(row[6]), #E
										int(row[7]), #F
                                                         int(row[8]), #G
										int(row[9]), #H
                                                         int(row[10]), #I
										int(row[11]), #J
                                                         int(row[12]), #K
										int(row[13]), #L
                                                         int(row[14]), #M
										int(row[15]), #N
                                                         int(row[16]), #O
										int(row[17]), #P
                                                         int(row[18]), #Q
										int(row[19])) #R
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
