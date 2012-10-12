/**
 * Copyright (C) 2012 Huayra GNU/Linux
 *
 * Author Miguel Angel Garcia <miguel.garcia@gmail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; version 2
 * of the License
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 */


/**
 * This array contains all the bullets, each bullet must contain these properties:
 * - title
 * - content
 * - can_close 
 */
bullets = Array();

bullets[0] = {
    'title': '¡Bienvenido a Huayra!',
    'content': '¡Bienvenido a Huayra, el sistema operativo libre GNU/Linux de \
        Conectar Igualdad! Huayra es más seguro, más ágil y desarrollado en \
        Argentina teniendo en cuenta las necesidades tantos de estudiantes como \
        de docentes y manteniendo la identidad nacional.<br /> Como todos los sistemas \
        operativos libres, Huayra tiene muchas ventajas que irás descubriendo.<br /> \
        Para saber cómo usar Huayra y aprovechar todas sus funcionalidades, irán \
        apareciendo notificaciones como esta que te guiarán con los programas y \
        aplicaciones. También tu netbook tiene incorporado un manual que podrás \
        encontrar haciendo click en F1 estando el escritorio o haciendo click en ayuda.',
    'can_close': false
};

bullets[1] = {
    'title': 'Ventanas y Aplicaciones: ¿qué son y para qué sirven?',
    'content': 'Llevando el puntero del mouse hacia la esquina superior\
        izquierda del monitor aparecen las Ventanas y Aplicaciones. En Ventanas\
        voy a ver todas las ventanas que tengo abiertas, mientras que en\
        Aplicaciones voy a ver las aplicaciones disponibles en Huayra agrupadas\
        por tema. Sobre la izquierda voy a encontrar una barra con mis aplicaciones\
        preferidas (si quiero agregar alguna aplicación solamente tengo que arrastrarla\
        desde el menú de aplicaciones hasta esta barra). Por último, en la parte\
        superior derecha voy a encontrar un buscador. Este me permite buscar\
        aplicaciones, pero también buscar en Google o Wikipedia. haciendo clic\
        en uno de los dos botones que aparecen en la parte inferior del monitor.',
    'can_close': false
};

bullets[2] = {
    'title': 'Menú de Usuario y apagado: ¿qué son y para qué sirven?',
    'content': 'Puedo ingresar al "Menú de usuario" al hacer clic en el ícono de\
        la barra de arriba a la derecha. Este menú me permite hacer varias tareas,\
        entre ellas: Apagar/Reiniciar la netbook, cerrar la sesión, suspender,\
        entre otras. También puedo configurar el sistema, es decir: ajustar la\
        fecha y la hora, agregar una impresora, configurar el teclado, el mouse\
        y el touchpad.',
    'can_close': false
};

bullets[3] = {
    'title': '¿Qué es el Menu Huayra?',
    'content': 'El Menu Huayra es similar al que tradicionalmente encontramos en\
        los otros sistemas operativos como Microsoft Windows o MacOS X. Para\
        acceder hago click en "Huayra" en la barra superior a la izquierda.<br />\
        En este espacio de trabajo, voy a ver a la izquierda los Marcadores, que\
        son las carpetas que más utilizo. En el centro voy a encontrar las\
        aplicaciones disponibles agrupadas por tema. En la parte superior puedo\
        hacer click en Favoritos y voy a poder ver las aplicaciones que uso con\
        mayor frecuencia. O tambien puedo buscarlas usando el buscador.',
    'can_close': false
};

bullets[4] = {
    'title': '¿Cómo puedo instalar programas en Huayra?',
    'content': 'Para instalar programas tengo que ir al "Centro de software"\
        (desde Aplicaciones llevando el mouse a la esquina superior izquierda y\
        luego en Herramientas del Sistema o desde el Menu Huayra en Administración).\
        Esta aplicación me permite buscar todos los programas que quiera instalar.\
        Puedo buscar por tema o por categoría; ej. Gráficos, Juegos, etc.\
        Estos programas en su mayoría son software libre, con lo cual vamos a\
        estar accediendo a las versiones oficiales y de manera totalmente libre\
        y gratuita.',
    'can_close': true
};

