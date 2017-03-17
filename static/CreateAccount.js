// JavaScript File
$(document).ready( function() {
    console.log("IS READY");
    $('#Create_Account').click(function() {
 
   // console.log("Click Function");
        $.ajax({
            url: '/createaccount',
            data: $("form").serialize(),
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