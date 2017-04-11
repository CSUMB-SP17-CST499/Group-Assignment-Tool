// JavaScript File


// Function to delete employee whose email is in the text field of employee.html
$("#delete-employee").on('click', function(e){
    var personToDelete = $("#employeeToDelete").val();
    var personToDelete_ID = null;

    // Lookup employee to get their ID
    $.ajax({
        url: '/api/employees',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = (JSON.parse(response))['employees'];
            tableRows = Object.keys(json).length;
            
            for(x = 0; x < tableRows; x++){
                if(json[x]['email'] == personToDelete){
                    personToDelete_ID = json[x]['id']
                }
            }
        },
        error: function(error) {
            try {
                json = JSON.parse(error.responseText);
                if (json.message) {
                    $('#message').html(json.message);
                    $('#alert-message')[0].classList.add('alert-danger');
                    $('#alert-message').show();
                }
            }
            catch (e) {
                console.log(e);
            }
        }
    });
    
    // If the ID is found, delete the user.
    if(personToDelete_ID != null){
    $.ajax({
        url: '/api/employee',
        method: 'DELETE',
        data: personToDelete_ID,
        success: function(response) {
            // CONTINUE HERE?!
        },
        error: function(error) {
            try {
                json = JSON.parse(error.responseText);
                if (json.message) {
                    $('#message').html(json.message);
                    $('#alert-message')[0].classList.add('alert-danger');
                    $('#alert-message').show();
                }
            }
            catch (e) {
                console.log(e);
            }
        }
    });
    }
});

$(document).ready(function(){
    //Initialize globals
    var json = [];
    var table = $('#employees-table')[0]; // Get table from html
    var tableRows = 0;
    
    $.ajax({
        url: '/api/employees',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = (JSON.parse(response))['employees'];
            tableRows = Object.keys(json).length;
            loadTable(table, tableRows);
            displayEmployees(table, json);
        },
        error: function(error) {
            try {
                json = JSON.parse(error.responseText);
                if (json.message) {
                    $('#message').html(json.message);
                    $('#alert-message')[0].classList.add('alert-danger');
                    $('#alert-message').show();
                }
            }
            catch (e) {
                console.log(e);
            }
        }
    });
    
    function displayEmployees(table, employees) {
        if (employees) {
            console.log(Object.keys(employees).length);
            for (var index = 0; index < employees.length; index++) {
                var employee = employees[index];
                
                var role_names = getEmployeeRoles(employee);
                

                table.rows[index + 1].cells[1].innerHTML = employee['first_name'] + " " + employee['last_name'];//name
                table.rows[index + 1].cells[2].innerHTML = employee['email'];//email
                table.rows[index + 1].cells[3].innerHTML = role_names;//Role
            }
        }
    }
    
    function getEmployeeRoles(employee) {
        var roles = employee["roles"];
        var role_names = [];
        
        for(var index = 0;  index < roles.length; index++){
            
        role_names.push(roles[index]["name"])
            
        }
        return role_names
    
    }
  
    function loadTable(table, tableRows) {
        
        var column_amt = 4;
        
        var inner_table = "";
        var row = 0; 
        
       
        inner_table = "<thead><tr><th> <input id='all-checkbox' type='checkbox' name='' /> Select All </th><th>Name</th><th>Email</th><th>Roles</th></tr></thead>"
        inner_table += "<tbody>"
        for (; row < tableRows; row++){
            
            inner_table += "<tr>";
            var col = 0; 
            for(;col < column_amt;col++ ){
                inner_table += "<td><input class='checkbox' type='checkbox' name='' /></td>";
            }
            inner_table += "</tr>";
        }
        inner_table += "</tbody>"
        $(table).append(inner_table);
    }
    
    $('#all-checkbox').on('click', function(e) {
        var checkboxes = $('.checkbox');
        if (this.checked) {
            for (var i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].type == 'checkbox') {
                    checkboxes[i].checked = true;
                }
         }
        }
        else {
            for (var i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].type == 'checkbox') {
                    checkboxes[i].checked = false;
                }
         }
        }
    });
    
    function clearTable(table) {
        
    }
    
});