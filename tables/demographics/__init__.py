from hispanic_origin_table import HISPANIC_ORIGIN_Table
from household_language_limited_table import HOUSEHOLD_LANGUAGE_LIMITED_Table
from household_relationship_table import HOUSEHOLD_RELATIONSHIP_Table
from median_age_sex_table import MEDIAN_AGE_SEX_Table
from race_table import RACE_Table
from relationship_65_table import RELATIONSHIP_65_Table
from relationship_children_table import RELATIONSHIP_CHILDREN_Table
from sex_age_veteran_table import SEX_AGE_VETERAN_Table
from sex_marital_status_table import SEX_MARITAL_STATUS_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 MEDIAN_AGE_SEX_Table.table_name : MEDIAN_AGE_SEX_Table(),
		 RACE_Table.table_name : RACE_Table(),
		 HISPANIC_ORIGIN_Table.table_name : HISPANIC_ORIGIN_Table(),
		 RELATIONSHIP_CHILDREN_Table.table_name : RELATIONSHIP_CHILDREN_Table(),
		 HOUSEHOLD_RELATIONSHIP_Table.table_name : HOUSEHOLD_RELATIONSHIP_Table(),
		 RELATIONSHIP_65_Table.table_name : RELATIONSHIP_65_Table(),
		 SEX_MARITAL_STATUS_Table.table_name : SEX_MARITAL_STATUS_Table(),
		 HOUSEHOLD_LANGUAGE_LIMITED_Table.table_name : HOUSEHOLD_LANGUAGE_LIMITED_Table(),
		 SEX_AGE_VETERAN_Table.table_name : SEX_AGE_VETERAN_Table()
}

def getTableName(client_table_name) :
	return {
			'Median_Age_Sex' : MEDIAN_AGE_SEX_Table.table_name,
			'Race' : RACE_Table.table_name,
			'Hispanic_Origin' : HISPANIC_ORIGIN_Table.table_name,
			'Relationship_Children' : RELATIONSHIP_CHILDREN_Table.table_name,
			'Household_Relationship' : HOUSEHOLD_RELATIONSHIP_Table.table_name,
			'Relationship_65' : RELATIONSHIP_65_Table.table_name,
			'Sex_Marital_Status' : SEX_MARITAL_STATUS_Table.table_name,
			'Household_Language_Limited' : HOUSEHOLD_LANGUAGE_LIMITED_Table.table_name,
			'Sex_Age_Veteran': SEX_AGE_VETERAN_Table.table_name
	}[client_table_name]

def getDemographicsTableObject(client_table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(client_table_name)]

def parseAndInsertDemographicData(csvFile, tableName, fromDate, toDate) :
	stored_table_name = getTableName(tableName)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	return tableObject.insertDataFromCSVFile(csvFile, fromDate, toDate)
