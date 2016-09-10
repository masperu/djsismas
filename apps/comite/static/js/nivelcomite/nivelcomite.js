$( document ).ready(function() {

	
	toastr.options = {
		  "closeButton": false,
		  "debug": false,
		  "newestOnTop": false,
		  "progressBar": false,
		  "positionClass": "toast-bottom-right",
		  "preventDuplicates": false,
		  "onclick": null,
		  "showDuration": "300",
		  "hideDuration": "1000",
		  "timeOut": "5000",
		  "extendedTimeOut": "1000",
		  "showEasing": "swing",
		  "hideEasing": "linear",
		  "showMethod": "fadeIn",
		  "hideMethod": "fadeOut"
		}	
	//toastr.options.positionClass = "toast-bottom-left";

	//alert("Hola ");
    $('#agregarNivelComite').on('click', function(e){
	  	e.preventDefault();
	  	// alert("Hola ");
	 	$('#modalNivelComite').modal('show').find('.modal-body').load($(this).attr('href'));
	 	
	 	$('#modalNivelComite').on('shown.bs.modal', function(){
	 		$(".modal-title").text("Agregar");
	 		$('#id_nombre').focus();
	 	});

	});


	$(".menuEditar").on('click', function(e){
		e.preventDefault();
		$('#modalNivelComite').modal('show').find('.modal-body').load($(this).attr('href'));



		$('#modalNivelComite').on('shown.bs.modal', function(){
			$(".modal-title").text("Editar");
	 		$('#id_nombre').focus();
	 	});
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
            		
					toastr.success(d['msg'], 'Correcto');

					setTimeout(function(){
						location.reload();
					}, 1500);

					// toastr.options.onHidden = function() { 
					// 	alert("Cerrando mensaje de estado");
					// }

					
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





