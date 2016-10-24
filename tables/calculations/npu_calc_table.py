from tables.basic_calc_table import Base_Calc_Table

class NPU_CALC_Table(Base_Calc_Table):
	"The definition of the NPU Calculations in the database"

	num_of_rows_to_leave = 1
	table_name = "NPU_CALC"
	columns = 	Base_Table.columns + ["A", "B", "C", "D", "E", "F", "G", "H", "I",
				"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
	 			"W", "X", "Y", "Z"]

	def __init__(self) :
		Base_Table.__init__()
