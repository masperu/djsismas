	$('.selectpicker').selectpicker({
			size: 5
	});
	$('#datetimepicker1').datetimepicker({
		format:'YYYY-MM-DD',
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


	var tipoubigeo = '';
	var depaN = "";
	var provN = "";
	var disN = "";	
	var depaR = "";
	var provR = "";
	var disR = "";

	$("#btnAgregarUbigeoN").click(function(e) {
		tipoubigeo="N";
		e.preventDefault();
		
		if(tipoubigeo=="N"){
			disN = $("#id_ubigeonacimiento").val();
			if(disN){
		
				$.post("/persona.ubigeo/listar/",
				{
				  iddistrito: disN, 
				  csrfmiddlewaretoken : csrftoken
				},
				function(data,status){
					// $('#modalPersonaAlert').modal('hide');
					depaN = data.coddep;
					provN = data.codprov;
				});
			}
		}

		$('#modalUbigeo').modal('show').find('#divDep').load("/persona.ubigeonacimiento/listar/");
		$('#modalUbigeo').on('shown.bs.modal', function(e) {
			// $('#selectDepartamento').selectpicker('render');


			

			$('#selectDepartamento').on('hide.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			$('#selectDepartamento').on('rendered.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			$('#selectDepartamento').on('refreshed.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			$('#selectDepartamento').on('loaded.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			$('#selectDepartamento').on('rendered.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});

			if(tipoubigeo=="N"){
				if(depaN){

					$('#selectDepartamento').val(depaN);
					$('#selectDepartamento').selectpicker('refresh');
				}
			}
			// $('#selectProvincia').selectpicker('render');
			// alert($('#selectProvincia').val());

	
		
		});


	});	



	$("#modalUbigeo .modal-title").text("Ubigeo");	


	
	$("#btnAgregarUbigeoR").click(function(e) {
		tipoubigeo="R";
		e.preventDefault();

		if(tipoubigeo=="R"){
			disR = $("#id_ubigeoresidencia").val();

			if(disR){
		
				$.post("/persona.ubigeo/listar/",
				{
				  iddistrito: disR, 
				  csrfmiddlewaretoken : csrftoken
				},
				function(data,status){
					// $('#modalPersonaAlert').modal('hide');
					depaR = data.coddep;
					provR = data.codprov;
				});
			}
		}

		$('#modalUbigeo').modal('show').find('#divDep').load("/persona.ubigeonacimiento/listar/");
		$('#modalUbigeo').on('shown.bs.modal', function(e) {
			
			// $('#selectDepartamento').val("06");
			// $('#selectDepartamento').selectpicker('refresh');
			// var modal = $(this);
			$('#selectDepartamento').on('hide.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			$('#selectDepartamento').on('rendered.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			$('#selectDepartamento').on('refreshed.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			$('#selectDepartamento').on('loaded.bs.select', function (e) {
				$('#divProv').load("/persona.ubigeonacimiento/listar/"+$(this).val()+"/");
			});
			if(tipoubigeo=="R"){
				if(depaR){

					$('#selectDepartamento').val(depaR);
					$('#selectDepartamento').selectpicker('refresh');
				}
			}
		
		});
		$("#modalUbigeo .modal-title").text("Ubigeo");	

	});

	$('#btnGuardarUbigeo').click(function(){
		// console.log($('#selectDistrito').val());
		// console.log($('#selectDistrito option[value='+$('#selectDistrito').val()+']').text());
		// console.log($('#selectProvincia').val());
		// console.log($('#selectProvincia option[value='+$('#selectProvincia').val()+']').text());
		// console.log($('#selectDepartamento').val());
		// console.log($('#selectDepartamento option[value='+$('#selectDepartamento').val()+']').text());

		if(tipoubigeo=='N'){
			$("#txtubigeonacimiento").val($('#selectDepartamento option[value='+$('#selectDepartamento').val()+']').text()+"/"
				+$('#selectProvincia option[value='+$('#selectProvincia').val()+']').text()+"/"
				+$('#selectDistrito option[value='+$('#selectDistrito').val()+']').text());

			$("#id_ubigeonacimiento").val($('#selectDistrito').val());
		}
		else if(tipoubigeo=='R'){
			$("#txtubigeoresidencia").val($('#selectDepartamento option[value='+$('#selectDepartamento').val()+']').text()+"/"
				+$('#selectProvincia option[value='+$('#selectProvincia').val()+']').text()+"/"
				+$('#selectDistrito option[value='+$('#selectDistrito').val()+']').text());
			$("#id_ubigeoresidencia").val($('#selectDistrito').val());

		}


		$('#modalUbigeo').modal('hide');

	});

	
	