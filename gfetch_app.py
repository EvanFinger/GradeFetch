from textual.app import App
from textual.widgets import Footer, Header, Button, Input, Static


class test(Static):
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if(event.button.id == "yes")
        {
            self.add_class("yes")
        }
        
    def compose(self):
        yield Button("Yes", id="yes")
        yield Button("No", id="no")


class GradeFetchApp(App):

    BINDINGS = [
                ("d", "toggle_dark_mode", "Dark Mode")
            ]

    CSS_PATH = "test.tcss"

    def compose(self):

        """Defines Widgets"""
        yield Header()
        yield Footer()
        yield test()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark
