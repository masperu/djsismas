	$('.selectpicker').selectpicker({
			size: 5
	});
	$('#datetimepicker1').datetimepicker({
		format:'YYYY-MM-DD',
	});
	var tipoubigeo = '';
	$("#btnAgregarUbigeoN").click(function(e) {
		tipoubigeo="N";
		e.preventDefault();
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
		
		});
		$("#modalUbigeo .modal-title").text("Ubigeo");	

	});	
	
	$("#btnAgregarUbigeoR").click(function(e) {
		tipoubigeo="R";
		e.preventDefault();
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

	