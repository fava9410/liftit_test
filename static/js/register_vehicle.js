$( document ).ready(function() {

    $("#license_plate").val("")

	$("#license_plate").on("change keyup paste", function(){

        $.ajax({
        type:"POST",
        cache:false,
        url:"check_license_plate",
        data:{"license_plate":$("#license_plate").val()},
        success: function (response) {
            if(response == "True"){
                console.log("entre")
                $("#error_message").text("La placa ya existe");
            } else {
                $("#error_message").text("La placa no existe");
            }
        }
      });
    });
});