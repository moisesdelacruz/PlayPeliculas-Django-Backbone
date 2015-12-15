Pelicula.Views.App = Backbone.View.extend({
	el : 'body',

	events : {
		"keyup .Busqueda .Busqueda-barra .Busqueda-formInputText": "buscarMovie",
		"change .Busqueda .Conten-selectores #year": "buscarMovie",
		"change .Busqueda .Conten-selectores #quality": "buscarMovie",
		"change .Busqueda .Conten-selectores #gender": "buscarMovie",
		"click .ListaGeneros-opcion": "filtroMovie",
	},

	initialize : function() {
		var self = this;

		window.routers.base.on('route:root', function() {
			//Oculta description
			//la siguiente funcion se encuentra en "modulos/descripcion.js"
			ocultarligthbox();

		});
		window.routers.base.on('route:peliculaDescription', function() {

			if (window.app.movie === self.model.get('slug').toString()) {
				var model = self.model
				//Muestra description
				//la siguiente funcion se encuentra en "modulos/descripcion.js"
				mostrarligthbox(model);
			}
		})
	},

	agregarPelicula : function(model) {
		var view = new Pelicula.Views.Peliculas({model: model});

		view.render();

		view.$el.prependTo('.Peliculas-contenPrincipal');
	},

	//Llama la funcion de busqueda avanzada..
	buscarMovie : function(ev) {
		var fil = buscarPelicula(ev)
		this.collectionsFiltro(fil)
	},

	//Llama la funcion de filtrado por genero.. 
	filtroMovie : function(ev) {
		var fil = filtroGenero(ev)
		this.collectionsFiltro(fil)
	},

	collectionsFiltro : function(filtroPeliculas){
		//Limpia el contenedor para agregar las peliculas encontradas..
		$('.Peliculas-contenPrincipal').html('');
		filtroPeliculas.forEach(this.agregarPelicula, this);
	},
});