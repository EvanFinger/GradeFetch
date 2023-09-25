from textual.app import App
from textual.widgets import Footer, Header

class GradeFetchApp(App):
    def compose(self):
        """Defines Widgets"""
        yield Header()
        yield Footer()

