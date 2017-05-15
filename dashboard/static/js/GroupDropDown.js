// JavaScript File
$(document).ready(function(){

    //Initialize globals
    var json = [];
    var table = $('#groups')[0]; // Get table from html
    
    $.ajax({
        url: '/api/groups',
        method: 'GET',
        contentType: 'application/json',
        success: function(response) {
            json = JSON.parse(response)
            var groups = json['roles'];
            displayGroupsByName(table, groups);
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
    
    function displayGroupsByName(table, groups) {
        if (groups) {
            for (var index = 0; index < groups.length; index++) {
                var group = groups[index];
                var option = $('<option></option>');
                option.val(group.id);
                option.text(group.name);
                $('#groups').append(option);
            }
        }
    }
    
    
});
