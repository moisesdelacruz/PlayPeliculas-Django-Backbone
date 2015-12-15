$(document).ready(function() {
	
	window.routers.base = new Pelicula.Routers.rutas();

	window.collections.peliculas = new Pelicula.Collections.Peliculas();
	
	window.collections.peliculas.on('add', function(model){
		var views = new Pelicula.Views.App({model:model});
		views.agregarPelicula(model)
	});
	
	var xhr = window.collections.peliculas.fetch();

	xhr.done(function(){
		Backbone.history.start({
			root : '/',
			pushState:true
		});
	});
	
});