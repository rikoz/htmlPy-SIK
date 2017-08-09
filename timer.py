from PySide.QtCore import QTimer

#Get current time

def tick():
    print 'tick'

timer = QTimer()
timer.timeout.connect(tick)
timer.start(1000)