$(document).ready(function(){

    //Initialize globals
    var json = [];
    var table = $('#roles-table')[0]; // Get table from html
    var tableRows = 0;

    $.ajax({
        url: '/api/roles',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = (JSON.parse(response))['roles'];
            tableRows = Object.keys(json).length;
            loadTable(table, tableRows,4);
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
        }
    });
    
    function displayRoles(table, roles) {
        if (roles) {
            
            for (var roles_index = 0; roles_index < roles.length; roles_index++) {
                
                var role = roles[roles_index];
                
                console.log(role["name"])
                table.rows[roles_index + 1].cells[1].innerHTML = role["name"]//name
                table.rows[roles_index + 1].cells[2].innerHTML = role['description'];//description
                
                var roles_cell = table.rows[roles_index + 1].cells[3]
                displayGroups(table, role['groups'], roles_cell)
            
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