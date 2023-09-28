from textual.widgets import OptionList, Static, Label
from textual.widgets.option_list import Option, Separator

class SavedCredentials(Static):
    
    def compose(self):
        yield Label("SAVED PROFILES")
        yield OptionList(id="profile_options")
        
    def init_options(self):
        ProfileList = ["op1", "op2", "op3"]
        for item in ProfileList:
            self.query_one("#profile_options", OptionList).add_option(Option(item, id=item))
            self.query_one("#profile_options", OptionList).add_option(Separator())
