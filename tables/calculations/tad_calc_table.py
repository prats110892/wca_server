from tables.basic_calc_table import Base_Calc_Table

class TAD_CALC_Table(Base_Calc_Table):
	"The definition of the TAD Calc in the database"

	num_of_rows_to_leave = 1
	table_name = "TAD_CALC"
	columns = 	Base_Table.columns + ["Atlantic Station", "Beltline", "Cambellton",
									"Eastside", "Hollowell MLK", "Metropolitan Pkwy",
									"Perry Bolton", "Princeton Lakes", "Stadium  ",
									"Westside"]

	def __init__(self) :
		Base_Table.__init__()
