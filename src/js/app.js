var path = require('path');
var fs = require('fs');
var replaceStream = require('replacestream');

Reveal.initialize({
  controls: false,
  progress: true,
  history: true,
  help:false,
  center: true,
  embedded: true,
  autoSlide: 60000,

  transition: 'slide',

  // Fondo paralaje
  parallaxBackgroundImage: 'css/fondo.svg',
  parallaxBackgroundSize: '1600px 900px',

    // Optional reveal.js plugins
  dependencies: [
  { src: 'lib/js/classList.js', condition: function() { return !document.body.classList; } },
  { src: 'plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
  { src: 'plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
    { src: 'plugin/highlight/highlight.js', async: true, condition: function() { return !!document.querySelector( 'pre code' ); }, callback: function() { hljs.initHighlightingOnLoad(); } },
    { src: 'plugin/zoom-js/zoom.js', async: true },
      { src: 'plugin/notes/notes.js', async: true }
  ]
});

var botonIzquierda = document.getElementById('botonIzquierda');
var botonDerecha = document.getElementById('botonDerecha');
var checkboxIniciar = document.getElementById('check');

function actualizar_estados() {

  if (Reveal.isFirstSlide())
    botonIzquierda.setAttribute('disabled', 'disabled');
  else
    botonIzquierda.removeAttribute('disabled');

  if (Reveal.isLastSlide())
    botonDerecha.setAttribute('disabled', 'disabled');
  else
    botonDerecha.removeAttribute('disabled');
}

Reveal.addEventListener('ready', function(event) {
  actualizar_estados();
});

botonIzquierda.onclick = function() {
  // NOTA: usar Reveal.navigateLeft() si no queremos que ingrese en
  // los slides inferiores.
  Reveal.prev();
  actualizar_estados();
}

botonDerecha.onclick = function() {
  // NOTA: usar Reveal.navigateRight() si no queremos que ingrese en
  // los slides inferiores.
  Reveal.next();
  actualizar_estados();
};


function copiar_archivo(desde, hasta, autostart) {
  fs.createReadStream(desde).
    pipe(replaceStream('Terminal=false', "Terminal=false\nX-MATE-Autostart-enabled=" + autostart)).
    pipe(fs.createWriteStream(hasta));
}


function actualizar_acceso_inicio_automatico(reiniciar) {
  var ruta_desktop_original = "/usr/share/applications/huayra-bullets.desktop";
  var ruta_desktop_home = path.join(process.env['HOME'], '.config/autostart/huayra-bullets.desktop');

  if (fs.existsSync(ruta_desktop_original)) {
    copiar_archivo(ruta_desktop_original, ruta_desktop_home, reiniciar);
  } else {
    console.error("El archivo " + ruta_desktop_original + " no existe, no se puede cambiar preferencias de inicio...");
  }

}

function mostrar_estado_iniciar_checkbox() {
  var ruta_desktop_home = path.join(process.env['HOME'], '.config/autostart/huayra-bullets.desktop');

  if (fs.existsSync(ruta_desktop_home)) {
    var activado = /X-MATE-Autostart-enabled=true/.test(fs.readFileSync(ruta_desktop_home).toString());

    if (activado) {
      checkboxIniciar.checked = true;
    }
  }
}

checkboxIniciar.onchange = function() {
  actualizar_acceso_inicio_automatico(checkboxIniciar.checked);
};

mostrar_estado_iniciar_checkbox();

