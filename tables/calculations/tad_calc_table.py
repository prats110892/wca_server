import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from basic_calc_table import Base_Calc_Table

class TAD_CALC_Table(Base_Calc_Table):
	"The definition of the TAD Calc in the database"


	table_name = "TAD_CALC"
	def __init__(self) :
		self.table_name = TAD_CALC_Table.table_name
		self.columns = Base_Calc_Table.columns + ["Atlantic Station", "Beltline", "Cambellton",
										"Eastside", "Hollowell MLK", "Metropolitan Pkwy",
										"Perry Bolton", "Princeton Lakes", "Stadium",
										"Westside"]
		self.initalize()
