from tables.base_table_class import Base_Table

class RECEIPT_FOOD_SNAP_DISABILITY_Table(Base_Table):

	table_name = "RECEIPT_FOOD_SNAP_DISABILITY"

	def __init__(self) :
		self.table_name = RECEIPT_FOOD_SNAP_DISABILITY_Table.table_name
		self.columns = Base_Table.columns + ["Total households","Household received Food Stamps/SNAP in the past 12 months","Household did not receive Food Stamps/SNAP in the past 12 months","Household received Food Stamps/SNAP in the past 12 months","Households with 1 or more persons with a disability","Households with no persons with a disability","Household did not receive Food Stamps/SNAP in the past 12 months","Households with 1 or more persons with a disabil","Households with no persons with a disability"]
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
										int(row[7]), #D
                                                         int(row[4]), #E
										int(row[5]), #F
                                                         int(row[6]), #G
										int(row[7]), #H
                                                         int(row[8]), #I
										int(row[9])) #J
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
