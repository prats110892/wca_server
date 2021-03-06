# this file is used to create the output CSV for a class of data and a given region
# it also has the function which creates the JSON for the API functionality

import os
from tables.Dbhelper import Dbhelper
from tables.base_table_class import Base_Table
from tables.basic_calc_table import Base_Calc_Table

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = CURRENT_DIRECTORY + "/uploads"


class Base_Output_Table(object):
	"This is the base table class that all other table classes will extend"

	def initalize(self, forYear, dataTableObject, calcTableObject) :
		self.dbHelper = Dbhelper()
		self.forYear = forYear
		self.calcTableObject = calcTableObject
		self.dataTableObject = dataTableObject
		self.dataTableObjectName = dataTableObject.table_name
		self.calcTableObjectName = calcTableObject.table_name
		self.columns = ["Year", self.calcTableObjectName]
		self.populateMatrices()

	#this function is used to get the column names for a table
	
	#it calls the virtual SQL table INFORMATION_SCHEMA which has all the 
	#metadata for a given table
	def getColumnNames(self, table_name) :
		getColumnsQuery = "SELECT `COLUMN_NAME` " \
		"FROM `INFORMATION_SCHEMA`.`COLUMNS` " \
		"WHERE `TABLE_SCHEMA`='wca_data_dashboard' " \
	    "AND `TABLE_NAME`="
		getColumnsQuery = getColumnsQuery + "\'" + table_name + "\';"
		return self.dbHelper.executeQuery(getColumnsQuery).fetchall()

	#this is used to get the sums for a data attribute
	
	#these are pre-calculated in the Excel spreadsheets we work with, 
	#so its not necessary to get the sums ourselves. 
	def getSumNumbers(self, table_name) :
		#321M200US131206004000 is the GEO_ID for the whole city of atlanta.
		#selecting this row is useful because it contains the total of each column for Atlanta
		selectQuery = """SELECT * FROM `{0}` WHERE Id = '321M200US131206004000' AND `{1}` <= {3} AND `{2}` >= {3};""".format(self.dataTableObjectName, Base_Table.columns[0], Base_Table.columns[1], self.forYear)

		return self.dbHelper.executeQuery(selectQuery).fetchall()

	#this populates the matrices that we loop through in this file
	
	#it selects all the data from the DB, then we work with the arrays in the other functions
	def populateMatrices(self) :
		self.dataMatrix = []
		self.calcMatrix = []
		selectQuery = """SELECT * FROM `{0}` a INNER JOIN `{1}` b ON a.`Id` = b.`Id` WHERE a.`{2}` <= {4} AND a.`{3}` >= {4} AND b.`{5}`={6}""".format(self.dataTableObjectName, self.calcTableObjectName, Base_Table.columns[0], Base_Table.columns[1], int(self.forYear), Base_Calc_Table.columns[0], self.getImmediateCalcYear(self.forYear))
		joinedData = self.dbHelper.executeQuery(selectQuery).fetchall()

		for row in joinedData :
			self.dataMatrix.append(row[:len(self.dataTableObject.columns)])
			self.calcMatrix.append(row[len(self.dataTableObject.columns):])

	# this is used to make sure we are getting the most recent possible year for a calc file
	
	# its possible to have multiple years of calc files, since the regions can change
	# so, we want to use the most recent one that works with the data we have
	def getImmediateCalcYear(self, requestedYear) :
		query = "SELECT `{0}` FROM `{1}` WHERE `{0}`<={2};".format(Base_Calc_Table.columns[0], self.calcTableObjectName, requestedYear)
		cursor = self.dbHelper.executeQuery(query)
		immediateYear = -1;
		for row in cursor :
			if (int(row[0]) > immediateYear) :
				immediateYear = int(row[0])
		return immediateYear

	#this is the function that actually makes the CSV file

	#it creates a new CSV and returns the path to the new file
	def getOutputCSVPath(self) :
		#this gets a matrix of all the calc_npu data
		regionTableMatrix = self.calcMatrix
		dataTableMatrix = self.dataMatrix

		#print (len(regionTableMatrix))
		#print (len(dataTableMatrix))

		#this can probably be gotten from base table metadata.
		calc_cols_to_skip = len(Base_Calc_Table.columns)
		data_cols_to_skip = len(Base_Table.columns)

		#print(dataTableMatrix[1])

		columnsListData = self.getColumnNames(self.dataTableObjectName)
		columnsListCalc = self.getColumnNames(self.calcTableObjectName)

		fileName = self.dataTableObjectName + "_" + self.calcTableObjectName + ".csv"
		fileToWrite = open(fileName, 'w')

		outputLine = 'Descriptor, Region Unit, Variable Region Population, Variable Atlanta Population, Region Total Population, Atlanta Total Population'
		#write to the CSV (comma separated columns, newline separated rows)
		fileToWrite.write(outputLine + "\n")

		variableName = ''
		#this loops through all the variables (data table columns)
		#totalAtlantaPopulation = 0


		sumVals = self.getSumNumbers(self.dataTableObjectName)
		totalAtlantaPopulation = int(sumVals[0][data_cols_to_skip])

		for variableIndex in range(data_cols_to_skip, len(dataTableMatrix[0])) :
			variableWritten = 0
			#this loops through all the regions (calc table columns)
			for regionIndex in range(calc_cols_to_skip, len(regionTableMatrix[0])) :
				#we are getting a sum, so this is our running total.
				variableRegionPopulation = 0

				#VariableAtlanta and TotalAtlanta are already calculated, so I'm just pulling a row from the DB basically.
				variableAtlantaPopulation = int(sumVals[0][variableIndex])
				totalAtlantaPopulation = int(sumVals[0][data_cols_to_skip])
				totalRegionPopulation = 0
				#this loops through the rows of data and selects a cell at a time
				for i in range(len(regionTableMatrix)) :
					#this is a basically a cell of data. It is a total for a given variable in one census tract
					censusTractTotal = int(dataTableMatrix[i][variableIndex])

					#this is the percent (float from 0 to 1) of the current census tract in a given region.
					#its basically a cell in the calculations table
					  #as an example, 0.0462 of census tract '130670303391' is inside NPU 'A'
					percentInCurrentRegion = float(regionTableMatrix[i][regionIndex])
					#so we multiply the total for a variable * the percent in the region
					#the sum of all of these will give us the total for a variable for a region
					if (percentInCurrentRegion > 0 and variableIndex == data_cols_to_skip  and regionIndex == calc_cols_to_skip) :
						print (str(i) + " " + str(censusTractTotal) + " " + str(percentInCurrentRegion))
					variableRegionPopulation += (censusTractTotal * percentInCurrentRegion)

					#to calculate totalRegionPopulation, we use data from the total column (column 3)
					  #that's why its dataTableMatrix[i][data_cols_to_skip]
					totalRegionPopulation += (int(dataTableMatrix[i][data_cols_to_skip]) * percentInCurrentRegion)

					if (percentInCurrentRegion > 0 and variableIndex == data_cols_to_skip  and regionIndex == calc_cols_to_skip) :
						print (str(i) + " " + str(totalAtlantaPopulation) + " " + str(percentInCurrentRegion))


				if (variableIndex == data_cols_to_skip) :
					#totalAtlantaPopulation = variableAtlantaPopulation
					pass

				else :
					if (variableWritten == 0) :
						variableName = str(columnsListData[variableIndex])[2:-3]
						variableWritten = 1
					else :
						variableName = ''

					regionString = str(columnsListCalc[regionIndex])[2:-3]
					variableRegionPopulationString = str(round(variableRegionPopulation))
					variableAtlantaPopulationString = str(variableAtlantaPopulation)
					totalRegionPopulationString = str(round(totalRegionPopulation))
					totalAtlantaPopulationString = str(totalAtlantaPopulation)

					outputLine = variableName + ", " + regionString + ", " + variableRegionPopulationString + ", " + variableAtlantaPopulationString + ", " + totalRegionPopulationString + ", " + totalAtlantaPopulationString
					# write to the CSV (comma separated columns, newline separated rows)
					fileToWrite.write(outputLine + "\n")

		fileToWrite.close()
		filename = fileToWrite.name
		os.rename(os.path.join(CURRENT_DIRECTORY, filename), os.path.join(UPLOAD_FOLDER, filename))
		return filename

	# this is similar to the CSV creator function, 
	# but instead of making a file, it returns a big JSON string
	
	# this is useful for the API call functionality
	def getJSON(self) :
		#this gets a matrix of all the calc_npu data
		regionTableMatrix = self.calcMatrix
		dataTableMatrix = self.dataMatrix

		calc_cols_to_skip = len(Base_Calc_Table.columns)
		data_cols_to_skip = len(Base_Table.columns)

		columnsListData = self.getColumnNames(self.dataTableObjectName)
		columnsListCalc = self.getColumnNames(self.calcTableObjectName)

		variableName = ''
		#this loops through all the variables (data table columns)
		#totalAtlantaPopulation = 0
		sumVals = self.getSumNumbers(self.dataTableObjectName)
		totalAtlantaPopulation = int(sumVals[0][data_cols_to_skip])

		jsonString = '{"total_atlanta_pop" : ' + str(totalAtlantaPopulation) + ','


		variablesString = '"variables_data" : ['
		regionsString = '"total_region_pops" : ['
		for variableIndex in range(data_cols_to_skip, len(dataTableMatrix[0])) :
			variableWritten = 0
			#this loops through all the regions (calc table columns)
			if(variableIndex != data_cols_to_skip) :

				variableAtlantaPopulation = int(sumVals[0][variableIndex])
				variablesString += '{"variable_name" : "' + str(columnsListData[variableIndex])[2:-3] + '",'
				variablesString += '"var_atlanta_pop" : ' +	str(variableAtlantaPopulation) + ','
				variablesString += '"region_data" : ['


			for regionIndex in range(calc_cols_to_skip, len(regionTableMatrix[0])) :
				#we are getting a sum, so this is our running total.
				variableRegionPopulation = 0

				#VariableAtlanta and TotalAtlanta are already calculated, so I'm just pulling a row from the DB basically.
				variableAtlantaPopulation = int(sumVals[0][variableIndex])
				totalAtlantaPopulation = int(sumVals[0][data_cols_to_skip])
				totalRegionPopulation = 0
				#this loops through the rows of data and selects a cell at a time
				for i in range(len(regionTableMatrix)) :
					#this is a basically a cell of data. It is a total for a given variable in one census tract
					censusTractTotal = int(dataTableMatrix[i][variableIndex])

					#this is the percent (float from 0 to 1) of the current census tract in a given region.
					#its basically a cell in the calculations table
					  #as an example, 0.0462 of census tract '130670303391' is inside NPU 'A'
					percentInCurrentRegion = float(regionTableMatrix[i][regionIndex])
					#so we multiply the total for a variable * the percent in the region
					#the sum of all of these will give us the total for a variable for a region
					if (percentInCurrentRegion > 0 and variableIndex == data_cols_to_skip  and regionIndex == calc_cols_to_skip) :
						#print (str(i) + " " + str(censusTractTotal) + " " + str(percentInCurrentRegion))
						pass
					variableRegionPopulation += (censusTractTotal * percentInCurrentRegion)

					#to calculate totalRegionPopulation, we use data from the total column (column 3)
					  #that's why its dataTableMatrix[i][data_cols_to_skip]
					totalRegionPopulation += (int(dataTableMatrix[i][data_cols_to_skip]) * percentInCurrentRegion)

					if (percentInCurrentRegion > 0 and variableIndex == data_cols_to_skip  and regionIndex == calc_cols_to_skip) :
						#print (str(i) + " " + str(totalAtlantaPopulation) + " " + str(percentInCurrentRegion))
						pass

				if (variableIndex == data_cols_to_skip) :
					regionString = str(columnsListCalc[regionIndex])[2:-3]
					variableRegionPopulationString = str(round(variableRegionPopulation))

					regionsString += ' {"region_name" : "' + regionString + '",'
					regionsString += '  "total_region_population" : ' + variableRegionPopulationString + '}, '

				else :
					if (variableWritten == 0) :
						variableName = str(columnsListData[variableIndex])[2:-3]
						variableWritten = 1
					else :
						variableName = ''

					regionString = str(columnsListCalc[regionIndex])[2:-3]
					variableRegionPopulationString = str(round(variableRegionPopulation))

					variableAtlantaPopulationString = str(variableAtlantaPopulation)
					totalRegionPopulationString = str(round(totalRegionPopulation))
					totalAtlantaPopulationString = str(totalAtlantaPopulation)

					variablesString += ' {"region_name" : "' + regionString + '",'
					variablesString += '  "var_region_population" : ' + variableRegionPopulationString + '}, '


			if(variableIndex != data_cols_to_skip) :
				variablesString = variablesString[:-2]
				variablesString += "]},"
			else :
				regionsString = regionsString[:-2]
				regionsString += "],"


		#return "output/" + fileName

		jsonString += regionsString
		jsonString += variablesString + "]"
		jsonString = jsonString[:-2] + "]}"
		#print(jsonString)
		return jsonString
