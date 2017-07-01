import os
import sys
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cbt.settings")
import htmlPy
from PySide import QtCore,QtGui
from PyQt4 import QtGui

#Run a termainal operation and command in background
#os.system("gnome-terminal -e 'sudo apt-get update'")


# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppGUI(title=u"SIK Test Center", maximized=True, plugins=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")


#GUI Templates
#app.template = ("index.html", {})
app.template = ("login.html", {})
#app.template = ("profile.html", {})
#app.template = ("test.html", {})
#app.template = ("submission.html", {})


app.web_app.setMinimumWidth(1366)
app.web_app.setMinimumHeight(768)


#Currently used only to DISABLE right clicking on application except for input fields.
app.right_click_setting(htmlPy.settings.DISABLE)


#Currently used only to DISABLE text selection on application.
app.text_selection_setting(htmlPy.settings.DISABLE)


#Displays the app in full screen
#app.window.showFullScreen()

## Binding of back-end functionalities with GUI

# Import back-end functionalities
from back_end import sikTest

# Register back-end functionalities
#app.bind(sikTest())
pers1 = sikTest("rikome")
print(pers1.showName())

# Instructions for running application
if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional

    app.start()