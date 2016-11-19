from tables.base_table_class import Base_Table

class SEX_SCHOOL_ENROLLMENT_LEVEL_Table(Base_Table):

	table_name = "SEX_SCHOOL_ENROLLMENT_LEVEL"

	def __init__(self) :
		self.table_name = SEX_SCHOOL_ENROLLMENT_LEVEL_Table.table_name
		self.columns = Base_Table.columns + ["Total population 3 years and over","Enrolled in school","Not enrolled in school","Enrolled in school 2","Nursery school, preschool","Kindergarten","Grade 1 to grade 4","Grade 5 to grade 8","Grade 9 to grade 12","College undergraduate","Graduate or professional school","Enrolled in school 3","Public","Private","Enrolled in nursery school, preschool","Public 3","Private 2","Enrolled in kindergarten","Public 4","Private 3","Enrolled in grade 1 to grade 4","Public 5","Private 4","Enrolled in grade 5 to grade 8","Public 6","Private 5","Enrolled in grade 9 to grade 12","Public 7","Private 6","Enrolled in college undergraduate years","Public 8","Private 7","Enrolled in graduate or professional school","Public 9","Private 8"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, \
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[5])+int(row[29]), #C
										int(row[27])+int(row[51]), #D
                                                         int(row[5])+int(row[29]), #E
										int(row[6])+int(row[30]), #F
                                                         int(row[9])+int(row[33]), #G
										int(row[12])+int(row[36]), #H
                                                         int(row[15])+int(row[39]), #I
										int(row[18])+int(row[42]), #J
                                                         int(row[21])+int(row[45]), #K
										int(row[24])+int(row[48]), #L
                                                         int(row[5])+int(row[29]), #M
										int(row[7])+int(row[10])+int(row[13])+int(row[16])+int(row[19])+int(row[22])+int(row[25])+int(row[31])+int(row[34])+int(row[37])+int(row[40])+int(row[43])+int(row[46])+int(row[49]), #N
                                                         int(row[8])+int(row[11])+int(row[14])+int(row[17])+int(row[20])+int(row[23])+int(row[26])+int(row[32])+int(row[35])+int(row[38])+int(row[41])+int(row[44])+int(row[47])+int(row[50]), #O
										int(row[6])+int(row[30]), #P
                                                         int(row[7])+int(row[31]), #Q
										int(row[8])+int(row[32]), #R
                                                         int(row[9])+int(row[33]), #S
										int(row[10])+int(row[34]), #T
                                                         int(row[11])+int(row[35]), #U
										int(row[12])+int(row[36]), #V
                                                         int(row[13])+int(row[37]), #W
										int(row[14])+int(row[38]), #X
                                                         int(row[15])+int(row[39]), #Y
										int(row[16])+int(row[40]), #Z
                                                         int(row[17])+int(row[41]), #AA
										int(row[18])+int(row[42]), #AB
                                                         int(row[19])+int(row[43]), #AC
                                                         int(row[20])+int(row[44]), #AD
                                                         int(row[21])+int(row[45]), #AE
										int(row[22])+int(row[46]), #AF
                                                         int(row[23])+int(row[47]), #AG
										int(row[24])+int(row[48]), #AH
                                                         int(row[25])+int(row[49]), #AI
										int(row[26])+int(row[50])) #AJ
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
