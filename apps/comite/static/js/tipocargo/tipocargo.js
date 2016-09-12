$( document ).ready(function() {

	$(window).keydown(function(event){
		if(event.keyCode == 13) {
		  event.preventDefault();
		  return false;
		}
	});

	$("#guardarTipoCargo").button('reset');

	//alert("Hola ");
    $('#agregarTipoCargo').on('click', function(e){

    	// $(".th1").hide();
    	// $(".td1").hide(); Ocultamos columnas de una tabla

	  	e.preventDefault();

	  	// return;
	  	// alert("Hola ");
	 	$('#modalTipoCargo').modal('show').find('.modal-body').load($(this).attr('href'));
	 	
	 	$('#modalTipoCargo').on('shown.bs.modal', function(){
	 		$(".modal-title").text("Agregar");
	 		$('#id_nombre').focus();
	 	});

	});


	$(".tipoCargoEditar").on('click', function(e){
		e.preventDefault();


		$('#modalTipoCargo').modal('show').find('.modal-body').load($(this).attr('href'));

		$('#modalTipoCargo').on('shown.bs.modal', function(){
			$(".modal-title").text("Editar");
	 		$('#id_nombre').focus();
	 	});
	});


	$(".tipoCargoEliminar").confirm({

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
	    dialogClass: "modal-dialog modal-lg" // Bootstrap classes for large modal
	});



	$("#guardarTipoCargo").on('click', function(e){

		var $this = $(this);
		$this.button('loading');

        $.ajax({
            url:  $("#formTipoCargo").attr('action'),
            type: "post",
            data: $("#formTipoCargo").serialize(),

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





