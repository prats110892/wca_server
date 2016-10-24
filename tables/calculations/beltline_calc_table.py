from tables.basic_calc_table import Base_Calc_Table

class BELTLINE_CALC_Table(Base_Calc_Table):
	"The definition of the Beltline Calculations in the database"

	num_of_rows_to_leave = 1
	table_name = "BELTLINE_CALC"
	columns = 	Base_Table.columns + ["Total Beltline Zone", "Northeast Study Area",
										"Northside Study Area", "Southeast Study Area",
										"Southwest Study Area", "Westside Study Area",
										"Northeast Zone", "Northside Zone", "Southeast Zone",
										"Southwest Zone", "Westside Zone"]

	def __init__(self) :
		Base_Table.__init__()
