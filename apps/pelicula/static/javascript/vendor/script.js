$(document).ready(main);


function main () {
	
	//Mostrar y Ocultar Menu Mobile
	var contador = true;
	$('.botonMenu').on('click',function(ev){
		ev.preventDefault();

		if (contador) {
			$(this).addClass("icon-menuActivo");
			$('.Menu').animate({
				left: '0',
			});
			contador = false;

		} else {
			contador = true;
			$(this).removeClass("icon-menuActivo")
			$('.Menu').animate({
				left: '-100%'
			});
		}

	});

	//BarraBuscar Mobile
	$(".botonBuscar").on('click',function(ev){
		ev.preventDefault();
		var contenido=$(this).next(".accordion-content");
      
	   if(contenido.css("display")=="none"){ //open   
	   	contenido.slideDown(250);   

	   	$(this).addClass("icon-cross");
	   	$(this).removeClass("icon-search");

	   }else{ //close    
	   	contenido.slideUp(250);
	 
	   	$(this).addClass("icon-search");
	   	$(this).removeClass("icon-cross");
	   }
	});
}