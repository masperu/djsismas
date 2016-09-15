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
	$('#agregarTipoCalle').on('click', function(e){
		e.preventDefault();
		// alert("Hola ");
		$('#modalTipoCalleForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalTipoCalleForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		});
		$(".modal-title").text("Agrando");

		
	});


	$(".tipocalleEditar").on('click', function(e){
		e.preventDefault();
		$('#modalTipoCalleForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalTipoCalleForm').on('shown.bs.modal', function() {
			$('#id_nombre').focus();
		});
		$(".modal-title").text("Editando");

		
	});

	
	$("#guardarTipoCalle").on('click', function(e){

		var $this = $(this);
		// $this.button('loading');

		$.ajax({
			url:  $("#formTipoCalle").attr('action'),
			type: "post",
			data: $("#formTipoCalle").serialize(),
			success: function(d) {

				if ( d["msg"] ) {
					$('#modalTipoCalleForm').modal('hide');
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
		$('#modalTipoCalleAlert').modal('show').find(".modal-title").text("Eliminado");
		m = "#tipocalle"+x;
		$('#modalTipoCalleAlert').modal('show').find("p").text("Desea eliminar el "+$(m).text());

		$("#EliminarTipoCalle").click(function(){
			
			$.post("/persona.tipocalle/eliminar/",
			{
			  idtipocalle: x, 
			  csrfmiddlewaretoken : csrftoken
			},
			function(data,status){
				$('#modalTipoCalleAlert').modal('hide');
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

