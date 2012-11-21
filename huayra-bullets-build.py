# -*- coding: utf-8 -*-
from django.utils.encoding import smart_str, smart_unicode
import sys, os
sys.stdout.softspace = 0
bullets = [
	[
		'Ventanas y Aplicaciones',
		'<p>Llevá el mouse a la esquina de arriba a la izquierda. Fijate qué pasa. Es la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades">texto del link</a>vista de actividades</a> : acá vas a ver las ventanas abiertas, tus aplicaciones y el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador </a>.</p>',
		'01'
	],
	[
		'Menú de Usuario y Apagar',
		'<p>Hacé clic en el ícono de la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la derecha. Este es el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:Men-de-usuario-7"> Menú de usuario </a>  desde donde apagás la netbook, configurarla o <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-30">cambiar de usuario</a>.</p>',
		'01'
	],
	[
		'¿Qué es el Menú Huayra?',
		'<p>Hacé clic en "Huayra" en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la izquierda y se despliega el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Men-Huayra-1">menú </a>. A la izquierda están <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-59#sec:Marcadores-de-carpeta">los marcadores </a> de carpetas que más usás y a la derecha las aplicaciones. Arriba podés buscar aplicaciones o ver las más usadas con Favoritas.</p>',
		'01'
	],
	[
		'¿Cómo instalo programas en Huayra?',
		'<p>Desde el <a href="[exec]software-center">"Centro de software"</a> instalo todos los programas en sus versiones oficiales y libres. Puedo buscar por tema o por categoría. El Centro está en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Men-Huayra-1">Menú Huayra</a>/ Administración (o uso el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador</a>)</p>',
		'01'
	],
	[
		'Lo que hacías con MS Office lo haces con Libre Office',
		'<p>Lo que antes hacías con Microsoft Word ahora lo podés hacer con Libre Office Writer (LINK A AP). <a href="[doc]/usr/share/huayra/help/ayuda.xml#sec:Dnde-encuentro-en-27">Buscador </a>¿Dónde encuentro en Huayra los otros programas que más usaba en Windows?</a></p>',
		'01'
	],
	[
		'¿Sabías que Huayra no tiene virus?',
		'<p>Es sencillo como eso, con Huayra no hay virus. Los diferentes permisos bloquean toda actividad nociva y las rápidas actualizaciones de la comunidad del <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-365#//autoid-397">Software Libre</a> eliminan toda amenaza.</p>',
		'01'
	],
	[
		'¿Cómo me conecto a Internet?',
		'<p>Hago clic en el ícono de <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-136#">conexiones</a> en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la derecha y elejo la red (WiFi o cableada) La primera vez que me conecte tengo que ingresar mi <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-30">contraseña</a> (-alumno- por default).</p>',
		'01'
	],
	[
		'¿Cómo configuro mi escritorio?',
		'<p>En <a href="[exec]gnome-tweak-tool"> Configuración avanzada</a> (<a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Men-Huayra-1">Menú Huayra</a>/Preferencias) puedo cambiar el aspecto de iconos y ventanas y otras configuraciones de escritorio. <a href="[doc]/usr/share/huayra/help/ayuda.xml#part:Tune-tu-escritorio-9">Con Huayra ningún escritorio es igual a otro</a>.</p>',
		'01'
	],
	[
		'¿Dónde encuentro mis archivos?',
		'<p>En Carpeta Personal (LINK A CARPETA PERSONAL) están los archivos de <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-30">MI usuario</a>  organizadas por categoría ("Imágenes", "Descargas", etc:) con su ícono. También puedo acceder desde el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Men-Huayra-1">Menú Huayra</a> o desde el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador</a>.</p>',
		'01'
	],
	[
		'¿Cómo abro un pen-drive?',
		'<p>Huayra lo detecta automáticamente y muestra un recuadro en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-inferior#//autoid-12">Barra de notificaciones</a> donde podés abrir el contenido. Expulsalo de forma segura con el botón derecho en el ícono del pen del escritorio.</p>',
		'01'
	],
	[
		'¿Qué navegador de Internet uso?',
		'<p>Huayra tiene un Navegador web propio y puedo instalar todos los navegadores libres que quiera como Firefox, Chromium, etc. desde el  <a href="[exec]software-center">"Centro de software"</a>.</p>',
		'01'
	],
	[
		'¿Cómo recupero archivos borrados?',
		'<p>En la papelera (LINK PAPELERA) selecciono el archivo borrado por equivocación, y hago clic en "Restaurar los elementos seleccionados". De esa manera, <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-76">el archivo</a> irá a su carpeta original.</p>',
		'01'
	],
	[
		'¿Cómo agrego una impresora?',
		'<p>En <a href="[exec]gnome-control-center"> "Configuración del sistema"</a> (<a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:Men-de-usuario-7"> Menú de usuario </a> arriba a la derecha), bajo el título Hardware hago clic en la opción <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Impresoras">"Impresoras"</a> y ahí "Agregar una impresora nueva".</p>',
		'01'
	],
	[
		'¿Cómo cambio la fecha y hora?',
		'<p>Hago clic en la barra superior donde aparece la fecha y la hora,y ahí en"Ajustes de fecha y hora". También puedo modificar la fecha y la hora en <a href="[exec]gnome-control-center"> "Configuración del sistema"</a> (en el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:Men-de-usuario-7"> Menú de usuario </a>)</p>',
		'01'
	],
	[
		'¿Cuánta batería me queda?',
		'<p>El ícono de batería en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la derecha me lo indica al hacer clic. Desde <a href="[exec]gnome-control-center"> "Configuración del sistema"</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:Men-de-usuario-7"> Menú de usuario </a> arriba a la derecha) puedo optimizar el uso de la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Energa-y-Batera-9">Batería</a>.</p>',
		'01'
	],
	[
		'¿Cómo cambio mis aplicaciones predeterminadas?',
		'<p>Puedo elegir <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-76#sec:Abrir-archivos-com">con qué aplicación</a> quiero abrir mi música, videos, etc. en "Configuración del sistema"</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:Men-de-usuario-7"> Menú de usuario </a> arriba a la derecha), Detalles y luego en “Aplicaciones predeterminadas” elijo la opción (Web, Correo, Calendario, Música, Videos, Fotos)</p>',
		'01'
	],
	[
		'¿"Software libre" es lo mismo que "software gratuito"?',
		'<p>No. El <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-365#//autoid-397">Software Libre</a> es gratis por ser libre, por respetar las libertades de los usuarios y de la comunidad de "copiar", "distribuir", "estudiar", "modificar" y "mejorar el software".</p>',
		'01'
	],
	[
		'Con F3 y Ctrl + T veo mejor mis archivos',
		'<p>Cuando este viendo <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-76">mis archivos y carpetas</a>, puedo usar Ctrl + T para abrir dentro de una misma ventana diferentes solapas, igual que en los navegadores de Internet. También puedo dividir la ventana en dos con F3.</p>',
		'01'
	],
	[
		'Buscador Huayra',
		'<p>En la parte superior derecha de la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades">texto del link</a>vista de actividades</a> encuentro el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador Huayra </a>. Al poner las primeras letras de lo que estoy buscando irán apareciendo los resultados, ya sean Aplicaciones, Contactos o Documentos o Google y Wikipedia usando los botones de abajo.</p>',
		'01'
	],
	[
		'¿Cómo creo MI USUARIO en Huayra?',
		'<p>CREO <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-30">MI USUARIO</a> en "Configuración del sistema"</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:Men-de-usuario-7"> Menú de usuario </a>), Cuenta de Usuario. Primero desbloqueo con mi contraseña y luego creo mi usuario haciendo clic en "+".</p>',
		'01'
	],
	[
		'¿Cómo cambio mi clave?',
		'<p>En "Configuración del sistema"</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:Men-de-usuario-7"> Menú de usuario </a>), Cuenta de Usuario. Primero desbloqueo con mi contraseña y luego hago clic en los círculos al lado de “Contraseña”.</p>',
		'01'
	],
	[
		'¿Como escucho musica?',
		'<p>Con un simple doble clic en el archivo de música se abre el reproductor Clementine desde donde puedo administrar mis discos, listas y mucho más. Puedo <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-76#sec:Abrir-archivos-com">cambiar la aplicación predeterminada</a> para abrir mi música.</p>',
		'01'
	],
	[
		'¿Como veo videos?',
		'<p>Con un simple doble clic en el archivo de música se abre el reproductor VLC Media Player. Puedo cambiar <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-76#sec:Abrir-archivos-com">cambiar la aplicación predeterminada</a> para abrir mi música.</p>',
		'01'
	],
	[
		'¿Cómo comprimo archivos?',
		'<p>Simplemente hago clic con el botón derecho y elijo la opción <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-76#sec:Comprimir-y-descomprimir">"Comprimir"</a>. Luego elijo el nombre del archivo final y la <a href="[doc]/usr/share/huayra/help/ayuda.xml#//autoid-390#sub:Extensin-de-archivo-20">extensión</a> (zip, rar, 7z, tar.gz etc.). La opción 7z que es la que más y mejor comprime.</p>',
		'01'
	],
]

