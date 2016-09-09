$( document ).ready(function() {

	//alert("Hola ");
    $('#agregarNivelComite').on('click', function(e){
	  e.preventDefault();
	  // alert("Hola ");
	 //  $('#modalNivelComite').modal('show').find('.modal-body').load($(this).attr('href'), function( response, status, xhr ) {
		// 	if ( status == "error" ) {
		// 		var msg = "Sorry but there was an error: ";
		// 		$( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
		// 	}
		// 	if(status == "success")
  //           	alert("External content loaded successfully!");
		// });
		$.ajax({
		   url: $(this).attr('href'),
		   // data: {
		   //    format: 'json'
		   // },
		   // error: function() {
		   //    $('#info').html('<p>An error has occurred</p>');
		   // },
		   // dataType: 'html',
		   success: function(data) {
		      // var $title = $('<h1>').text(data.talks[0].talk_title);
		      // var $description = $('<p>').text(data.talks[0].talk_description);
		      // $('#info')
		      //    .append($title)
		      //    .append($description);
		      	$('#modalNivelComite').modal('show').find('.modal-body').html(data);
		    	// setTimeout($('input[type=text]').focus(), 2000);
		    	$(data).find("#id_nombre").focus();
		   },
		   type: 'GET'
		});

	});


	$(".menuEditar").on('click', function(e){
		e.preventDefault();
		$('#modalNivelComite').modal('show').find('.modal-body').load($(this).attr('href'));
	});

	$("#guardarNivelComite").on('click', function(e){
		alert("Iniciamos la validación de datos");
	});
});

