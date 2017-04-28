/*
 *  Filename: table.js
 *  Description: This script will handle modifications to the data tables.
 *
 */

function loadTable(table, tableRows, IDtype, json) {
    var column_amt;
    var inner_table = "";
    var id, name, description;
    
    if (IDtype === "rows"){
        column_amt = 4;
    }
    
    inner_table += "<tbody>"
    
    for (var row = 0; row < tableRows; row++){
        if (IDtype == "rows"){
            id = json[row]["id"];
        }
        inner_table += "<tr>";
        inner_table += "<td><input class='checkbox' type='checkbox' value='" + id + "' id='" + id + "' /></td>";
        for(var col = 1; col < column_amt; col++){
            inner_table += "<td></td>";
        }
        inner_table += "</tr>";
    }
    inner_table += "</tbody>";
    $(table).append(inner_table);
}