
from textual import on
from textual.app import ComposeResult, App
from textual.widgets import Static, Label, Button, ProgressBar



class ProfileUI_Layer1(Static):
    def compose(self):
        yield ProfileDetailLabel()
    
    
class ProfileDetailLabel(Static):
    def compose(self):
        yield Label(id="user_name_display")
        yield Label(id="user_id_display")
        
class ProfileUI_Layer2(Static):
    def compose(self):
        yield Button("CLOSE PROFILE", id="close_profile", variant="error")
        yield Button("SAVE PROFILE", id="save_profile")
        yield Button("FETCH", id="fetch", variant="success")
        yield FetchProgress(id="fetch_progress")
        
class FetchProgress(Static):
    
    def compose(self):
        yield ProgressBar(id="course_progress")
        yield ProgressBar(id="course_assignment_group_progress")
        yield ProgressBar(id="assignment_progress")
        
class ProfileUI(Static):
    
    def compose(self):
        yield ProfileUI_Layer1()
        yield ProfileUI_Layer2()
        
    
    
    