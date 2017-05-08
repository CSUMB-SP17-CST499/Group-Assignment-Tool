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


function loadTableHead(table, array) {
    var tblHead = $('<thead></thead>');
    var tblRow = $('<tr></tr>');
    
    for (var index = 0; index < array.length; index++) {
        var tblData = $('<td></td>');
        tblData.html(array[index]);
        tblRow.append(tblData);
    }
    
    table.append(tblHead.get(0));
}


function loadTableBody(table, array, callback) {
    
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }
    
    var tblBody = $('<tbody></tbody>')
    for (var index = 0; index < array.length; index++) {
        tblRow = callback(array[index]);
        tblBody.append(tblRow);
    }
    
    table.append(tblBody.get(0));
}


function createLabel(text) {
    var label = $('<span>');

    label.text(text);
    label.addClass('btn btn-primary btn-xs');
    label.css('margin-right','5px');
    
    return label.get(0);
}