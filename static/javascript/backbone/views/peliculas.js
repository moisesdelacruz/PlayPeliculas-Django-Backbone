Pelicula.Views.Peliculas = Backbone.View.extend({
	events : {
		"click" : "navigate",
	},

	tagName   : "article",
	className : "Peliculas-articulo",


	initialize : function() {
		this.template = _.template( $('#peliculas-template').html() );
		//this.template = swig.compile( $('#peliculas-template').html() );
		var self = this;
		this.model.on('change', function(){
			self.render();
		});
	},

	navigate: function(e) {
		e.preventDefault();
		Backbone.history.navigate('/movie/' + this.model.get('slug') + '/', {trigger:true});
	},

	render : function() {
		var data = this.model.toJSON();

		var html = this.template(data);

		this.$el.html(html);
	}
});