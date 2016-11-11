from age_costs_percent_income_table import AGE_COSTS_PERCENT_INCOME_Table
from age_gross_rent_percent_income_table import AGE_GROSS_RENT_PERCENT_INCOME_Table
from age_meals_rent_table import AGE_MEALS_RENT_Table
from aggregate_contract_rent_table import AGGREGATE_CONTRACT_RENT_Table
from aggregate_gross_rent_table import AGGREGATE_GROSS_RENT_Table
from aggregate_number_vehicles_tenure_table import AGGREGATE_NUMBER_VEHICLES_TENURE_Table
from aggregate_rooms_tenure_table import AGGREGATE_ROOMS_TENURE_Table
from aggretate_number_rooms_table import AGGREGATE_NUMBER_ROOMS_Table
from bedrooms_gross_rent_table import BEDROOMS_GROSS_RENT_Table
from bedrooms_table import BEDROOMS_Table
from contract_rent_table import CONTRACT_RENT_Table
from gross_rent_percentage_income_table import GROSS_RENT_PERCENTAGE_INCOME_Table
from gross_rent_table import GROSS_RENT_Table
from household_65_table import HOUSEHOLD_65_Table
from household_nonrelatives_table import HOUSEHOLD_NONRELATIVES_Table
from household_relatives_table import HOUSEHOLD_RELATIVES_Table
from household_tenure_table import HOUSEHOLD_TENURE_Table
from household_type_size_table import HOUSEHOLD_TYPE_SIZE_Table
from household_type_table import HOUSEHOLD_TYPE_Table
from household_units_table import HOUSEHOLD_UNITS_Table
from inclusion_utilities_rent_table import INCLUSION_UTILITIES_RENT_Table
from income_gross_rent_percent_income_table import INCOME_GROSS_RENT_PERCENT_INCOME_Table
from kitchen_meals_rent_table import KITCHEN_MEALS_RENT_Table
from kitchen_table import KITCHEN_Table
from mortgage_status_costs_percent_income_table import MORTGAGE_STATUS_COSTS_PERCENT_INCOME_Table
from mortgage_status_selected_costs_table import MORTGAGE_STATUS_SELECTED_COSTS_Table
from mortgage_status_table import MORTGAGE_STATUS_Table
from occupancy_table import OCCUPANCY_Table
from plumbing_table import PLUMBING_Table
from price_asked_table import PRICE_ASKED_Table
from race_housholder_table import RACE_HOUSHOLDER_Table
from rent_asked_table import RENT_ASKED_Table
from rooms_table import ROOMS_Table
from tenure_age_table import TENURE_AGE_Table
from tenure_bedrooms_table import TENURE_BEDROOMS_Table
from tenure_kitchen_table import TENURE_KITCHEN_Table
from tenure_occupants_room_table import TENURE_OCCUPANTS_ROOM_Table
from tenure_plumbing_table import TENURE_PLUMBING_Table
from tenure_rooms_table import TENURE_ROOMS_Table
from tenure_size_table import TENURE_SIZE_Table
from tenure_table import TENURE_Table
from tenure_telephone_age_table import TENURE_TELEPHONE_AGE_Table
from tenure_units_structure_table import TENURE_UNITS_STRUCTURE_Table
from tenure_vehicles_age_table import TENURE_VEHICLES_AGE_Table
from tenure_vehicles_available_table import TENURE_VEHICLES_AVAILABLE_Table
from tenure_year_moved_into_table import TENURE_YEAR_MOVED_INTO_Table
from tenure_year_structure_built_table import TENURE_YEAR_STRUCTURE_BUILT_Table
from total_pop_occupied_tenure_table import TOTAL_POP_OCCUPIED_TENURE_Table
from total_pop_tenure_units_table import TOTAL_POP_TENURE_UNITS_Table
from units_structure_table import UNITS_STRUCTURE_Table
from vacancy_table import VACANCY_Table
from value_table import VALUE_Table
from year_structure_built_table import YEAR_STRUCTURE_BUILT_Table

TABLE_NAME_TO_OBJECT_MAPPING = {
		 AGE_COSTS_PERCENT_INCOME_Table.table_name : AGE_COSTS_PERCENT_INCOME_Table(),
		 AGE_GROSS_RENT_PERCENT_INCOME_Table.table_name : AGE_GROSS_RENT_PERCENT_INCOME_Table(),
		 AGE_MEALS_RENT_Table.table_name : AGE_MEALS_RENT_Table(),
		 AGGREGATE_CONTRACT_RENT_Table.table_name : AGGREGATE_CONTRACT_RENT_Table(),
		 AGGREGATE_GROSS_RENT_Table.table_name : AGGREGATE_GROSS_RENT_Table(),
		 AGGREGATE_NUMBER_VEHICLES_TENURE_Table.table_name : AGGREGATE_NUMBER_VEHICLES_TENURE_Table(),
		 AGGREGATE_ROOMS_TENURE_Table.table_name : AGGREGATE_ROOMS_TENURE_Table(),
		 AGGREGATE_NUMBER_ROOMS_Table.table_name : AGGREGATE_NUMBER_ROOMS_Table(),
		 BEDROOMS_GROSS_RENT_Table.table_name : BEDROOMS_GROSS_RENT_Table(),
		 BEDROOMS_Table.table_name : BEDROOMS_Table(),
		 CONTRACT_RENT_Table.table_name : CONTRACT_RENT_Table(),
		 GROSS_RENT_PERCENTAGE_INCOME_Table.table_name : GROSS_RENT_PERCENTAGE_INCOME_Table(),
		 GROSS_RENT_Table.table_name : GROSS_RENT_Table(),
		 HOUSEHOLD_65_Table.table_name : HOUSEHOLD_65_Table(),
		 HOUSEHOLD_NONRELATIVES_Table.table_name : HOUSEHOLD_NONRELATIVES_Table(),
		 HOUSEHOLD_RELATIVES_Table.table_name : HOUSEHOLD_RELATIVES_Table(),
		 HOUSEHOLD_TENURE_Table.table_name : HOUSEHOLD_TENURE_Table(),
		 HOUSEHOLD_TYPE_SIZE_Table.table_name : HOUSEHOLD_TYPE_SIZE_Table(),
		 HOUSEHOLD_TYPE_Table.table_name : HOUSEHOLD_TYPE_Table(),
		 HOUSEHOLD_UNITS_Table.table_name : HOUSEHOLD_UNITS_Table(),
		 INCLUSION_UTILITIES_RENT_Table.table_name : INCLUSION_UTILITIES_RENT_Table(),
		 INCOME_GROSS_RENT_PERCENT_INCOME_Table.table_name : INCOME_GROSS_RENT_PERCENT_INCOME_Table(),
		 KITCHEN_MEALS_RENT_Table.table_name : KITCHEN_MEALS_RENT_Table(),
		 KITCHEN_Table.table_name : KITCHEN_Table(),
		 MORTGAGE_STATUS_COSTS_PERCENT_INCOME_Table.table_name : MORTGAGE_STATUS_COSTS_PERCENT_INCOME_Table(),
		 MORTGAGE_STATUS_SELECTED_COSTS_Table.table_name : MORTGAGE_STATUS_SELECTED_COSTS_Table(),
		 MORTGAGE_STATUS_Table.table_name : MORTGAGE_STATUS_Table(),
		 OCCUPANCY_Table.table_name : OCCUPANCY_Table(),
		 PLUMBING_Table.table_name : PLUMBING_Table(),
		 PRICE_ASKED_Table.table_name : PRICE_ASKED_Table(),
		 RACE_HOUSHOLDER_Table.table_name : RACE_HOUSHOLDER_Table(),
		 RENT_ASKED_Table.table_name : RENT_ASKED_Table(),
		 ROOMS_Table.table_name : ROOMS_Table(),
		 TENURE_AGE_Table.table_name : TENURE_AGE_Table(),
		 TENURE_BEDROOMS_Table.table_name : TENURE_BEDROOMS_Table(),
		 TENURE_KITCHEN_Table.table_name : TENURE_KITCHEN_Table(),
		 TENURE_OCCUPANTS_ROOM_Table.table_name : TENURE_OCCUPANTS_ROOM_Table(),
		 TENURE_PLUMBING_Table.table_name : TENURE_PLUMBING_Table(),
		 TENURE_ROOMS_Table.table_name : TENURE_ROOMS_Table(),
		 TENURE_SIZE_Table.table_name : TENURE_SIZE_Table(),
		 TENURE_Table.table_name : TENURE_Table(),
		 TENURE_TELEPHONE_AGE_Table.table_name : TENURE_TELEPHONE_AGE_Table(),
		 TENURE_UNITS_STRUCTURE_Table.table_name : TENURE_UNITS_STRUCTURE_Table(),
		 TENURE_VEHICLES_AGE_Table.table_name : TENURE_VEHICLES_AGE_Table(),
		 TENURE_VEHICLES_AVAILABLE_Table.table_name : TENURE_VEHICLES_AVAILABLE_Table(),
		 TENURE_YEAR_MOVED_INTO_Table.table_name : TENURE_YEAR_MOVED_INTO_Table(),
		 TENURE_YEAR_STRUCTURE_BUILT_Table.table_name : TENURE_YEAR_STRUCTURE_BUILT_Table(),
		 TOTAL_POP_OCCUPIED_TENURE_Table.table_name : TOTAL_POP_OCCUPIED_TENURE_Table(),
		 TOTAL_POP_TENURE_UNITS_Table.table_name : TOTAL_POP_TENURE_UNITS_Table(),
		 UNITS_STRUCTURE_Table.table_name : UNITS_STRUCTURE_Table(),
		 VACANCY_Table.table_name : VACANCY_Table(),
		 VALUE_Table.table_name : VALUE_Table(),
		 YEAR_STRUCTURE_BUILT_Table.table_name : YEAR_STRUCTURE_BUILT_Table()
}

