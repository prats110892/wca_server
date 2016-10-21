from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
import sys, getopt


def getQuery(xl_sheet, tableName) :
	return {
             "MedianAgeSex" : mapFunction_median_age_sex(xl_sheet),
             "Race" : mapFunction_race(xl_sheet),
             "HispanicOrigin" : mapFunction_hispanic_origin(xl_sheet),
             "RelationshipChildren" : mapFunction_relationship_children(xl_sheet),
             "HouseholdRelationship" : mapFunction_household_relationship(xl_sheet),
             "Relationship65" : mapFunction_relationship_65(xl_sheet),
             "SexMaritalStatus" : mapFunction_sex_marital_status(xl_sheet),
             "HouseholdLanguageLimited" : mapFunction_household_language_limited(xl_sheet),
             "SexAgeVeteran" : mapFunction_sex_age_veteran(xl_sheet)
	}[tableName]


 
def mapFunction_median_age_sex(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO MedianAgeSex VALUES "
	#print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                               %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                               %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d),\
                               " %(row[0].value,
																int(row[3].value), #B
																int(row[5].value+row[29].value), #C
																int(row[6].value+row[30].value), #D
																int(row[7].value+row[31].value), #E
																int(row[8].value+row[32].value), #F
																int(row[9].value+row[33].value), #G
																int(row[10].value+row[34].value), #H
																int(row[11].value+row[35].value), #I
																int(row[12].value+row[36].value), #J
																int(row[13].value+row[37].value), #K
																int(row[14].value+row[38].value), #L
																int(row[15].value+row[39].value), #M
																int(row[16].value+row[40].value), #N
																int(row[17].value+row[41].value), #O
																int(row[18].value+row[42].value), #P
																int(row[19].value+row[43].value), #Q
																int(row[20].value+row[44].value), #R
																int(row[21].value+row[45].value), #S
																int(row[22].value+row[46].value), #T
																int(row[23].value+row[47].value), #U
																int(row[24].value+row[48].value), #V
																int(row[25].value+row[49].value), #W
																int(row[26].value+row[50].value), #X
																int(row[27].value+row[51].value), #Y
																int(row[3].value), #Z
																int(row[5].value+row[29].value), #AA
																int(row[6].value+row[7].value+row[8].value+row[30].value+row[31].value+row[32].value), #AB
																int(row[9].value+row[10].value+row[11].value+row[12].valuerow[33].value+row[34].value+row[35].value+row[36].value), #AC
																int(row[13].value+row[14].value+row[15].value+row[37].value+row[38].value+row[39].value), #AD
																int(row[16].value+row[17].value+row[18].value+row[19].value+row[20].value+row[21].value+row[40].value+row[41].value+row[42].value+row[43].value+row[44].value+row[45].value), #AE
																int(row[22].value+row[23].value+row[24].value+row[25].value+row[26].value+row[27].value+row[46].value+row[47].value+row[48].value+row[49].value+row[50].value+row[51].value), #AF
																int(row[25].value+row[26].value+row[27].value+row[49].value+row[50].value+row[51].value), #AG
																int(row[27].value+row[51].value)) #AH

	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery

def mapFunction_race(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO Race VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d)," %(row[0].value,
																int(row[3].value), #B
																int(row[4].value), #C
																int(row[5].value), #D
																int(row[6].value), #E
																int(row[7].value), #F
																int(row[8].value), #G
																int(row[9].value), #H                                                                            
																int(row[10].value)) #I
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
 
def mapFunction_hispanic_origin(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO HispanicOrigin VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d)," %(row[0].value,
																int(row[3].value), #B
																int(row[4].value), #C
																int(row[5].value)) #D
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
 
def mapFunction_relationship_children(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO RelationshipChildren VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d)," %(row[0].value,
																int(row[3].value),
																int(row[5].value),
																int(row[6].value),
																int(row[7].value),
																int(row[8].value),
																int(row[9].value),
																int(row[10].value))
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
 
