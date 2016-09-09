$( document ).ready(function() {

	var myToast = $.toast('Some toast that needs to be removed.');

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
                //alert(d);

             $this.button('reset');
             myToast.update({
			    text : '<strong>Updated after a few seconds</strong>',
			    bgColor : '#23B65D'
			  });

             //return;

             if ( d["msg"] ) {
             	//alert(d["msg"]);
             	mostrarMesaje(d["msg"]);
             }
             else {
             	$( ".modal-body" ).find("form").remove();
             	$( ".modal-body" ).html(d);
             }

            }
        });

	});

	function mostrarMesaje(msj) {
		$.toast({
		    heading: 'Correcto',
		    text: msj,
		    showHideTransition: 'slide',
		    icon: 'success'
		});
	}
});





