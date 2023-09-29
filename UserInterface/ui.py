from textual.app import ComposeResult
from textual.widgets import Static

from GradeFetch.Source.UserInterface.login_ui import LoginUI

class GradeFetchUI(Static):
    
    def compose(self):
        yield LoginUI()
        yield LoadedProfileUI()
    