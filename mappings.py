from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
import sys, getopt


def getQuery(xl_sheet, tableName) :
	return {
		"RelationshipChildren" : mapFunction_relationship_children(xl_sheet)
	}[tableName]

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
