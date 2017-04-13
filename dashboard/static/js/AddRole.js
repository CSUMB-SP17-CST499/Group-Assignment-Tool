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

        
        data = {
            'name': roleName, 
            'description': roleDescription
        };
                
        $.ajax({
            url: '/api/role',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                 $('#message').html("Role was created");
                 $('#alert-message')[0].classList.add('alert-success');
                 $('#alert-message').show();
                 // refresh the page so that the valeus are not still on the page after the user was created
                 //document.url;
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