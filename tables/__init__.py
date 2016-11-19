import os, sys
import time

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIRECTORY)

from id_table import ID_Table
from demographics import parseAndInsertDemographicData, getDemographicsTableObject
from education import parseAndInsertEducationData, getEducationTableObject
# from employment import parseAndInsertEmploymentData, getEmploymentTableObject
# from health import parseAndInsertHealthData, getHealthTableObject
# from housing import parseAndInsertHousingData, getHousingTableObject
# from income import parseAndInsertIncomeData, getIncomeTableObject
# from transportation import parseAndInsertTransportationData, getTransportationTableObject
from calculations import parseAndInsertCalculationsData, getCalculationsTableObject
from categories import DataCategories
import base_table_class
import basic_calc_table
import Dbhelper


TABLE_NAME_TO_OBJECT_MAPPING = {
		 ID_Table.table_name : ID_Table()
}

def getTableName(client_table_name) :
	return {
			'GEO_ID' : ID_Table.table_name
	}[client_table_name]

def getTableObject(category, table_name) :
		if (category.lower() == DataCategories.ID.lower()) :
			print("Inside ID")
			return TABLE_NAME_TO_OBJECT_MAPPING[table_name]

		if category.lower() == DataCategories.DEMOGRAPHICS.lower() :
			print("Inside Demographics")
			return getDemographicsTableObject(table_name)

		elif category.lower() == DataCategories.EDUCATION.lower() :
			print("Inside Education")
			return getEducationTableObject(table_name)

		elif category.lower() == DataCategories.EMPLOYMENT.lower() :
			print("Inside Employment")
			return getEmploymentTableObject(table_name)

		elif category.lower() == DataCategories.HEALTH.lower() :
			print("Inside Health")
			return getHealthTableObject(table_name)

		elif category.lower() == DataCategories.HOUSING.lower() :
			print("Inside Housing")
			return getHousingTableObject(table_name)

		elif category.lower() == DataCategories.INCOME.lower() :
			print("Inside Income")
			return getIncomeTableObject(table_name)

		elif category.lower() == DataCategories.TRANSPORTATION.lower() :
			print("Inside Transportation")
			return getTransportationTableObject(table_name)

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
