from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
import sys, getopt
import MySQLdb

#print('Argument List:', str(sys.argv[1]))
#tableName = sys.argv[1]

# Open the workbook
fname = join(dirname(dirname(abspath(__file__))), 'Dataset', 'GeoID.xlsx')
xl_workbook = xlrd.open_workbook(fname)

# Or grab the first sheet by index
#  (sheets are zero-indexed)
#
xl_sheet = xl_workbook.sheet_by_index(0)

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
							user="root",         # your username
							passwd="aguamenti92",
							db="wca_data_dashboard")

cursor = db.cursor()

column1 = xl_sheet.cell_value(0, 0)
column2 = xl_sheet.cell_value(0, 1)
column3 = xl_sheet.cell_value(0, 2)

cursor.execute("DROP TABLE GeoID;")

createTableQuery = "CREATE TABLE GeoID(" + column1 + " VARCHAR(50) NOT NULL, " + column2 + " BIGINT, " + column3 + " VARCHAR(150), PRIMARY KEY(" + column1 + "));"
cursor.execute(createTableQuery)

insertDataQuery = "INSERT INTO GeoID VALUES "

for i in range(1, xl_sheet.nrows) :
	row = xl_sheet.row(i)
	insertDataQuery += "('%s', %d, '%s')," % (row[0].value, 0 if row[1].value == '' else int(row[1].value), row[2].value)

insertDataQuery = insertDataQuery[:-1]
insertDataQuery += ";"

cursor.execute(insertDataQuery)
db.commit();
db.close()
