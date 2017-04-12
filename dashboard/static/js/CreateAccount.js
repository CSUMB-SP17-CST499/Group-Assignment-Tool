// JavaScript File
// Todo: Disable button click while processing a request
// Todo: Make only one alert message visible at a time,
//      stack the alert messages with a number, 
//      and display messages as close button is pressed

$(document).ready( function() {
    
    $('.alert .close').on('click', function(e) {
        $(this).parent().hide();
    });
    
    $('#Create_Account').click(function() {
    
        var firstname = $('#firstname').val();
        var lastname = $('#lastname').val();
        var email = $('#email').val();
        var username = $('#username').val();
        var password = $('#password').val();
        
        data = {
            'firstname': firstname, 
            'lastname': lastname,
            'email': email, 
            'username': username, 
            'password': password
        }
                
        $.ajax({
            url: '/createaccount',
            method: 'POST',
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