from tables.base_table_class import Base_Table

class HOUSEHOLD_TYPE_Table(Base_Table):

	table_name = "HOUSEHOLD_TYPE"

	def __init__(self) :
		self.table_name = HOUSEHOLD_TYPE_Table.table_name
		self.columns = Base_Table.columns + ["Total households","Married-couple family","Male householder, no wife present","Female householder, no husband present","Householder living alone","Householder living with nonfamiliy members"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[5]), #C
										int(row[7]), #D
                                                         int(row[8]), #E
										int(row[10]), #F
                                                         int(row[11])) #G
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
