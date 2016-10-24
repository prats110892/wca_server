from tables.basic_calc_table import Base_Calc_Table

class ZIP_CALC_Table(Base_Calc_Table):
	"The definition of the ZIP Calc in the database"

	num_of_rows_to_leave = 1
	table_name = "ZIP_CALC"
	columns = 	Base_Table.columns + ["30030", "30032", "30080", "30082", "30126",
									"30288", "30297", "30303", "30305", "30306",
									"30307", "30308", "30309", "30310", "30311",
									"30312", "30313", "30314", "30315", "30316",
									"30317", "30318", "30319", "30320", "30324",
									"30326", "30327", "30330", "30331", "30334",
									"30336", "30339", "30342", "30344", "30354",
									"30363"]

	def __init__(self) :
		Base_Table.__init__()
