from tables.base_table_class import Base_Table

class AGE_GROSS_RENT_PERCENT_INCOME_Table(Base_Table):

	table_name = "AGE_GROSS_RENT_PERCENT_INCOME"

	def __init__(self) :
		self.table_name = AGE_GROSS_RENT_PERCENT_INCOME_Table.table_name
		self.columns = Base_Table.columns + ["Total renter-occupied housing units","Householder 15 to 24 years","Less than 20.0 percent 1","20.0 to 24.9 percent 1","25.0 to 29.9 percent 1","30.0 to 34.9 percent 1","35.0 percent or more 1","Not computed 1","Householder 25 to 34 years","Less than 20.0 percent 2","20.0 to 24.9 percent 2","25.0 to 29.9 percent 2","30.0 to 34.9 percent 2","35.0 percent or more 2","Not computed 2","Householder 35 to 64 years","Less than 20.0 percent 3","20.0 to 24.9 percent 3","25.0 to 29.9 percent 3","30.0 to 34.9 percent 3","35.0 percent or more 3","Not computed 3","Householder 65 years and over","Less than 20.0 percent 4","20.0 to 24.9 percent 4","25.0 to 29.9 percent 4","30.0 to 34.9 percent 4","35.0 percent or more 4","Not computed 4"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
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
										int(row[19]), #R
                                                         int(row[20]), #S
										int(row[21]), #T
                                                         int(row[22]), #U
										int(row[23]), #V
                                                         int(row[24]), #W
										int(row[25]), #X
                                                         int(row[26]), #Y
										int(row[27]), #Z
                                                         int(row[28]), #AA
										int(row[29]), #AB
                                                         int(row[30]), #AC
                                                         int(row[31])) #AD
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
