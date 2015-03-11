/*
 * Keystrokes event for jQuery
 * http://www.boedesign.com/
 */ 

easter_eggs = new Array();

easter_eggs.equipo_huayra = '<div class="easter-egg-wrapper">\
	<div class="acerca-de-logos">\
		<img src="assets/images/eggs/logos_acercade.png" />\
	</div>\
	<div class="comunicacion">\
		<h1>Nuestros canales de comunicación</h1>\
		<span>\
			<img src="assets/images/eggs/logo_twitter.png" />@HuayraLinux\
		</span>\
		<span>\
			<img src="assets/images/eggs/logo_facebook.png" />/HuayraLinux\
		</span>\
		<span>\
			huarya.conectarigualdad.gob.ar\
		</span>\
	</div>\
	<div class="participa">\
		¡Participá del proyecto!\
	</div>\
</div>';

$(document).ready(function(){
	$(document).bind('keystrokes', {
		keys: ['h', 'u', 'a', 'y', 'r', 'a', 'space', 't', 'e', 'a', 'm']
	}, function(event){
		jQuery('<div class="egg" id="easter-egg-equipo-huayra">' + easter_eggs['equipo_huayra'] + '</div>').appendTo('body').fadeIn().click(function(){jQuery(this).fadeOut()});
					
	});
});
    
