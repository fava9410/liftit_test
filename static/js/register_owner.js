$( document ).ready(function() {

    $("#number_document").val("")

	$("#number_document").on("change keyup paste", function(){

        $.ajax({
        type:"POST",
        cache:false,
        url:"check_owner",
        data:{"number_document":$("#number_document").val()},
        success: function (response) {

            if(response == "True"){
                console.log("entre")
                $("#error_message").text("El propietario ya existe");
            } else {
                $("#error_message").text("El propietario no ha sido registrado");
            }
        }
      });
    });
});