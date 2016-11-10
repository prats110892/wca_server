from tables.base_table_class import Base_Table

class EDUCATIONAL_ATTAINMENT_Table(Base_Table):

	table_name = "EDUCATIONAL_ATTAINMENT"

	def __init__(self) :
		self.table_name = EDUCATIONAL_ATTAINMENT_Table.table_name
		self.columns = Base_Table.columns + ["Total population 25 years and over","No schooling completed","No high school","High school, no diploma","Regular high school diploma","GED or alternative credential","Some college, less than 1 year","Some college, 1 or more years, no degree","Associate's degree","Bachelor's degree","Master's degree","Professional school degree","Doctorate degree"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[4]), #B
										int(row[5]), #C
										int(row[6])+int(row[7])+int(row[8])+int(row[9])+int(row[10])+int(row[11])+int(row[12])+int(row[13])+int(row[14])+int(row[15]), #D
                                                         int(row[16])+int(row[17])+int(row[18])+int(row[19]), #E
										int(row[20]), #F
                                                         int(row[21]), #G
										int(row[22]), #H
                                                         int(row[23]), #I
										int(row[24]), #J
                                                         int(row[25]), #K
										int(row[26]), #L
                                                         int(row[27]), #M
										int(row[28])) #N
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
