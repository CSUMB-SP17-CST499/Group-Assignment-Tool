<!DOCTYPE html>
<html>
    <head>
      
        <link rel = "stylesheet" href = "EditUserRoles.css">
         
        <title>Edit User Roles</title>
        
        <!--This include the Menubar HTML(as well as boostrap and jQuery)-->
        <?php include("../Menubar/Menubar.php");?>
     
    </head>

    <body>
    
    <div class="container">
    	<div class="text-center">
          <h1>Edit Permissions</h1>
        </div>
    </div>
    
    <table class="table table-striped table table-bordered table-hover"  style = "margin:0px">
    	<thead>
			<tr align="center">
				<td style="font-weight:bold">Groups</td>
			
			</tr>
	    <thead>
	</table>

    <table class="table table-striped table table-bordered table-hover"  style = "margin:0px">

			<tr>
				<th>Role</th>
				<th>Engineer (Bugzilla)</th>
				<th>L2-Support (Bugzilla)</th>
				<th>Finance (Bugzilla)</th>
				<th>Engineer (Slack)</th>
				<th>Sales (Slack)</th>
				<th>PMO (Smartsheets)</th>
				<th>Engineer (Smartsheets)</th>
				<th>Mfg (Smartsheets)</th>
			</tr>
	  </thead>
	  </thead>
    	
	  		<tr>
				<td>Engineer</td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>

	 		</tr>
			 <tr>
				<td>PMO</td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
			
	  		</tr>
	  		<tr>
			<td>Product Manager</td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
			
			</tr>
			<tr>
				<td>Operations</td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
			
			</tr>
			<tr>
				<td>L2-Support</td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
			
			</tr>
			<tr>
				<td>L3-Support</td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				
			</tr>
			
			<tr>
				<td>Sales</td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
				<td><input type="checkbox"></td>
			
			</tr>
			
			
			
	  </tbody>
	  
   	  </table>
   	 
   	  <input type="submit" value="Save Permissions" class="btn btn-info btn-block">
	  <input type="submit" value="Cancel" class="btn btn-info btn-block">
   	 
    </body>
      
</html>