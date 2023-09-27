from textual import on
from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static, ProgressBar, Label
from credential_input import CredentialInput


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
