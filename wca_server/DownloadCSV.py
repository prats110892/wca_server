import MySQLdb
import os
import math
from tables import Dbhelper

#i'm not sure if we still use this file -- I think the functionality has been superseded in base_output_table.py


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

