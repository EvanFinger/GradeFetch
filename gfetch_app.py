from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static, ProgressBar, Label

from UserInterface.login_ui import LoginUI, CredentialInputs, SavedLoginSelector
from UserInterface.saved_credentials import SavedCredentials
from UserInterface.loaded_profile import LoadedProfile_Layer1, LoadedProfile_Layer2

from API.canvas_api import canvas_api

class GradeFetchApp(App):

    BINDINGS = [
                ("d", "toggle_dark_mode", "Dark Mode")
            ]

    CSS_PATH = [
        "UserInterface\\CSS\\test.tcss",
        "UserInterface\\CSS\\login_ui_css.tcss"
    ]
    
    api = canvas_api()

    def compose(self):

        """Defines Widgets"""
        yield Header()
        yield Footer()
        yield LoginUI()

#######################################
#######################################
    
# Define Keybinds for Application
    
#######################################
#######################################
    
    def action_toggle_dark_mode(self):
        self.dark = not self.dark


#######################################
    
# Handle LoginUI Events
    
#######################################

    @on(Button.Pressed, "#btn_load_profile")
    @on(Input.Submitted)
    def LoadProfile(self):
            
        input = self.query_one("#url_input", Input)
        API_URL = input.value
        input = self.query_one("#token_input", Input)
        API_TOKEN = input.value
        try:
            self.api.LoadCanvasProfile(API_URL=API_URL, API_TOKEN=API_TOKEN)
            self.user_name = self.api.user_name
            self.user_uid = self.api.user_id
            
            self.query_one(LoginUI).remove_class("InvalidLogin")
        except Exception as e:
            self.query_one(LoginUI).add_class("InvalidLogin")
            self.query_one("#lbl_error", Label).update(str(e))
    

        
    @on(Button.Pressed, "#close")
    def UnloadProfile(self):
        self.canvas_api = None
        self.user_name = "-----"
        self.user_uid = "-----"
        self.query_one(CredentialInput).ProfileLoaded(False)
        self.query_one(CredentialInput).EditDisplay(self.user_name, self.user_uid)
        
    @on(Button.Pressed, "#saved")
    def ShowSavedProfileList(self):
        obj = self.query_one(SavedCredentials)
        
        if(obj.initialized):
            obj.init_options()
            
        if(obj.has_class("hidden")):
            obj.remove_class("hidden")
        else:
            obj.add_class("hidden")
        obj.initialized = True
        