i = 1
bullets_list_file = open(os.getcwd() + '/pages/bullets/bullets_list.py', 'w+')

print >>bullets_list_file, '# -*- coding: utf-8 -*-'
print >>bullets_list_file, ''
print >>bullets_list_file, 'animations = {'
print >>bullets_list_file, '	"01": {"class": "01", "dir": "01", "exit_duration": "3000"},'
print >>bullets_list_file, '}'
print >>bullets_list_file, ''
print >>bullets_list_file, 'bullets_list = ['

for b in bullets:
	if(i < 10):
		n = '0' + str(i)
	else:
		n = str(i)

	print >>bullets_list_file, '	{"file": "' + n + '.html", "title": "' + b[0].replace('"', '\\"') + '", "variant": "variant-01", "animation": animations["01"]},'
	
	f = open(os.getcwd() + '/pages/bullets/' + n + '.html', 'w+')
	print >>f, '<div id="bullet-content">'
	print >>f, '	<div id="question">'
	print >>f, '		<h1>'+b[0]+'</h1>'
	print >>f, '	</div> <!-- question -->'
	print >>f, '	<div id="actions">'
	print >>f, '	{{ prev_bullet_link }}{{ close_app_button }}{{ next_bullet_link }}'
	print >>f, '		<div id="show-next-startup">'
	print >>f, '			<label for="chkAutoStart">Mostrar en el siguiente inicio:</label>'
	print >>f, '			<input type="checkbox" checked="checked" id="chkAutoStart" />'
	print >>f, '		</div> <!-- show-next-time -->'
	print >>f, '	</div> <!-- actions -->'
	print >>f, '	<div id="animation" class="animation-{{ animation_class }}">'
	print >>f, '		<img src="" />'
	print >>f, '	</div> <!-- animation -->'
	print >>f, '	<div id="answer">'
	print >>f, '		'+b[1]
	print >>f, '	</div> <!-- answer -->'
	print >>f, '</div> <!-- bullet-content -->'
	i = i+1

print >>bullets_list_file, ']'


	
		
	