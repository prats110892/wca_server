from tables.base_table_class import Base_Table

class SEX_CLASS_Table(Base_Table):

	table_name = "SEX_CLASS"

	def __init__(self) :
		self.table_name = SEX_CLASS_Table.table_name
		self.columns = Base_Table.columns + ["Total employed population 16 years and over","Private for-profit","Private not-for-profit","Local government","State government","Federal government","Self-employed in own not incorporated business","Unpaid family","Private for-profit workers","Employee of private company","Self-employed in own incorporated business"]
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
										int(row[5])+int(row[15]), #C
										int(row[8])+int(row[18]), #D
                                                         int(row[9])+int(row[19]), #E
										int(row[10])+int(row[20]), #F
                                                         int(row[11])+int(row[21]), #G
										int(row[12])+int(row[22]), #H
                                                         int(row[13])+int(row[23]), #I
										int(row[5])+int(row[15]), #J
                                                         int(row[6])+int(row[16]), #K
										int(row[7])+int(row[17])) #L
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