def getTableName(client_table_name) :
	return {
			'Median_Age_Sex' : MEDIAN_AGE_SEX_Table.table_name,
			'Race' : RACE_Table.table_name,
			'Hispanic_Origin' : HISPANIC_ORIGIN_Table.table_name,
			'Relationship_Children' : RELATIONSHIP_CHILDREN_Table.table_name,
			'Household_Relationship' : HOUSEHOLD_RELATIONSHIP_Table.table_name,
			'Relationship_65' : RELATIONSHIP_65_Table.table_name,
			'Sex_Marital_Status' : SEX_MARITAL_STATUS_Table.table_name,
			'Household_Language_Limited' : HOUSEHOLD_LANGUAGE_LIMITED_Table.table_name,
			'Sex_Age_Veteran': SEX_AGE_VETERAN_Table.table_name

        		 'Age_Costs_Percent_Income' : AGE_COSTS_PERCENT_INCOME_Table.table_name,
        		 'Age_Gross_Rent_Percent_Income' : AGE_GROSS_RENT_PERCENT_INCOME_Table.table_name,
        		 'Age_Meals_Rent' : AGE_MEALS_RENT_Table.table_name,
        		 'Aggregate_Contract_Rent' : AGGREGATE_CONTRACT_RENT_Table.table_name,
        		 'Aggregate_Gross_Rent' : AGGREGATE_GROSS_RENT_Table.table_name,
        		 'Aggregate_Number_Vehicles_tenure' : AGGREGATE_NUMBER_VEHICLES_TENURE_Table.table_name,
        		 'Aggregate_Rooms_Tenure' : AGGREGATE_ROOMS_TENURE_Table.table_name,
        		 'Aggretate_Number_Rooms' : AGGREGATE_NUMBER_ROOMS_Table.table_name,
        		 'Bedrooms_Gross_Rent' : BEDROOMS_GROSS_RENT_Table.table_name,
        		 'Bedrooms' : BEDROOMS_Table.table_name,
        		 'Contract_Rent' : CONTRACT_RENT_Table.table_name,
        		 'Gross_Rent_Percentage_Income' : GROSS_RENT_PERCENTAGE_INCOME_Table.table_name,
        		 'Gross_Rent' : GROSS_RENT_Table.table_name,
        		 'Household_65_table' : HOUSEHOLD_65_Table.table_name,
        		 'Household_Nonrelatives' : HOUSEHOLD_NONRELATIVES_Table.table_name,
        		 'Household_Relatives' : HOUSEHOLD_RELATIVES_Table.table_name,
        		 'Household_Tenure' : HOUSEHOLD_TENURE_Table.table_name,
        		 'Household_Type_size' : HOUSEHOLD_TYPE_SIZE_Table.table_name,
        		 'Household_Type' : HOUSEHOLD_TYPE_Table.table_name,
        		 'Household_Units' : HOUSEHOLD_UNITS_Table.table_name,
        		 'Inclusion_Utilities_Rent' : INCLUSION_UTILITIES_RENT_Table.table_name,
        		 'Income_Gross_Rent_Percent_Income' : INCOME_GROSS_RENT_PERCENT_INCOME_Table.table_name,
        		 'Kitchen_Meals_Rent' : KITCHEN_MEALS_RENT_Table.table_name,
        		 'Kitchen' : KITCHEN_Table.table_name,
        		 'Mortgage_Status_Costs_Percent_Income' : MORTGAGE_STATUS_COSTS_PERCENT_INCOME_Table.table_name,
        		 'Mortgage_Status_Selected_Costs' : MORTGAGE_STATUS_SELECTED_COSTS_Table.table_name,
        		 'Mortgage_Status' : MORTGAGE_STATUS_Table.table_name,
        		 'Occupancy' : OCCUPANCY_Table.table_name,
        		 'Plumbing' : PLUMBING_Table.table_name,
        		 'Price_Asked' : PRICE_ASKED_Table.table_name,
        		 'Race_Housholder' : RACE_HOUSHOLDER_Table.table_name,
        		 'Rent_Asked' : RENT_ASKED_Table.table_name,
        		 'Rooms' : ROOMS_Table.table_name,
        		 'Tenure_Age' : TENURE_AGE_Table.table_name,
        		 'Tenure_Bedrooms' : TENURE_BEDROOMS_Table.table_name,
        		 'Tenure_Kitchen' : TENURE_KITCHEN_Table.table_name,
        		 'Tenure_Occupants_Room' : TENURE_OCCUPANTS_ROOM_Table.table_name,
        		 'Tenure_Plumbing' : TENURE_PLUMBING_Table.table_name,
        		 'Tenure_Rooms' : TENURE_ROOMS_Table.table_name,
        		 'Tenure_Size' : TENURE_SIZE_Table.table_name,
        		 'Tenure' : TENURE_Table.table_name,
        		 'Tenure_Telephone_Age' : TENURE_TELEPHONE_AGE_Table.table_name,
        		 'Tenure_Units_Structure' : TENURE_UNITS_STRUCTURE_Table.table_name,
        		 'Tenure_Vehicles_Age' : TENURE_VEHICLES_AGE_Table.table_name,
        		 'Tenure_Vehicles_Available' : TENURE_VEHICLES_AVAILABLE_Table.table_name,
        		 'Tenure_Year_Moved_Into' : TENURE_YEAR_MOVED_INTO_Table.table_name,
        		 'Tenure_Year_Structure_Built' : TENURE_YEAR_STRUCTURE_BUILT_Table.table_name,
        		 'Total_Pop_Occupied_Tenure' : TOTAL_POP_OCCUPIED_TENURE_Table.table_name,
        		 'Total_Pop_Tenure_Units' : TOTAL_POP_TENURE_UNITS_Table.table_name,
        		 'Units_Structure' : UNITS_STRUCTURE_Table.table_name,
        		 'Vacancy' : VACANCY_Table.table_name,
        		 'Value' : VALUE_Table.table_name,
        		 'Year_Structure_Built' : YEAR_STRUCTURE_BUILT_Table.table_name
	}[client_table_name]

def getHousingTableObject(table_name) :
	return TABLE_NAME_TO_OBJECT_MAPPING[table_name]

def parseAndInsertHousingData(csvFile, tableName, fromDate, toDate) :
	print(tableName)
	stored_table_name = getTableName(tableName)
	print(stored_table_name)
	tableObject = TABLE_NAME_TO_OBJECT_MAPPING[stored_table_name]
	print(tableObject.table_name)
	return tableObject.insertDataFromCSVFile(csvFile, fromDate, toDate)
