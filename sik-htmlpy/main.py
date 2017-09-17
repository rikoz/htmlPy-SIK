import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cbt.settings")
django.setup()

import sys
import htmlPy

#Import back-end functionality
from back_end import SikTest
from PySide import QtCore,QtGui


#Run a termainal operation and command in background (keyboard shortcuts, mouse clicks, Unmount drives, launch apps as embedded)
#os.system("gnome-terminal -e 'udisksctl unmount -f --block-device /dev/sdb1'")
#os.system("gnome-terminal -e 'udisksctl unmount -f --block-device /dev/sdb2'")
#os.system("gnome-terminal -e 'udisksctl unmount -f --block-device /dev/sdb3'")
#os.system("gnome-terminal -e 'udisksctl power-off --block-device /dev/sdb'")


# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppGUI(title=u"SIK Test Center", maximized=True, plugins=True, allow_overwrite=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")
app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

#GUI Templates
#app.template = ("wifi.html", {})
app.template = ("index.html", {})
#app.template = ("login.html", {})
#app.template = ("profile.html", {})
#app.template = ("test.html", {})
#app.template = ("submission.html", {})

#GUI Geometry
#app.web_app.setMinimumWidth(1366)
#app.web_app.setMinimumHeight(768)


#Currently used only to DISABLE right clicking on application except for input fields.
app.right_click_setting(htmlPy.settings.DISABLE)

#Currently used only to DISABLE text selection on application.
app.text_selection_setting(htmlPy.settings.DISABLE)

#Displays the app in full screen
app.window.showFullScreen()

#Binding of Back-end functionalities
app.bind(SikTest(app))


# Instructions for running application

if __name__ == "__main__":
	
    app.start()
    	