from age_own_children_living_arrangements_employment_table import AGE_OWN_CHILDREN_LIVING_ARRANGEMENTS_EMPLOYMENT_Table
from employment_table import EMPLOYMENT_Table
from full_time_year_round_work_table import FULL_TIME_YEAR_ROUND_WORK_Table
from own_children_employment_status_table import OWN_CHILDREN_EMPLOYMENT_STATUS_Table
from poverty_disability_employment_table import POVERTY_DISABILITY_EMPLOYMENT_Table
from sex_class_table import SEX_CLASS_Table
from sex_hours_worked_week_16_65_table import SEX_HOURS_WORKED_WEEK_16_65_Table
from sex_hours_worked_week_over65_table import SEX_HOURS_WORKED_WEEK_OVER65_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 AGE_OWN_CHILDREN_LIVING_ARRANGEMENTS_EMPLOYMENT_Table.table_name : AGE_OWN_CHILDREN_LIVING_ARRANGEMENTS_EMPLOYMENT_Table(),
		 EMPLOYMENT_Table.table_name : EMPLOYMENT_Table(),
		 FULL_TIME_YEAR_ROUND_WORK_Table.table_name : FULL_TIME_YEAR_ROUND_WORK_Table(),
		 OWN_CHILDREN_EMPLOYMENT_STATUS_Table.table_name : OWN_CHILDREN_EMPLOYMENT_STATUS_Table(),
		 POVERTY_DISABILITY_EMPLOYMENT_Table.table_name : POVERTY_DISABILITY_EMPLOYMENT_Table(),
		 SEX_CLASS_Table.table_name : SEX_CLASS_Table(),
		 SEX_HOURS_WORKED_WEEK_16_65_Table.table_name : SEX_HOURS_WORKED_WEEK_16_65_Table(),
		 SEX_HOURS_WORKED_WEEK_OVER65_Table.table_name : SEX_HOURS_WORKED_WEEK_OVER65_Table(),
}

def getTableName(client_table_name) :
	return {
			'Age_Own_Children_Living_Arrangements_Employment' : AGE_OWN_CHILDREN_LIVING_ARRANGEMENTS_EMPLOYMENT_Table.table_name,
			'Employment' : EMPLOYMENT_Table.table_name,
			'Full_Time_Year_Round_Work' : FULL_TIME_YEAR_ROUND_WORK_Table.table_name,
			'Own_Children_Employment_Status' : OWN_CHILDREN_EMPLOYMENT_STATUS_Table.table_name,
			'Poverty_Disability_Employment' : POVERTY_DISABILITY_EMPLOYMENT_Table.table_name,
			'Sex_Class_Table' : SEX_CLASS_Table.table_name,
			'Sex_Hours_Worked_Week_16_65' : SEX_HOURS_WORKED_WEEK_16_65_Table.table_name,
			'Sex_Hours_Worked_Week_Over65' : SEX_HOURS_WORKED_WEEK_OVER65_Table.table_name,
	}[client_table_name]

def getTableObject(client_table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(client_table_name)]

def parseAndInsertEmploymentData(csvFile, tableName, fromDate, toDate) :
	stored_table_name = getTableName(tableName)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	return tableObject.insertDataFromCSVFile(csvFile, fromDate, toDate)
