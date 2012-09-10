#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gio
import gtk
import gtk.gdk
import webkit 
import os
import sys
import subprocess
import urllib2

BASE_KEY = "apps.conectar-bullets"

class BulletsBrowser(webkit.WebView):
	def __init__(self, settings):
		webkit.WebView.__init__(self)
		self.settings = settings
		self.get_property("settings").set_property("enable-default-context-menu", False)
		self.connect('navigation-policy-decision-requested', self._on_navigate_decision)
		self.load_uri("file://" + os.path.dirname(os.path.abspath(__file__)) + "/1.html")
    
	def _on_navigate_decision(self, view, frame, req, action, decision):
		parts =  req.get_uri().split("://", 1)
		if len(parts) == 2:
			if parts[0] == 'exec':
				command = urllib2.unquote(parts[1])
				subprocess.Popen(command, shell=True)
				return True
			if parts[0] == 'ui':
				params = parts[1].split("?", 1)
				if params[0] == 'finalize':
					for p in params:
						if p == 'autostart':
							settings.set_boolean("auto-start", True)
						elif p == 'no_autostart':
							settings.set_boolean("auto-start", False)
					gtk.main_quit()
				return True
		return False

if __name__ == '__main__':
	settings = Gio.Settings.new(BASE_KEY)
	if not settings.get_boolean('auto-start'):
		sys.exit(0)
	sw = gtk.ScrolledWindow()
	bullet_browser = BulletsBrowser(settings) 
	sw.add(bullet_browser) 
	win = gtk.Window(gtk.WINDOW_TOPLEVEL)
	win.add(sw) 
	win.set_resizable(False)
	bullet_browser.set_size_request(600, 400)
	win.set_default_size(600, 400)
	win.set_title("Primeros pasos")
	win.set_position(gtk.WIN_POS_CENTER)
	win.set_deletable(False)
	win.show_all() 

	win.connect("destroy", gtk.main_quit)
	gtk.main()
