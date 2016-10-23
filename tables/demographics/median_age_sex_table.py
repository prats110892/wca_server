from tables.base_table_class import Base_Table
import csv

class MEDIAN_AGE_SEX_Table(Base_Table):
	"The definition of the Median_Age_Sex in the database"

	table_name = "MEDIAN_AGE_SEX"
	columns = 	Base_Table.columns + ["Total", "Under 5 years",
	 			"5 to 9 years", "10 to 14 years", "15 to 17 years",
				"18 and 19 years", "20 years", "21 years",
				"22 to 24 years", "25 to 29 years", "30 to 34 years",
				"35 to 39 years", "40 to 44 years", "45 to 49 years",
				"50 to 54 years", "55 to 59 years", "60 and 61 years",
				"62 to 64 years", "65 and 66 years", "67 to 69 years",
				"70 to 74 years", "75 to 79 years", "80 to 84 years",
				"85 years and over", "Total", "Under 5", "5 to 17",
				"18 to 24 years", "25 to 39 years", "40 to 64 years",
				"65 years and over", "75 years and over", "85 years and over"]

	def __init__(self) :
		Base_Table.__init__()

	def getInsertQueryForCSV(self, csvReader) :
		skipCount = 0
		insertDataQuery = "INSERT INTO " + table_name + " VALUES "
		for row in csvReader:
			if (skipCount < num_of_rows_to_leave) :
				skipCount += 1
				continue
			insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
	                               %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
	                               %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d),\
	                               " %(row[0],
																	int(row[3]), #B
																	int(row[5]+row[29]), #C
																	int(row[6]+row[30]), #D
																	int(row[7]+row[31]), #E
																	int(row[8]+row[32]), #F
																	int(row[9]+row[33]), #G
																	int(row[10]+row[34]), #H
																	int(row[11]+row[35]), #I
																	int(row[12]+row[36]), #J
																	int(row[13]+row[37]), #K
																	int(row[14]+row[38]), #L
																	int(row[15]+row[39]), #M
																	int(row[16]+row[40]), #N
																	int(row[17]+row[41]), #O
																	int(row[18]+row[42]), #P
																	int(row[19]+row[43]), #Q
																	int(row[20]+row[44]), #R
																	int(row[21]+row[45]), #S
																	int(row[22]+row[46]), #T
																	int(row[23]+row[47]), #U
																	int(row[24]+row[48]), #V
																	int(row[25]+row[49]), #W
																	int(row[26]+row[50]), #X
																	int(row[27]+row[51]), #Y
																	int(row[3]), #Z
																	int(row[5]+row[29]), #AA
																	int(row[6]+row[7]+row[8]+row[30]+row[31]+row[32]), #AB
																	int(row[9]+row[10]+row[11]+row[12]row[33]+row[34]+row[35]+row[36]), #AC
																	int(row[13]+row[14]+row[15]+row[37]+row[38]+row[39]), #AD
																	int(row[16]+row[17]+row[18]+row[19]+row[20]+row[21]+row[40]+row[41]+row[42]+row[43]+row[44]+row[45]), #AE
																	int(row[22]+row[23]+row[24]+row[25]+row[26]+row[27]+row[46]+row[47]+row[48]+row[49]+row[50]+row[51]), #AF
																	int(row[25]+row[26]+row[27]+row[49]+row[50]+row[51]), #AG
																	int(row[27]+row[51])) #AH

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
