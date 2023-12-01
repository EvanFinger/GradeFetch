from Screens.screen import Screen
from API.canvas_api import canvas_api
from time import sleep

class Summary(Screen):
    
    def __init__(self, URL = None, TOKEN = None, EXISTING_USER = None):
        if not EXISTING_USER:
            self._apiLink = canvas_api()
            self._apiLink.LoadCanvasUser(URL, TOKEN)
            print(self._apiLink.user_name)
            super().__init__('USER SUMMARY for ' + self._apiLink.user_name)
            self.print_text()
            
            self.loadProfileToAPI()
            
    def loadProfileToAPI(self):
        self._apiLink.loadProfileData()
        self._apiLink.processProfileData()

        
        
        