bullets[5] = {
    'title': 'Lo que hacía con Microsoft Word lo puedo hacer con Libre Office Writer',
    'content': 'Lo que antes hacía con Microsoft Word ahora lo puedo hacer con\
        Libre Office Writer. Para saber con qué otras aplicaciones puedo hacer\
        los mismos trabajos que hacía en Windows puedo leer  “Lo que hacía con,\
        lo puedo hacer con” en la carpeta de Ayuda del escritorio.',
    'can_close': true
};

bullets[6] = {
    'title': '¿Sabías que Huayra no tiene virus?',
    'content': 'Mi computadora es más segura porque con Huayra es virtualmente\
        imposible que tenga virus. Esto es por los diferentes permisos que hacen\
        imposible a un virus realizar actividades nocivas dentro del sistema y a\
        las rápidas actualizaciones que se suceden a diario en Huayra, propias\
        del modelo de software libre.',
    'can_close': true
};

bullets[7] = {
    'title': '¿Cómo me conecto a Internet? ¿Cómo se cuando estoy conectado?',
    'content': 'En la barra superior a la derecha donde está el ícono de “Conexiones”,\
        puedo conectarme vía wifi o red cableada. Cuando me conecte por primera\
        vez a una red nueva voy a tener que ingresar mi contraseña (-alumno- por default).\
        Si me conecto a una red WiFi con contraseña necesito poner la contraseña\
        de la red. Una vez conectado podré ver cómo cambió el ícono. El ícono del\
        wifi me mostrará la intensidad de la señal y saber así si estoy conectado\
        o no.',
    'can_close': true
};

bullets[8] = {
    'title': '¿Cómo puedo configurar mi escritorio?',
    'content': 'En Huayra puedo configurar mi escritorio como yo quiera. Con\
        Huayra vienen muchas extensiones que me dejan cambiarlo para adaptarlo a\
        mis usos y gustos. Para explorarlas, modificarlas o agregar más debo ir\
        a Gnome Extensions en https://extensions.gnome.org/.',
    'can_close': true
};

bullets[9] = {
    'title': '¿Dónde encuentro mis archivos ?',
    'content': 'Puedo acceder desde a mis archivos: desde el menú Huayra, desde\
        el ícono del escritorio o desde el ícono que se enceuntra en la barra de\
        aplicaciones preferidas. Ahí dentro tendré diferentes carpetas "Imágenes",\
        "Videos", "Descargas", "Documentos" con su ícono representativo.',
    'can_close': true
};

bullets[10] = {
    'title': '¿Cómo abro un pen-drive?',
    'content': 'Cuando inserto el pendrive en la netbook Huayra lo detecta\
        automáticamente y me muestra un recuadro donde voy a poder abrir el\
        contenido o expulsarlo de modo seguro. También voy a ver un ícono en el\
        escritorio con el nombre del pendrive. Al hacer doble clic puedo ver el\
        contenido. Para quitarlo: hago clic con el botón derecho y selecciono\
        “Expulsar unidad de forma segura”.',
    'can_close': true
};

bullets[11] = {
    'title': '¿Qué navegador puedo usar para Internet?',
    'content': 'En Huayra viene instalado Firefox. Pero puedo instalar todos los\
        navegadores libres que quiera como Chromium (el navegador libre sobre el\
        que se basa Google Chrome), IceWeasel, etc.',
    'can_close': true
};

bullets[12] = {
    'title': '¿Cómo recupero archivos borrados por equivocación?',
    'content': 'Tengo que ir a la papelera, y desde ahí, selecciono el archivo\
        borrado por equivocación, y hago clic en en "Restaurar los elementos\
        seleccionados". De esa manera, el archivo irá a su carpeta original.',
    'can_close': true
};

bullets[13] = {
    'title': '¿Cómo agrego una impresora?',
    'content': 'Para instalar una impresora tengo que entrar en "Configuración\
        del sistema" (desde Actividades llevando el mouse a la esquina superior\
        izquierda o desde el Menú Huayra en la esquina superior derecha).\
        Bajo el título Hardware hago clic en la opción "Impresoras" y allí\
        "Agregar una impresora nueva".',
    'can_close': true
};

