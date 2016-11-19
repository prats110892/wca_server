from tables.base_table_class import Base_Table

class INCOME_GROSS_RENT_PERCENT_INCOME_Table(Base_Table):

	table_name = "INCOME_GROSS_RENT_PERCENT_INCOME"

	def __init__(self) :
		self.table_name = INCOME_GROSS_RENT_PERCENT_INCOME_Table.table_name
		self.columns = Base_Table.columns + ["Total renter-occupied housing units","Less than $10,000","Less than 20.0 percent 1","20.0 to 24.9 percent 1","25.0 to 29.9 percent 1","30.0 to 34.9 percent 1","35.0 to 39.9 percent 1","40.0 to 49.9 percent 1","50.0 percent or more 1","Not computed 1","$10,000 to $19,999","Less than 20.0 percent 2","20.0 to 24.9 percent 2","25.0 to 29.9 percent 2","30.0 to 34.9 percent 2","35.0 to 39.9 percent 2","40.0 to 49.9 percent 2","50.0 percent or more 2","Not computed 2","$20,000 to $34,999","Less than 20.0 percent 3","20.0 to 24.9 percent 3","25.0 to 29.9 percent 3","30.0 to 34.9 percent 3","35.0 to 39.9 percent 3","40.0 to 49.9 percent 3","50.0 percent or more 3","Not computed 3","$35,000 to $49,999","Less than 20.0 percent 4","20.0 to 24.9 percent 4","25.0 to 29.9 percent 4","30.0 to 34.9 percent 4","35.0 to 39.9 percent 4","40.0 to 49.9 percent 4","50.0 percent or more 4","Not computed 4","$50,000 to $74,999","Less than 20.0 percent 5","20.0 to 24.9 percent 5","25.0 to 29.9 percent 5","30.0 to 34.9 percent 5","35.0 to 39.9 percent 5","40.0 to 49.9 percent 5","50.0 percent or more 5","Not computed 5","$75,000 to $99,999","Less than 20.0 percent 6","20.0 to 24.9 percent 6","25.0 to 29.9 percent 6","30.0 to 34.9 percent 6","35.0 to 39.9 percent 6","40.0 to 49.9 percent 6","50.0 percent or more 6","Not computed 6","$100,000 or more","Less than 20.0 percent 7","20.0 to 24.9 percent 7","25.0 to 29.9 percent 7","30.0 to 34.9 percent 7","35.0 to 39.9 percent 7","40.0 to 49.9 percent 7","50.0 percent or more 7","Not computed 7"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d \
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[5]), #D
                                                         int(row[6]), #E
										int(row[7]), #F
                                                         int(row[8]), #G
										int(row[9]), #H
                                                         int(row[10]), #I
										int(row[11]), #J
                                                         int(row[12]), #K
										int(row[13]), #L
                                                         int(row[14]), #M
										int(row[15]), #N
                                                         int(row[16]), #O
										int(row[17]), #P
                                                         int(row[18]), #Q
										int(row[19]), #R
                                                         int(row[20]), #S
										int(row[21]), #T
                                                         int(row[22]), #U
										int(row[23]), #V
                                                         int(row[24]), #W
										int(row[25]), #X
                                                         int(row[26]), #Y
										int(row[27]), #Z
                                                         int(row[28]), #AA
										int(row[29]), #AB
										int(row[30]), #AC
										int(row[31]), #AD
                                                         int(row[32]), #AE
										int(row[33]), #AF
                                                         int(row[34]), #AG
										int(row[35]), #AH
                                                         int(row[36]), #AI
										int(row[37]), #AJ
                                                         int(row[38]), #AK
										int(row[39]), #AL
                                                         int(row[40]), #AM
										int(row[41]), #AN
                                                         int(row[42]), #AO
										int(row[43]), #AP
                                                         int(row[44]), #AQ
										int(row[45]), #AR
                                                         int(row[46]), #AS
										int(row[47]), #AT
                                                         int(row[48]), #AU
										int(row[49]), #AV
                                                         int(row[50]), #AW
										int(row[51]), #AX
                                                         int(row[52]), #AY
										int(row[53]), #AZ
                                                         int(row[54]), #BA
										int(row[55]), #BB
										int(row[56]), #BC
										int(row[57]), #BD
                                                         int(row[58]), #BE
										int(row[59]), #BF
                                                         int(row[60]), #BG
										int(row[61]), #BH
                                                         int(row[62]), #BI
										int(row[63]), #BJ
                                                         int(row[64]), #BK
										int(row[65]), #BL
                                                         int(row[66])) #BM
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
