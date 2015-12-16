$(function() {
    var $contenedor =  $('.form_container');
    var swift = true

    $('.right').click(
        function (e) {  
            if (swift){
                $contenedor.animate({scrollLeft: "800px"}, 2000);     
            }
            swift = false;
      });

    $('.left').click(
        function (e) {
          
            if (swift == false){
                $contenedor.animate({scrollLeft: "0px"}, 800);
            }
            swift = true;
                
      }
    );
});
