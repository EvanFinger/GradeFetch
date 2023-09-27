from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static, ProgressBar, Label

class ProgBars(Static):
    
    def compose(self):
        yield ProgressBar(id="course_progress")
        yield ProgressBar(id="course_assignment_group_progress")
        yield ProgressBar(id="assignment_progress")

class CredInput_Layer2(Static):
    def compose(self):
        yield Button("FETCH", id="fetch", variant="success")
        yield Label("User:     UID:     ", id="name_uid_display")
        yield ProgBars()
        
        
        

class CredentialInput(Static):
                
    def compose(self):
        yield Input(value="https://canvas.vt.edu", id="url_input")
        yield Input(placeholder="Your Canvas Access Token (4511~...)", id="token_input")
        yield CredInput_Layer2()

class MainContainer(Static):
    
    def compose(self):
        yield CredentialInput()

class GradeFetchApp(App):

    BINDINGS = [
                ("d", "toggle_dark_mode", "Dark Mode")
            ]

    CSS_PATH = "test.tcss"

    def compose(self):

        """Defines Widgets"""
        yield Header()
        yield Footer()
        yield MainContainer()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark
