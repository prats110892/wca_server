from aggregate_household_income_table import AGGREGATE_HOUSEHOLD_INCOME_Table
from aggregate_income_table import AGGREGATE_INCOME_Table
from earnings_table import EARNINGS_Table
from household_income_table import HOUSEHOLD_INCOME_Table
from interest_dividends_rental_income_table import INTEREST_DIVIDENDS_RENTAL_INCOME_Table
from other_income_table import OTHER_INCOME_Table
from poverty_age_table import POVERTY_AGE_Table
from poverty_family_children_table import POVERTY_FAMILY_CHILDREN_Table
from public_assistance_income_table import PUBLIC_ASSISTANCE_INCOME_Table
from receipt_food_snap_disability_table import RECEIPT_FOOD_SNAP_DISABILITY_Table
from retirement_income_table import RETIREMENT_INCOME_Table
from self_employment_income_table import SELF_EMPLOYMENT_INCOME_Table
from social_security_income_table import SOCIAL_SECURITY_INCOME_Table
from supplemental_security_income_table import SUPPLEMENTAL_SECURITY_INCOME_Table
from wage_salary_table import WAGE_SALARY_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 AGGREGATE_HOUSEHOLD_INCOME_Table.table_name : AGGREGATE_HOUSEHOLD_INCOME_Table(),
		 AGGREGATE_INCOME_Table.table_name : AGGREGATE_INCOME_Table(),
		 EARNINGS_Table.table_name : EARNINGS_Table(),
		 HOUSEHOLD_INCOME_Table.table_name : HOUSEHOLD_INCOME_Table(),
		 INTEREST_DIVIDENDS_RENTAL_INCOME_Table.table_name : INTEREST_DIVIDENDS_RENTAL_INCOME_Table(),
		 OTHER_INCOME_Table.table_name : OTHER_INCOME_Table(),
		 POVERTY_AGE_Table.table_name : POVERTY_AGE_Table(),
		 POVERTY_FAMILY_CHILDREN_Table.table_name : POVERTY_FAMILY_CHILDREN_Table(),
		 PUBLIC_ASSISTANCE_INCOME_Table.table_name : PUBLIC_ASSISTANCE_INCOME_Table(),
		 RECEIPT_FOOD_SNAP_DISABILITY_Table.table_name : RECEIPT_FOOD_SNAP_DISABILITY_Table(),
		 RETIREMENT_INCOME_Table.table_name : RETIREMENT_INCOME_Table(),
		 SELF_EMPLOYMENT_INCOME_Table.table_name : SELF_EMPLOYMENT_INCOME_Table(),
		 SOCIAL_SECURITY_INCOME_Table.table_name : SOCIAL_SECURITY_INCOME_Table(),
		 SUPPLEMENTAL_SECURITY_INCOME_Table.table_name : SUPPLEMENTAL_SECURITY_INCOME_Table(),
		 WAGE_SALARY_Table.table_name : WAGE_SALARY_Table()
}

def getTableName(client_table_name) :
	return {
        		 'Aggregate_Household_Income' : AGGREGATE_HOUSEHOLD_INCOME_Table.table_name,
        		 'Aggregate_Income' : AGGREGATE_INCOME_Table.table_name,
        		 'Earnings' : EARNINGS_Table.table_name,
        		 'Household_Income' : HOUSEHOLD_INCOME_Table.table_name,
        		 'Interest_Dividends_Rental_Income' : INTEREST_DIVIDENDS_RENTAL_INCOME_Table.table_name,
        		 'Other_Income' : OTHER_INCOME_Table.table_name,
        		 'Poverty_Age' : POVERTY_AGE_Table.table_name,
        		 'Poverty_Family_Children' : POVERTY_FAMILY_CHILDREN_Table.table_name,
        		 'Public_Assistance_Income' : PUBLIC_ASSISTANCE_INCOME_Table.table_name,
        		 'Receipt_Food_Snap_Disability' : RECEIPT_FOOD_SNAP_DISABILITY_Table.table_name,
        		 'Retirement_Income' : RETIREMENT_INCOME_Table.table_name,
        		 'Self_Employment_Income' : SELF_EMPLOYMENT_INCOME_Table.table_name,
        		 'Social_Security_Income' : SOCIAL_SECURITY_INCOME_Table.table_name,
        		 'Supplemental_Security_Income' : SUPPLEMENTAL_SECURITY_INCOME_Table.table_name,
        		 'Wage_Salary' : WAGE_SALARY_Table.table_name
	}[client_table_name]


def parseAndInsertIncomeData(csvFile, tableName, fromDate, toDate) :
	print(tableName)
	stored_table_name = getTableName(tableName)
	print(stored_table_name)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	print(tableObject.table_name)
	return tableObject.insertDataFromCSVFile(csvFile, fromDate, toDate)
