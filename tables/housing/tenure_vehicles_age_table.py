from tables.base_table_class import Base_Table

class TENURE_VEHICLES_AGE_Table(Base_Table):

	table_name = "TENURE_VEHICLES_AGE"

	def __init__(self) :
		self.table_name = TENURE_VEHICLES_AGE_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied: - No vehicle available","Householder 15 to 34 years 1","Householder 35 to 64 years 1","Householder 65 years and over 1","Owner occupied: - 1 or more vehicles available","Householder 15 to 34 years 2","Householder 35 to 64 years 2","Householder 65 years and over 2","Renter occupied: - No vehicle available","Householder 15 to 34 years 3","Householder 35 to 64 years 3","Householder 65 years and over 3","Renter occupied: - 1 or more vehicles available","Householder 15 to 34 years 4","Householder 35 to 64 years 4","Householder 65 years and over 4"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[5]), #B
										int(row[6]), #C
										int(row[7]), #D
                                                         int(row[8]), #E
										int(row[9]), #F
                                                         int(row[10]), #G
										int(row[11]), #H
                                                         int(row[12]), #I
										int(row[14]), #J
                                                         int(row[15]), #K
										int(row[16]), #L
                                                         int(row[17]), #M
										int(row[18]), #N
                                                         int(row[19]), #O
										int(row[20]), #P
                                                         int(row[21])) #Q
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
