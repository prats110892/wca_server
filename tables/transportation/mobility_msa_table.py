from tables.base_table_class import Base_Table

class MOBILITY_MSA_Table(Base_Table):

	table_name = "MOBILITY_MSA"

	def __init__(self) :
		self.table_name = MOBILITY_MSA_Table.table_name
		self.columns = Base_Table.columns + ["Total population 1 year and over living in a MSA","Same house 1 year ago","Different house in United States 1 year ago 1","Different house in United States 1 year ago 2","Moved from inside metro Atlanta","Moved from outside metro Atlanta","Lived abroad"]
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
                                                         int(row[5]), #E
										int(row[6]), #F
                                                         int(row[9]), #G
										int(row[16])) #H
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
