$(document).ready(function(){

    //Initialize globals
    var json = [];
    var table = $('#roles-table')[0]; // Get table from html
    var tableRows = 0;
    loadTable(table, tableRows,3);
    
    $.ajax({
        url: '/api/roles',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = (JSON.parse(response))['roles'];
            tableRows = Object.keys(json).length;
            loadTable(table, tableRows,3);
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
    
    // var roles_json = '{"roles": [{"name": "kunf_fu_master", "description": "kung fu fighting", "id": 11111}, {"name": "gym_teacher", "description": "teach gym", "id": 22222}]}'
    // var roles = JSON.parse(roles_json)["roles"];
    
    // displayRoles(table, roles);
    
    function displayRoles(table, roles) {
        if (roles) {
            
            for (var index = 0; index < roles.length; index++) {
                
                var role = roles[index];
                
                console.log(role["name"])
                table.rows[index + 1].cells[1].innerHTML = role["name"]//name
                table.rows[index + 1].cells[2].innerHTML = role['description'];//description
                
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