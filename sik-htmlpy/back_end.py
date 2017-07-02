import htmlPy
import json
#from main import app as htmlPy_app


#htmlPy_app = htmlPy.AppGUI()


class sikTest(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self):
        super(sikTest, self).__init__()
        # Initialize the class here, if required.
        return

    def showName(self):
        return self.name

    @htmlPy.Slot()
    def function_name(self):
        # This is the function exposed to GUI events.
        # You can change app HTML from here.
        # Or, you can do pretty much any python from here.
        #
        # NOTE: @htmlPy.Slot decorater needs argument and return data-types.
        # Refer to API documentation.
        return

    @htmlPy.Slot()
    def about(self):
        ## Change HTML of the app using Jinja2 templates
        #htmlPy_app.template = ("./login.html", {})
        print("it works")
        return

#############################################################################################

    @htmlPy.Slot(str, result=str)
    def sikLoginForm(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot(str, result=str)
    def sikTestform(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

#############################################################################################

    @htmlPy.Slot()
    def javascript_function(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI

        ## Execute javascript on currently displayed HTML in the app
        htmlPy_app.evaluate_javascript("alert('Hello from back-end')")
        return


## You have to bind the class instance to the AppGUI instance to be
## callable from GUI
#htmlPy.AppGUI.bind(sikTest())