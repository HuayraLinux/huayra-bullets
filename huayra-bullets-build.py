# -*- coding: utf-8 -*-
import sys, os, shutil
sys.stdout.softspace = 0

bullets_types = ['shell', 'mate', 'other']


bullets_shell = [
	[
		'Ventanas y Aplicaciones',
		'<p>Llevá el mouse a la esquina de arriba a la izquierda. Fijate qué pasa. Es la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades">Vista de actividades</a>: acá vas a ver las ventanas abiertas, tus aplicaciones y el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador </a>.</p>',
		'01',
		'01',
	],
	[
		'Menú de Usuario y Apagar',
		'<p>Hacé clic en el ícono de la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la derecha. Este es el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:menu-de-usuario"> Menú de usuario </a>  desde donde podés apagar la netbook, configurarla y <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Cuentas-de-usuario">crear un usuario</a>.</p>',
		'01',
		'01',
	],
	[
		'¿Qué es el Menú Huayra?',
		'<p>Hacé clic en "Huayra" en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la izquierda y se despliega el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:menuhuayra">Menú Huayra</a>. A la izquierda están <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Archivos-y-carpetas#sec:Marcadores-de-carpeta">los marcadores </a> de carpetas que más usás y a la derecha las aplicaciones. Arriba podés buscar aplicaciones o ver las más usadas con Favoritas.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo instalo programas en Huayra?',
		'<p>Desde el <a href="[exec]software-center">Centro de software</a> instalás todos los programas en sus versiones oficiales y libres. Podés buscar por tema o por categoría. El Centro está en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:menuhuayra">Menú Huayra</a>/ Administración (o podés usar el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador</a> para encontrarlo)</p>',
		'01',
		'01',
	],
	[
		'Lo que hacías con MS Office lo haces con Libre Office',
		'<p>Lo que antes hacías con Microsoft Word ahora lo podés hacer con <a href="[exec]loffice">Libre Office Writer</a>. <a href="[doc]/usr/share/huayra/help/ayuda.xml#sec:loquehaciascon">¿Dónde encuentro en Huayra los otros programas que más usaba en Windows?</a></p>',
		'01',
		'01',
	],
		[
		'¿Cómo creo MI USUARIO en Huayra?',
		'<p>Creo <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Cuentas-de-usuario">MI USUARIO</a> en <a href="[exec]gnome-control-center"> Configuración del sistema</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:menu-de-usuario"> Menú de usuario</a>), Cuenta de Usuario. Primero desbloqueo con mi <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Cuentas-de-usuario">contraseña</a> (-alumno- por default) y luego creo mi usuario haciendo clic en "+".</p>',
		'01',
		'01',
	],
	[
		'¿Sabías que Huayra no tiene virus?',
		'<p>Es sencillo como eso, con Huayra no hay virus. Los diferentes permisos bloquean toda actividad nociva y las rápidas actualizaciones de la comunidad del <a href="[doc]/usr/share/huayra/help/ayuda.xml#sec:S#sub:Software-libre">Software Libre</a> eliminan toda amenaza.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo me conecto a Internet?',
		'<p>Hago clic en el ícono de <a href="[doc]/usr/share/huayra/help/ayuda.xml#part:Internet-y-conectividad">conexiones</a> en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la derecha y elijo la red (WiFi o cableada) La primera vez que me conecte tengo que ingresar mi <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Cuentas-de-usuario">contraseña</a> (-alumno- por default).</p>',
		'01',
		'01',
	],
	[
		'¿Cómo configuro mi escritorio?',
		'<p>En <a href="[exec]gnome-tweak-tool"> Configuración avanzada</a> (<a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:menuhuayra">Menú Huayra</a>/Preferencias) puedo cambiar el aspecto de iconos y ventanas y otras configuraciones de escritorio. <a href="[doc]/usr/share/huayra/help/ayuda.xml#part:tu-escritorio">Con Huayra ningún escritorio es igual a otro</a>.</p>',
		'01',
		'01',
	],
	[
		'¿Dónde encuentro mis archivos?',
		'<p>En <a href="[exec]nautilus">Carpeta Personal</a>  están los archivos de <a href="[doc]/usr/share/huayra/help/ayuda.xml#part:usuarios">MI usuario</a> organizadas por categoría ("Imágenes", "Descargas", etc:) con su ícono. También puedo acceder desde el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:menuhuayra">Menú Huayra</a> desde <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Archivos-y-carpetas#sec:Marcadores-de-carpeta">los marcadores </a> de carpetas que más usás.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo abro un pen-drive?',
		'<p>Huayra detecta el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Discos-y-almacenamiento#sec:pendrive">pen-drive</a> automáticamente y muestra un recuadro en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-inferior#sec:notificaciones">Barra de notificaciones</a> desde donde podés abrir el contenido. Expulsalo de forma segura con haciendo clic con el botón derecho en el ícono del pen que está en el escritorio.</p>',
		'01',
		'01',
	],
	[
		'¿Qué navegador de Internet uso?',
		'<p>Huayra tiene un Navegador web propio y puedo instalar todos los navegadores libres que quiera como Firefox, Chromium, etc. desde el  <a href="[exec]software-center">Centro de software</a>.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo recupero archivos borrados?',
		'<p>En <a href="[exec]nautilus trash://">la papelera</a> selecciono el archivo borrado y hago clic en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Archivos-y-carpetas#sec:Recuperar-un-archivo">"Restaurar los elementos seleccionados"</a>. De esa manera, el archivo irá a su carpeta original.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo agrego una impresora?',
		'<p>En <a href="[exec]gnome-control-center"> Configuración del sistema</a> (<a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:menu-de-usuario"> Menú de usuario </a> arriba a la derecha), bajo el título Hardware hago clic en la opción <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Impresoras">"Impresoras"</a> y ahí "Agregar una impresora nueva".</p>',
		'01',
		'01',
	],
	[
		'¿Cómo cambio la fecha y hora?',
		'<p>Hago clic en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> donde aparece la fecha y la hora, luego en "Ajustes de fecha y hora". También puedo modificar la fecha y la hora en <a href="[exec]gnome-control-center"> Configuración del sistema</a> / Fecha y Hora (en el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:menu-de-usuario"> Menú de usuario </a>)</p>',
		'01',
		'01',
	],
	[
		'¿Cuánta batería me queda?',
		'<p>El ícono de <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:energia">batería</a> en la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior">barra superior</a> a la derecha me lo indica al hacer clic. Desde <a href="[exec]gnome-control-center"> Configuración del sistema</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:menu-de-usuario"> Menú de usuario </a> arriba a la derecha) puedo optimizar el uso de la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:energia">Batería</a>.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo cambio mis aplicaciones predeterminadas?',
		'<p>Puedo elegir <a href="[doc]/usr/share/huayra/help/ayuda.xml#sec:Abrir-archivos-con">con qué aplicación</a> quiero abrir mi música, videos, etc. en <a href="[exec]gnome-control-center"> Configuración del sistema</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:menu-de-usuario"> Menú de usuario </a> arriba a la derecha), Detalles y luego en “Aplicaciones predeterminadas” elijo la opción (Web, Correo, Calendario, Música, Videos, Fotos)</p>',
		'01',
		'01',
	],
	[
		'¿"Software libre" es lo mismo que "software gratuito"?',
		'<p>No. El <a href="[doc]/usr/share/huayra/help/ayuda.xml#sec:S#sub:Software-libre">Software Libre</a> es gratis por ser libre, por respetar las libertades de los usuarios y de la comunidad de "copiar", "distribuir", "estudiar", "modificar" y "mejorar el software".</p>',
		'01',
		'01',
	],
	[
		'Con F3 y Ctrl + T veo mejor mis archivos',
		'<p>Cuando este viendo <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Archivos-y-carpetas#sec:Examinar-archivos-y">mis archivos y carpetas</a>, puedo usar Ctrl + T para abrir dentro de una misma ventana diferentes solapas, igual que en los navegadores de Internet. También puedo dividir la ventana en dos con F3.</p>',
		'01',
		'01',
	],
	[
		'Buscador Huayra',
		'<p>En la parte superior derecha de la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades">vista de actividades</a> encuentro el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador Huayra </a>. Al poner las primeras letras de lo que estoy buscando irán apareciendo los resultados, ya sean Aplicaciones, Contactos o Documentos. También puedo buscar en Google, Wikipedia o Educ.ar usando los botones de abajo.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo cambio mi clave?',
		'<p>En <a href="[exec]gnome-control-center">Configuración del sistema</a> (en <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Barra-superior#sec:menu-de-usuario"> Menú de usuario</a>), Cuenta de Usuario. Primero desbloqueo con mi <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Cuentas-de-usuario">contraseña</a> (-alumno- por default) y luego hago clic en los círculos al lado de “Contraseña”.</p>',
		'01',
		'01',
	],
	[
		'¿Como escucho musica?',
		'<p>Con un simple doble clic en el archivo de música se abre el reproductor <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Aplicaciones-recomendadas-en#sec:Clementine">Clementine</a> desde donde puedo administrar mis discos, listas y mucho más. Puedo <a href="[doc]/usr/share/huayra/help/ayuda.xml#sec:Abrir-archivos-con">cambiar la aplicación predeterminada</a> para abrir mi música.</p>',
		'01',
		'01',
	],
	[
		'¿Como veo videos?',
		'<p>Con un simple doble clic en el archivo de música se abre el reproductor <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Aplicaciones-recomendadas-en#sec:VLC-Media-Player">VLC Media Player</a>. Puedo <a href="[doc]/usr/share/huayra/help/ayuda.xml#sec:Abrir-archivos-con">cambiar la aplicación predeterminada</a> para abrir mi música.</p>',
		'01',
		'01',
	],
	[
		'¿Cómo comprimo archivos?',
		'<p>Simplemente hago clic con el botón derecho y elijo la opción <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Archivos-y-carpetas#sec:Comprimir-y-descomprimir">"Comprimir"</a>. Luego elijo el nombre del archivo final y la extensión (zip, rar, 7z, tar.gz etc.). La opción 7z que es la que más y mejor comprime.</p>',
		'01',
		'01',
	],
]

