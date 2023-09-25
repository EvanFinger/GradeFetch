from textual.app import App
from textual.widgets import Footer, Header, Button, Input


class GradeFetchApp(App):

    BINDINGS = [
                ("d", "toggle_dark_mode", "Dark Mode")
            ]

    def compose(self):

        """Defines Widgets"""
        yield Header()
        yield Footer()
        yield Input()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark
