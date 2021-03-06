from tables.base_table_class import Base_Table

class TENURE_BEDROOMS_Table(Base_Table):

	table_name = "TENURE_BEDROOMS"

	def __init__(self) :
		self.table_name = TENURE_BEDROOMS_Table.table_name
		self.columns = Base_Table.columns + ["Owner occupied","No bedroom 1","1 bedroom 1","2 bedrooms 1","3 bedrooms 1","4 bedrooms 1","5 or more bedrooms 1","Renter occupied","No bedroom 2","1 bedroom 2","2 bedrooms 2","3 bedrooms 2","4 bedrooms 2","5 or more bedrooms 2","Total occupied housing units","No bedroom 3","1 bedroom 3","2 bedrooms 3","3 bedrooms 3","4 bedrooms 3","5 or more bedrooms 3"]
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
                       %d, %d, %d, %d, %d" %(int(row[4]), #B
										int(row[5]), #C
										int(row[6]), #D
                                                         int(row[7]), #E
										int(row[8]), #F
                                                         int(row[9]), #G
										int(row[10]), #H
                                                         int(row[11]), #I
										int(row[12]), #J
                                                         int(row[13]), #K
										int(row[14]), #L
                                                         int(row[15]), #M
										int(row[16]), #N
                                                         int(row[17]), #O
										int(row[3]), #P
                                                         int(row[5])+int(row[12]), #Q
										int(row[6])+int(row[13]), #R
                                                         int(row[7])+int(row[14]), #S
										int(row[8])+int(row[15]), #T
                                                         int(row[9])+int(row[16]), #U
										int(row[10])+int(row[17])) #V
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
