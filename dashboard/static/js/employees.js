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
<<<<<<< HEAD
    
        $('#editButton').click(function(){
            console.log("Hello")
        var editperson = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            editperson.push($(this).val());
        });
        
        data = {
            'id': editperson,
        }
        
        console.log(editperson);
        
        $.ajax({
            url: '/api/employee',
            method: 'GET',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                    print(data);
                // window.location = "/employees";
            },
            error: function(error) {
                try {
                    json = JSON.parse(error.responseText);
=======
        
        
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
>>>>>>> a5346c1bf007898fd85e816b40b896ed38976d53
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
<<<<<<< HEAD
    });
}
=======
    }
>>>>>>> a5346c1bf007898fd85e816b40b896ed38976d53
});