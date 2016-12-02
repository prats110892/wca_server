from tables.base_table_class import Base_Table

class TENURE_TELEPHONE_AGE_Table(Base_Table):

	table_name = "TENURE_TELEPHONE_AGE"

	def __init__(self) :
		self.table_name = TENURE_TELEPHONE_AGE_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied","With telephone service available 1","No telephone service available 1","Estimate; Renter occupied:","With telephone service available 2","No telephone service available 2","Owner occupied: - With telephone service available","Householder 15 to 34 years 1","Householder 35 to 64 years 1","Householder 65 years and over 1","Owner occupied: - No telephone service available","Householder 15 to 34 years 2","Householder 35 to 64 years 2","Householder 65 years and over 2","Renter occupied: - With telephone service available","Householder 15 to 34 years 3","Householder 35 to 64 years 3","Householder 65 years and over 3","Renter occupied: - No telephone service available","Householder 15 to 34 years 4","Householder 35 to 64 years 4","Householder 65 years and over 4"]
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
                       %d, %d, %d, %d, %d, %d" %(int(row[4]), #B
										int(row[5]), #C
										int(row[9]), #D
                                                         int(row[13]), #E
										int(row[14]), #F
                                                         int(row[18]), #G
										int(row[5]), #H
                                                         int(row[6]), #I
										int(row[7]), #J
                                                         int(row[8]), #K
										int(row[9]), #L
                                                         int(row[10]), #M
										int(row[11]), #N
                                                         int(row[12]), #O
										int(row[14]), #P
                                                         int(row[15]), #Q
										int(row[16]), #R
                                                         int(row[17]), #S
										int(row[18]), #T
                                                         int(row[19]), #U
										int(row[20]), #V
                                                         int(row[21])) #W
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
