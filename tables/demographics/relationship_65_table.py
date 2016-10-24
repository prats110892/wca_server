from tables.base_table_class import Base_Table
import csv

class RELATIONSHIP_65_Table(Base_Table):
	"The definition of the Relationship 65 Table in the database"

	num_of_rows_to_leave = 2
	table_name = "RELATIONSHIP_65"
	columns = 	Base_Table.columns +
				["Total Population in 65 years and over",
				"In households", "In group quarters",
	 			"Householder",
				"Male householder (in family and nonfamily households)",
				"Female householder (in family and nonfamily households)",
				"In Households", "Householder", "Spouse", "Parent",
				"Parent-in-law", "Other relatives", "Other nonrelatives",
				"In Households", "Male living alone", "Female living alone"]

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
	                  %d, %d, %d, %d, %d, %d" %(int(row[3]), #B
					  int(row[4]), #C
					  int(row[23]), #D
					  int(row[7]+row[16]+row[8]+row[19]), #E
					  int(row[7]+row[16]), #F
					  int(row[8]+row[19]), #G
					  int(row[4]), #H
					  int(row[7]+row[16]+row[8]+row[19]), #I
					  int(row[9]), #J
					  int(row[10]), #K
					  int(row[11]), #L
					  int(row[12]), #M
					  int(row[4]-row[7]-row[16]-row[8]-row[19]-row[9]-row[10]-row[11]-row[12]), #N
					  int(row[4]), #O
					  int(row[17]), #P
					  int(row[19])) #Q
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
