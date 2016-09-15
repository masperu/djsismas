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
	$('#agregarEstadoCivil').on('click', function(e){
		e.preventDefault();
		// alert("Hola ");
		$('#modalEstadoCivilForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalEstadoCivilForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		});
		$(".modal-title").text("Agrando");

		
	});


	$(".estadocivilEditar").on('click', function(e){
		e.preventDefault();
		$('#modalEstadoCivilForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalEstadoCivilForm').on('shown.bs.modal', function() {
			$('#id_nombre').focus();
		});
		$(".modal-title").text("Editando");

		
	});

	$("#guardarEstadoCivil").on('click', function(e){


		var $this = $(this);
		// $this.button('loading');

		$.ajax({
			url:  $("#formEstadoCivil").attr('action'),
			type: "post",
			data: $("#formEstadoCivil").serialize(),
			success: function(d) {

				if ( d["msg"] ) {
					$('#modalEstadoCivilForm').modal('hide');
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
		$('#modalEstadoCivilAlert').modal('show').find(".modal-title").text("Eliminado");
		m = "#estadocivil"+x;
		$('#modalEstadoCivilAlert').modal('show').find("p").text("Desea eliminar el "+$(m).text());

		$("#EliminarEstadoCivil").click(function(){
			
			$.post("/persona.estadocivil/eliminar/",
			{
			  idestadocivil: x, 
			  csrfmiddlewaretoken : csrftoken
			},
			function(data,status){
				$('#modalEstadoCivilAlert').modal('hide');
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

