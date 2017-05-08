/*
    global $
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
    
    if (table) {
        for (var i = 0; i < table.tBodies.length; i++) {
            table.tBodies.item(0).remove()
        }
    }
    
    var tblBody = $('<tbody></tbody>')
    for (var index = 0; index < array.length; index++) {
        var tblRow = callback(array[index]);
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

function createLabels(titles) {
    var labels = [];
    for (var index = 0; index < titles.length; index++) {
        var label = createLabel(titles[index]);
        labels.push(label);
    }
    return labels;
}

function createTableDataCheckbox(value) {
    var tblData = $('<td>');
    var checkbox = $('<input>');
    checkbox.addClass('checkbox');
    checkbox.attr('type', 'checkbox');
    checkbox.val(value);
    tblData.append(checkbox);
    return tblData;
}

function createTableDataText(text) {
    var tblData = $('<td>');
    tblData.text(text);
    return tblData;
}

function createTableDataLabels(labelTexts) {
    var tblData = $('<td>');
    var labels = createLabels(labelTexts);
    tblData.append(labels);
    return tblData;
}