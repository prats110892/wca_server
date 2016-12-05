from tables.base_table_class import Base_Table

class MEDIAN_AGE_SEX_Table(Base_Table):
	"The definition of the Median_Age_Sex in the database"

	table_name = "MEDIAN_AGE_SEX"
	def __init__(self) :
		self.table_name = MEDIAN_AGE_SEX_Table.table_name
		self.columns = Base_Table.columns + ["Total", "Under 5 years",
		 			"5 to 9 years", "10 to 14 years", "15 to 17 years",
					"18 and 19 years", "20 years", "21 years",
					"22 to 24 years", "25 to 29 years", "30 to 34 years",
					"35 to 39 years", "40 to 44 years", "45 to 49 years",
					"50 to 54 years", "55 to 59 years", "60 and 61 years",
					"62 to 64 years", "65 and 66 years", "67 to 69 years",
					"70 to 74 years", "75 to 79 years", "80 to 84 years",
					"85 years and over", "Total For Larger Age Brackets", "Under 5", "5 to 17",
					"18 to 24 years", "25 to 39 years", "40 to 64 years",
					"65 years and over", "75 years and over", "85 years and over Larger brackets"]

		self.table_extra_meta_data = Base_Table.table_extra_meta_data
		self.initalize()

	def getInsertQueryForCSV(self, csvFile, fromYear, toYear) :
		skipCount = 0
		insertDataQuery = """INSERT INTO `{0}` VALUES """.format(self.table_name)
		for line in csvFile:
			row = line.split(",")
			print(row)
			if (skipCount < Base_Table.num_of_rows_to_leave) :
				skipCount += 1
				continue

			defaultQuery = self.getIDAndYearQueryForRow(row, fromYear, toYear)
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
								   int(row[5])+int(row[29]), #C
								   int(row[6])+int(row[30]), #D
								   int(row[7])+int(row[31]), #E
								   int(row[8])+int(row[32]), #F
								   int(row[9])+int(row[33]), #G
								   int(row[10])+int(row[34]), #H
								   int(row[11])+int(row[35]), #I
								   int(row[12])+int(row[36]), #J
								   int(row[13])+int(row[37]), #K
								   int(row[14])+int(row[38]), #L
								   int(row[15])+int(row[39]), #M
								   int(row[16])+int(row[40]), #N
								   int(row[17])+int(row[41]), #O
								   int(row[18])+int(row[42]), #P
								   int(row[19])+int(row[43]), #Q
								   int(row[20])+int(row[44]), #R
								   int(row[21])+int(row[45]), #S
								   int(row[22])+int(row[46]), #T
								   int(row[23])+int(row[47]), #U
								   int(row[24])+int(row[48]), #V
								   int(row[25])+int(row[49]), #W
								   int(row[26])+int(row[50]), #X
								   int(row[27])+int(row[51]), #Y
								   int(row[3]), #Z
								   int(row[5])+int(row[29]), #AA
								   int(row[6])+int(row[7])+int(row[8])+int(row[30])+int(row[31])+int(row[32]), #AB
								   int(row[9])+int(row[10])+int(row[11])+int(row[12])+int(row[33])+int(row[34])+int(row[35])+int(row[36]), #AC
								   int(row[13])+int(row[14])+int(row[15])+int(row[37])+int(row[38])+int(row[39]), #AD
								   int(row[16])+int(row[17])+int(row[18])+int(row[19])+int(row[20])+int(row[21])+int(row[40])+int(row[41])+int(row[42])+int(row[43])+int(row[44])+int(row[45]), #AE
								   int(row[22])+int(row[23])+int(row[24])+int(row[25])+int(row[26])+int(row[27])+int(row[46])+int(row[47])+int(row[48])+int(row[49])+int(row[50])+int(row[51]), #AF
								   int(row[25])+int(row[26])+int(row[27])+int(row[49])+int(row[50])+int(row[51]), #AG
								   int(row[27])+int(row[51]))
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
