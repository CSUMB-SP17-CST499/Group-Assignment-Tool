// JavaScript File
// JavaScript File
$(document).ready( function() {
    
    $('.alert .close').on('click', function(e) {
        $(this).parent().hide();
    });
    
    $('#create_role').on('click',function(e) {
        console.log('I clicked a button');
    
        var roleName = $('#role_name').val();
        var roleDescription = $('#role_description').val();
        var groups = $('#groups').val();

        //console.log("Name", roleName);
        var data = {
            'name': roleName, 
            'description': roleDescription,
            'groups': groups
        };
    
        console.log(data)
        
        $.ajax({
            url: '/api/role',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                 $('#message').html("Role was created");
                 $('#alert-message')[0].classList.add('alert-success');
                 $('#alert-message').show();
                 window.location = '/roles';
                
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