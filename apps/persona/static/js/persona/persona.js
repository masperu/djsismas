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
	$('#agregarPersona').on('click', function(e){
		e.preventDefault();
		// alert("Hola ");
		$('#modalPersonaForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalPersonaForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		});

		$(".modal-title").text("Agregando");
		
	});


	$(".personaEditar").on('click', function(e){
		e.preventDefault();
		$('#modalPersonaForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalPersonaForm').on('shown.bs.modal', function() {
			$('#id_nombre').focus();
		});
		$(".modal-title").text("Editando");		
	});

	
	$("#guardarPersona").on('click', function(e){

		var $this = $(this);
		// $this.button('loading');
		
		$.ajax({
			url:  $("#formPersona").attr('action'),
			type: "post",
			data: $("#formPersona").serialize(),
			success: function(d) {

				if ( d["msg"] ) {
					$('#modalPersonaForm').modal('hide');
					alert(d.msg)
					location.reload();	
				}
				else {
					$('#modalPersonaForm').modal('show').find('form').remove();
					$('#modalPersonaForm').modal('show').find( ".modal-body" ).html(d);
				// 	$( ".modal-body" ).find("form").remove();
				// 	$( ".modal-body" ).html(d);
				}

			}
		});

	});



	$("tr a#numeroeliminar").click(function(){
		x = $(this).attr('numeroid');
		$('#modalPersonaAlert').modal('show').find(".modal-title").text("Eliminado");
		m = "#persona"+x;
		$('#modalPersonaAlert').modal('show').find("p").text("Desea eliminar el "+$(m).text());

		$("#EliminarPersona").click(function(){
			
			$.post("/persona.persona/eliminar/",
			{
			  idpersona: x, 
			  csrfmiddlewaretoken : csrftoken
			},
			function(data,status){
				$('#modalPersonaAlert').modal('hide');
				if(data.success){
					alert(data.success);
				}else if (data.error){
					alert(data.error);
				}
				location.reload();
			});

		});


	});

});

