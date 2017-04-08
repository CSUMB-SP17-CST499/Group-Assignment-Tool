// JavaScript File



$(document).ready(function(){
    
    

    // var employees_json = '{"employees": [{"roles": [{"role_id": 11111, "name": "kunf_fu_master", "description": "kung fu fighting"},{"role_id": 11112, "name": "sal_thekunf_fu_master", "description": "sal is kung fu fighting"}], "first_name": "Eliasar", "email": "elgandara@csumb.edu", "last_name": "Gandara"}, {"roles": [{"role_id": 22222, "name": "gym_teacher", "description": "teach gym"}], "first_name": "fake", "email": "fakeemail@fake.edu", "last_name": "person"}]}'
    var json = "";

    
    $.ajax({
        url: '/api/employees',
        method: 'GET',
        contentType: 'application/json',
        success: function(response) {
            console.log(response);
            json = response;
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

    var table = $('#employees-table')[0]; // Get table from html
    var tableRows = (json.length >= 10) ? 10 : json.length;

    loadTable(table, tableRows);
    displayEmployees(table, json)
    
    function displayEmployees(table, json) {
        if (json['employees']) {
            var employees = json['employees'];

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
        
       
        inner_table = "<thead><tr><th> <input id='all-checkbox' type='checkbox' name= '' /> Select All </th><th>Name</th><th>Email</th><th>Roles</th></tr></thead>"
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