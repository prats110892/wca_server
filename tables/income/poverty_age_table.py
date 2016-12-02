from tables.base_table_class import Base_Table

class POVERTY_AGE_Table(Base_Table):

	table_name = "POVERTY_AGE"

	def __init__(self) :
		self.table_name = POVERTY_AGE_Table.table_name
		self.columns = Base_Table.columns + ["Total","Below Poverty","Under 25 years 1","25 to 44 years 1","45 to 64 years 1","Below Poverty Over 65","At or Above Poverty","Under 25 years 2","25 to 44 years 2","45 to 64 years 2","At or Above Poverty 65"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[7])+int(row[13])+int(row[18])+int(row[24])+int(row[29]), #D
                                                         int(row[8])+int(row[14])+int(row[19])+int(row[25])+int(row[30]), #E
										int(row[9])+int(row[15])+int(row[20])+int(row[26])+int(row[31]), #F
                                                         int(row[10])+int(row[16])+int(row[21])+int(row[27])+int(row[32]), #G
										int(row[33]), #H
                                                         int(row[36])+int(row[42])+int(row[47])+int(row[53])+int(row[58]), #I
										int(row[37])+int(row[43])+int(row[48])+int(row[54])+int(row[59]), #J
                                                         int(row[38])+int(row[44])+int(row[49])+int(row[55])+int(row[60]), #K
										int(row[39])+int(row[45])+int(row[50])+int(row[56])+int(row[61])) #L
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
