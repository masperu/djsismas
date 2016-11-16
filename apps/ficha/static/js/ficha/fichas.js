var txtComitePadre = "";

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

    
    $('#agregarFicha').on('click', function(e){
	  	e.preventDefault();
	 	$('#modalFichaForm').modal('show').find('.modal-body').load($(this).attr('href'));
	 	
	 	$('#modalFichaForm').on('shown.bs.modal', function(){
	 		$(".modal-title").text("Agregar ficha");
	 		$('#nombre').focus();

	 		$("#nivelcomite").val($("#nivelcimiteid").val());

			$('#comitepadre_text').autocomplete({
				serviceUrl: '/comite/ajax/',
				onSelect: function (suggestion) {
				    $("#comitepadre").val(suggestion.data);
				    txtComitePadre = suggestion.value;
				}
			});



	 	});

	});


	$(".comiteEditar").on('click', function(e){

		e.preventDefault();
		// return;

		$('#modalComite').modal('show').find('.modal-body').load($(this).attr('href'));



		$('#modalComite').on('shown.bs.modal', function(){
			$(".modal-title").text("Editar ficha");
	 		$('#id_nombre').focus();

	 		$("#nivelcomite").val($("#nivelcimiteid").val());

			$('#comitepadre_text').autocomplete({
				serviceUrl: '/comite/ajax/',
				onSelect: function (suggestion) {
				    //alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
				    $("#comitepadre").val(suggestion.data);
				    txtComitePadre = suggestion.value;
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
					
					$("#nivelcomite").val($("#nivelcimiteid").val());

					$("#comitepadre_text").val(txtComitePadre);

					$('#comitepadre_text').autocomplete({
						serviceUrl: '/comite/ajax/',
						onSelect: function (suggestion) {
						    //alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
						    $("#comitepadre").val(suggestion.data);
				    		txtComitePadre = suggestion.value;
						}
					});

				}

            }
        });

	});


	$("#validarDNI").on("click", function(e){

		alert("Validamos los datos del DNI");
		
	});

	



});





