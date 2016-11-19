from tables.base_table_class import Base_Table

class HOUSEHOLD_65_Table(Base_Table):

	table_name = "HOUSEHOLD_65"

	def __init__(self) :
		self.table_name = HOUSEHOLD_65_Table.table_name
		self.columns = Base_Table.columns + ["Total households","Households with one or more people 65 years and over 1","Households with no people 65 years and over 1","Households with one or more people 65 years and over 2","1-person household","2-or-more-person household 1","Households with no people 65 years and over 2","1-person households","2-or-more-person household 2"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[9]), #D
                                                         int(row[4]), #E
										int(row[5]), #F
                                                         int(row[6]), #G
										int(row[9]), #H
                                                         int(row[10]), #I
                                                         int(row[11])) #J
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"
		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
