from tables.basic_calc_table import Base_Calc_Table

class APS_CALC_Table(Base_Calc_Table):
	"The definition of the APS Calculations in the database"

	num_of_rows_to_leave = 1
	table_name = "APS_CALC"
	columns = 	Base_Table.columns + ["Carver ", "Douglass", "Grady", "Jackson",
									"Mays", "North Atlanta", "South Atlanta",
									"Therrell", "Washington"]

	def __init__(self) :
		Base_Table.__init__()
