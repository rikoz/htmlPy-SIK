import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://localhost:8000"))
web.show()

sys.exit(app.exec_())