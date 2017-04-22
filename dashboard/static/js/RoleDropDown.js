// JavaScript File

$(document).ready(function(){

    //Initialize globals
    var json = [];
    var table = $('#role_select')[0]; // Get table from html
    var tableRows = 0;
    
    $.ajax({
        url: '/api/roles',
        method: 'GET',
        contentType: 'application/json',
        success: function(response) {
            json = JSON.parse(response)
            roles = json['roles'];
            displayRolesByName(table, roles);
            console.log("ROLES");
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
    
    function displayRolesByName(table, roles) {
        if (roles) {
            for (var index = 0; index < roles.length; index++) {
                var role = roles[index];
                var option = $('<option></option>');
                option.val(role.id);
                option.text(role.name);
                $('#roles').append(option);
            }
        }
    }
});
