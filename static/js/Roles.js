// JavaScript File



$(document).ready(function(){

    var employees_json = '{"employees": [{"roles": [{"role_id": 11111, "name": "kunf_fu_master", "description": "kung fu fighting"},{"role_id": 11112, "name": "sal_thekunf_fu_master", "description": "sal is kung fu fighting"}], "first_name": "Eliasar", "email": "elgandara@csumb.edu", "last_name": "Gandara"}, {"roles": [{"role_id": 22222, "name": "gym_teacher", "description": "teach gym"}], "first_name": "fake", "email": "fakeemail@fake.edu", "last_name": "person"}]}'
    var json = JSON.parse(employees_json);
    var table = $('#roles-table')[0]; // Get table from html
    var tableRows = (json.employees.length >= 10) ? 10 : json.employees.length;
    console.log(tableRows);

    
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