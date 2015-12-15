var indicador = 0;

$(document).on('ready',function(){
	$('.left').on('click', function(e){
		e.preventDefault;
		moveSlider('left');
	});
	$('.right').on('click', function(e){
		e.preventDefault;
		moveSlider('right');
	});
	//defineSizes();
});

/*function defineSizes(){
	$('.form_container .slide').each(function(i,el){
		$(el).css({
			'background-image': "url("+$(el).data("background")+")",
			'height': (250 * 1)+'px',
			'width': 123+'px'  
		});
	});
}*/

function moveSlider(direccion){
	var limite = $('.form_container .slide').length;

	if (direccion=='right'){
		indicador++
		if (indicador >= 5) {
			indicador = 0
		}
	}else{	
		indicador--
		if (indicador < 0) {
			indicador = limite -5; 
		};
	} 
	/*indicador = (direccion == 'right') ? indicador + 1 : indicador - 1;
	indicador = (indicador >= limite) ? 0 : indicador;
	indicador = (indicador < 0) ? limite - 1 : indicador;
*/
	
	$('.form_container .slideContainer').animate({
		'margin-left': -(indicador * 520)+'px'
	});
}