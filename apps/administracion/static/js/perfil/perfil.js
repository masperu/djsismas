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

	// $("#usuarioSelecPerfil").on('hidden.bs.select', function (e) {

	// 	$.get( "/perfilroles/listar/?iduser="+$(this).val(), function( data ) {
	// 		$("#cargarRolePerfil").html(data);
	// 	});

	// });
	$("#usuarioSelecPerfil").on('hidden.bs.select', function (e) {

		$.get( "/perfilroles/listar/?iduser="+$(this).val(), function( data ) {
			$("#cargarRolePerfil").html(data);
		});

	});
	$("#usuarioSelecPerfil").on('loaded.bs.select', function (e) {

		$.get( "/perfilroles/listar/?iduser="+$(this).val(), function( data ) {
			$("#cargarRolePerfil").html(data);
		});

	});
	$("#usuarioSelecPerfil").on('rendered.bs.select', function (e) {

		$.get( "/perfilroles/listar/?iduser="+$(this).val(), function( data ) {
			$("#cargarRolePerfil").html(data);
		});

	});	
	$("#usuarioSelecPerfil").on('refreshed.bs.select', function (e) {

		$.get( "/perfilroles/listar/?iduser="+$(this).val(), function( data ) {
			$("#cargarRolePerfil").html(data);
		});

	});

	$("#btnGuardarPerfilRol").on('click', function(data){

		alert("asasasa");
	});

});

