$(document).ready(function(){

    //Initialize globals
    var information = [];
    var json = [];
    var table = $('#employees-table')[0]; // Get table from html
    var tableRows = 0;
    
    $.ajax({
        url: '/api/employees',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            information = JSON.parse(response);
            json = response;
            tableRows = information["employees"].length;
            loadEmployeeTable(table, tableRows, 4);
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


    function getEmployeeRoles(employee) {
        var roles = employee["roles"];
        var role_names = [];
        
        for(var index = 0;  index < roles.length; index++){
            
        role_names.push(roles[index]["name"])
            
        }
        return role_names
    
    }
    
    $('#all-checkbox').on('click', function(e) {
        var checkboxes = $('.checkbox');
        if (this.checked) {
            for (var i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].type == 'checkbox') {
                    checkboxes[i].checked = true;
                }
            }
        }
        else {
            for (var i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].type == 'checkbox') {
                    checkboxes[i].checked = false;
                }
         }
        }
    });
    
    function loadEmployeeTable(table, tableRows, columnAmt) {
    var column_amt = columnAmt;
    var inner_table = "";
    var id, name, email;
    inner_table += "<tbody>"

    for (var row = 0; row < tableRows; row++){
        id = information["employees"][row]["id"];
        name = information["employees"][row]["first_name"] + ' ' + information["employees"][row]["last_name"];
        email = information["employees"][row]["email"];
        arrayOfRoles = information["employees"][row]["roles"];
        var rolesString = ""
        var role = "";
            for(var x = 0; x < arrayOfRoles.length; x++){
                role = arrayOfRoles[x]["name"];
                if(x > 0){
                    rolesString += ", " + role
                }else{
                    rolesString += role;
                }
            }
        inner_table += "<tr>";
        inner_table += "<td><input class='checkbox' type='checkbox' value='" + id + "' id='" + id + "' /></td>";
        inner_table += "<td>"+ name +"</td>";
        inner_table += "<td>"+ email +"</td>";
        inner_table += "<td>"+ rolesString +"</td>";
        inner_table += "<td></td>";
        inner_table += "</tr>";
    };
    inner_table += "</tbody>";
    
    $(table).append(inner_table);
    
    $('#deleteButton').click(function(){
        var peopleToDelete = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            peopleToDelete.push($(this).val());
        });
        
        data = {
            'ids': peopleToDelete,
        }
                
        $.ajax({
            url: '/api/employees',
            method: 'DELETE',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                message = (peopleToDelete.length > 1) ? 'Users deleted.' : 'User deleted.'
                $('#message').html(message);
                $('#alert-message')[0].classList.add('alert-success');
                $('#alert-message').show();
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
    
        $('#editButton').click(function(){
            console.log("Hello")
        var editperson = [];
        
        $('.checkbox:checkbox:checked').each(function() {
            editperson.push($(this).val());
        });
        
        data = {
            'id': editperson,
        }
        
        console.log(editperson);
        
        $.ajax({
            url: '/api/employee',
            method: 'GET',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                    print(data);
                // window.location = "/employees";
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
}
});