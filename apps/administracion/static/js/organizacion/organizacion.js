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
	$('#agregarOrganizacion').on('click', function(e){
		e.preventDefault();
		// alert("Hola ");
		$('#modalOrganizacionForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalOrganizacionForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		});
		$(".modal-title").text("Agrando");

		
	});


	$(".organizacionEditar").on('click', function(e){
		e.preventDefault();
		$('#modalOrganizacionForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalOrganizacionForm').on('shown.bs.modal', function() {
			$('#id_nombre').focus();
		});
		$(".modal-title").text("Editando");

		
	});

	$("#guardarOrganizacion").on('click', function(e){


		var $this = $(this);
		// $this.button('loading');

		$.ajax({
			url:  $("#formOrganizacion").attr('action'),
			type: "post",
			data: $("#formOrganizacion").serialize(),
			success: function(d) {

				if ( d["msg"] ) {
					$('#modalOrganizacionForm').modal('hide');
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
		$('#modalOrganizacionAlert').modal('show').find(".modal-title").text("Eliminado");
		m = "#organizacion"+x;
		$('#modalOrganizacionAlert').modal('show').find("p").text("Desea eliminar el "+$(m).text());

		$("#EliminarOrganizacion").click(function(){
			
			$.post("/organizacion/eliminar/",
			{
			  idorganizacion: x, 
			  csrfmiddlewaretoken : csrftoken
			},
			function(data,status){
				$('#modalOrganizacionAlert').modal('hide');
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

