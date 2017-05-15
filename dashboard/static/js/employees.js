/*
    global $
    global loadTableBody
    global createLabels
    global createTableDataText
    global createTableDataCheckbox
    global createTableDataLabels
*/
$(document).ready(function(){    
    loadEmployeeTable();
  
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
    
    
    
    $('#remove_roles_dd').click(function() {
        $('.collapse').collapse('hide');
    });
    
    $('#add_roles_dd').click(function() {
        $('.collapse').collapse('hide');
    });

    
    $('#deleteButton').click(function() {
    
        var peopleToDelete = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            peopleToDelete.push($(this).val());
        });
        
        var data = {
            'ids': peopleToDelete,
        }
                
        $.ajax({
            url: '/api/employees',
            method: 'DELETE',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                var message = (peopleToDelete.length > 1) ? 'Users deleted.' : 'User deleted.'
                $('#message').html(message);
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
                
                loadEmployeeTable();
            },
            error: function(error) {
                try {
                    var json = JSON.parse(error.responseText);
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
    });
    
        $('#save').click(function(){
        
        
        var rolesSelected = $('#roles').val()
        
        console.log(rolesSelected)
        
        
        var employeesSelected = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            employeesSelected.push($(this).val());
        });
        
        
        var data = {
            
            'employee_ids': employeesSelected,
            'role_ids': rolesSelected
            
        }
        console.log(employeesSelected)
        $.ajax({
            url: '/api/employee/roles',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                $('#message').html("Role was added");
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
               
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
                    console.log("error!");
                }
            }
        });
    });
       
       
    $('#remove').click(function(){
        
        
        var rolesSelected = $('#roles1').val()
        
        console.log(rolesSelected)
        
        
        var employeesSelected = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            employeesSelected.push($(this).val());
        });
        
        
        var data = {
            
            'employee_ids': employeesSelected,
            'role_ids': rolesSelected
            
        }
        console.log(employeesSelected)
        $.ajax({
            url: '/api/employee/roles',
            method: 'DELETE',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                $('#message').html("Role was deleted");
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
               
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
                    console.log("error!");
                }
            }
        });
    });    
        
    function createEmployeeRow(employee) {
        var tblRow = $('<tr>');
        
        var tblData = createTableDataCheckbox(employee.id)
        tblRow.append(tblData);
        
        var employeeName = employee.first_name + ' ' + employee.last_name;
        tblData = createTableDataText(employeeName);
        tblRow.append(tblData);
        
        tblData = createTableDataText(employee.email)
        tblRow.append(tblData);
        
        var roleNames = getRoleNames(employee.roles);
        tblData = createTableDataLabels(roleNames);
        tblRow.append(tblData);
        
        return tblRow;
    }
    
    
    function getRoleNames(roles) {
        var names = roles.map(function(role) {
            return role.name;
        });
        return names;
    }
    
    function loadEmployeeTable() {
        $.ajax({
            url: '/api/employees',
            method: 'GET',
            success: function(response) {
                
                try {
                    var json = JSON.parse(response);
                    var employees = json.employees;
                    var table = $('#employees-table')[0];
                    loadTableBody(table, employees, createEmployeeRow);
                }
                catch(e) {
                    console.log(e);
                }
            },
            error: function(response) {
                try {
                    var json = JSON.parse(response.responseText);
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