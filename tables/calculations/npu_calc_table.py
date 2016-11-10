import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from basic_calc_table import Base_Calc_Table

class NPU_CALC_Table(Base_Calc_Table):
	"The definition of the NPU Calculations in the database"

	table_name = "NPU_CALC"
	def __init__(self) :
		self.table_name = NPU_CALC_Table.table_name
		self.columns = Base_Calc_Table.columns + ["A", "B", "C", "D", "E", "F", "G", "H", "I",
					"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V",
		 			"W", "X", "Y", "Z"]
		self.initalize()
