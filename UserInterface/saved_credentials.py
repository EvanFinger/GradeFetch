from textual.widgets import OptionList, Static, Label
from textual.widgets.option_list import Option, Separator
import csv

class SavedCredentials(Static):
    initialized = False
    
    def compose(self):
        yield Label("SAVED PROFILES")
       
        
    def init_options(self):
        ProfileList = ["op1", "op2", "op3"]
        for item in ProfileList:
            self.query_one("#profile_options", OptionList).add_option(Option(item, id=item))
            self.query_one("#profile_options", OptionList).add_option(Separator())
