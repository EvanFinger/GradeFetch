from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static, ProgressBar, Label
from credential_input import CredentialInput, CredentialDisplay
from saved_credentials import SavedCredentials

from canvasapi import Canvas


class MainContainer(Static):
    
    def compose(self):
        yield CredentialInput()
        yield SavedCredentials()
        

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
        
        self.query_one(CredentialInput).EditDisplay("-----", "-----")
        
        input = self.query_one("#url_input", Input)
        API_URL = input.value
        input = self.query_one("#token_input", Input)
        API_TOKEN = input.value
        try:
            self.canvas_api = Canvas(API_URL, API_TOKEN)
            self.user_name = self.canvas_api.get_current_user().name
            self.user_uid = self.canvas_api.get_current_user().id
            self.query_one(CredentialInput).ToggleFetch(False)
            
            # update butttons
            self.query_one(CredentialInput).ProfileLoaded(True)
        except Exception as e:
            self.user_name = e
            self.user_uid = "Invalid Token"
            self.query_one(CredentialInput).ToggleFetch(True)
            
        self.query_one(CredentialInput).EditDisplay(self.user_name, self.user_uid)
        