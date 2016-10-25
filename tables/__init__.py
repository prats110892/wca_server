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

	if category.lower() == DataCategories.CALCULATIONS.lower() :
		print("Inside calculations")
		parseAndInsertCalculationsData(csv_file, table_name, from_Date, to_Date)
