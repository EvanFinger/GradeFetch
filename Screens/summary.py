from Screens.screen import Screen
from API.canvas_api import canvas_api
from tqdm import tqdm
from time import sleep

class Summary(Screen):
    
    def __init__(self, URL = None, TOKEN = None, EXISTING_USER = None):
        if not EXISTING_USER:
            self._apiLink = canvas_api()
            self._apiLink.LoadCanvasProfile(URL, TOKEN)
            print(self._apiLink.user_name)
            super().__init__('USER SUMMARY for ' + self._apiLink.user_name)
            self.print_text()
            
            self.loadFromCanvas()
            
    def loadFromCanvas(self):
        with tqdm(range(0, len(self._apiLink.courses)), ncols=100, colour='red', desc='Fetching Courses... ', leave=False) as progBar:
            for courseNumber in progBar:
                pass

        
        
        