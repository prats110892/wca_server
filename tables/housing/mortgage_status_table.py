from tables.base_table_class import Base_Table

class MORTGAGE_STATUS_Table(Base_Table):

	table_name = "MORTGAGE_STATUS"

	def __init__(self) :
		self.table_name = MORTGAGE_STATUS_Table.table_name
		self.columns = Base_Table.columns + ["Total owner-occupied housing units","With a mortgage, contract to purchase, or similar debt 1","Without a mortgage","With a mortgage, contract to purchase, or similar debt 2","With either a second mortgage or home equity loan, but not both: - Second mortgage only","With either a second mortgage or home equity loan, but not both: - Home equity loan only","Both second mortgage and home equity loan","No second mortgage and no home equity loan"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[10]), #D
                                                         int(row[4]), #E
										int(row[6]), #F
                                                         int(row[7]), #G
										int(row[8]), #H
                                                         int(row[9])) #I
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
