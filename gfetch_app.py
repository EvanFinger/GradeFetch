from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static, ProgressBar, Label

from UserInterface.login_ui import LoginUI
from UserInterface.saved_credentials import SavedCredentials
from UserInterface.profile_ui import ProfileUI

from API.canvas_api import canvas_api
from API.canvas_account import CanvasAccount

import csv, time

class GradeFetchApp(App):

    BINDINGS = [
                ("d", "toggle_dark_mode", "Dark Mode")
            ]

    CSS_PATH = [
        "UserInterface\\CSS\\gfetch_app.tcss",
        "UserInterface\\CSS\\login_ui.tcss",
        "UserInterface\\CSS\\profile_ui.tcss"
    ]
    
    api = canvas_api()
    user = CanvasAccount()

    def compose(self):

        """Defines Widgets"""
        yield Header()
        yield Footer()
        yield LoginUI()
        yield ProfileUI()

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
            self.user_name = self.api.num_courses
            self.user_uid = self.api.user_id
            
            self.query_one(LoginUI).remove_class("InvalidLogin")
            self.add_class("ProfileLoaded")
            self.query_one("#user_name_display", Label).update(str(self.user_name))
            self.query_one("#user_id_display", Label).update(str(self.user_uid))
        except Exception as e:
            self.query_one(LoginUI).add_class("InvalidLogin")
            self.query_one("#lbl_error", Label).update(str(e))
        
        self.query_one("#token_input", Input).value = ""
    

        
    @on(Button.Pressed, "#close_profile")
    def CloseProfile(self):
        self.remove_class("ProfileLoaded")
        self.api.UnloadCanvasProfile()
        
    @on(Button.Pressed, "#save_profile")
    def SaveProfile(self):
        new_profile = True
        with open("app_data\\saved_profiles.csv", "r+") as file:
            csv_reader = csv.DictReader(file)
            for profile in csv_reader:
                if str(self.user_uid) == profile["uid"]:
                    new_profile = False
            if new_profile:
                csv_writer = csv.writer(file)
                csv_writer.writerow(
                    [
                        str(self.user_name), 
                        str(self.user_uid), 
                        str(self.api.api_url), 
                        str(self.api.api_token)
                        ]
                    )
    
    @on(Button.Pressed, "#fetch")
    def Fetch(self):
        course_progress = self.query_one("#course_progress", ProgressBar)
        self.api.Fetch()
        course_progress.total = len(self.api.courses)
        for course in self.api.courses:
            time.sleep(1)
            course_progress.advance(1)
            
            
        