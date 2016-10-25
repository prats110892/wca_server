from tables.basic_calc_table import Base_Calc_Table

class BELTLINE_CALC_Table(Base_Calc_Table):
	"The definition of the Beltline Calculations in the database"
	table_name = "BELTLINE_CALC"

	def __init__(self) :
		self.table_name = BELTLINE_CALC_Table.table_name
		self.columns = Base_Calc_Table.columns + ["Total Beltline Zone", "Northeast Study Area",
											"Northside Study Area", "Southeast Study Area",
											"Southwest Study Area", "Westside Study Area",
											"Northeast Zone", "Northside Zone", "Southeast Zone",
											"Southwest Zone", "Westside Zone"]

		self.initalize()
