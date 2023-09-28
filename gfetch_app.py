from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static, ProgressBar, Label
from credential_input import CredentialInput

from canvasapi import Canvas, exceptions
from canvasapi.exceptions import CanvasException


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

#######################################
#######################################
    
# Define Keybinds for Application
    
#######################################
#######################################
    
    def action_toggle_dark_mode(self):
        self.dark = not self.dark

#######################################
#######################################
    
# Handle Events within the Application
    
#######################################
#######################################
    
    @on(Button.Pressed, "#load")
    @on(Input.Submitted)
    def LoadProfile(self):
        input = self.query_one("#url_input", Input)
        API_URL = input.value
        input = self.query_one("#token_input", Input)
        API_TOKEN = input.value
        try:
            self.canvas_api = Canvas(API_URL, API_TOKEN)
            self.user_name = self.canvas_api.get_current_user().name
            self.user_uid = self.canvas_api.get_current_user().id
        except (
            CanvasException, exceptions.InvalidAccessToken, exceptions.ResourceDoesNotExist,
            exceptions.BadRequest, exceptions.Unauthorized, exceptions.Forbidden,
            exceptions.RateLimitExceeded, exceptions.Conflict, exceptions.UnprocessableEntity, 
            exceptions.RequiredFieldMissing, Exception
            ) as e:
            self.user_name = "Invalid Token"
            self.user_uid = e
            print(e)
            
        label = self.query_one("#name_display", Label)
        label.update(self.user_name)
        label = self.query_one("#uid_display", Label)
        label.update(str(self.user_uid))
        self.mount(Label(self.canvas_api.get_current_user().name + " " + str(self.canvas_api.get_current_user().id)))
        