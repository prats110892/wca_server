var details_options = {
    Demographics: ['Median_Age_Sex', 'Race', 'Hispanic_Origin',  'Relationship_Children', 'Household_Relationship', 'Race',
    				'Relationship_65','Sex_Marital_Status','Household_Language_Limited','Sex_Age_Veteran',],
    Education: ['Sex_School_Enrolment', 'Sex_School_Enrolment_Attainment', 'Educational_Attainment','Bachelors'],
    Employment: ['Own_Children_Employment_Status', 'Age_Own_Children_Living_Arrangements', 'Sex_Hours_Worked_Week','Poverty_Disability_Employment',
                    'Sex_Hours_Worked_Week_Over65','Full_Time_Year_Around_Work','Sex_Class'],
    Health: ['Health_insurance'],
    Housing: ['Household-Type','Household_Relatives','Household_65', 'Household_Tenure'],
    Income: ['First Option', 'Second Option', 'Third Option'],
    Transportation: ['First Option', 'Second Option', 'Third Option']
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
