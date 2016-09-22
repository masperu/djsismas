// var txtUsuarioPadre = "";
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
	$('#agregarUsuario').on('click', function(e){
		e.preventDefault();
		// alert("Hola ");
		$('#modalUsuarioForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalUsuarioForm').on('shown.bs.modal', function() {
		  $('#id_nombre').focus();
		 //  $('#menupadre_text').autocomplete({
			// 	serviceUrl: '/menu/ajax/',
			// 	onSelect: function (suggestion) {
			// 	    //alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
			// 	    $("#menupadre").val(suggestion.data);
			// 	    txtUsuarioPadre = suggestion.value;
			// 	}
			// });
		});
		$(".modal-title").text("Agrando");

		
	});


	$(".usuarioEditar").on('click', function(e){
		e.preventDefault();
		$('#modalUsuarioForm').modal('show').find('.modal-body').load($(this).attr('href'));
		$('#modalUsuarioForm').on('shown.bs.modal', function() {
			$('#id_nombre').focus();
			// $('#menupadre_text').autocomplete({
			// 	serviceUrl: '/menu/ajax/',
			// 	onSelect: function (suggestion) {
			// 	    // alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
			// 	    $("#menupadre").val(suggestion.data);
			// 	    txtUsuarioPadre = suggestion.value;
			// 	}
			// });
		});
		$(".modal-title").text("Editando");

		
	});

	$("#guardarUsuario").on('click', function(e){


		// if ( $.trim( $("#menupadre_text").val() ).length == 0 ) {
		// 	$("#menupadre").val("");
		// 	$("#menupadre_text").val("");
		// }


		var $this = $(this);
		// $this.button('loading');

		$.ajax({
			url:  $("#formUsuario").attr('action'),
			type: "post",
			data: $("#formUsuario").serialize(),
			success: function(d) {

				if ( d["msg"] ) {
					$('#modalUsuarioForm').modal('hide');
					alert(d.msg)
					location.reload();	
				}
				else {
					$( ".modal-body" ).find("form").remove();
					$( ".modal-body" ).html(d);
					// $("#menupadre_text").val(txtUsuarioPadre);
					// $('#menupadre_text').autocomplete({
					// 	serviceUrl: '/menu/ajax/',
					// 	onSelect: function (suggestion) {
					// 	    //alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
					// 	    $("#menupadre").val(suggestion.data);
				 //    		txtUsuarioPadre = suggestion.value;
					// 	}
					// });
				}

			}
		});

	});



	$("tr a#numeroeliminar").click(function(){
		x = $(this).attr('numeroid');
		$('#modalUsuarioAlert').modal('show').find(".modal-title").text("Eliminado");
		m = "#usuario"+x;
		$('#modalUsuarioAlert').modal('show').find("p").text("Desea eliminar el usuario "+$(m).text());

		$("#EliminarUsuario").click(function(){
			
			$.post("/usuario/eliminar/",
			{
			  idusuario: x, 
			  csrfmiddlewaretoken : csrftoken
			},
			function(data,status){
				$('#modalUsuarioAlert').modal('hide');
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

