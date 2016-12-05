from tables.base_table_class import Base_Table

class AGE_OWN_CHILDREN_LIVING_ARRANGEMENTS_EMPLOYMENT_Table(Base_Table):

	table_name = "AGE_OWN_CHILDREN_LIVING_ARRANGEMENTS_EMPLOYMENT"

	def __init__(self) :
		self.table_name = AGE_OWN_CHILDREN_LIVING_ARRANGEMENTS_EMPLOYMENT_Table.table_name
		self.columns = Base_Table.columns + ["Total with own children under 18 years in families/subfamilies","Under 6 years:","Living with two parents 1","Living with one parent 1","6 to 17 years","Living with two parents 2","Living with one parent 2","Under 6 years","Living with two parents: - Both parents in labor force 2","Living with two parents: - Father only in labor force 2","Living with two parents: - Mother only in labor force 2","Living with two parents: - Neither parent in labor force 2","Under 6 years living with one parent (father only)","In labor force 2","Not in labor force 2","Under 6 years living with one parent (mother only)","In labor force 3","Not in labor force 3","6 to 17 years:","Living with two parents: - Both parents in labor force 3","Living with two parents: - Father only in labor force 3","Living with two parents: - Mother only in labor force 3","Living with two parents: - Neither parent in labor force 3","6 to 17 years: - Living with one parent: - father:","In labor force 4","Not in labor force 4","6 to 17 years: - Living with one parent: - mother:","In labor force 5","Not in labor force 5"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[5]), #D
                                                         int(row[10]), #E
										int(row[17]), #F
                                                         int(row[18]), #G
										int(row[23]), #H
                                                         int(row[4]), #I
										int(row[6]), #J
                                                         int(row[7]), #K
										int(row[8]), #L
                                                         int(row[9]), #M
										int(row[11]), #N
                                                         int(row[12]), #O
										int(row[13]), #P
                                                         int(row[14]), #Q
										int(row[15]), #R
                                                         int(row[16]), #S
										int(row[17]), #T
                                                         int(row[19]), #U
										int(row[20]), #V
                                                         int(row[21]), #W
										int(row[22]), #X
                                                         int(row[24]), #Y
										int(row[25]), #Z
                                                         int(row[26]), #AA
										int(row[27]), #AB
                                                         int(row[28]), #AC
										int(row[29])) #AD                                                         
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
