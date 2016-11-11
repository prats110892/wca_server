from tables.base_table_class import Base_Table

class FULL_TIME_YEAR_ROUND_WORK_Table(Base_Table):

	table_name = "FULL_TIME_YEAR_ROUND_WORK_Table"

	def __init__(self) :
		self.table_name = FULL_TIME_YEAR_ROUND_WORK_Table.table_name
		self.columns = Base_Table.columns + ["Total population 16 years and over","Worked full-time, year-round","Worked less than full-time, year","Did not work in the past 12 months","16 to 19 years","Worked in the past 12 months: - Worked full-time, year-round","Worked less than full-time, year-round","Did not work in the past 12 months","20 to 24 years","Worked full-time, year-round","Worked less than full-time, year-round","Did not work in the past 12 months","25 to 44 years","Worked full-time, year-round","Worked less than full-time, year-round","Did not work in the past 12 months","45 to 54 years","Worked full-time, year-round","Worked less than full-time, year-round","Did not work in the past 12 months","55 to 64 years","Worked full-time, year-round","Worked less than full-time, year-round","Did not work in the past 12 months","65 to 69 years","Worked full-time, year-round","Worked less than full-time, year-round","Did not work in the past 12 months","70 years and over","Worked full-time, year-round","Worked less than full-time, year-round","Did not work in the past 12 months"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[6])+int(row[11])+int(row[16])+int(row[21])+int(row[26])+int(row[31])+int(row[36]), #C
										int(row[7])+int(row[12])+int(row[17])+int(row[22])+int(row[27])+int(row[32])+int(row[37]), #D
                                                         int(row[8])+int(row[13])+int(row[18])+int(row[23])+int(row[28])+int(row[33])+int(row[38]), #E
										int(row[4]), #F
                                                         int(row[6]), #G
										int(row[7]), #H
                                                         int(row[8]), #I
										int(row[9]), #J
                                                         int(row[11]), #K
										int(row[12]), #L
                                                         int(row[13]), #M
										int(row[14]), #N
                                                         int(row[16]), #O
										int(row[17]), #P
                                                         int(row[18]), #Q
										int(row[19]), #R
                                                         int(row[21]), #S
										int(row[22]), #T
                                                         int(row[23]), #U
										int(row[24]), #V
                                                         int(row[26]), #W
										int(row[27]), #X
                                                         int(row[28]), #Y
										int(row[29]), #Z
                                                         int(row[31]), #AA
										int(row[32]), #AB
                                                         int(row[33]), #AC
                                                         int(row[34]), #AD
                                                         int(row[36]), #AE
										int(row[37]), #AF
                                                         int(row[38])) #AG
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
