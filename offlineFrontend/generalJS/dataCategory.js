var details_options = {
    Demographics: ['Median_Age_Sex', 'Race', 'Hispanic_Origin',  'Relationship_Children', 'Household_Relationship', 'Race',
    				'Relationship_65','Sex_Marital_Status','Household_Language_Limited','Sex_Age_Veteran'],
    Education: ['Sex_School_Enrolment', 'Sex_School_Enrolment_Attainment', 'Educational_Attainment','Bachelors'],
    Employment: ['Own_Children_Employment_Status', 'Age_Own_Children_Living_Arrangements', 'Sex_Hours_Worked_Week','Poverty_Disability_Employment',
                    'Sex_Hours_Worked_Week_Over65','Full_Time_Year_Around_Work','Sex_Class'],
    Health: ['Health_insurance'],
    Housing: ['Household-Type','Household_Relatives','Household_65', 'Household_Tenure'],
    Income: ['First Option', 'Second Option', 'Third Option'],
    Transportation: ['First Option', 'Second Option', 'Third Option']
};

metadata_demographics={
Median_Age_Sex: "This table shows the population in different geographic units belonging to different age groups (ages 5-85). Both sexes are accounted for.",
Relationship_Children: "This table gives the total population under 18 divided according to their relationship to the householder."
// Race', 'Hispanic_Origin',  'Relationship_Children', 'Household_Relationship', 'Race',
//                     'Relationship_65','Sex_Marital_Status','Household_Language_Limited','Sex_Age_Veteran'

};
var dataCategoryForm;
var selectedOption;
var detailForm;

function populateDetails() {
    // Create the list element:
    dataCategoryForm=document.getElementById("dataCategory")
    selectedOption=dataCategoryForm.options[dataCategoryForm.selectedIndex].value
    var arr=details_options[selectedOption]
    console.log(arr);

    detailForm = document.getElementById("dataDetail");
    detailForm.options.length = 0;


    for (var i=0;i<arr.length;i++) {
        var opt=document.createElement('option');
        opt.innerHTML=arr[i];
        console.log(opt.innerHTML);
        detailForm.appendChild(opt);
    }

$('.selectpicker').selectpicker('refresh');
    
}

function displayMetadata() {
    // Create the list element:
    var para=document.getElementById("metaDataDownload");
    var detailSelected=detailForm.options[detailForm.selectedIndex].value;

    
        var mData=metadata_demographics[detailSelected];
        para.innerHTML=mData;
        para.style.display="block";
    



$('.selectpicker').selectpicker('refresh');
    
}