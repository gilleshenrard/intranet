/**
 * Compares the regex sent to the ID value, and sets the form-group and tip accordingly
 * @param {string} regex
 * @param {string} id
 */
function checkValues(regex, id){
    if (regex.test($("#id_"+id).val())) {
        $("#group_"+id).removeClass("has-danger");
        $("#group_"+id).addClass("has-success");
        $("#fb_"+id).removeClass("glyphicon-remove");
        $("#fb_"+id).addClass("glyphicon-ok");
        //$("#tip_"+id).addClass("hidden");
        //return true;
    } else {
        $("#group_"+id).removeClass("has-success");
        $("#group_"+id).addClass("has-danger");
        $("#fb_"+id).removeClass("glyphicon-ok");
        $("#fb_"+id).addClass("glyphicon-remove");
        //$("#tip_"+id).removeClass("hidden");
        //return false;
    }
}

/**
 * Makes an Ajax call through a POST message
 */
function update_profile(){
	$.ajax({
		url : $("#id_username").val(),
		type : "POST",
		data : { first_name : $("#id_first_name").val(),
				last_name : $("#id_last_name").val(),
				country : $("#id_country").val(),
				email : $("#id_email").val(),
				phone : $("#id_phone").val(),
				field : $("#id_field").val(),
				occupation : $("#id_occupation").val(),
				birthdate : $("#id_birthdate").val(),
				description : $("#id_description").val()},
		
		success : function(json) {
			console.log("SUCCESS! " + $("#id_username").val() + " updated!")
		},
		
		error : function(xhr, errmsg, err) {
			console.log("Oops! We have encountered an error: "+errmsg);
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}

$(document).ready(function(){
    
    /**
     * Impedes the default submission to replace it with Ajax
     */

    $("#profile_form").on('submit', function(event){
    	event.preventDefault();
    	console.log("Form submitted");
    	update_profile();
    });

});