from tables.base_table_class import Base_Table

class SEX_SCHOOL_ENROLLMENT_ATTAINMENT_16_19_Table(Base_Table):

	table_name = "SEX_SCHOOL_ENROLLMENT_ATTAINMENT_16_19"

	def __init__(self) :
		self.table_name = SEX_SCHOOL_ENROLLMENT_ATTAINMENT_16_19_Table.table_name
		self.columns = Base_Table.columns + ["Population 16 to 19 years Enrolled in school","Employed","Unemployed","Not in labor force","Employed 16 - 19","High school graduate (includes equivalency): - Employed","Not high school graduate: - Employed","Unemployed 16-19","High school graduate (includes equivalency): - Unemployed","Not high school graduate: - Unemployed","Not in labor force 16-19","High school graduate(includes equivalency) Not in labor force","Not high school graduate: - Not in labor force","Not enrolled in school 16-19","Not enrolled in school: High school graduate","Not enrolled in school: Not High school graduate"]
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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[5])+int(row[19]), #B
										int(row[6])+int(row[20]), #C
										int(row[7])+int(row[21]), #D
                                                         int(row[8])+int(row[22]), #E
										int(row[11])+int(row[15])+int(row[25])+int(row[29]), #F
                                                         int(row[11])+int(row[25]), #G
										int(row[15])+int(row[29]), #H
                                                         int(row[12])+int(row[16])+int(row[26])+int(row[30]), #I
										int(row[12])+int(row[26]), #J
                                                         int(row[16])+int(row[30]), #K
										int(row[13])+int(row[17])+int(row[27])+int(row[31]), #L
                                                         int(row[13])+int(row[27]), #M
										int(row[17])+int(row[31]), #N
                                                         int(row[9])+int(row[23]), #O
										int(row[10])+int(row[24]), #P
                                                         int(row[14])+int(row[28])) #Q
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