bullets_mate = [
	[
		'Ventanas y Aplicaciones',
		'<p>Llevá el mouse a la esquina de arriba a la izquierda. Fijate qué pasa. Es la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades">Vista de actividades</a>: acá vas a ver las ventanas abiertas, tus aplicaciones y el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador </a>.</p>',
		'01',
		'01',
	],
]

bullets_other = [
	[
		'Ventanas y Aplicaciones',
		'<p>Llevá el mouse a la esquina de arriba a la izquierda. Fijate qué pasa. Es la <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades">Vista de actividades</a>: acá vas a ver las ventanas abiertas, tus aplicaciones y el <a href="[doc]/usr/share/huayra/help/ayuda.xml#chap:Vista-de-actividades#sec:Buscador-Huayra">Buscador </a>.</p>',
		'01',
		'01',
	],
]



bullets_variants = {
	'01' : '''	<div id="bullet-content">
		<div id="question">
			<h1>{{ question }}</h1>
		</div> <!-- question -->
		<div id="actions">
		{{ prev_bullet_link }}{{ close_app_button }}{{ next_bullet_link }}
			<div id="show-next-startup">
				<label for="chkAutoStart">Mostrar en el siguiente inicio:</label>
				{{ autostart_checkbox }}
			</div> <!-- show-next-time -->
		</div> <!-- actions -->
		<div id="animation" class="animation-{{ animation_class }}">
		{{ animation_file }}
		</div> <!-- animation -->
		<div id="answer">
			{{ answer }}
			<div id="vaca-volve">
				<a href="#"><span>Vaca Volvé!</span></a>
			</div>
		</div> <!-- answer -->
	</div> <!-- bullet-content -->''',
}

