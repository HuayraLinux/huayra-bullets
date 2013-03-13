// https://github.com/nakajima/jquery-easter-eggs

easter_eggs = new Array();
easter_eggs['equipo_huayra'] = "\
<div class='easter-egg-wrapper'>\
	<h1>Huayra GNU/Linux</h1>\
	<div class='personas' id='directores-huayra'>\
		<h3>Director Ejecutivo de la ANSES:</h3>\
		<p>Diego Bossio</p>\
		<h3>Directora Ejecutiva del Programa Conectar Igualdad:</h3>\
		<p>Silvina Gvirtz</p>\
		<h3>Directora de Comunicación y Contenidos del Programa Conectar Igualdad:</h3>\
		<p>Constanza Necuzzi</p>\
	</div>\
\
	<h2>Los integrantes de Huayra somos:</h2>\
	<div class='personas' id='equipo-huayra'>\
		<h3>Coordinador General:</h3>\
		<p>Javier Castrillo</p>\
		<h3>Jefe de Proyecto:</h3>\
		<p>Vladimir di Fiore Prieto</p>\
		<h3>Equipo Desarrollo:</h3>\
		<p>Héctor Sánchez - Fernando Toledo, Miguel García, Luciano Baraglia, Mauro Lizaur, Julia Palandri</p>\
		<h3>Equipo de Documentación:</h3>\
		<p>Felipe Diego González - Ornella Lotito, Celeste Mandrut</p>\
		<h3>Equipo Arte y Diseño:</h3>\
		<p>Claudio Andaur - Carolina Hortal, Mercedes Elgarte, Iván Hoffmann</p>\
	</div>\
	<p>Agradecemos la iniciativa de <strong>Pablo Fontdevila</strong>, quien creyó en este proyecto desde el inicio y a todos los colaboradores de la <strong>comunidad educativa</strong> y del <strong>Software Libre</strong>.\
</div>\
";


$(document).ready(function(){
	$(document).bind('keystrokes', {
		keys: ['h', 'u', 'a', 'y', 'r', 'a', 'space', 't', 'e', 'a', 'm']
	}, function(event){
		jQuery('<div class="egg" id="easter-egg-equipo-huayra">' + easter_eggs['equipo_huayra'] + '</div>').appendTo('body').fadeIn().click(function(){jQuery(this).fadeOut()});
					
	});
});
