
$( document ).ready(function() {

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
	$('#agregarMenu').on('click', function(e){
	  e.preventDefault();
	  // alert("Hola ");
	  $('#modalMenuForm').modal('show').find('.modal-body').load($(this).attr('href'));
	  $('#modalMenuForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		});
	  $(".modal-title").text("Agrando");
	});


	$(".menuEditar").on('click', function(e){
		e.preventDefault();
		$('#modalMenuForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalMenuForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		});
		$(".modal-title").text("Editando");
	});

	$("#guardarMenu").on('click', function(e){

		var $this = $(this);
		// $this.button('loading');

		$.ajax({
			url:  $("#formMenu").attr('action'),
			type: "post",
			data: $("#formMenu").serialize(),
			success: function(d) {

				if ( d["msg"] ) {
					$('#modalMenuForm').modal('hide');
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
		$('#modalMenuAlert').modal('show').find(".modal-title").text("Eliminado");
		m = "#menu"+x;
		$('#modalMenuAlert').modal('show').find("p").text("Desea eliminar el "+$(m).text());

		$("#EliminarMenu").click(function(){
			
			$.post("/menu/eliminar/",
			{
			  idmenu: x, 
			  csrfmiddlewaretoken : csrftoken
			},
			function(data,status){
				$('#modalMenuAlert').modal('hide');
				if(data.success){
					alert(data.success);
				}else if (data.error){
					alert(data.error);
				}
				location.reload();
			});

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

