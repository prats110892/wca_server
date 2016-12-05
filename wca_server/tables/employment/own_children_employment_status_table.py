from tables.base_table_class import Base_Table

class OWN_CHILDREN_EMPLOYMENT_STATUS_Table(Base_Table):

	table_name = "OWN_CHILDREN_EMPLOYMENT_STATUS"

	def __init__(self) :
		self.table_name = OWN_CHILDREN_EMPLOYMENT_STATUS_Table.table_name
		self.columns = Base_Table.columns + ["With own children under 6 years for females 20-64 years old","In labor force 1","Not in labor force 1","With own children under 18 years for females 20-64 years old","In labor force 2","Not in labor force 2","No own children under 18 years for females 20-64 years old","In labor force 3","Not in labor force 3","With own children under 6 years for in labor force females 20-64 years old","Employed 1","Unemployed 1","With own children under 18 years for in labor force females 20-64 years old","Employed 2","Unemployed 2","No own children under 18 years for in labor force females 20-64 years old","Employed 3","Unemployed 3","Total females 20 to 64 years in households","With own children under 6 years ","With own children under 18 years:","No own children under 18 years:"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, \
                       %d, %d, %d, %d, %d, %d" %(int(row[6])+int(row[11])+int(row[13])+int(row[18]), #B
										int(row[6])+int(row[13]), #C
										int(row[11])+int(row[18]), #D
                                                         int(row[6])+int(row[11])+int(row[13])+int(row[18])+int(row[20])+int(row[25]), #E
										int(row[6])+int(row[13])+int(row[20]), #F
                                                         int(row[11])+int(row[18])+int(row[25]), #G
										int(row[26]), #H
                                                         int(row[27]), #I
										int(row[32]), #J
                                                         int(row[6])+int(row[13]), #K
										int(row[9])+int(row[16]), #L
                                                         int(row[10])+int(row[17]), #M
										int(row[6])+int(row[13])+int(row[20]), #N
                                                         int(row[9])+int(row[16])+int(row[23]), #O
										int(row[10])+int(row[17])+int(row[24]), #P
                                                         int(row[27]), #Q
										int(row[30]), #R
                                                         int(row[31]), #S
										int(row[3]), #T
                                                         int(row[6])+int(row[11])+int(row[13])+int(row[18]), #U
										int(row[4]), #V
                                                         int(row[27])+int(row[32])) #W
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
