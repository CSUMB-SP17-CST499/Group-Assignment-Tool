/*
 *  Filename: table.js
 *  Description: This script will handle modifications to the data tables.
 *
 */

function loadTable(table, tableRows, columnAmt) {
    var column_amt = columnAmt;
    var inner_table = "";
    inner_table += "<tbody>"
    
    for (var row = 0; row < tableRows; row++){
        inner_table += "<tr>";
        inner_table += "<td><input class='checkbox' type='checkbox' name='' /></td>";
        for(var col = 1; col < columnAmt; col++){
            inner_table += "<td></td>";
        }
        inner_table += "</tr>";
    }
    inner_table += "</tbody>";
    $(table).append(inner_table);
}

function loadEmployeeTable(table, tableRows, columnAmt) {
    var json;
    var column_amt = columnAmt;
    var inner_table = "";
    inner_table += "<tbody>"
    
    $.ajax({
        url: '/api/employees',
        method: 'GET',
        contentType: 'json',
        success: function(response) {
            json = response;
            for (var row = 0; row < tableRows; row++){
                var id = JSON.parse(json)["employees"][row]['id'];
                console.log(id);
                inner_table += "<tr>";
                inner_table += "<td><input class='checkbox' type='checkbox' id='" + id + "' /></td>";
                for(var col = 1; col < column_amt; col++){
                    inner_table += "<td></td>";
                };
                inner_table += "</tr>";
            };
            inner_table += "</tbody>";
            $(table).append(inner_table);
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
    console.log(json);
    

}