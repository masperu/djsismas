
$( document ).ready(function() {

	$(window).keydown(function(event){
		if(event.keyCode == 13) {
		  event.preventDefault();
		  return false;
		}
	});

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');


	//alert("Hola ");
	$('#agregarRol').on('click', function(e){
		e.preventDefault();
		// alert("Hola ");
		$('#modalRolForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalRolForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		});
		$(".modal-title").text("Agrando");

		
	});


	$(".rolEditar").on('click', function(e){
		e.preventDefault();
		$('#modalRolForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalRolForm').on('shown.bs.modal', function() {
			$('#id_nombre').focus();
		});
		$(".modal-title").text("Editando");

		
	});

	$(".rolEditarAcceso").on('click', function(e){
		x = $(this).attr('numeroid');
		m = "#rol"+x;

		e.preventDefault();
		$('#modalRolForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalRolForm').on('shown.bs.modal', function() {
			$('#id_menus').addClass('list-group nav nav-pills nav-stacked');
			$('#id_menus li').addClass('list-group-item ');
			// $('#id_menus li input').css({"float":"left","margin-right":"10px",});

		});
		$(".modal-title").text("Asignado menus al rol "+$(m).text());

		
	});

	$("#guardarRol").on('click', function(e){


		var $this = $(this);
		// $this.button('loading');

		$.ajax({
			url:  $("#formRol").attr('action'),
			type: "post",
			data: $("#formRol").serialize(),
			success: function(d) {

				if ( d["msg"] ) {
					$('#modalRolForm').modal('hide');
					alert(d.msg)
					location.reload();	
				}
				else {
					$( ".modal-body" ).find("form").remove();
					$( ".modal-body" ).html(d);
				}

			}
		});

	});



	$("tr a#numeroeliminar").click(function(){
		x = $(this).attr('numeroid');
		$('#modalRolAlert').modal('show').find(".modal-title").text("Eliminado");
		m = "#rol"+x;
		$('#modalRolAlert').modal('show').find("p").text("Desea eliminar el "+$(m).text());

		$("#EliminarRol").click(function(){
			
			$.post("/rol/eliminar/",
			{
			  idrol: x, 
			  csrfmiddlewaretoken : csrftoken
			},
			function(data,status){
				$('#modalRolAlert').modal('hide');
				if(data.success){
					alert(data.success);
				}else if (data.error){
					alert(data.error);
				}
				location.reload();
			});

		});
			


	});

	$("body").on('click', "#tablaRol .tabla-row", function(){

		$("#tablaRol .tabla-row").removeClass("filasSeleccionada");
		$(this).addClass("filasSeleccionada");
	
		// alert($(this).attr('id'));
		$.post( "/acceso/",{idrol : $(this).attr('id'), csrfmiddlewaretoken : csrftoken}, function( data ) {
			$( "body .divClassTablaMenu" ).html( data );
			// $( "body .divClassTablaMenu" ).show();
			// alert( data );
		});
	});

	$("#tablaRol .tabla-row").addClass("selecting");

});

