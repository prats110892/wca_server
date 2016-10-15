from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
import sys, getopt
import MySQLdb
import mappings


tableName = sys.argv[1]

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
							user="root",         # your username
							passwd="aguamenti92",
							db="wca_data_dashboard")
cursor = db.cursor()
cursor.execute("DROP TABLE RelationshipChildren;")
cursor.execute("CREATE TABLE RelationshipChildren(ID VARCHAR(50), Total BIGINT, BiologicalChild BIGINT, AdoptedChild BIGINT, StepChild BIGINT, GrandChild BIGINT, OtherRelatives BIGINT, FosterOrUnrelatedChild BIGINT, FOREIGN KEY(ID) REFERENCES GeoID(Id));")
cursor.execute(mappings.getQuery(tableName, "RelationshipChildren"))
db.commit()
db.close()
