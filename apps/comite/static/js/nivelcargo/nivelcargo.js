var txtComitePadre = "";

$( document ).ready(function() {

	$(window).keydown(function(event){
		if(event.keyCode == 13) {
		  event.preventDefault();
		  return false;
		}
	});

	$("#nivelcomite").val(0);

	// if ($("#totalTipoCargo").val() == 0) {
	// 	$("#guardarNivelCargo").hide();
	// }


	$('#nivelcomite').on('change', function() {
		//alert( this.value + " traemos datos" );
		// $("#guardarNivelCargo").hide();

		if ( this.value == 0) {
			$( "#contentTipoCargo" ).find("form").remove();
			return;
		}
		


		$.ajax({
            url: $("#formNivelCargo").attr('action'),
            type: "post",
            data: $("#formNivelCargo").serialize(),
            // data: {
            // 		'idnivelcomite':this.value,
            // 		'csrfmiddlewaretoken': $( "input[name=csrfmiddlewaretoken]" ).val(),
            // 		},
            success: function(d) {
				$( "#contentTipoCargo" ).find("form").remove();
				$("#contentTipoCargo").html(d);

				//TotalTipoCargo
				if ($("#totalTipoCargo").val() > 0) {
					$("#guardarNivelCargo").show();
				}

            }
        });

	});

	//Variables para autocomplete
	

	//toastr.success("Datos guardados correctamente");


	$("#guardarNivelCargo").on('click', function(e){

		var $this = $(this);
		$this.button('loading');

		//alert($("#formNivelTipoCargo").serialize());

        $.ajax({
            url:  $("#formNivelTipoCargo").attr('action'),
            type: "post",
            data: $("#formNivelTipoCargo").serialize(),

            success: function(d) {

				if ( d["msg"] ) {
					
					$this.button('reset');

					$( ".close" ).trigger( "click" );
            		
					toastr.success(d['msg']);

					setTimeout(function(){
						location.reload();
					}, 750);

				}
				else {
					$this.button('reset');
					toastr.error("Aun no guarda");
				}

            }
        });

	});


});





