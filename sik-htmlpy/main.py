import htmlPy
import os

app = htmlPy.AppGUI(title=u"SIK Test Center", maximized=True)

app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")

app.template = ("index.html", {"username": "htmlPy_user"})

if __name__ == "__main__":
    app.start()