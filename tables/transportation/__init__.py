from means_transpo_table import MEANS_TRANSPO_Table
from mobility_msa_table import MOBILITY_MSA_Table
from time_leaving_work_table import TIME_LEAVING_WORK_Table
from travel_time_table import TRAVEL_TIME_Table
from workers_sex_place_work_state_county_table import WORKERS_SEX_PLACE_WORK_STATE_COUNTY_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 MEANS_TRANSPO_Table.table_name : MEANS_TRANSPO_Table(),
		 MOBILITY_MSA_Table.table_name : MOBILITY_MSA_Table(),
		 TIME_LEAVING_WORK_Table.table_name : TIME_LEAVING_WORK_Table(),
		 TRAVEL_TIME_Table.table_name : TRAVEL_TIME_Table(),
		 WORKERS_SEX_PLACE_WORK_STATE_COUNTY_Table.table_name : WORKERS_SEX_PLACE_WORK_STATE_COUNTY_Table(),
}

def getTableName(client_table_name) :
	return {
			'Means_Transpo' : MEANS_TRANSPO_Table.table_name,
			'Mobility_Msa' : MOBILITY_MSA_Table.table_name,
			'Time_Leaving_Work' : TIME_LEAVING_WORK_Table.table_name,
			'Travel_Time' : TRAVEL_TIME_Table.table_name,
			'Workers_Sex_Place_Work_State_County' : WORKERS_SEX_PLACE_WORK_STATE_COUNTY_Table.table_name,
	}[client_table_name]

def getTableObject(client_table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(client_table_name)]

def parseAndInsertDemographicData(csvFile, tableName, fromDate, toDate) :
	stored_table_name = getTableName(tableName)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	return tableObject.insertDataFromCSVFile(csvFile, fromDate, toDate)
