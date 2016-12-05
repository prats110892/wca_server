from aps_calc_table import APS_CALC_Table
from beltline_calc_table import BELTLINE_CALC_Table
from cd_calc_table import CD_CALC_Table
from choicepercent_calc_table import CHOICE_PERCENT_CALC_Table
from neighbourhood_calc_table import NEIGHBOURHOOD_CALC_Table
from npu_calc_table import NPU_CALC_Table
from tad_calc_table import TAD_CALC_Table
from zip_calc_table import ZIP_CALC_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 APS_CALC_Table.table_name : APS_CALC_Table(),
		 BELTLINE_CALC_Table.table_name : BELTLINE_CALC_Table(),
		 CD_CALC_Table.table_name : CD_CALC_Table(),
		 CHOICE_PERCENT_CALC_Table.table_name : CHOICE_PERCENT_CALC_Table(),
		 NEIGHBOURHOOD_CALC_Table.table_name : NEIGHBOURHOOD_CALC_Table(),
		 NPU_CALC_Table.table_name : NPU_CALC_Table(),
		 TAD_CALC_Table.table_name : TAD_CALC_Table(),
		 ZIP_CALC_Table.table_name : ZIP_CALC_Table(),
}

def getTableName(client_table_name) :
	return {
			'APS' : APS_CALC_Table.table_name,
			'beltline' : BELTLINE_CALC_Table.table_name,
			'CD' : CD_CALC_Table.table_name,
			'choicePercent' : CHOICE_PERCENT_CALC_Table.table_name,
			'neighborhood' : NEIGHBOURHOOD_CALC_Table.table_name,
			'NPU' : NPU_CALC_Table.table_name,
			'TAD' : TAD_CALC_Table.table_name,
			'ZIP' : ZIP_CALC_Table.table_name,
	}[client_table_name]

def getCalculationsTableObject(calc_table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(calc_table_name)]

def parseAndInsertCalculationsData(csvFile, tableName, fromDate) :
	stored_table_name = getTableName(tableName)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	return tableObject.insertDataFromCSVFile(csvFile, fromDate)
