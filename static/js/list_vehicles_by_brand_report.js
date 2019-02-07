$( document ).ready(function() {
    $('#vehicles').DataTable();

	$("#search").click(function(){
        $.ajax({
            type:"GET",
            cache:false,
            url:"filter_vehicles_by_brand/"+$("#vehicle_brand").val(),
            success: function (response) {
                console.log(response)
            }
        });
    });
});