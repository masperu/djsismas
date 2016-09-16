$( document ).ready(function() {

	$(window).keydown(function(event){
		if(event.keyCode == 13) {
		  event.preventDefault();
		  return false;
		}
	});

	//toastr.success("Datos guardados correctamente");

	//alert("Hola ");
    $('#agregarNivelComite').on('click', function(e){

    	// $(".th1").hide();
    	// $(".td1").hide(); Ocultamos columnas de una tabla

	  	e.preventDefault();

	  	// return;
	  	// alert("Hola ");
	 	$('#modalNivelComite').modal('show').find('.modal-body').load($(this).attr('href'));
	 	
	 	$('#modalNivelComite').on('shown.bs.modal', function(){
	 		$(".modal-title").text("Agregar");
	 		$('#id_nombre').focus();
	 	});

	});


	$(".nivelComiteEditar").on('click', function(e){

		// $(".td1").show();
  		//$(".td1").show(); Mostramos columnas ocultas de la tabla

		e.preventDefault();
		// return;

		$('#modalNivelComite').modal('show').find('.modal-body').load($(this).attr('href'));



		$('#modalNivelComite').on('shown.bs.modal', function(){
			$(".modal-title").text("Editar");
	 		$('#id_nombre').focus();
	 	});
	});


	$(".nivelComiteEliminar").confirm({

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
	    //dialogClass: "modal-dialog modal-lg" // Bootstrap classes for large modal
	    dialogClass: "modal-dialog"
	});



	$("#guardarNivelComite").on('click', function(e){

		var $this = $(this);
		$this.button('loading');

        $.ajax({
            url:  $("#formNivelComite").attr('action'),
            type: "post",
            data: $("#formNivelComite").serialize(),

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
				}

            }
        });

	});
});





