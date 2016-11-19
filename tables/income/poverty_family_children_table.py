from tables.base_table_class import Base_Table

class POVERTY_FAMILY_CHILDREN_Table(Base_Table):

	table_name = "POVERTY_FAMILY_CHILDREN"

	def __init__(self) :
		self.table_name = POVERTY_FAMILY_CHILDREN_Table.table_name
		self.columns = Base_Table.columns + ["Total number of families","In poverty 1","At or above poverty 1","In poverty 2","In poverty Families with children under 5","In Poverty Families with children under 18","At or above poverty 2","Not in Poverty Families with children under 5","Not in poverty families under 18"]
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
										int(row[24]), #D
                                                         int(row[4]), #E
										int(row[7])+int(row[8])+int(row[14])+int(row[15])+int(row[20])+int(row[21]), #F
                                                         int(row[6])+int(row[13])+int(row[19]), #G
										int(row[24]), #H
                                                         int(row[27])+int(row[28])+int(row[34])+int(row[35])+int(row[40])+int(row[41]), #I
										int(row[26])+int(row[33])+int(row[39])) #J
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
