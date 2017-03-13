// JavaScript File
$(function() {
    $('#Create Account').click(function() {
 
        $.ajax({
            url: '/createaccount',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});