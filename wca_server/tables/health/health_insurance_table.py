from tables.base_table_class import Base_Table

class HISPANIC_ORIGIN_Table(Base_Table):
	"The definition of the Hispanic Origin Table in the database"

	table_name = "HISPANIC_ORIGIN"

	def __init__(self) :
		self.table_name = HISPANIC_ORIGIN_Table.table_name
		self.columns = Base_Table.columns + ["Total civilian noninstitutionalized population","With one type of health insurance coverage:","With two or more types of health insurance coverage:","No health insurance coverage"]
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
			dataQuery = "%d, %d, %d, %d" %(int(row[3]), #B
										int(row[5])+int(row[21])+int(row[37])+int(row[54]), #C
										int(row[12])+int(row[28])+int(row[44])+int(row[60]), #D
                                                         int(row[19])+int(row[35])+int(row[52])+int(row[68])) #E
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
