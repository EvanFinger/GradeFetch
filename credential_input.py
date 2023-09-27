from textual import on
from textual.widgets import Button, Input, Static, ProgressBar, Label


class ProgBars(Static):
    
    def compose(self):
        yield ProgressBar(id="course_progress")
        yield ProgressBar(id="course_assignment_group_progress")
        yield ProgressBar(id="assignment_progress")
        
class CredentialDisplay(Static):
    
    def compose(self):
        yield Label("User", id="name_label")
        yield Label("-----", id="name_display")
        yield Label("-----", id="uid_display")

class CredInput_Layer2(Static):
    def compose(self):
        yield Button("FETCH", id="fetch", variant="success")
        yield CredentialDisplay()
        yield ProgBars()

class CredentialInput(Static):
    API_URL = ""
    API_TOKEN = ""
    
    @on(Button.Pressed, "#fetch")
    @on(Input.Submitted)
    def getInput(self):
        input = self.query_one("#url_input", Input)
        API_URL = input.value
        input = self.query_one("#token_input", Input)
        API_TOKEN = input.value
        self.mount(Label(API_URL + " " + API_TOKEN))
                        
    def compose(self):
        yield Input(value="https://canvas.vt.edu", id="url_input")
        yield Input(placeholder="Your Canvas Access Token (4511~...)", id="token_input")
        yield CredInput_Layer2()