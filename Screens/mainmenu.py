from Screens.screen import Screen

class MainMenu(Screen):
    
    def __init__(self):
        super().__init__('Grade Fetch')
        
        self.text_lines.append('[1] Load a New Profile [1]')
        self.text_lines.append('[2] Load Existing Profile [2]')
        self.text_lines.append('[Quit] Quit Program [Quit]')
    
    def translate_input(self):
        super().translate_input()
        
        if self.input == '1':
            self.message = '_nav_new_profile><'
    