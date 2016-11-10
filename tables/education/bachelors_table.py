from tables.base_table_class import Base_Table

class BACHELORS_Table(Base_Table):

	table_name = "BACHELORS"

	def __init__(self) :
		self.table_name = BACHELORS_Table.table_name
		self.columns = Base_Table.columns + ["Total population 25 years and over with a bachelor's degree or higher attainment","Arts, Humanities, and Other","Business","Education","Science and Engineering","Total Science and Engineering","Computers, Mathematics and Statistics","Biological, Agricultural, and Environmental Sciences","Physical and Related Sciences","Psychology","Social Sciences","Engineering","Multidisciplinary Studies","Related Fields","Arts, Humanities, and Other","Literature and Languages","Liberal Arts and History","Visual and Performing Arts","Communications","Other"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, \
                       %d, %d, %d, %d" %(int(row[3]), #B
										int(row[14])+int(row[15])+int(row[16])+int(row[17])+int(row[18]), #C
										int(row[12]), #D
                                                         int(row[13]), #E
										int(row[4])+int(row[5])+int(row[6])+int(row[7])+int(row[8])+int(row[9])+int(row[10])+int(row[11]), #F
                                                         int(row[4])+int(row[5])+int(row[6])+int(row[7])+int(row[8])+int(row[9])+int(row[10])+int(row[11]), #G
										int(row[4]), #H
                                                         int(row[5]), #I
										int(row[6]), #J
                                                         int(row[7]), #K
										int(row[8]), #L
                                                         int(row[9]), #M
										int(row[10]), #N
                                                         int(row[11]), #O
										int(row[14])+int(row[15])+int(row[16])+int(row[17])+int(row[18]), #P
                                                         int(row[14]), #Q
										int(row[15]), #R
                                                         int(row[16]), #S
										int(row[17]), #T
                                                         int(row[18])) #U
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
