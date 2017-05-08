$(document).ready(function(){

    //Initialize globals
    // var information = [];
    // var json = [];
    // var table = $('#employees-table')[0]; // Get table from html
    // var tableRows = 0;
    // loadTable(table, tableRows,5);

    
    $.ajax({
        url: '/api/employees',
        method: 'GET',
        success: function(response) {
            // information = JSON.parse(response);
            // json = response;
            // tableRows = information["employees"].length;
            // loadEmployeeTable(table, tableRows,5);
            
            try {
                json = JSON.parse(response);
                employees = json.employees;
                table = $('#employees-table')[0];
                loadTableBody(table, employees, createEmployeeRow);
            }
            catch(e) {
                console.log(e);
            }
        },
        error: function(response) {
            try {
                json = JSON.parse(response.responseText);
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
            
            data = {
                'ids': peopleToDelete,
            }
                    
            $.ajax({
                url: '/api/employees',
                method: 'DELETE',
                data: JSON.stringify(data),
                contentType: 'application/json',
                success: function(response) {
                    message = (peopleToDelete.length > 1) ? 'Users deleted.' : 'User deleted.'
                    $('#message').html(message);
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
                    }
                }
            });
        });
        
    function createEmployeeRow(employee) {
        var tblRow = $('<tr>');
        
        var tblData = $('<td>');
        var checkbox = $('<input>');
        checkbox.addClass('checkbox');
        checkbox.attr('type', 'checkbox');
        checkbox.val(employee.id);
        tblData.append(checkbox);
        tblRow.append(tblData);
        
        tblData = $('<td>');
        tblData.text(employee.first_name + ' ' + employee.last_name);
        tblRow.append(tblData);
        
        tblData = $('<td>');
        tblData.text(employee.email);
        tblRow.append(tblData);
        
        tblData = $('<td>');
        var roleLabels = createRoleLabels(employee.roles);
        tblData.append(roleLabels);
        tblRow.append(tblData);
        
        return tblRow;
    }
    
    function createRoleLabels(roles) {
        var labels = [];
        for (var index = 0; index < roles.length; index++) {
            var label = createLabel(roles[index].name);
            labels.push(label);
        }
        return labels;
    }
});