from tables.base_table_class import Base_Table

class HOUSEHOLD_LANGUAGE_LIMITED_Table(Base_Table):
	"The definition of the Household Language Limited Table in the database"

	table_name = "HOUSEHOLD_LANGUAGE_LIMITED"

	def __init__(self) :
		self.table_name = HOUSEHOLD_LANGUAGE_LIMITED_Table.table_name
		self.columns = Base_Table.columns + ["Total Households",
					"English only",
					"Spanish",
		 			"Indo-European languages",
					"Asian and Pacific Island languages",
					"Other Languages",
					"Spanish Category",
					"Spanish: Limited English speaking household",
					"Spanish: Not a limited English speaking household",
					"Indo-European languages Category",
					"Indo-European: Limited English speaking household",
					"Indo-European: Not a limited English speaking household",
					"Asian and Pacific Island languages Category",
					"Asian and Pacific: Limited English speaking household",
					"Asian and Pacific: Not a limited English speaking household",
					"Other languages Category",
					"Other: Limited English speaking household",
					"Other: Not a limited English speaking household",
					"Total Households English vs Not Limited English",
					"Limited english speaking",
					"Not limited English speaking"]

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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
	                     %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
						 int(row[4]), #C
						 int(row[5]), #D
						 int(row[8]), #E
						 int(row[11]), #F
						 int(row[14]), #G
						 int(row[5]), #H
						 int(row[6]), #I
						 int(row[7]), #J
						 int(row[8]), #K
						 int(row[9]), #L
						 int(row[10]), #M
						 int(row[11]), #N
						 int(row[12]), #O
						 int(row[13]), #P
						 int(row[14]), #Q
						 int(row[15]), #R
						 int(row[16]), #S
						 int(row[3]), #T
						 int(row[6])+int(row[9])+int(row[12])+int(row[15]), #U
						 int(row[7])+int(row[10])+int(row[13])+int(row[16]))
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
