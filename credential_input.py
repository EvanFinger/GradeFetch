from textual import on
from textual.widgets import Placeholder, Button, Input, Static, ProgressBar, Label


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
        yield Button("LOAD PROFILE", id="load")
        yield Button("SAVED PROFILES", id="saved")
        yield Button("FETCH", id="fetch", variant="success")
        yield CredentialDisplay()
        yield ProgBars()

class CredentialInput(Static):
    
    
                        
    def compose(self):
        yield Input(value="https://canvas.vt.edu", id="url_input")
        yield Input(placeholder="Your Canvas Access Token (4511~...)", id="token_input")
        yield CredInput_Layer2()
        
    def EditDisplay(self, name_display, uid_display):
        label = self.query_one("#name_display", Label)
        label.update(str(name_display))
        label = self.query_one("#uid_display", Label)
        label.update(str(uid_display))
        
    def ToggleFetch(self, disabled = None):
        obj = self.query_one("#fetch", Button)
        if disabled == None:
            obj.disabled = not obj.disabled
        else:
            obj.disabled = disabled
    
    def ProfileLoaded(self, profile_loaded):
        self.query_one("#fetch", Button).add_class("profile_loaded")
        self.query_one("#saved", Button).add_class("profile_loaded")
        