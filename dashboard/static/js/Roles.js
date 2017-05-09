$(document).ready(function(){

    //Initialize globals
    var json = [];
    var table = $('#roles-table')[0]; // Get table from html
    var tableRows = 0;
    get_role_data();

    function get_role_data(){
        $.ajax({
        url: '/api/roles',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = (JSON.parse(response))['roles'];
            tableRows = Object.keys(json).length;
            loadTable(table, tableRows, "rows", json);
            displayRoles(table, json);
           
            
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
        }});
    }

    $('#deleteRoleButton').click(function(){
        var rolesToDelete = [];
        var endpoint = '/api/role';
        
        $('.checkbox:checkbox:checked').each(function() {
            rolesToDelete.push($(this).val());
        });
        
        if(rolesToDelete.length > 1){
            endpoint = '/api/roles';
        }
        
        data = {
            'id': rolesToDelete,
        }
        
        $.ajax({
            url: endpoint,
            method: 'DELETE',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                $('#message').html("Role(s) deleted");
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
                window.location = "/roles";
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
    
    $("#remove_groups").click(function(){
        $("#action-button").hide();
    });
    
  
    function displayRoles(table, roles) {// call this to reload table
        if (roles) {
            
            console.log(roles)
            for (var roles_index = 0; roles_index < roles.length; roles_index++) {
                
                var role = roles[roles_index];
                console.log(table);
                table.rows[roles_index + 1].cells[1].innerHTML = role["name"]; //name
                table.rows[roles_index + 1].cells[2].innerHTML = role['description'];//description
                
                var roles_cell = table.rows[roles_index + 1].cells[3];
                displayGroups(table, role['groups'], roles_cell);
            
            }
        }
    }
    
    function displayGroups(table, groups, roles_cell) {
        
        if (groups) {
        
            for (var index = 0; index < groups.length; index++) {
                
                var group = groups[index];
                var item = $('<span></span>');
         
                item.text(group.name);
                item.addClass();
                item.css('margin-right','5px');
    
                roles_cell.append(item[0]);
            }
        }
    }
    
    function clearTable(response){
    
        $('#roles-table').find("tbody").remove();
        get_role_data()

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
        
        console.log(rolesSelected);
        
        $.ajax({
            url: '/api/roles/groups',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                $('#message').html("Group was added");
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
                
                clearTable(response);
               
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
});