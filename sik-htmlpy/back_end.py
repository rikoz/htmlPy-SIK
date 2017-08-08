import htmlPy
import json
from app.models import Course, Question, Option


class SikTest(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self, app):
        super(SikTest, self).__init__()
        self.app = app
        self.network_config()
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
            self.app.template = ("profile.html", {"stud_id": "PSC120345", "lvl": "300", "cour_code": "CPE382", "time_allwd": "48", 
                "dp": "img/thumb_sign-in.png"})
        else:
            self.login_val_error()

        #dumps the dictionary key-value pairs as json format into a variable
        #d = json.dumps(form_data)

        #with open("/home/rikoz/Desktop/fyp/htmlPy-SIK/koz.txt", "w") as f:
        #    f.write(g)
        return

    @htmlPy.Slot()
    def strt_tst(self):
        self.app.template = ("test.html", {})
        return

    @htmlPy.Slot(str, result=str)
    def sik_test_form(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

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