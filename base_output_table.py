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

	def getColumnNames(self, table_name) :
		getColumnsQuery = "SELECT `COLUMN_NAME` " \
		"FROM `INFORMATION_SCHEMA`.`COLUMNS` " \
		"WHERE `TABLE_SCHEMA`='wca_data_dashboard' " \
	    "AND `TABLE_NAME`="
		getColumnsQuery = getColumnsQuery + "\'" + table_name + "\';"
		return self.dbHelper.executeQuery(getColumnsQuery).fetchall()

	def getSumNumbers(self, table_name) :
		#321M200US131206004000 is the GEO_ID for the whole city of atlanta.
		#selecting this row is useful because it contains the total of each column for Atlanta
		selectQuery = """SELECT * FROM `{0}` WHERE Id = '321M200US131206004000' AND `{1}` <= {3} AND `{2}` >= {3};""".format(self.dataTableObjectName, Base_Table.columns[0], Base_Table.columns[1], self.forYear)

		return self.dbHelper.executeQuery(selectQuery).fetchall()

	def populateMatrices(self) :
		self.dataMatrix = []
		self.calcMatrix = []
		selectQuery = """SELECT * FROM `{0}` a INNER JOIN `{1}` b ON a.`Id` = b.`Id` WHERE a.`{2}` <= {4} AND a.`{3}` >= {4} AND b.`{5}`={6}""".format(self.dataTableObjectName, self.calcTableObjectName, Base_Table.columns[0], Base_Table.columns[1], int(self.forYear), Base_Calc_Table.columns[0], self.getImmediateCalcYear(self.forYear))
		joinedData = self.dbHelper.executeQuery(selectQuery).fetchall()

		for row in joinedData :
			self.dataMatrix.append(row[:len(self.dataTableObject.columns)])
			self.calcMatrix.append(row[len(self.dataTableObject.columns):])
		#print(str(len(self.dataMatrix)) + ", " + str(len(self.calcMatrix)))

	def getImmediateCalcYear(self, requestedYear) :
		query = "SELECT `{0}` FROM `{1}` WHERE `{0}`<={2};".format(Base_Calc_Table.columns[0], self.calcTableObjectName, requestedYear)
		cursor = self.dbHelper.executeQuery(query)
		immediateYear = -1;
		for row in cursor :
			if (int(row[0]) > immediateYear) :
				immediateYear = int(row[0])
		return immediateYear

	def getOutputCSVPath(self) :
		#this gets a matrix of all the calc_npu data
		regionTableMatrix = self.calcMatrix
		dataTableMatrix = self.dataMatrix

		print (len(regionTableMatrix))
		print (len(dataTableMatrix))

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

		jsonString = "{\"total_atlanta_pop\" : " + str(totalAtlantaPopulation) + ", \n"


		variablesString = "\"variables_data\" : [\n"
		regionsString = "\"total_region_pops\" : [\n"
		for variableIndex in range(data_cols_to_skip, len(dataTableMatrix[0])) :
			variableWritten = 0
			#this loops through all the regions (calc table columns)
			if(variableIndex != data_cols_to_skip) : 

				variableAtlantaPopulation = int(sumVals[0][variableIndex])
				variablesString += "{\"variable_name\" : \"" + str(columnsListData[variableIndex])[2:-3] + "\",\n"
				variablesString += "\"var_atlanta_pop\" : " +	str(variableAtlantaPopulation) + ",\n"
				variablesString += "\"region_data\" : [\n"


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

					regionsString += " {\"region_name\" : \"" + regionString + "\",\n"
					regionsString += "  \"total_region_population\" : " + variableRegionPopulationString + "}, \n"

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
					
					variablesString += " {\"region_name\" : \"" + regionString + "\",\n"
					variablesString += "  \"var_region_population\" : " + variableRegionPopulationString + "}, \n"


					# write to the CSV (comma separated columns, newline separated rows)
					#fileToWrite.write(outputLine + "\n")
			if(variableIndex != data_cols_to_skip) : 
				variablesString = variablesString[:-3]
				variablesString += "]},\n\n"
			else : 
				regionsString = regionsString[:-3]
				regionsString += "],"


		#return "output/" + fileName

		jsonString += regionsString
		jsonString += variablesString + "]"
		jsonString = jsonString[:-4] + "]}"
		print(jsonString)
		return jsonString


