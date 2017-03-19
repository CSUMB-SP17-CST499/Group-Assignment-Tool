// JavaScript File
$(document).ready( function() {
    $('#login').click(function() {
        
    var username = $('#username').val();
    var password = $('#userPassword').val();
    
   // console.log("Click Function");
        $.ajax({
            url: '/loginDB',
            data: $('form').serialize(),
            method: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
     });
});