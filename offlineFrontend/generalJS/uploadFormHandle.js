

function validateAndSubmit() {
    // Create the list element:
    //get Data category and detail values
    var dataCategoryForm=document.getElementById("dataCategory")
    var selectedDataOption=dataCategoryForm.options[dataCategoryForm.selectedIndex].value
    var detailForm=document.getElementById("dataDetail");
    var selectedDetailOption=detailForm.options[detailForm.selectedIndex].value

    //get filenames chosen in the first two forms
    var dataFile = document.getElementById("js-upload-dataFile").files[0];
    var calcFile = document.getElementById("js-upload-calcFile").files[0];

    //get the daterange

    var fromDate=document.getElementById("fromDate").value;
    var toDate=document.getElementById("toDate").value;
    
    console.log(dataCategoryForm);
    console.log(selectedDetailOption);
    console.log(dataFile);
    console.log(calcFile);
    console.log(fromDate);
    console.log(toDate);

    //check if all fields are populated else give an alert and exit

    //create a hidden form and populate fields with values above
    var mapForm = document.createElement("form");
      mapForm.method = "POST";
      // Create an input
      var mapInputDataFile = document.createElement("input");
      mapInputDataFile.type = "file";
      mapInputDataFile.file=dataFile;

      // Add the input to the form
      mapForm.appendChild(mapInputDataFile);

      document.body.appendChild(mapForm);

      var frm = $(mapForm);
      frm.submit(function () {
          $.ajax({
              type: frm.attr('method'),
              url: frm.attr('action'),
              data: frm.serialize(),
              success: function (data) {
                  alert('ok');
              }
          });

          return false;
      });


    
}

function validateAndSubmitCalc() {
    // Create the list element:
    //get Data category and detail values
 
    var selected_value;

    for(var i = 1; i <=8; i++){
      var name="optradio" + i.toString();
      console.log(name);
      var radioButton=document.getElementById(name);
      if (radioButton.checked) {
        console.log("check found");
        selected_value=radioButton.value;
      }
    }

    //get filenames chosen in the first two forms
    var calcFile = document.getElementById("js-upload-calcFile").files[0];

    //get the daterange

    var fromDate=document.getElementById("applicableFromDate").value;
    console.log(selected_value);



      var mapForm = document.createElement("form");
      mapForm.method = "POST";
      // Create an input
      var mapInputDataFile = document.createElement("input");
      mapInputDataFile.type = "file";
      mapInputDataFile.file=calcFile;

      // Add the input to the form
      mapForm.appendChild(mapInputDataFile);

      document.body.appendChild(mapForm);

      var frm = $(mapForm);
      frm.submit(function () {
          $.ajax({
              type: frm.attr('method'),
              url: frm.attr('action'),
              data: frm.serialize(),
              success: function (data) {
                  alert('ok');
              }
          });

          return false;
      });


    
}
