from tables.base_table_class import Base_Table

class POVERTY_DISABILITY_EMPLOYMENT_Table(Base_Table):

	table_name = "POVERTY_DISABILITY_EMPLOYMENT"

	def __init__(self) :
		self.table_name = POVERTY_DISABILITY_EMPLOYMENT_Table.table_name
		self.columns = Base_Table.columns + ["Total population 20 to 64 years","Below poverty level 1","At or above poverty level 1","Below poverty level 2","With a disability 1","No disability 1","At or above poverty level 2","With a disability 2","No disability 2","With a disability - Below poverty level","Employed 1","Unemployed 1","Not in labor force 1","No disability - below poverty","Employed 2","Unemployed 2","Not in labor force 2","At or above poverty with disability","Employed 3","Unemployed 3","Not in labor force 3","At or above poverty no disability","Employed","Unemployed","Not in labor force"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[4]), #B
										int(row[5]), #C
										int(row[6]), #D
                                                         int(row[7]), #E
										int(row[8]), #F
                                                         int(row[9]), #G
										int(row[10]), #H
                                                         int(row[11]), #I
										int(row[12]), #J
                                                         int(row[13]), #K
										int(row[14]), #L
                                                         int(row[15]), #M
										int(row[16]), #N
                                                         int(row[17]), #O
										int(row[18]), #P
                                                         int(row[19]), #Q
										int(row[20]), #R
                                                         int(row[21]), #S
										int(row[22]), #T
                                                         int(row[23]), #U
										int(row[24]), #V
                                                         int(row[25]), #W
										int(row[26]), #X
                                                         int(row[27]), #Y
										int(row[28])) #Z
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
