/*
 * Keystrokes event for jQuery
 * http://www.boedesign.com/
 */ 

easter_eggs = new Array();

easter_eggs['equipo_huayra'] = "\
<div class='easter-egg-wrapper'>\
	<h1>Huayra GNU/Linux 2.0</h1>\
	<div class='personas' id='directores-huayra'>\
		<h3>Presidenta de la Nación:</h3>\
		<p>Dra. Cristina Fernández de Kirchner</p>\
		<h3>Director Ejecutivo de la ANSES:</h3>\
		<p>Lic. Diego Bossio</p>\
		<h3>Directora Ejecutiva del Programa Conectar Igualdad:</h3>\
		<p>Lic. Silvina Gvirtz</p>\
		<h3>Directora de Comunicación y Contenidos del Programa Conectar Igualdad:</h3>\
		<p>Lic. Constanza Necuzzi</p>\
	</div>\
\
	<h2>Los integrantes de Huayra somos:</h2>\
	<div class='personas' id='equipo-huayra'>\
		<h3>Coordinador General:</h3>\
		<p>Javier Castrillo</p>\
		<h3>Gestión y asistencia en coordinación:</h3>\
		<p>Adriana Pauluk</p>\
        <h3>Equipo Desarrollo:</h3>\
		<p>Héctor \"Karucha\" Sanchez, Fernando \"Maraka\" Toledo, Mike García, Luciano Baraglia, Mauro Lizaur, Hugo \"Hugol\" Ruscitti, Ignacio \"Preciosa\" Benedetti</p>\
		<h3>Equipo de Documentación:</h3>\
		<p>Felipe \"|\" González, Ornella Lotito, Celeste Mandrut</p>\
		<h3>Equipo Arte y Diseño:</h3>\
		<p>Claudio \"Maléfico\" Andaur, Carolina Hortal, Iván Hoffmann</p>\
        <h3>Servidores y soporte:</h3>\
		<p>Pablo \"Pablito\" Carrai, Facundo Alaniz, Santiago Armas</p>\
        <h3>Alma mater:</h3>\
		<p>Laura Penacca</p>\
	</div>\
	<h3>Agradecemos:</h3>\
	<p>A <strong>Pablo Fontdevila</strong> que desde el inicio creyó en este proyecto</p>\
    <br><p>A los equipos provinciales del programa Conectar Igualdad,\
 las comunidades de Huayra de todo el país, las organizaciones, organismos, universidades \
y dependencias públicas que han adoptado Huayra, a los compañeros de educ.ar, \
a todos los que han colaborado con código, reportando errores, ideas y proponiendo contenidos. \
</p>\
	\
</div>\
";

$(document).ready(function(){
	$(document).bind('keystrokes', {
		keys: ['s', 'o', 'p', 'l', 'a', 'space', 'h', 'u', 'a', 'y', 'r', 'a']
	}, function(event){
		jQuery('<div class="egg" id="easter-egg-equipo-huayra">' + easter_eggs['equipo_huayra'] + '</div>').appendTo('body').fadeIn().click(function(){jQuery(this).fadeOut()});
					
	});
});
    
