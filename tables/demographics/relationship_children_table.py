from tables.base_table_class import Base_Table
import csv

class RELATIONSHIP_CHILDREN_Table(Base_Table):
	"The definition of the Relationship Children Table in the database"

	num_of_rows_to_leave = 2
	table_name = "RELATIONSHIP_CHILDREN"
	columns = 	Base_Table.columns + ["Estimate: Total",
				"Estimate: Own child - Biological child",
	 			"Estimate: Own child - Adopted child",
				"Estimate: Own child - Stepchild",
				"Estimate: Grandchild",
				"Estimate: Other relatives",
				"Estimate: Foster child or Other Unrelated child"]

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
			dataQuery = "%d, %d, %d, %d, %d, %d, %d" %(int(row[3]),
														int(row[5]),
														int(row[6]),
														int(row[7]),
														int(row[8]),
														int(row[9]),
														int(row[10]))
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery
