from tables.basic_calc_table import Base_Calc_Table

class CHOICE_PERCENT_CALC_Table(Base_Calc_Table):
	"The definition of the Choice Percent in the database"

	num_of_rows_to_leave = 1
	table_name = "CHOICE_PERCENT_CALC"
	columns = 	Base_Table.columns + ["Choice Percent"]
	
	def __init__(self) :
		Base_Table.__init__()
