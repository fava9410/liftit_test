$( document ).ready(function() {
    var vehicle_exists = true;
    $("#vehicle_submit").prop("disabled",vehicle_exists);
    $("#license_plate").val("")

	$("#license_plate").on("change keyup paste", function(){

        $.ajax({
            type:"POST",
            cache:false,
            url:"check_license_plate",
            data:{"license_plate":$("#license_plate").val()},
            success: function (response) {

                if(response == "True"){
                    vehicle_exists = true;
                    $("#error_message").text("La placa ya existe");
                } else {
                    vehicle_exists = false;
                    $("#error_message").text("La placa no existe");
                }

                $("#vehicle_submit").prop("disabled",vehicle_exists);
            }
        });
    });
});