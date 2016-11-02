import os

#This file takes the column list and data mappings and actually writes the .py file.

def writeFile(name, columnsList, dataQueryStr) :
	
	#TODO make this cleaner -- probably use a triple quote string and 1 outfile.write() call
	outFile = open(name.lower() + "_table.py", 'w')
	outFile.write("from tables.base_table_class import Base_Table\n")
	outFile.write("\n")
	outFile.write("class " + name.upper() + "_Table(Base_Table):\n")
	outFile.write("\t\"The definition of the " + name + " Table in the database\"\n\n")
	outFile.write("\ttable_name = \"" + name.upper() + "\"\n\n")
	outFile.write("\tdef __init__(self) :\n")
	outFile.write("\t\tself.table_name = " + name.upper() + "_Table.table_name\n")
	outFile.write("\t\tself.columns = Base_Table.columns + [\n")
	
	#this loops through the columns list and does some tabbing and newlines and stuff
	columns = ''
	for col in columnsList :
		columns = columns + "\t\t\t\"" + col + "\",\n"
	columns = columns[:-2] + "]\n"
	outFile.write(columns)

	outFile.write("\t\tself.table_extra_meta_data = Base_Table.table_extra_meta_data\n\n")
	outFile.write("\t\tself.initialize()\n\n")

	str1 = """\t
	def getInsertQueryForCSV(self, csvFile, fromYear, toYear) :
		skipCount = 0
		insertDataQuery = \"\"\"INSERT INTO `{0}` VALUES \"\"\".format(self.table_name)
		for line in csvFile:
			row = line.split(\",\")
			if (skipCount < Base_Table.num_of_rows_to_leave) :
				skipCount += 1
				continue

			defaultQuery = self.getIDAndYearQueryForRow(row, fromYear, toYear)\n"""

	outFile.write(str1)
	outFile.write("\t\t\tdataQuery = " + dataQueryStr)

	str1 = """
			insertDataQuery += "(" + defaultQuery + dataQuery + "),"

		insertDataQuery = insertDataQuery[:-1]
		insertDataQuery += ";"
		return insertDataQuery"""

	outFile.write(str1)



