from tables.demographics import parseAndInsertDemographicData
from tables.calculations import parseAndInsertCalculationsData
from tables.categories import DataCategories
import base_table_class
import basic_calc_table
import Dbhelper
from id_table import ID_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 ID_Table.table_name : ID_Table()
}

def getTableName(client_table_name) :
	return {
			'Id_codes' : ID_Table.table_name
	}[client_table_name]

def updateIdTableWithNewCSVFile(csvFile, table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[getTableName(table_name)].insertDataFromCSVFile(csvFile)

def parseAndInsertData(category, csv_file, table_name, from_Date, to_Date) :
	print(category)
	if (category.lower() == DataCategories.ID.lower()) :
		print("Inside ID")
		updateIdTableWithNewCSVFile(csv_file, table_name)

	if category.lower() == DataCategories.DEMOGRAPHICS.lower() :
		print("Inside Demographics")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.EDUCATION.lower() :
		print("Inside Education")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.EMPLOYMENT.lower() :
		print("Inside Employment")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.HEALTH.lower() :
		print("Inside Health")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.HOUSING.lower() :
		print("Inside Housing")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.INCOME.lower() :
		print("Inside Income")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)
	elif category.lower() == DataCategories.TRANSPORTATION.lower() :
		print("Inside Transportation")
		parseAndInsertDemographicData(csv_file, table_name, from_Date, to_Date)

def parseAndInsertCalculations(csv_file, table_name, from_Date) :
	print("Inside calculations")
	parseAndInsertCalculationsData(csv_file, table_name, from_Date)
