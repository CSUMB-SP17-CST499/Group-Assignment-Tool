$(document).ready(function(){

    //Initialize globals
    var json = [];
    var table = $('#employees-table')[0]; // Get table from html
    var tableRows = 0;
    loadEmployeeTable(table, tableRows,5);

    
    $.ajax({
        url: '/api/employees',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = (JSON.parse(response))['employees'];
            tableRows = Object.keys(json).length;
            loadEmployeeTable(table, tableRows,5);
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
});