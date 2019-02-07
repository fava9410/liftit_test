$( document ).ready(function() {

	$("#search").click(function(){
        console.log($("#vehicle_brand").val());
        $.ajax({
            type:"POST",
            cache:false,
            url:"filter_vehicles_by_brand",
            data:{
                "brand":$("#vehicle_brand").val()
                },
            success: function (response) {

                if(response == "True"){
                    $("#error_message").text("El propietario ya existe");
                } else {
                    $("#error_message").text("El propietario no ha sido registrado");
                }
            }
        });
    });
});