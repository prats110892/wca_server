from bachelors_table import BACHELORS_Table
from educational_attainment_table import EDUCATIONAL_ATTAINMENT_Table
from sex_school_enrollment_attainment_16_19_table import SEX_SCHOOL_ENROLLMENT_ATTAINMENT_16_19_Table
from sex_school_enrollment_level_table import SEX_SCHOOL_ENROLLMENT_LEVEL_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 BACHELORS_Table.table_name : BACHELORS_Table(),
		 EDUCATIONAL_ATTAINMENT_Table.table_name : EDUCATIONAL_ATTAINMENT_Table(),
		 SEX_SCHOOL_ENROLLMENT_ATTAINMENT_16_19_Table.table_name : SEX_SCHOOL_ENROLLMENT_ATTAINMENT_16_19_Table(),
		 SEX_SCHOOL_ENROLLMENT_LEVEL_Table.table_name : SEX_SCHOOL_ENROLLMENT_LEVEL_Table(),
}

def getTableName(client_table_name) :
	return {
			'Bachelors' : BACHELORS_Table.table_name,
			'Educational_Attainment' : EDUCATIONAL_ATTAINMENT_Table.table_name,
			'Sex_School_Enrollment_Attainment_16_19' : SEX_SCHOOL_ENROLLMENT_ATTAINMENT_16_19_Table.table_name,
			'Sex_School_Enrollment_Level' : SEX_SCHOOL_ENROLLMENT_LEVEL_Table.table_name,
	}[client_table_name]

def getEducationTableObject(client_table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(client_table_name)]

def parseAndInsertEducationData(csvFile, tableName, fromDate, toDate) :
	stored_table_name = getTableName(tableName)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	return tableObject.insertDataFromCSVFile(csvFile, fromDate, toDate)
