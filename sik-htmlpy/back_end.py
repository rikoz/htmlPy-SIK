import subprocess
import json
import htmlPy
import sik_api
from PySide import QtCore, QtGui, QtNetwork


class SikTest(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self, app):
        super(SikTest, self).__init__()
        self.app = app
        self.profile = {}
        self.test = {}
        self.time_allowed = 0
        self.logged_in = False
        self.network_config()
        self.clear_clipboard()

        return

    def show_name(self):
        return self.name

    #automatically connects to the specified network SSID and password
    def network_config(self):
        mgr = QtNetwork.QNetworkConfigurationManager()
        #deflt = mgr.allConfigurations(QNetworkConfiguration.Active)
        return

    #Reconfigure Key Combinations
    def clear_clipboard(self):
        clip_board = QtGui.QClipboard()
        clip_board.clear()
        return

    @htmlPy.Slot()
    def about(self):
        self.app.template = ("about.html",{"name": "hello chibie"})
        return

    @htmlPy.Slot()
    def get_started(self):
        self.app.template = ("login.html", {"error": "Please make sure your device is successfully connected to the Wi-Fi network specified for this test."})
        return

    @htmlPy.Slot()
    def sik_edit_file(self, app_command, filename):

        # open a file with specified filename and terminal command
        p = subprocess.Popen([app_command,filename], stdout=subprocess.PIPE)
        p.communicate()

        return

    @htmlPy.Slot(str, result=str)
    def sik_login_form(self, json_data):
        
        #loads form data
        mat_number = json.loads(json_data)['mat_number']
        password = json.loads(json_data)['password']

        if sik_api.auth_user(mat_number, password):
            self.profile = sik_api.get_profile(mat_number)
            self.test = sik_api.get_test(password)
            self.time_allowed = self.test['duration']
            
            data = {
                "student": self.profile,
                "test": {"duration": self.time_allowed}
            }

            data['test']['course_title'] = self.test['course_title']
            data['test']['course_code'] = self.test['course_code']
            data['test']['course_lecturers'] = self.test['course_lecturers']
            data['test']['venue'] = self.test['venue']
            data['test']['date'] = self.test['date'].split("T")[0]

            self.logged_in = True

            self.app.template = ("profile.html", data)
        
            #Listen for trigger to start test and timer 

        else:
            self.app.template = ("login.html", {"error": "Wrong Login Credentials / Device WiFi Connection, Try Again!"})

        return

    #Listening to socket for trigger broadcast - Loop
    @htmlPy.Slot()
    def start_test(self):
        data = {
            "student": self.profile,
            "test": self.test
        }
        data['test']['time_left'] = self.test_timer()

        self.app.template = ("test.html", data)
        return

    #Test Count-down timer
    @htmlPy.Slot()
    def test_timer(self):
        msec = (self.time_allowed * 60 * 1000) + 500
        h = self.time_allowed // 60
        m = (self.time_allowed % 60)
        s = 1
        tf = str(h)+":"+str(m)+":"+str(s)
        time = QtCore.QTime()
        time_left = time.fromString(tf, "h:m:s")
        
        QtCore.QTimer.singleShot(msec, self.final_submit)

        return time_left.toString("hh:mm:ss")
        
    #############################################################################################################

    @htmlPy.Slot(str, result=str)
    def sik_test_form(self, json_data):
        
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot()
    def final_submit(self):
        self.app.template = ("submission.html", {})
        #command_line()
        return 

    @htmlPy.Slot()
    def command_line(self):
        #os.system("gnome-terminal -e 'sudo shutdown -P now'")
        return