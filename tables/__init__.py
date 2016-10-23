from id_table import ID_Table
from demographics import parseAndInsertDemographicData
from categories import DataCategories

def updateIdTableWithNewCSVFile(csvFile) :
	return id_table.ID_Table().insertDataFromCSVFile(csvFile)

def parseAndInsertData(category, csvFile, tableName) :
	return {
		DataCategories.DEMOGRAPHICS : parseAndInsertDemographicData(csvFile=csvFile, tableName=tableName)
	}[category]
