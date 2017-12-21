Pelicula.Views.Description = Backbone.View.extend({

	tagName   : "div",
	className : "Conten-descripcion", 

	events : {
		"click .Descripcion-btCerrar" : "opacityOn"
	},

	initialize : function () {
		this.template = _.template( $('#descripcion-template').html() )
	},

	opacityOn : function(){
		ocultarligthbox()
	},

	render : function() {
		var data = this.model.attributes;

		var html = this.template(data);
		
		this.$el.html(html);
	}
})