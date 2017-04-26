// JavaScript File
$(document).ready( function() {
    
    $('.alert .close').on('click', function(e) {
        $(this).parent().hide();
    });
    
    $('#login').click(function() {
        console.log('I clicked a button');
        var username = $('#username').val();
        var password = $('#password').val();
        
        data = {
            'username': username, 
            'password': password,
        };
                
        $.ajax({
             // ajax call to users.py post method, if it returns true it logs the guest in 
            //  and redirects the user to the homepage
            url: '/api/user',
            method: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
          success: function(response) {
              console.log('woot');
                 $('#message').html("you logged in");
                 $('#alert-message')[0].classList.add('alert-success');
                 $('#alert-message').show();
                 window.location = '/';
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