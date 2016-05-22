#!/usr/bin/env python
# coding: utf-8

# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html

import os
import signal
import json
import subprocess
import tkMessageBox
import sys
import window
import ConfigParser

from glob import glob
from urllib2 import Request, urlopen, URLError
from Tkinter import *

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'UtilityMenu'

def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('IMG/tools.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())
	notify.init(APPINDICATOR_ID)
	gtk.main()

def build_menu():
	menu = gtk.Menu()
	item_named_restart = gtk.MenuItem('Named Restart')
	item_named_restart.connect('activate', service_named_restart)
	menu.append(item_named_restart)

	item_agnclientd_restart = gtk.MenuItem('Agnclientd Restart')
	item_agnclientd_restart.connect('activate', service_agnclientd_restart)
	menu.append(item_agnclientd_restart)

	menu.append(build_workspaces_menu())

	image = gtk.Image()
	image.set_pixel_size(1)
	image.set_from_file(os.path.abspath('IMG/eclipse.xpm'))
	menu_item = gtk.ImageMenuItem("Xucripse")
	menu_item.set_image(image)
	menu.append(menu_item)

	item_quit = gtk.MenuItem('Fechar')
	item_quit.connect('activate', quit)
	menu.append(item_quit)
	menu.show_all()
	return menu

def build_workspaces_menu():
	workspaces_path = read_config("workspaces", "path")

	item_workspaces = gtk.MenuItem('Eclipse')
	menu_workspaces = gtk.Menu()
	item_workspaces.set_submenu(menu_workspaces)

	for entry in os.listdir(workspaces_path):
		if (os.path.isfile(entry) == False):
			for workspace_folder in os.listdir(os.path.join(workspaces_path, entry)):
				if (os.path.isfile(workspace_folder) == False and workspace_folder == ".metadata"):
					item_submenu = gtk.MenuItem(entry)
					item_submenu.connect('activate', open_eclipse, os.path.join(workspaces_path, entry))
					menu_workspaces.append(item_submenu)
					break

	return item_workspaces

def open_eclipse(widget, path):
	eclipse_path = read_config("eclipse", "path")
	subprocess.call(eclipse_path + "/./eclipse -data " + path, shell=True)

def read_config(section, name):
	config = ConfigParser.ConfigParser()
	config.readfp(open('config.properties'))
	return config.get(section, name)

def service_named_restart(_):
	resultado = None
	while resultado == None or resultado == 1:
		root=Tk()
		m=window.popupWindow(root)
		root.mainloop()
		if m.senha != None:
			resultado=subprocess.call("echo " + m.senha + " | sudo -S service named restart", shell=True)
			if resultado != 1:
				notify.Notification.new("Reinicialização de Serviço", "Serviço named reiniciado", None).show()

def service_agnclientd_restart(_):
	resultado = None
	while resultado == None or resultado == 1:
		root=Tk()
		m=window.popupWindow(root)
		root.mainloop()
		if m.senha != None:
			resultado=subprocess.call("echo " + m.senha + " | sudo -S service agnclientd restart", shell=True)
			if resultado != 1:
				notify.Notification.new("Reinicialização de Serviço", "Serviço agnclientd reiniciado", None).show()

def quit(_):
	notify.uninit()
	gtk.main_quit()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()