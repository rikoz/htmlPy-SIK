#local server
import htmlPy
from PySide import QtCore, QtGui, QtNetwork


#Recieve broadcast to start exam and load test page
class Receiver(htmlPy.Object):
    def __init__(self, parent=None):
        super(Receiver, self).__init__(parent)

        self.udpSocket = QtNetwork.QUdpSocket(self)
        self.udpSocket.bind(45454)
        
        self.udpSocket.readyRead.connect(self.processPendingDatagrams)


    def processPendingDatagrams(self):
        while self.udpSocket.hasPendingDatagrams():
            datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())

            try:
                # Python v3.
                datagram = str(datagram, encoding='ascii')
            except TypeError:
                # Python v2.
                pass