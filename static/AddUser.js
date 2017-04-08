// JavaScript File
$(document).ready( function() {
    
    $('.alert .close').on('click', function(e) {
        $(this).parent().hide();
    });
    
    $('#create_user').click(function() {
    
        var firstname = $('#first_name').val();
        var lastname = $('#last_name').val();
        var email = $('#email').val();
        var role = $('#Role').val();
        
        data = {
            'firstname': firstname, 
            'lastname': lastname,
            'email': email, 
            'role': role
        }
                
        $.ajax({
            url: '/api/employee',
            method: 'PUT',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
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