#This file handles all the database operations
#It is called by a few different files


import MySQLdb

class Dbhelper :
	"A Class that handles all database operations"

	def __init__(self) :
		self.db = None

	#This opens a connections to the MYSQL database
	#You may need to change the credentials
	def openConnection(self) :
		self.db = MySQLdb.connect(host="127.0.0.1",port=3306,  # your host, usually localhost
							user="root",         # your username
							passwd="aguamenti92",
							db="wca_data_dashboard")
	
	
	#this is a general execute query function, which is used to run an SQL statement, such as
	#SELECT * FROM <table_name>... or INSERT INTO <table_name>...
	def executeQuery(self, query) :
		self.openConnection()
		cursor = self.db.cursor()
		cursor.execute(query)
		self.db.commit()
		self.closeDb()
		return cursor

	def closeDb(self) :
		self.db.close()

	#this creates a new table in the database
	def createTable(self, tableName, columns, columnDataTypes, tableMetaData) :
			createTableQuery = """CREATE TABLE `{0}` (""".format(tableName)
			for i in range(0, len(columns)) :
				if len(columnDataTypes) == len(columns) or i < len(columnDataTypes) :
					createTableQuery += """`{0}` {1}, """.format(columns[i], columnDataTypes[i])
				else :
					createTableQuery += """`{0}` {1}, """.format(columns[i], columnDataTypes[(len(columnDataTypes) - 1)])

			if tableMetaData is not "" :
				createTableQuery += " " + tableMetaData
			else :
				createTableQuery = createTableQuery[:-1]

			createTableQuery += ");"
			print(createTableQuery)
			return self.executeQuery(createTableQuery)

	#used to drop a table, in case you need to update the table schema or something
	def deleteTable(self, tableName) :
		deleteTableQuery = "DROP TABLE " + tableName + ";"
		return self.executeQuery(deleteTableQuery)

	#this is a helper which can be used to check if a table exists
	#It's useful because we create new tables at intial runtime if they don't exist already
	def checkIfTableExists(self, tableName) :
		query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}' """.format(tableName.replace('\'', '\'\''))
		result = self.executeQuery(query)
		if result.fetchone()[0] == 1:
			return True
		return False
