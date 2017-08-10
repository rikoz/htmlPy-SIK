from PySide.QtCore import QTime

def test_timer():
	msec = 3 * 60 * 1000
	time = QtCore.QTime()
	curr_time = time.currentTime()
	end_time = curr_time.addMSecs(msec)
	ret = end_time.toString("hh:mm:ss")
return ret