def generate(bullets_types):
	"remove and create dir"
	shutil.rmtree(os.getcwd() + '/bullets')
	os.mkdir(os.getcwd() + '/bullets')
	open(os.getcwd() + '/bullets/__init__.py', 'w+')  
	
	for t in bullets_types:
		i = 1
		bullets_list = eval('bullets_' + t)
		os.mkdir(os.getcwd() + '/bullets/' + t)
		bullets_dir = os.getcwd() + '/bullets/' + t
		open(bullets_dir + '/__init__.py', 'w+')  
		bullets_list_file = open(bullets_dir + '/bullets_list.py', 'w+')  
		
		print >>bullets_list_file, '# -*- coding: utf-8 -*-'
		print >>bullets_list_file, ''
		print >>bullets_list_file, 'animations = {'
		print >>bullets_list_file, '	"01": {"class": "01", "dir": "01", "exit_duration": "3000"},'
		print >>bullets_list_file, '}'
		print >>bullets_list_file, ''
		print >>bullets_list_file, 'bullets_list = ['

		for b in bullets_list:
			if(i < 10):
				n = '0' + str(i)
			else:
				n = str(i)

			print >>bullets_list_file, '	{"file": "' + n + '.html", "title": "' + b[0].replace('"', '\\"') + '", "variant": "' + b[2] + '", "animation": animations["' + b[3] + '"]},'
			
			f = open(os.getcwd() + '/bullets/' + t + '/' + n + '.html', 'w+')
			
			bullet_content = bullets_variants[b[2]].replace('{{ question }}', b[0]) 
			bullet_content = bullet_content.replace('{{ answer }}', b[1]) 
			print >>f, bullet_content
			
			i = i+1

		print >>bullets_list_file, ']'

		

generate(bullets_types)
