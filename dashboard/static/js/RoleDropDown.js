// JavaScript File

$(document).ready(function(){

    //Initialize globals
    var json = [];
    var table = $('#role_select')[0]; // Get table from html
    var tableRows = 0;
    loadList(table, tableRows);
    
    $.ajax({
        
        url: '/api/roles',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = (JSON.parse(response))['roles'];
            tableRows = Object.keys(json).length;
            loadList(table, tableRows);
            displayRolesByName(table, json);
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
    
            function displayRolesByName(table,roles) {
        if (roles) {
            
            for (var index = 0; index < roles.length; index++) {
                
                var role = roles[index];
                
                console.log(role["name"]);
               // table.rows[index + 1].cells[1].innerHTML = role["name"];//name
                
            }
         
               
            
        }
    }
    
function loadList(table, tableRows) {
    var inner_table = "";
    
    for (var row = 0; row < tableRows; row++){
        inner_table += "<option>";
        inner_table += "</option>";
    }
    $(table).append(inner_table);
}

});
