
	$('.selectpicker').selectpicker({
		// 	// style: 'btn-info',
			size: 5
	});
	$('#datetimepicker1').datetimepicker({
		format:'YYYY-MM-DD',
	});
	// $("#idubigeonacimiento").click(function(e) {
	// 	$('#modalUbigeo').modal('show').find('.modal-body').load($(this).attr('href'));
	// 	// $('#modalUbigeo').on('shown.bs.modal', function() {

	// 	// });


	// });
	$('#modalUbigeo').on('shown.bs.modal', function() {
			  $('#btnAgregarUbigeo').on('click', function(){
				alert("asas");
			});
		});