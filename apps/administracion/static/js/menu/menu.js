
$( document ).ready(function() {

	//alert("Hola ");
    $('#agregarMenu').on('click', function(e){
	  e.preventDefault();
	  // alert("Hola ");
	  $('#modalMenuForm').modal('show').find('.modal-body').load($(this).attr('href'));
	});


	$(".menuEditar").on('click', function(e){
		e.preventDefault();
		$('#modalMenuForm').modal('show').find('.modal-body').load($(this).attr('href'));
	});
});

