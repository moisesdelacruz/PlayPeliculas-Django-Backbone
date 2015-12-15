function buscarPelicula (ev){
	ev.preventDefault();
	//--- Datos de entada de la app ---
	var title = $('.Busqueda .Busqueda-formInputText').val().toLowerCase();
	var year = $('.Busqueda #year').val();
	var gender = $('.Busqueda #gender').val();
	var quality = $('.Busqueda #quality').val();

	//--- Variable Filtro contiene toda la logica de filtrado de peliculas ---
	var filtro = window.collections.peliculas.filter(function(model){
		//--- Datos de los Modelos ---
		var title_movie = model.get('title_movie').substring(0, title.length).toLowerCase();
		var year_movie = model.get('year');
		var gender_movie = model.get('gender');
		var quality_movie = model.get('quality');
		//--- Condiciones de Filtrado ---
		/*--- Condicion para el año ---*/
		if (year != "Año" && year == year_movie || year == "Año") {
			/*--- Condicion para el genero ---*/
			for (var i = gender_movie.length - 1; i >= 0; i--) {
			
				if (gender != "Genero" && gender == gender_movie[i] || gender == "Genero") {
					/*--- Condicion para la calidad ---*/
					if (quality != "Calidad" && quality === quality_movie || quality == "Calidad") {
						/*--- Condicion para el buscador por titulo ---*/
						if (title === title_movie && title.length == title_movie.length && title != 0 && title_movie != 0) {
							return model;
						}
						else if (title_movie.length == 0 && title.length == 0){
							return model;
						}
					}
				}
			};
		}
	});

	//Retorna las peliculas encontradas
	return filtro;
}

function filtroGenero (ev){
	ev.preventDefault();
	var gender = $((ev.target)).attr('href');
	var filtro = window.collections.peliculas.filter(function(model){
		var gender_movie = model.get('gender');
		for (var i = gender_movie.length - 1; i >= 0; i--) {
			if (gender == gender_movie[i]) {
				return model;
			}
		};
	});

	//Retorna las peliculas encontradas
	return filtro;
}