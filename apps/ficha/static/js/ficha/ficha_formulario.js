var txtComitePadre = "";

$( document ).ready(function() {

	$(window).keydown(function(event){
		if(event.keyCode == 13) {
		  event.preventDefault();
		  return false;
		}
		if(event.keyCode == 27) {
		  event.preventDefault();
		  $( ".close" ).trigger( "click" );
		}
	});


	$("#validarDNI").on("click", function(e){

		e.preventDefault();
		link = this;

		if ( $.trim( $("#persona_text").val() ).length == 0 ) {
			//toastr.error("El campo DNI está vacío!!!");

			$(this).parent().parent().find(".alert-danger").text("Ingrese un DNI válido.")
			$("#persona_text").focus();

			return;
		}
		else{
			$(this).parent().parent().find(".alert-danger").text("")
		}

		$.ajax({
            url:  $(link).attr('href'),
            type: "post",
            data: { 
		        'dni': $("#persona_text").val(),
		        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
		    },
            success: function(d) {

				if ( d["success"] ) {
					
					toastr.success(d['success']);
					setTimeout(function(){
						location.reload();
					}, 500);

				}

				for (key in d[0].fields ) {
					console.log(key, d[0].fields[key] );
				}
				
				//console.log(d[0].fields);

				// if ( d["fields"]) {
				// 	console.log(d["fields"]);
				// }

				// else {
				// 	toastr.success(d['error']);
				// }

            },
            error: function(d){
            	alert(d);
            }
        });



	});


});





