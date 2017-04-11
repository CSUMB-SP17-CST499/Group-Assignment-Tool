// JavaScript File


$(document).ready(function(){
    
    var employees_json = '{"employees": [{"roles": [{"role_id": 11111, "name": "kunf_fu_master", "description": "kung fu fighting"},{"role_id": 11112, "name": "sal_thekunf_fu_master", "description": "sal is kung fu fighting"}], "first_name": "Eliasar", "email": "elgandara@csumb.edu", "last_name": "Gandara"}, {"roles": [{"role_id": 22222, "name": "gym_teacher", "description": "teach gym"}], "first_name": "fake", "email": "fakeemail@fake.edu", "last_name": "person"}]}'
    var json = JSON.parse(employees_json);
      
    var page = document.getElementById("page_name").getAttribute('name'); 


    
    var table = $('#' + page)[0]; // Get table from html
    var tableRows = (json.employees.length >= 10) ? 10 : json.employees.length;
    console.log(tableRows);
    
    
    loadTable(table, tableRows);
    function loadTable(table, tableRows) {
        
        var column_amt = 4;
        
        var inner_table = "";
        var row = 0; 
        
       
        inner_table = "<thead><tr><th> <input id='all-checkbox' type='checkbox' name= '' /> Select All </th><th>Name</th><th>Email</th><th>Roles</th></tr></thead>"
        inner_table += "<tbody>"
        for (; row < tableRows; row++){
            
            inner_table += "<tr>";
            var col = 0; 
            for(;col < column_amt;col++ ){
                inner_table += "<td><input class='checkbox' type='checkbox' name='' /></td>";
            }
            inner_table += "</tr>";
        }
        inner_table += "</tbody>"
        $(table).append(inner_table);
    }
    
    
    
});