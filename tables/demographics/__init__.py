from hispanic_origin_table import HISPANIC_ORIGIN_Table
from household_language_limited_table import HOUSEHOLD_LANGUAGE_LIMITED_Table
from household_relationship_table import HOUSEHOLD_RELATIONSHIP_Table
from median_age_sex_table import MEDIAN_AGE_SEX_Table
from race_table import RACE_Table
from relationship_65_table import RELATIONSHIP_65_Table
from relationship_children_table import RELATIONSHIP_CHILDREN_Table
from sex_age_veteran_table import SEX_AGE_VETERAN_Table
from sex_marital_status_table import SEX_MARITAL_STATUS_Table

def parseAndInsertDemographicData(csvFile, tableName) :
	return {
             MEDIAN_AGE_SEX_Table.table_name : MEDIAN_AGE_SEX_Table().insertDataFromCSVFile(csvFile),
             RACE_Table.table_name : RACE_Table().insertDataFromCSVFile(csvFile),
             HISPANIC_ORIGIN_Table.table_name : HISPANIC_ORIGIN_Table().insertDataFromCSVFile(csvFile),
             RELATIONSHIP_CHILDREN_Table.table_name : RELATIONSHIP_CHILDREN_Table().insertDataFromCSVFile(csvFile),
             HOUSEHOLD_RELATIONSHIP_Table.table_name : HOUSEHOLD_RELATIONSHIP_Table().insertDataFromCSVFile(csvFile),
             RELATIONSHIP_65_Table.table_name : RELATIONSHIP_65_Table().insertDataFromCSVFile(csvFile),
             SEX_MARITAL_STATUS_Table.table_name : SEX_MARITAL_STATUS_Table().insertDataFromCSVFile(csvFile),
             HOUSEHOLD_LANGUAGE_LIMITED_Table.table_name : HOUSEHOLD_LANGUAGE_LIMITED_Table().insertDataFromCSVFile(csvFile),
             SEX_AGE_VETERAN_Table.table_name : SEX_AGE_VETERAN_Table().insertDataFromCSVFile(csvFile)
	}[tableName]
