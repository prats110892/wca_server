from tables.base_table_class import Base_Table

class RENT_ASKED_Table(Base_Table):

	table_name = "RENT_ASKED"

	def __init__(self) :
		self.table_name = RENT_ASKED_Table.table_name
		self.columns = Base_Table.columns + ["Total vacant-for-rent and rent, not occupied housing units","Less than $100","$100 to $149","$150 to $199","$200 to $249","$250 to $299","$300 to $349","$350 to $399","$400 to $449","$450 to $499","$500 to $549","$550 to $599","$600 to $649","$650 to $699","$700 to $749","$750 to $799","$800 to $899","$900 to $999","$1,000 to $1,249","$1,250 to $1,499","$1,500 to $1,999","$2,000 or more"]
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
                       %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
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
                                                         int(row[24])) #W	
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
