import MySQLdb

class Dbhelper :
	"A Class that handles all database operations"

	db = NULL
	def openConnection() :
		db = MySQLdb.connect(host="localhost",  # your host, usually localhost
							user="root",         # your username
							passwd="aguamenti92",
							db="wca_data_dashboard")

	def executeQuery(query) :
		openConnection()
		cursor = db.cursor()
		result = cursor.execute(query)
		db.commit()
		closeDb()
		return result

	def closeDb() :
		db.close()


	def createTable(tableName, columns, columnDataTypes, tableMetaData) :
			createTableQuery = "CREATE TABLE " + tableName + "("
			for i in range(0, len(columns)) :
				if len(columnDataTypes > 2 or i is 0) :
					createTableQuery += columns[i] + " " + columnDataTypes[i] + " ,"
				else :
					createTableQuery += columns[i] + " " + columnDataTypes[1] + " ,"

			if table_extra_meta_data is not "" :
				createTableQuery += " " + tableMetaData
			else :
				createTableQuery = createTableQuery[:-1]

			createTableQuery += ");"
			return executeQuery(createTableQuery)

	def deleteTable(tableName) :
		deleteTableQuery = "DROP TABLE " + tableName + ";"
		return executeQuery(deleteTableQuery)

	def checkIfTableExists(tableName) :
		query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}' """.format(tablename.replace('\'', '\'\''))
		result = executeQuery(query)
		if result.fetchone()[0] == 1:
			return True
    	return False