def mapFunction_household_relationship(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO HouseholdRelationship VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                               %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                               %d, %d)," %(row[0].value,
																int(row[3].value), #B
																int(row[4].value), #C
																int(row[40].value), #D
																int(row[6].value+row[27].value), #E
																int(row[7].value+row[28].value), #F
																int(row[8].value+row[29].value), #G
																int(row[4].value), #H
																int(row[6].value+row[27].value), #I
																int(row[9].value), #J
																int(row[10].value), #K
																int(row[14].value), #L
																int(row[15].value), #M
																int(row[16].value), #N
																int(row[17].value), #O
																int(row[18].value), #P
																int(row[19].value), #Q
																int(row[21].value+row[35].value), #R
																int(row[22].value+row[36].value), #S
																int(row[23].value+row[37].value), #T
																int(row[24].value+row[38].value), #U
																int(row[25].value+row[39].value), #V
																int(row[4].value), #W
																int(row[29].value), #X
																int(row[32].value)) #Y
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
 
def mapFunction_relationship_65(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO Relationship65 VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                  %d, %d, %d, %d, %d, %d)," %(row[0].value,
																int(row[3].value), #B
																int(row[4].value), #C
																int(row[23].value), #D
																int(row[7].value+row[16].value+row[8].value+row[19].value), #E
																int(row[7].value+row[16].value), #F
																int(row[8].value+row[19].value), #G
																int(row[4].value), #H
																int(row[7].value+row[16].value+row[8].value+row[19].value), #I
																int(row[9].value), #J
																int(row[10].value), #K
																int(row[11].value), #L
																int(row[12].value), #M
																int(row[4].value-row[7].value-row[16].value-row[8].value-row[19].value-row[9].value-row[10].value-row[11].value-row[12].value), #N
																int(row[4].value), #O
																int(row[17].value), #P
																int(row[19].value)) #Q
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
 
def mapFunction_sex_marital_status(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO SexMaritalStatus VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d)," %(row[0].value,
																int(row[3].value), #B
																int(row[5].value+row[14].value), #C
																int(row[6].value+row[15].value), #D
																int(row[9].value+row[18].value), #E
																int(row[12].value+row[21].value), #F
																int(row[11].value+row[20].value), #G
																int(row[6].value+row[15].value), #H
																int(row[7].value+row[16].value), #I					
																int(row[8].value+row[17].value)) #J
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
 
def mapFunction_household_language_limited(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO HouseholdLanguageLimited VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,\
                               %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d),\
                               " %(row[0].value,
																int(row[3].value), #B
																int(row[4].value), #C
																int(row[5].value), #D
																int(row[8].value), #E
																int(row[11].value), #F
																int(row[14].value), #G
																int(row[5].value), #H
																int(row[6].value), #I
																int(row[7].value), #J
																int(row[8].value), #K
																int(row[9].value), #L
																int(row[10].value), #M
																int(row[11].value), #N
																int(row[12].value), #O
																int(row[13].value), #P
																int(row[14].value), #Q
																int(row[15].value), #R
																int(row[16].value), #S
																int(row[3].value), #T
																int(row[6].value+row[9].value+row[12].value+row[15].value), #U
																int(row[7].value+row[10].value+row[13].value+row[16].value)) #V
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
 
def mapFunction_sex_age_veteran(sheetName) :
	fname = join(dirname(dirname(abspath(__file__))), 'Dataset', sheetName + ".xlsx")
	xl_workbook = xlrd.open_workbook(fname)
	xl_sheet = xl_workbook.sheet_by_index(0)

	insertDataQuery = "INSERT INTO SexAgeVeteran VALUES "
	print (xl_sheet.nrows)
	for i in range (2, xl_sheet.nrows) :
		row = xl_sheet.row(i)
		insertDataQuery += "('%s', %d, %d, %d)," %(row[0].value,
																int(row[3].value), #B
																int(row[4].value), #C
																int(row[5].value)) #D
	insertDataQuery = insertDataQuery[:-1]
	insertDataQuery += ";"
	return insertDataQuery
