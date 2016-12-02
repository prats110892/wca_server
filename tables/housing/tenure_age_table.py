from tables.base_table_class import Base_Table

class TENURE_AGE_Table(Base_Table):

	table_name = "TENURE_AGE"

	def __init__(self) :
		self.table_name = TENURE_AGE_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied","Householder 15 to 24 years 1","25 to 34 years 1","35 to 44 years 1","45 to 54 years 1","55 to 59 years 1","60 to 64 years 1","65 to 74 years 1","75 to 84 years 1","85 years and over 1","Renter occupied","Householder 15 to 24 years 2","25 to 34 years 2","35 to 44 years 2","45 to 54 years 2","55 to 59 years 2","60 to 64 years 2","65 to 74 years 2","75 to 84 years 2","85 years and over 2"]
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
                       %d, %d, %d, %d" %(int(row[4]), #B
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
                                                         int(row[23])) #U
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
