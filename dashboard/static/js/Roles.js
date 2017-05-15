/*
    global $
    global loadTableBody
    global createLabels
    global createTableDataText
    global createTableDataCheckbox
    global createTableDataLabels
*/
$(document).ready(function(){    
    loadRoleTable();
  
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
    
        var rolesToDelete = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            rolesToDelete.push($(this).val());
        });
        
        print(rolesToDelete)
        var data = {
            'ids': rolesToDelete,
        }
        
        $.ajax({
            url: '/api/roles',
            method: 'DELETE',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                var message = (rolesToDelete.length > 1) ? 'Users deleted.' : 'User deleted.'
                $('#message').html(message);
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
                
                loadRoleTable();
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
        
        
    function createRoleRow(role) {
        var tblRow = $('<tr>');
        
        var tblData = createTableDataCheckbox(role.id)
        tblRow.append(tblData);
        
        var roleName = role.name;
        tblData = createTableDataText(roleName);
        tblRow.append(tblData);
        
        tblData = createTableDataText(role.description)
        tblRow.append(tblData);
        
        var groupNames = getGroupNames(role.groups);
        tblData = createTableDataLabels(groupNames);
        tblRow.append(tblData);
        
        return tblRow;
    }
    
  
    
    function getGroupNames(groups) {
        var names = groups.map(function(group) {
            return group.name;
        });
        return names;
    }
    
    function loadRoleTable() {////
        $.ajax({
            url: '/api/roles',
            method: 'GET',
            success: function(response) {
                
                try {
                    var json = JSON.parse(response);
                    var roles = json.roles;
                    var table = $('#roles-table')[0];
                    loadTableBody(table, roles, createRoleRow);
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
    
     $('#save').click(function(){
        
        
        var groupsSelected = $('#groups').val()
        
        console.log(groupsSelected)
        
        
        var rolesSelected = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            rolesSelected.push($(this).val());
        });
        
        var data = {
            
            'role_ids': rolesSelected,
            'group_ids': groupsSelected
            
        }
        console.log(rolesSelected)
        console.log(data)
        $.ajax({
            url: '/api/roles/groups',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                $('#message').html("Group was added");
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
               console.log("success") 
               loadRoleTable();
               
               
            },
            error: function(error) {
                try {
                    json = JSON.parse(error.responseText);
                    if (json.message) {
                        $('#message').html(json.message);
                        $('#alert-message')[0].classList.add('alert-danger');
                        $('#alert-message').show();
                        console.log("error!1");
                    }
                }
                catch (e) {
                    console.log(e);
                    console.log("error!2");
                }
            }
        });
    });
});