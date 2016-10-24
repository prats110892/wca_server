from tables.basic_calc_table import Base_Calc_Table

class CD_CALC_Table(Base_Calc_Table):
	"The definition of the CD Calc in the database"

	num_of_rows_to_leave = 1
	table_name = "CD_CALC"
	columns = 	Base_Table.columns + ["1", "2", "3", "4", "5", "6", "7", "8", "9",
										"10", "11", "12"]

	def __init__(self) :
		Base_Table.__init__()
