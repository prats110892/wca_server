import MySQLdb
import os
import math
from tables import Dbhelper




#this was used to initialize the calculations table
#this functionality doesn't exist yet in the web app as far as I could see
createQuery = "CREATE TABLE CALC_NPU (Id VARCHAR(50), "

for i in range(26) :
	 createQuery = createQuery + chr(i + 97) + " DOUBLE, "

createQuery = createQuery[:-2] + ");"

#print(createQuery)

def __init__(self) :
	self.db = None

#I'm connecting to the database in this file
#TODO: switch it so the executes are handled in Dbhelper
self = MySQLdb.connect(host="localhost",  # your host, usually localhost
							user="root",         # your username
							passwd="coolness",
							db="wca_data_dashboard")

#don't think I use this one
def executeQuery(query) :
	#self.openConnection()
	cursor = self.cursor()
	cursor.execute(query)
	self.commit()
	self.close()
	return cursor

#executeQuery(createQuery);


#loads data into calc_npu
cursor = self.cursor()
"""f = open("calcnpu.csv", 'r')
for line in f :
	insertQuery = "insert into CALC_NPU values (" + line + ");"
	print
	#cursor.execute(insertQuery)
"""

data_table_name = 'RELATIONSHIP_CHILDREN'
region_table_name = 'CALC_NPU'
data_year = 2011

def getColumnNames(table_name) :
	getColumnsQuery = "SELECT `COLUMN_NAME` " \
	"FROM `INFORMATION_SCHEMA`.`COLUMNS` " \
	"WHERE `TABLE_SCHEMA`='wca_data_dashboard' " \
    "AND `TABLE_NAME`="
	getColumnsQuery = getColumnsQuery + "\'" + table_name + "\';"
	cursor.execute(getColumnsQuery)
	return cursor.fetchall()

def getData(table_name) :
	selectQuery = "SELECT * FROM " + table_name + ";"
	cursor.execute(selectQuery)
	return cursor.fetchall()

def getMostRecentYear(fromYear, table_name) :
	pass



#todo: generalize to a function(year, table, region)
#take in region, year, tablename
def makeCSV(dataYear, data_table_name, region_table_name) :
	#this gets a matrix of all the calc_npu data
	#TODO: make sure it handles the possibility of multiple years for the same region
		#get the most recent valid year (make a separate function for this)
	regionTableMatrix = getData(region_table_name)

	#this can probably be gotten from base table metadata. 
	calc_cols_to_skip = 1;
	rel_child_cols_to_skip = 3



	dataTableMatrix = getData(data_table_name)
	#print(dataTableMatrix[1])

	columnsListData = getColumnNames(data_table_name)
	columnsListCalc = getColumnNames(region_table_name)

	fileToWrite = open(data_table_name + "_" + region_table_name + ".csv", 'w')

	variableName = ''
	#this loops through all the variables (data table columns)
	for variableIndex in range(len(dataTableMatrix[0]) - rel_child_cols_to_skip - 1) :

		variableWritten = 0
		#this loops through all the regions (calc table columns)
		for regionIndex in range(len(regionTableMatrix[0]) - 1) :
			#we are getting a sum, so this is our running total.
			total = 0
			#this loops through the rows of data and selects a cell at a time
			for i in range(len(regionTableMatrix) - 1) :
				#this is a basically a cell of data. It is a total for a given variable in one census tract
				censusTractTotal = int(dataTableMatrix[i+1][variableIndex + rel_child_cols_to_skip])

				#this is the percent (float from 0 to 1) of the current census tract in a given region.
				#its basically a cell in the calculations table
				  #as an example, 0.0462 of census tract '130670303391' is inside NPU 'A'
				percentInCurrentRegion = float(regionTableMatrix[i][regionIndex + calc_cols_to_skip])
				#so we multiply the total for a variable * the percent in the region
				#the sum all of these will give us the total for a variable for a region
				  #effectively, we are 
				total = total + (censusTractTotal * percentInCurrentRegion)

			#TODO: write to a csv rather than printing
			if(variableWritten == 0) :
				variableName = str(columnsListData[variableIndex + rel_child_cols_to_skip + 1])[2:-3]
				variableWritten = 1
			else :
				variableName = ''
			regionString = str(columnsListCalc[regionIndex + calc_cols_to_skip])[2:-3]
			totalString = str(round(total))

			outputLine = variableName + ", " + regionString + ", " + totalString
			#write to the CSV (comma separated columns, newline separated rows)
			fileToWrite.write(outputLine + "\n")


makeCSV(data_year, data_table_name, region_table_name)

