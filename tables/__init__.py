from id_table import ID_Table
from demographics import parseAndInsertDemographicData
from calculations import parseAndInsertCalculationsData
from categories import DataCategories
import base_table_class
import basic_calc_table
import Dbhelper

def updateIdTableWithNewCSVFile(csvFile) :
	return id_table.ID_Table().insertDataFromCSVFile(csvFile)

def parseAndInsertData(category, csv_file, table_name, from_Date, to_Date) :
	print(category)
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
