Backbone.Model.extend
Backbone.Collection.extend
Backbone.View.extend

Pelicula.Routers.rutas = Backbone.Router.extend({
	routes : {
		"" : "root",
		"movie/:slug/" : "peliculaDescription"
	},

	root : function(){
		console.log("Estamos en root");
		window.app.state = "root";
		window.app.movie = null;
	},

	peliculaDescription : function(slug){
		console.log("Estamos en description");
		window.app.state = "peliculaDescription";
		window.app.movie = slug;
	}
});