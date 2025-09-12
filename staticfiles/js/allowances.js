function bulkUpdateForms() {
    event.preventDefault();
    
    var update_form = document.getElementById('bulkEdit');
    var modal_name = document.getElementById('modal_name').textContent;
    var element_name = modal_name+"_amount";
    var start_date_names = modal_name+"_date_start";
    var end_date_names = modal_name+"_date_end";
    var comments = modal_name+"_comment";

    var allamounts = document.getElementsByClassName(String(element_name.toLowerCase()));
    var start_dates = document.getElementsByClassName(String(start_date_names.toLowerCase()));
    var end_dates = document.getElementsByClassName(String(end_date_names.toLowerCase()));
    

    console.log(allamounts);
    // Loop through all forms and collect data
    for (var i = 0; i < allamounts.length; i++) {
        var curr_value =  allamounts[i].value;
        var new_value = parseInt(document.getElementById("modal_amount").value);
        allamounts[i].value = document.getElementById("modal_amount").value;  
        if (curr_value == '--'){
            allamounts[i].style.border = '5px solid green';
            allamounts[i].style.color = 'black';
        }
        else if (parseInt(curr_value) > new_value) {
            allamounts[i].style.border = '5px solid red';
        }
        else {
            allamounts[i].style.border = '5px solid #FFA500';
        }
        
      
    }
    for (var j = 0; j < start_dates.length; j++) {
      start_dates[j].value = document.getElementById("modal_date_start").value;  
      
    }
    for (var k = 0; k < end_dates.length; k++) {
      end_dates[k].value = document.getElementById("modal_date_end").value;  
      
    }
    
    $('#bulkUpdate').modal('hide');
}

function unHiddeFields(containerID){
    document.getElementById(containerID).style.display = 'block';
    
}

function compareValues(input, type_name){
    var old_amount =  type_name.value;
    var curr_amount =  parseInt(input.value);
    if (type_name.value == 'None'){
        input.setAttribute( 'style', 'border: 5px solid #008000 !important;');
    }
    if(curr_amount > parseInt(type_name.value)){
        input.setAttribute( 'style', 'border: 5px solid #008000 !important;');
    }
    else if (curr_amount < parseInt(type_name.value)){
        input.setAttribute( 'style', 'border: 5px solid #FFA500 !important;');
    }
    else if (curr_amount == parseInt(old_amount)) {
        input.setAttribute( 'style', 'border: 1px solid black !important;');
    }
}

function showAllowanceModal(title_name) {
    console.log(title_name);
    $('#bulkUpdate').modal('show');
    document.getElementById('modal_name').innerHTML = title_name;
}

function hiddeFields(containerID){
    document.getElementById(containerID).style.display='none';
    
}