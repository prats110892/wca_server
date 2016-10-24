from tables.base_table_class import Base_Table
import csv

class HOUSEHOLD_LANGUAGE_LIMITED_Table(Base_Table):
	"The definition of the Household Language Limited Table in the database"

	num_of_rows_to_leave = 2
	table_name = "HOUSEHOLD_LANGUAGE_LIMITED"
	columns = 	Base_Table.columns +
				["Total Households",
				"English only",
				"Spanish",
	 			"Indo-European languages",
				"Asian and Pacific Island languages",
				"Other Languages",
				"Spanish",
				"Spanish: Limited English speaking household",
				"Spanish: Not a limited English speaking household",
				"Indo-European languages",
				"Indo-European: Limited English speaking household",
				"Indo-European: Not a limited English speaking household",
				"Asian and Pacific Island languages",
				"Asian and Pacific: Limited English speaking household",
				"Asian and Pacific: Not a limited English speaking household",
				"Other languages",
				"Other: Limited English speaking household",
				"Other: Not a limited English speaking household",
				"Total Households",
				"Limited english speaking",
				"Not limited English speaking"]

	def __init__(self) :
		Base_Table.__init__()

	def getInsertQueryForCSV(self, csvReader, fromYear, toYear) :
		skipCount = 0
		insertDataQuery = "INSERT INTO " + table_name + " VALUES "
		for row in csvReader:
			if (skipCount < num_of_rows_to_leave) :
				skipCount += 1
				continue

			defaultQuery = Base_Table().getIDAndYearQueryForRow(row, fromYear, toYear)
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
						 int(row[6]+row[9]+row[12]+row[15]), #U
						 int(row[7]+row[10]+row[13]+row[16]))
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
