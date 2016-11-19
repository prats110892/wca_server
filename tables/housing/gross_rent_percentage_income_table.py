from tables.base_table_class import Base_Table

class GROSS_RENT_PERCENTAGE_INCOME_Table(Base_Table):

	table_name = "GROSS_RENT_PERCENTAGE_INCOME"

	def __init__(self) :
		self.table_name = GROSS_RENT_PERCENTAGE_INCOME_Table.table_name
		self.columns = Base_Table.columns + ["Total renter-occupied housing units","Less than 10.0 percent","10.0 to 14.9 percent","15.0 to 19.9 percent","20.0 to 24.9 percent","25.0 to 29.9 percent","30.0 to 34.9 percent","35.0 to 39.9 percent","40.0 to 49.9 percent","50.0 percent or more","Not computed"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[5]), #D
                                                         int(row[6]), #E
										int(row[7]), #F
                                                         int(row[8]), #G
										int(row[9]), #H
                                                         int(row[10]), #I
										int(row[11]), #J
                                                         int(row[12]), #K
										int(row[13])) #L
                insertDataQuery += "(" + defaultQuery + dataQuery + "),"
                insertDataQuery += "(" + defaultQuery + dataQuery + "),"
                
		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
