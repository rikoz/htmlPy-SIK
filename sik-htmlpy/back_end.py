import htmlPy
import json
from app.models import Course, Question, Option


class SikTest(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self, app):
        super(SikTest, self).__init__()
        self.app = app
        return

    def show_name(self):
        return self.name

    @htmlPy.Slot()
    def function_name(self):
        return

    @htmlPy.Slot()
    def about(self):
        self.app.template = ("about.html", {"name": Course.objects.get(id=1).name})
        return

    @htmlPy.Slot(str, result=str)
    def sik_login_form(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot(str, result=str)
    def sik_test_form(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot()
    def javascript_function(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI

        ## Execute javascript on currently displayed HTML in the app
        self.app.evaluate_javascript("alert('Hello from back-end')")
        return