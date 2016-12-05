var details_options = {
    Demographics: ['Median_Age_Sex', 'Race', 'Hispanic_Origin',  'Relationship_Children', 'Household_Relationship', 'Race',
    				'Relationship_65','Sex_Marital_Status','Household_Language_Limited','Sex_Age_Veteran',],
    Education: ['Sex_School_Enrolment', 'Sex_School_Enrolment_Attainment', 'Educational_Attainment','Bachelors'],
    Employment: ['Own_Children_Employment_Status', 'Age_Own_Children_Living_Arrangements', 'Sex_Hours_Worked_Week','Poverty_Disability_Employment',
                    'Sex_Hours_Worked_Week_Over65','Full_Time_Year_Around_Work','Sex_Class','Employment'],
    Health: ['Health_insurance'],
    Housing: ['Age_Costs_Percent_Income','Mortgage_Status_Costs_Percent_Income','Mortgage_Status_Selected_Costs','Price_Asked','Mortgage_Status',
                    'Value','Income_Gross_Rent_Percent_Income','Age_Gross_Rent_Percent_Income','Gross_Rent_Percentage_Income',
                    'Inclusion_Utilities_Rent','Bedrooms_Gross_Rent','Aggregate_Gross_Rent','Gross_Rent','Rent_Asked','Aggregate_Contract_Rent',
                    'Contract_Rent','Age_Meals_Rent','Kitchen_Meals_Rent','Tenure_Kitchen','Kitchen','Tenure_Plumbing','Plumbing','Aggregate_Number_Vehicles_Tenure',
                    'Tenure_Vehicles_Age','Tenure_Vehicles_Available','Tenure_Telephone_Age','Tenure_Bedrooms','Bedrooms','Tenure_Year_Moved_Into',
                    'Tenure_Year_Stucture_Built','Year_Structure_Built','Total_Pop_Tenure_Units','Tenure_Units_Structure','Units_Structure','Aggregate_Rooms_Tenure,',
                    'Tenure_Rooms','Aggregate_Number_Rooms','Rooms','Tenure_Occupants_Room','Tenure_Size','Total_Pop_Occupied_Tenure','Tenure_Age','Race_Householder',
                    'Vacancy','Tenure','Occupancy','Housing_Units','Household_Type_Size','Household_NonRelatives','Household_Tenure','Household_65','Household_Relatives',
                    'Household_Type'],
    Income: ['Poverty_Family_Children','Poverty_Age','Household_Income','Aggregate_Household_Income','Earnings','Wage_Salary','Self_Employment_Income',
                    'Interest_Dividends_Rental_Income','Social_Security_Income','Supplemental_Security_Income','Public_Assistance_Income','Retirement_Income',
                    'Other_Income','Aggregate_Income','Receipt_Food_Stamps_SNAP_Disability'],
    Transportation: ['Mobility_MSA','Workers_Sex_Place_Work_State_County','Means_Transpo','Time_Leaving_Work','Travel_Time'],
    GEO_ID: ['GEO_ID']
};

function populateDetails() {
    // Create the list element:
    var dataCategoryForm=document.getElementById("dataCategory")
    var selectedOption=dataCategoryForm.options[dataCategoryForm.selectedIndex].value
    var arr=details_options[selectedOption]
    console.log(arr);

    var detailForm=document.getElementById("dataDetail");
    detailForm.options.length = 0;


    for (var i=0;i<arr.length;i++) {
        var opt=document.createElement('option');
        opt.innerHTML=arr[i];
        console.log(opt.innerHTML);
        detailForm.appendChild(opt);
    }

$('.selectpicker').selectpicker('refresh');
    
}
