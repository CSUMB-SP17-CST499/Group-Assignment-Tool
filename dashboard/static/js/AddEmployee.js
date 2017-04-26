// JavaScript File
$(document).ready( function() {
    
    $('.alert .close').on('click', function(e) {
        $(this).parent().hide();
    });
    
    $('#create_user').on('click',function(e) {
        var firstname = $('#first_name').val();
        var lastname = $('#last_name').val();
        var email = $('#email').val();
        var roles = $('#roles').val();


        data = {
            'first_name': firstname, 
            'last_name': lastname,
            'email': email, 
            'roles': roles
        };
        
        $.ajax({
            url: '/api/employee',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                 $('#message').html("Employee was created");
                 $('#alert-message')[0].classList.add('alert-success');
                 $('#alert-message').show();
                 window.location = '/employees';
            },
            error: function(response) {
                try {
                    json = JSON.parse(response.responseText);
                    error = json.error;
                    if (error == 'email_taken') {
                        $('#message').html('The provided email is already taken.');
                        $('#alert-message')[0].classList.add('alert-danger');
                        $('#alert-message').show();
                    }
                    else if (error == 'unexpected_error') {
                        $('#message').html('There was an unexpected error. Please contact the administrator.');
                        $('#alert-message')[0].classList.add('alert-danger');
                        $('#alert-message').show();
                    }
                    else if (error == 'missing_arguments') {
                        $('#message').html('There are missing fields.');
                        $('#alert-message')[0].classList.add('alert-danger');
                        $('#alert-message').show();
                    }
                    console.log(response);
                }
                catch (e) {
                    console.log(e);
                }
            }
        });
     });
});