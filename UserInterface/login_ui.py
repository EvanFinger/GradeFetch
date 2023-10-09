from textual import on
from textual.app import ComposeResult, App
from textual.widgets import Button, Input, Static, OptionList, Label
from textual.containers import ScrollableContainer

import csv


class CredentialInputs(Static):
     def compose(self):
        yield Input(value="https://canvas.vt.edu", id="url_input")
        yield Input(placeholder="Your Canvas Access Token (4511~...)", id="token_input")
        yield Label("", id="lbl_error")
        
class SavedLoginSelector(Static):
    profile_list = []
    def compose(self):
        yield Label("V Saved Profiles V", id="lbl_saved_profiles")
        yield ScrollableContainer(
            OptionList(id="profile_options")
            )  
    
    def UpdateList(self):
        with open('app_data\\saved_profiles.csv') as file:
            csv_reader = csv.DictReader(file)
            
            for profile in csv_reader:
                if profile not in self.profile_list:
                    self.profile_list.append(profile)
                    self.query_one("#profile_options", OptionList).add_option(profile["user_name"] + " " + profile["uid"])
        
class LoginButtons(Static):
    def compose(self):
        yield Button("LOAD PROFILE", id="btn_load_profile")
        yield Button("SAVED PROFILES", id="btn_saved_profiles")
        yield Button("CANCEL", id="btn_cancel_delete")
        yield Button("DELETE PROFILE", variant="error", id="btn_delete_profile")
        yield Button("NEW PROFILE", id="btn_new_profile")

class LoginUI(Static):
    
    def compose(self):
        yield CredentialInputs()
        yield SavedLoginSelector()
        yield LoginButtons()
        
        
    @on(Button.Pressed, "#btn_saved_profiles")
    def OpenSavedProfileList(self):
        self.remove_class("InvalidLogin")
        self.query_one(SavedLoginSelector).UpdateList()
        self.add_class("ShowSaved")
        
        
    @on(Button.Pressed, "#btn_new_profile")
    def OpenCredentialInputs(self):
        self.remove_class("ShowSaved")
        
    @on(Button.Pressed, "#btn_delete_profile")
    def DeleteProfile(self):
        self.add_class("DeleteMode")
    
    @on(Button.Pressed, "#btn_cancel_delete")
    def Cancel(self):
        self.remove_class("DeleteMode")
        
    def on_option_list_option_selected(self, message):
        index = message.option_index
        
        self.remove_class("ShowSaved")
        profile = self.query_one(SavedLoginSelector).profile_list[index]
        self.query_one("#url_input", Input).value = profile["api_url"]
        self.query_one("#token_input", Input).value = profile["api_token"]
        
    
        








