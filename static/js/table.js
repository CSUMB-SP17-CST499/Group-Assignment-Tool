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
        for(var col = 1; col < column_amt; col++){
            inner_table += "<td></td>";
        }
        inner_table += "</tr>";
    }
    inner_table += "</tbody>"
    $(table).append(inner_table);
}