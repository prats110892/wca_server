from tables.basic_calc_table import Base_Calc_Table

class CHOICE_PERCENT_CALC_Table(Base_Calc_Table):
	"The definition of the Choice Percent in the database"

	table_name = "CHOICE_PERCENT_CALC"
	def __init__(self) :
		self.table_name = CHOICE_PERCENT_CALC_Table.table_name
		self.columns = Base_Calc_Table.columns + ["Choice Percent"]
		self.initalize()
