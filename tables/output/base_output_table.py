from Dbhelper import Dbhelper
from id_table import ID_Table
import Base_Table
import Base_Calc_Table

class Base_Output_Table(object):
	"This is the base table class that all other table classes will extend"

	num_of_rows_to_leave = 2

	def initalize(self, forYear, dataTableObject, calcTableObject) :
		self.dbHelper = Dbhelper()
		self.forYear = forYear
		self.calcTableObject = calcTableObject
		self.dataTableObject = dataTableObject
		self.dataTableObjectName = dataTableObject.table_name
		self.calcTableObjectName = calcTableObject.table_name
		self.columns = ["Year", self.calcTableObjectName]

	def buildOutputFile(self) :
		dataQuery = """SELECT * FROM `{0}` WHERE {1}<={2} AND {3}>={1};""".format(self.dataTableObjectName, Base_Table.columns[0], Base_Table.columns[1], int(self.forYear))
		calcQuery = """SELECT * FROM `{0}` WHERE {1}=={2}""".format(self.calcTableObjectName, Base_Calc_Table.columns[0], self.getImmediateCalcYear(self.forYear))
		dataCursor = self.dbHelper.executeQuery(dataQuery)
		calcCursor = self.dbHelper.executeQuery(calcQuery)

		dataMatrix = dataCursor.fetchall()
		calcMatrix = calcCursor.fetchall()
		outputMatrix = []
		for calcColumn in xrange(len(Base_Calc_Table.columns), len(self.calcTableObject.columns) :
			outputRowForCalcColumn = []
			outputRowForCalcColumn.append(self.forYear)
			outputRowForCalcColumn.append(self.calcTableObjectName)
			int total = 0;
			for row in xrange(0, calcCursor.rowcount) :
				calcTableCell = calcMatrix[row][calcColumn]
				dataTableCell = dataMatrix[row + num_of_rows_to_leave]
				total =



	def getImmediateCalcYear(self, requestedYear) :
		query = "SELECT `{0}` FROM `{1}` WHERE {0}<={2}".format(Base_Calc_Table.columns[0], self.calcTableObjectName, requestedYear)
		cursor = self.dbHelper.executeQuery(query)
		immediateYear = -1;
		for row in cursor :
			if (int(row[0]) > immediateYear) :
				immediateYear = int(row[0])
		return immediateYear
