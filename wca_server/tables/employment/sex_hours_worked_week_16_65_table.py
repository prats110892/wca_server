from tables.base_table_class import Base_Table

class SEX_HOURS_WORKED_WEEK_16_65_Table(Base_Table):

	table_name = "SEX_HOURS_WORKED_WEEK_16_65"

	def __init__(self) :
		self.table_name = SEX_HOURS_WORKED_WEEK_16_65_Table.table_name
		self.columns = Base_Table.columns + ["Total population 16 to 64 years","Worked in the past 12 months:","Did not work in the past 12 months","Worked in the past 12 months","Usually worked 35 or more hours per week","Usually worked 15 to 34 hours per week","Usually worked 1 to 14 hours per week","Worked 1 to 13 weeks in the past 12 months","14 to 26 weeks","27 to 39 weeks","40 to 47 weeks","48 and 49 weeks","50 to 52 weeks"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[5])+int(row[29]), #C
										int(row[27])+int(row[51]), #D
                                                         int(row[5])+int(row[29]), #E
										int(row[6])+int(row[30]), #F
                                                         int(row[13])+int(row[37]), #G
										int(row[20])+int(row[44]), #H
                                                         int(row[11]), #I
										int(row[11])+int(row[18])+int(row[25])+int(row[35])+int(row[42])+int(row[49]), #J
                                                         int(row[10])+int(row[17])+int(row[24])+int(row[34])+int(row[41])+int(row[48]), #K
										int(row[9])+int(row[16])+int(row[23])+int(row[33])+int(row[40])+int(row[47]), #L
                                                         int(row[8])+int(row[15])+int(row[22])+int(row[32])+int(row[39])+int(row[46]), #M
										int(row[7])+int(row[14])+int(row[21])+int(row[31])+int(row[38])+int(row[45])) #N
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
