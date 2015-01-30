# Colores
N=[0m
V=[01;32m
A=[01;33m


all:
	@echo ""
	@echo "Comandos disponibles"
	@echo ""
	@echo "  $(A)De uso para desarrollo: $(N)"
	@echo ""
	@echo "    $(V)test_linux$(N)  Prueba la aplicación sobre GNU/Linux"
	@echo "    $(V)test_mac$(N)    Prueba la aplicación sobre OSX"
	@echo ""

test_mac:
	open -a /Applications/node-webkit.app --args /Users/hugoruscitti/proyectos/huayra-bullets/src

test_linux: 
	nw src

PHONY: dist
