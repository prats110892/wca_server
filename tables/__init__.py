from id_table import ID_Table
from demographics import parseAndInsertDemographicData
from education import parseAndInsertEducationData
from employment import parseAndInsertEmploymentData
from health import parseAndInsertHealthData
from housing import parseAndInsertHousingData
from income import parseAndInsertIncomeData
from transportation import parseAndInsertTransportationData
from calculations import parseAndInsertCalculationsData
from categories import DataCategories
import base_table_class
import basic_calc_table
import Dbhelper
import wca_server

TABLE_NAME_TO_OBJECT_MAPPING = {
		 ID_Table.table_name : ID_Table()
}

def getTableName(client_table_name) :
	return {
			'GEO_ID' : ID_Table.table_name
	}[client_table_name]

def updateIdTableWithNewCSVFile(csvFile, table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(table_name)].insertDataFromCSVFile(csvFile)

def parseAndInsertData(category, csv_file, table_name, from_Date, to_Date) :
	print(category)
	if (category.lower() == DataCategories.ID.lower()) :
		print("Inside ID")
		updateIdTableWithNewCSVFile(csvFile=csv_file)

	if category.lower() == DataCategories.DEMOGRAPHICS.lower() :
		print("Inside Demographics")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.EDUCATION.lower() :
		print("Inside Education")
		parseAndInsertEducationData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.EMPLOYMENT.lower() :
		print("Inside Employment")
		parseAndInsertEmploymentData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.HEALTH.lower() :
		print("Inside Health")
		parseAndInsertHealthData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.HOUSING.lower() :
		print("Inside Housing")
		parseAndInsertHousingData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.INCOME.lower() :
		print("Inside Income")
		parseAndInsertIncomeData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.TRANSPORTATION.lower() :
		print("Inside Transportation")
		parseAndInsertTransportationData(csv_file, table_name, from_Date, to_Date)

def parseAndInsertCalculations(csv_file, table_name, from_Date) :
	print("Inside calculations")
	parseAndInsertCalculationsData(csv_file, table_name, from_Date)
