from tables.basic_calc_table import Base_Calc_Table

class APS_CALC_Table(Base_Calc_Table):
	"The definition of the APS Calculations in the database"

	table_name = "APS_CALC"

	def __init__(self) :
		self.table_name = APS_CALC_Table.table_name
		self.columns = Base_Calc_Table.columns + ["Carver ", "Douglass", "Grady", "Jackson",
										"Mays", "North Atlanta", "South Atlanta",
										"Therrell", "Washington"]
		self.initalize()
