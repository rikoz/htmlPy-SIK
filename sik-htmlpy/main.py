import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<project_name>.settings")
import htmlPy
from PyQt4 import QtGui


# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppGUI(title=u"SIK Test Center", maximized=True, plugins=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

#GUI Templates
app.template = ("index.html", {})

app.web_app.setMinimumWidth(1366)
app.web_app.setMinimumHeight(768)


# Binding of back-end functionalities with GUI

# Import back-end functionalities
#from html_to_python import ClassName

# Register back-end functionalities
#app.bind(ClassName())


# Instructions for running application
if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    app.start()