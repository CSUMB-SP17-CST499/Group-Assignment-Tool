// JavaScript File
$(document).ready( function() {
    
    $('.alert .close').on('click', function(e) {
        $(this).parent().hide();
    });
    
    $('#create_user').on('click',function(e) {
        console.log('I clicked a button');
    
        var firstname = $('#first_name').val();
        var lastname = $('#last_name').val();
        var email = $('#email').val();
        var role = $('#Role').val();
        
        data = {
            'first_name': firstname, 
            'last_name': lastname,
            'email': email, 
            'role': role
        }
                
        $.ajax({
            url: '/api/employee',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                 $('#message').html("User was created");
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