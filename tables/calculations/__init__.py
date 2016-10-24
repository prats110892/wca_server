from aps_calc_table import APS_CALC_Table
from beltline_calc_table import BELTLINE_CALC_Table
from cd_calc_table import CD_CALC_Table
from choicepercent_calc_table import CHOICE_PERCENT_CALC_Table
from neighbourhood_calc_table import NEIGHBOURHOOD_CALC_Table
from npu_calc_table import NPU_CALC_Table
from tad_calc_table import TAD_CALC_Table
from zip_calc_table import ZIP_CALC_Table

def parseAndInsertCalculationsData(csvFile, tableName, fromDate, toDate) :
	return {
             APS_CALC_Table.table_name : APS_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate),
             BELTLINE_CALC_Table.table_name : BELTLINE_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate),
             CD_CALC_Table.table_name : CD_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate),
             CHOICE_PERCENT_CALC_Table.table_name : CHOICE_PERCENT_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate),
             NEIGHBOURHOOD_CALC_Table.table_name : NEIGHBOURHOOD_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate),
             NPU_CALC_Table.table_name : NPU_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate),
             TAD_CALC_Table.table_name : TAD_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate),
             ZIP_CALC_Table.table_name : ZIP_CALC_Table().insertDataFromCSVFile(csvFile, fromDate, toDate)
	}[tableName]
