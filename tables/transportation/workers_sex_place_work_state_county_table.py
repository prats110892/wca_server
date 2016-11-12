from tables.base_table_class import Base_Table

class WORKERS_SEX_PLACE_WORK_STATE_COUNTY_Table(Base_Table):

	table_name = "WORKERS_SEX_PLACE_WORK_STATE_COUNTY"

	def __init__(self) :
		self.table_name = WORKERS_SEX_PLACE_WORK_STATE_COUNTY_Table.table_name
		self.columns = Base_Table.columns + ["Total workers 16 years and over","Worked in Georgia","Worked outside Georgia","Worked in Georgia","Worked in county of residence","Worked outside county of residence"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[7]), #D
                                                         int(row[4]), #E
										int(row[5]), #F
                                                         int(row[6])) #G
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
