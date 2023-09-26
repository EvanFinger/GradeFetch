from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static


class test(Static):
    def compose(self):
        yield Button()
        yield Button()


class GradeFetchApp(App):

    BINDINGS = [
                ("d", "toggle_dark_mode", "Dark Mode")
            ]

    CSS_PATH = "test.css"

    def compose(self):

        """Defines Widgets"""
        yield Header()
        yield Footer()
        yield test()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark
