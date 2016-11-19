from tables.base_table_class import Base_Table

class BEDROOMS_GROSS_RENT_Table(Base_Table):

	table_name = "BEDROOMS_GROSS_RENT"

	def __init__(self) :
		self.table_name = BEDROOMS_GROSS_RENT_Table.table_name
		self.columns = Base_Table.columns + ["Total renter-occupied housing units","No bedroom","Less than $200 1","$200 to $299 1","$300 to $499 1","$500 to $749 1","$750 to $999 1","$1,000 or more 1","No cash rent 1","1 bedroom","Less than $200 2","$200 to $299 2","$300 to $499 2","$500 to $749 2","$750 to $999 2","$1,000 or more 2","No cash rent 2","2 bedrooms","Less than $200 3","$200 to $299 3","$300 to $499 3","$500 to $749 3","$750 to $999 3","$1,000 or more 3","No cash rent 3","3 or more bedrooms","Less than $200 4","$200 to $299 4","$300 to $499 4","$500 to $749 4","$750 to $999 4","$1,000 or more 4","No cash rent 4"]
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
                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
										int(row[4]), #C
										int(row[6]), #D
                                                         int(row[7]), #E
										int(row[8]), #F
                                                         int(row[9]), #G
										int(row[10]), #H
                                                         int(row[11]), #I
										int(row[12]), #J
                                                         int(row[13]), #K
										int(row[15]), #L
                                                         int(row[16]), #M
										int(row[17]), #N
                                                         int(row[18]), #O
										int(row[19]), #P
                                                         int(row[20]), #Q
										int(row[21]), #R
                                                         int(row[22]), #S
										int(row[24]), #T
                                                         int(row[25]), #U
										int(row[26]), #V
                                                         int(row[27]), #W
										int(row[28]), #X
                                                         int(row[29]), #Y
										int(row[30]), #Z
                                                         int(row[31]), #AA
										int(row[33]), #AB
                                                         int(row[34]), #AC
										int(row[35]), #AD
                                                         int(row[36]), #AE
										int(row[37]), #AF
                                                         int(row[38]), #AG
                                                         int(row[39])) #AH
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
