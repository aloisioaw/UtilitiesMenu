# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html

import os
import signal
import json
import subprocess
import tkMessageBox
import sys
import window

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

	item_quit = gtk.MenuItem('Fechar')
	item_quit.connect('activate', quit)
	menu.append(item_quit)
	menu.show_all()
	return menu

def service_named_restart(_):
	root=Tk()
	m=window.popupWindow(root)
	root.mainloop()
	#tkMessageBox.showinfo(title="Greetings", message="Hello World!")
	subprocess.call("echo " + m.senha + " > sudo -S service named restart", shell=True)
	#notify.Notification.new("<b>Joke</b>", fetch_joke(), None).show()

def quit(_):
	notify.uninit()
	gtk.main_quit()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()