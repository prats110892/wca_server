from tables.base_table_class import Base_Table

class BEDROOMS_GROSS_RENT_Table(Base_Table):

	table_name = "BEDROOMS_GROSS_RENT"

	def __init__(self) :
		self.table_name = BEDROOMS_GROSS_RENT_Table.table_name
		self.columns = Base_Table.columns + ["Total renter-occupied housing units","No bedroom","Less than $200","$200 to $299","$300 to $499","$500 to $749","$750 to $999","$1,000 or more","No cash rent","1 bedroom","Less than $200","$200 to $299","$300 to $499","$500 to $749","$750 to $999","$1,000 or more","No cash rent","2 bedrooms","Less than $200","$200 to $299","$300 to $499","$500 to $749","$750 to $999","$1,000 or more","No cash rent","3 or more bedrooms","Less than $200","$200 to $299","$300 to $499","$500 to $749","$750 to $999","$1,000 or more","No cash rent"]
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
