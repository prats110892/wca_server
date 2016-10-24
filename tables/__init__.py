from id_table import ID_Table
from demographics import parseAndInsertDemographicData
from calculations import parseAndInsertCalculationsData
from categories import DataCategories

def updateIdTableWithNewCSVFile(csvFile) :
	return id_table.ID_Table().insertDataFromCSVFile(csvFile)

def parseAndInsertData(category, csvFile, tableName, fromDate, toDate) :
	return {
		DataCategories.DEMOGRAPHICS : parseAndInsertDemographicData(csvFile, tableName, fromDate, toDate)
		DataCategories.CALCULATIONS : parseAndInsertCalculationsData(csvFile, tableName, fromDate, toDate)
	}[category]
