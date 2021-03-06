var txtComitePadre = "";
var txtUbigeo = "";

$( document ).ready(function() {

	$(window).keydown(function(event){
		if(event.keyCode == 13) {
		  event.preventDefault();
		  return false;
		}
		if(event.keyCode == 27) {
		  event.preventDefault();
		  $( ".close" ).trigger( "click" );
		}
	});




	//Variables para autocomplete
	

	//toastr.success("Datos guardados correctamente");

	//alert("Hola ");
    $('#agregarComite').on('click', function(e){

    	// $(".th1").hide();
    	// $(".td1").hide(); Ocultamos columnas de una tabla

	  	e.preventDefault();

	  	// return;
	  	// alert("Hola ");
	 	$('#modalComite').modal('show').find('.modal-body').load($(this).attr('href'));
	 	
	 	$('#modalComite').on('shown.bs.modal', function(){
	 		$(".modal-title").text("Agregar comite regional");
	 		$('#nombre').focus();

	 		$("#nivelcomiteid").val($("#nivelcomite").val());

	 		$('#comitepadre_text').autocomplete({
				serviceUrl: '/comite/nacional/ajax/',
				onSelect: function (suggestion) {
				    $("#comitepadre").val(suggestion.data);
				    txtComitePadre = suggestion.value;
				}
			});

			
			$('#ubigeo_text').autocomplete({
				serviceUrl: '/comite/ubigeo/regiones/ajax/',
				onSelect: function (suggestion) {
				    $("#ubigeo").val(suggestion.data);
				    txtUbigeo = suggestion.value;
				}
			});

	 	});

	});



	$(".comiteEditar").on('click', function(e){

		// $(".td1").show();
  		//$(".td1").show(); Mostramos columnas ocultas de la tabla

		e.preventDefault();
		// return;

		$('#modalComite').modal('show').find('.modal-body').load($(this).attr('href'));

		$('#modalComite').on('shown.bs.modal', function(){
			$(".modal-title").text("Editar comite regional");
	 		$('#nombre').focus();

	 		$("#nivelcomite").val($("#nivelcomiteid").val());

	 		$('#comitepadre_text').autocomplete({
				serviceUrl: '/comite/nacional/ajax/',
				onSelect: function (suggestion) {
				    $("#comitepadre").val(suggestion.data);
				    txtComitePadre = suggestion.value;
				}
			});

			
			$('#ubigeo_text').autocomplete({
				serviceUrl: '/comite/ubigeo/regiones/ajax/',
				onSelect: function (suggestion) {
				    $("#ubigeo").val(suggestion.data);
				    txtUbigeo = suggestion.value;
				}
			});

	 	});
	});


	$(".comiteEliminar").confirm({

	    text: "Seguro que desea eliminar el item?",
	    //title: "Confirmación requerida",
	    confirm: function(button) {

	    	var link = $(button);
	        $.ajax({
	            url:  $(link).attr('href'),
	            type: "get",
	            //data: $("#formNivelComite").serialize(),

	            success: function(d) {

					if ( d["success"] ) {
						
						toastr.success(d['success']);
						setTimeout(function(){
							location.reload();
						}, 500);

					}
					else {
						toastr.success(d['error']);
					}

	            },
	            error: function(d){
	            	alert(d);
	            }
	        });
	    },
	    cancel: function(button) {
	        // nothing to do
	    },
	    confirmButton: "Eliminar",
	    cancelButton: "Cancelar",
	    post: true,
	    confirmButtonClass: "btn-danger",
	    cancelButtonClass: "btn-default",
	    // dialogClass: "modal-dialog modal-lg" // Bootstrap classes for large modal
	    dialogClass: "modal-dialog"
	});



	$("#guardarComite").on('click', function(e){

		if ( $.trim( $("#comitepadre_text").val() ).length == 0 ) {
			$("#comitepadre").val("");
			$("#comitepadre_text").val("");
			txtComitePadre = "";
		}

		if ( $.trim( $("#ubigeo_text").val() ).length == 0 ) {
			$("#ubigeo").val("");
			$("#ubigeo_text").val("");
			txtUbigeo = "";
		}

		//return;

		var $this = $(this);
		$this.button('loading');

        $.ajax({
            url:  $("#formComite").attr('action'),
            type: "post",
            data: $("#formComite").serialize(),

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
					$( ".modal-body" ).find("form").remove();
					$( ".modal-body" ).html(d);
					
					$("#nivelcomite").val($("#nivelcomiteid").val());

					//Seteamos textos
					$("#comitepadre_text").val(txtComitePadre);
					$("#ubigeo_text").val(txtUbigeo);

					$('#comitepadre_text').autocomplete({
						serviceUrl: '/comite/ajax/',
						onSelect: function (suggestion) {
						    //alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
						    $("#comitepadre").val(suggestion.data);
				    		txtComitePadre = suggestion.value;
						}
					});

					$('#ubigeo_text').autocomplete({
						serviceUrl: '/comite/ubigeo/regiones/ajax/',
						onSelect: function (suggestion) {
						    $("#ubigeo").val(suggestion.data);
						    txtUbigeo = suggestion.value;
						}
					});

				}

            }
        });

	});


});





