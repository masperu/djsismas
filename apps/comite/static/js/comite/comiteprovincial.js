var txtComitePadre = "";
var txtUbigeo = "";
var txtRegion = "";
var idregion = 0;
var ubigeo = 0;


var tecla = jQuery.Event("keydown");
tecla.which = 8; // # Codigo del eliminar


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
    $('#agregarComite').on('click', function(e){

    	// $(".th1").hide();
    	// $(".td1").hide(); Ocultamos columnas de una tabla

	  	e.preventDefault();

	  	// return;
	  	// alert("Hola ");
	 	$('#modalComite').modal('show').find('.modal-body').load($(this).attr('href'));
	 	
	 	$('#modalComite').on('shown.bs.modal', function(){
	 		$(".modal-title").text("Agregar comite provincial");
	 		$('#nombre').focus();

	 		$("#nivelcomiteid").val($("#nivelcomite").val());

	 		$('#comitepadre_text').autocomplete({
				serviceUrl: '/comite/regional/ajax/',
				onSelect: function (suggestion) {
				    $("#comitepadre").val(suggestion.data);
				    txtComitePadre = suggestion.value;
				}
			});

			
			$('#region_text').autocomplete({
				serviceUrl: '/comite/ubigeo/regiones/ajax/',
				onSelect: function (suggestion) {
				    $("#regionid").val(suggestion.data);
				    $("#regionselected").val(suggestion.data);
				    txtRegion = suggestion.value;

				    $(this).prop('disabled', true);
				    $(".enabledautocomplete").show();


				    $(".enabledautocompleteubigeo").trigger('click');
				    //Desencademos el evento eliminar
				    
				}
			});


			$('#ubigeo_text').autocomplete({
				serviceUrl: '/comite/ubigeo/provincias/ajax/',
			    onSearchStart: function (){

			        $(this).autocomplete('setOptions', { params: { 'regionid' : $("#regionselected").val(), } });
			    },
				onSelect: function (suggestion) {
				    $("#ubigeo").val(suggestion.data);
				    txtUbigeo = suggestion.value;

				    $(this).prop('disabled', true);
				    $(".enabledautocompleteubigeo").show();

				}
			});


			$('.enabledautocomplete').on('click', function(){
				$(this).hide();
				$("#region_text").prop('disabled', false);
				$("#region_text").val("").focus();
				$("#regionid").val("0");
				$("#ubigeo_text").val("").prop('disabled', true);
				$("#ubigeo").val("0");
				//$(".enabledautocomplete").show();
			});


			$('.enabledautocompleteubigeo').on('click', function(){
				$(this).hide();
				$("#ubigeo_text").prop('disabled', false);
				$("#ubigeo_text").val("").focus();
				$("#ubigeo").val("0");

				$("#ubigeo_text").val("Escriba para buscar").select();;
				
				//$(".enabledautocomplete").show();
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
			$(".modal-title").text("Editar comite provincial");
	 		$('#nombre').focus();

	 		$("#nivelcomite").val($("#nivelcomiteid").val());

	 		$('#comitepadre_text').autocomplete({
				serviceUrl: '/comite/regional/ajax/',
				onSelect: function (suggestion) {
				    $("#comitepadre").val(suggestion.data);
				    txtComitePadre = suggestion.value;
				}
			});

			
			$('#region_text').autocomplete({
				serviceUrl: '/comite/ubigeo/regiones/ajax/',
				onSelect: function (suggestion) {
				    $("#regionid").val(suggestion.data);
				    $("#regionselected").val(suggestion.data);
				    txtRegion = suggestion.value;

				    $(this).prop('disabled', true);
				    $(".enabledautocomplete").show();


				    $(".enabledautocompleteubigeo").trigger('click');
				    //Desencademos el evento eliminar
				    
				}
			});


			$('#ubigeo_text').autocomplete({
				serviceUrl: '/comite/ubigeo/provincias/ajax/',
			    onSearchStart: function (){

			        $(this).autocomplete('setOptions', { params: { 'regionid' : $("#regionselected").val(), } });
			    },
				onSelect: function (suggestion) {
				    $("#ubigeo").val(suggestion.data);
				    txtUbigeo = suggestion.value;

				    $(this).prop('disabled', true);
				    $(".enabledautocompleteubigeo").show();

				}
			});


			$('.enabledautocomplete').on('click', function(){
				$(this).hide();
				$("#region_text").prop('disabled', false);
				$("#region_text").val("").focus();
				$("#regionid").val("0");
				$("#ubigeo_text").val("").prop('disabled', true);
				$("#ubigeo").val("0");
				//$(".enabledautocomplete").show();
			});


			$('.enabledautocompleteubigeo').on('click', function(){
				$(this).hide();
				$("#ubigeo_text").prop('disabled', false);
				$("#ubigeo_text").val("").focus();
				$("#ubigeo").val("0");

				$("#ubigeo_text").val("Escriba para buscar").select();;
				
				//$(".enabledautocomplete").show();
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
			toastr.error("Seleccione el comite padre");
			$("#comitepadre_text").focus();
			return;
		}

		if ( $.trim( $("#ubigeo_text").val() ).length == 0 ) {
			$("#ubigeo").val("");
			$("#ubigeo_text").val("");
			txtUbigeo = "";
			ubigeo = 0;
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
					$("#region_text").val(txtRegion);
					$("#ubigeo_text").val(txtUbigeo);

					$("#nivelcomiteid").val($("#nivelcomite").val());

			 		

					//Funciones de autocompletar
			 		$('#comitepadre_text').autocomplete({
						serviceUrl: '/comite/regional/ajax/',
						onSelect: function (suggestion) {
						    $("#comitepadre").val(suggestion.data);
						    txtComitePadre = suggestion.value;
						}
					});

					
					$('#region_text').autocomplete({
						serviceUrl: '/comite/ubigeo/regiones/ajax/',
						onSelect: function (suggestion) {
						    $("#regionid").val(suggestion.data);
						    $("#regionselected").val(suggestion.data);
						    txtRegion = suggestion.value;

						    $(this).prop('disabled', true);
						    $(".enabledautocomplete").show();


						    $(".enabledautocompleteubigeo").trigger('click');
						    //Desencademos el evento eliminar
						    
						}
					});


					$('#ubigeo_text').autocomplete({
						serviceUrl: '/comite/ubigeo/provincias/ajax/',
					    onSearchStart: function (){

					        $(this).autocomplete('setOptions', { params: { 'regionid' : $("#regionselected").val(), } });
					    },
						onSelect: function (suggestion) {
						    $("#ubigeo").val(suggestion.data);
						    txtUbigeo = suggestion.value;

						    $(this).prop('disabled', true);
						    $(".enabledautocompleteubigeo").show();

						}
					});


					$('.enabledautocomplete').on('click', function(){
						$(this).hide();
						$("#region_text").prop('disabled', false);
						$("#region_text").val("").focus();
						$("#regionid").val("0");
						$("#ubigeo_text").val("").prop('disabled', true);
						$("#ubigeo").val("0");
						//$(".enabledautocomplete").show();
					});


					$('.enabledautocompleteubigeo').on('click', function(){
						$(this).hide();
						$("#ubigeo_text").prop('disabled', false);
						$("#ubigeo_text").val("").focus();
						$("#ubigeo").val("0");

						$("#ubigeo_text").val("Escriba para buscar").select();;
						
						//$(".enabledautocomplete").show();
					});


				}

            }
        });

	});


});





