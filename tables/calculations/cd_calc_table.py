import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from basic_calc_table import Base_Calc_Table

class CD_CALC_Table(Base_Calc_Table):
	"The definition of the CD Calc in the database"

	table_name = "CD_CALC"
	def __init__(self) :
		self.table_name = CD_CALC_Table.table_name
		self.columns = Base_Calc_Table.columns + ["1", "2", "3", "4", "5", "6", "7", "8", "9",
											"10", "11", "12"]

		self.initalize()
