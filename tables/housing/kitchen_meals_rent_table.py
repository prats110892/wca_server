from tables.base_table_class import Base_Table

class KITCHEN_MEALS_RENT_Table(Base_Table):

	table_name = "KITCHEN_MEALS_RENT"

	def __init__(self) :
		self.table_name = KITCHEN_MEALS_RENT_Table.table_name
		self.columns = Base_Table.columns + ["Total renter-occupied housing units paying cash rent","Meals included in rent","No meals included in rent","Complete kitchen facilities:","Meals included in rent","No meals included in rent","Lacking complete kitchen facilities","Meals included in rent","No meals included in rent"]
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
										int(row[4])+int(row[8]), #C
										int(row[6])+int(row[9]), #D
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