bullets[14] = {
    'title': '¿Cómo cambio la fecha y hora?',
    'content': 'Para cambiar la fecha y hora hago clic en la barra superior donde\
        aparece la fecha y la hora,  que va a a abrir un cuadro de diálogo. En la\
        parte de abajo del mismo dice "Ajustes de fecha y hora". También puedo\
        modificar la fecha y la hora en "Configuración del sistema" (desde\
        Aplicaciones llevando el mouse a la esquina superior izquierda o desde\
        el Menú de Usuario en la esquina superior derecha). Bajo el título Sistema\
        entro a la opción "Fecha y Hora".',
    'can_close': true
};

bullets[15] = {
    'title': '¿Cómo se cuanta batería me queda?',
    'content': 'Para saber en qué estado está la batería de mi netbook, hay un\
        icono en la barra arriba a la derecha que me va indicando es estado. El\
        100% de carga de la batería equivale aproximadamente a 6 horas de duración.\
        Si quiero saber cuánto tiempo me resta y cuánto porcentaje de carga tengo,\
        debo hacer clic en el icono de la batería. Ahí se abrirá un cuadro de diálogo\
        que tendrá esta información. Además desde allí podré optimizar el uso de\
        la batería entrando en “Configuración de energía” para que dure más tiempo.\
        Para saber cuándo la batería se está cargando, tengo que observar si\
        junto al icono de la pila aparece una figura similar a un rayo.  ',
    'can_close': true
};

bullets[16] = {
    'title': '¿Cómo cambio el menú principal?',
    'content': 'Para configurar el menú de aplicaciones, agregar, quitar, etc.\
        tengo que ir a Herramientas del sistema y allí a la opción Menú principal.\
        A esta opción puedo acceder desde el Menú Huayra en Preferencias / Menú principal,\
        o desde Aplicaciones (llevando el mouse arriba a la izquierda) haciendo\
        clic en Herramientas del sistema y luego en Menú principal.',
    'can_close': true
};

bullets[17] = {
    'title': '¿Cómo cambio mis aplicaciones predeterminadas?',
    'content': 'Para poder elegir con qué aplicación quiero abrir mi música, video,\
        etc. puedo ir a Configuración del sistema (desde Actividades llevando el\
        mouse a la esquina superior izquierda o desde el Menú de Usuario en la\
        esquina superior derecha). Una vez allí bajo el título Sistema entro a\
        la opción Detalles y luego en Aplicaciones predeterminadas. Me van a\
        aparecer las diferentes opciones (Web, Correo, Calendario, Música, Videos,\
        Fotos).',
    'can_close': true
};

bullets[18] = {
    'title': '¿"Software libre" es lo mismo que "software gratuito"? ',
    'content': 'No. Para que un software sea denominado «libre» debe ante todo\
        respetar lo que se conoce como  las libertades de los usuarios y de la\
        comunidad. En términos generales, los usuarios tienen la libertad de\
        "copiar", "distribuir", "estudiar", "modificar" y "mejorar el software".\
        Con estas libertades, los usuarios (tanto individualmente como en forma\
        colectiva) controlan el programa y lo que hace.<br />\
        Por tanto, el «software libre» es ante todo una cuestión de libertad, no\
        de precio.<br /><br />\
        Un programa es software libre si los usuarios tienen las cuatro libertades\
        esenciales:<br /><br /><ol>\
            <li>0- La libertad de ejecutar el programa para cualquier propósito\
            (libertad 0).</li>\
            <li>1- La libertad de estudiar cómo funciona el programa, y cambiarlo\
            para que haga lo que usted quiera (libertad 1). El acceso al código\
            fuente es una condición necesaria para ello.</li>\
            <li>2- La libertad de redistribuir copias para ayudar a su prójimo\
            (libertad 2).</li>\
            <li>3- La libertad de distribuir copias de sus versiones modificadas\
            a terceros (libertad 3). Esto le permite ofrecer a toda la comunidad\
            la oportunidad de beneficiarse de las modificaciones. El acceso al\
            código fuente es una condición necesaria para ello.</li>\
            </ol>',
    'can_close': true
};
