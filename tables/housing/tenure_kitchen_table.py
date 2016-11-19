from tables.base_table_class import Base_Table

class TENURE_KITCHEN_Table(Base_Table):

	table_name = "TENURE_KITCHEN"

	def __init__(self) :
		self.table_name = TENURE_KITCHEN_Table.table_name
		self.columns = Base_Table.columns + ["Total occupied housing units","Owner occupied","Complete kitchen facilities 1","Lacking complete kitchen facilities 1","Renter occupied","Complete kitchen facilities 2","Lacking complete kitchen facilities 2"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[5]), #D
                                                         int(row[6]), #E
										int(row[7]), #F
                                                         int(row[8]), #G
										int(row[9])) #H
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
