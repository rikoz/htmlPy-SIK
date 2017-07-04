#local server
from PySide import QtCore, QtGui, QtNetwork


#Sends broadcast to start exam and load test page
class Sender(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Sender, self).__init__(parent)

        self.statusLabel = QtGui.QLabel("Ready to broadcast datagrams on port 45454")

        self.startButton = QtGui.QPushButton("&Start")
        quitButton = QtGui.QPushButton("&Quit")

        buttonBox = QtGui.QDialogButtonBox()
        buttonBox.addButton(self.startButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QtGui.QDialogButtonBox.RejectRole)

        self.timer = QtCore.QTimer(self)
        self.udpSocket = QtNetwork.QUdpSocket(self)
        self.messageNo = 1

        self.startButton.clicked.connect(self.startBroadcasting)
        quitButton.clicked.connect(self.close)
        self.timer.timeout.connect(self.broadcastDatagramm)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.statusLabel)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Broadcast Sender")

    def startBroadcasting(self):
        self.startButton.setEnabled(False)
        self.timer.start(1000)

    def broadcastDatagramm(self):
        self.statusLabel.setText("Now broadcasting datagram %d" % self.messageNo)
        datagram = "Broadcast message %d" % self.messageNo
        self.udpSocket.writeDatagram(datagram, QtNetwork.QHostAddress(QtNetwork.QHostAddress.Broadcast), 45454)
        self.messageNo += 1


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    sender = Sender()
    sender.show()
    sys.exit(sender.exec_())
