// Mostrar y Ocultar Opacidad
function opacityOn (ocultar){
	$(".u-bodyOpacity").fadeIn();
	$(".u-bodyOpacity").click(ocultar);
}

function opacityOff (){
	$(".u-bodyOpacity").fadeOut();
}

function ocultarligthbox (){
    $(".u-bodyOpacity").fadeOut();
    $(".Descripcion").fadeOut();
    $(".Descripcion").html('');
    Backbone.history.navigate('/', {trigger:true});
}

function mostrarligthbox (model){
    this.opacityOn(this.ocultarligthbox);
    $(".Descripcion").fadeIn();
    this.Description(model);  
}

function Description (model){
		var view = new Pelicula.Views.Description({model: model});

		view.render();

		view.$el.prependTo('.Descripcion');
}