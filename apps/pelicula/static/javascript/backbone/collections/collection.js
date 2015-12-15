Pelicula.Collections.Peliculas = Backbone.Collection.extend({
	model: Pelicula.Models.Peliculas,
	url: '/api/movies/',
	name: 'movie'
});