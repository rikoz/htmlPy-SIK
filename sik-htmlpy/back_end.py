import htmlPy
import json
from app.models import Course, Question, Option
from PySide import QtCore


class SikTest(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self, app):
        super(SikTest, self).__init__()
        self.app = app
        self.network_config()
        self.time_allwd = 1
        return

    def show_name(self):
        return self.name

    #automatically connects to the specified network SSID and password
    def network_config(self):
        self.network_prompt()
        return

    @htmlPy.Slot()
    def about(self):
        self.app.template = ("about.html", {"name": Course.objects.get(id=1).name})
        return

    @htmlPy.Slot()
    def get_started(self):
        self.app.template = ("login.html", {})
        return

    @htmlPy.Slot(str, result=str)
    def sik_login_form(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        
        #loads form data into a dictionary
        form_data = json.loads(json_data)

        if form_data['user_id'] == 'rikome' and form_data['password'] == 'animated50':
            self.app.template = ("profile.html", {"stud_id": "PSC120345", "lvl": "300", "cour_code": "CPE382", "time_allwd": self.time_allwd, 
                "full_name":"EREZI, R.Su.", "dp": "img/thumb_sign-in.png"})
        #Listen for trigger to start test and timer 

        else:
            self.login_val_error()

        #dumps the dictionary key-value pairs as json format into a variable
        #d = json.dumps(form_data)
        return

    #Listening to socket for trigger broadcast - Loop
    @htmlPy.Slot()
    def strt_tst(self):
        self.app.template = ("test.html", {"time_left": self.tst_timer(), "full_name":"EREZI, R.Su.", "dp": "img/thumb_sign-in.png"})  
        return

    #Test Count-down timer
    @htmlPy.Slot()
    def tst_timer(self):
        msec = (self.time_allwd * 60 * 1000) + 1000
        h = self.time_allwd // 60
        m = (self.time_allwd % 60)
        s = 1
        tf = str(h)+":"+str(m)+":"+str(s)
        time = QtCore.QTime()
        time_left = time.fromString(tf, "h:m:s")
        """
        timer = QtCore.QTimer()
        tmr = timer.singleShot(msec, Slot(self.final_submit()))
        tsh = timer.setSingleShot('true')
        tmr.start()
        """
        return time_left.toString("hh:mm:ss")

    #############################################################################################################
    @htmlPy.Slot(str, result=str)
    def sik_test_form(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot()
    def final_submit(self):
        self.app.template = ("submission.html", {})
        return 

    #####JAVASCRIPT########

    @htmlPy.Slot()
    def login_val_error(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI

        ## Execute javascript on currently displayed HTML in the app
        self.app.evaluate_javascript("alert('Wrong Credentials')")
        return

    @htmlPy.Slot()
    def network_prompt(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI

        ## Execute javascript on currently displayed HTML in the app
        self.app.evaluate_javascript("prompt('SSID', ''), prompt('Password', '')")
        return