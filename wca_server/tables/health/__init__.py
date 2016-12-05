from health_insurance_table import HEALTH_INSURANCE_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 HEALTH_INSURANCE_Table.table_name : HEALTH_INSURANCE_Table(),
}

def getTableName(client_table_name) :
	return {
			'Health_Insurance' : HEALTH_INSURANCE_Table.table_name,
	}[client_table_name]

def getHealthTableObject(client_table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(client_table_name)]

def parseAndInsertHealthData(csvFile, tableName, fromDate, toDate) :
	stored_table_name = getTableName(tableName)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	return tableObject.insertDataFromCSVFile(csvFile, fromDate, toDate)
