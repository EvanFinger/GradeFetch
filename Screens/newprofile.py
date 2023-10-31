from Screens.screen import Screen
from textwrap import dedent

class NewProfile(Screen):
    
    def __init__(self):
        super().__init__('Add a NEW profile using your CanvasAPI URL and TOKEN')
        
        self.text_lines.append('[Quit] Quit Program [Quit]')
        self.text_lines.append('') # Blank line
        self.text_lines.append('Enter API url. Defaults to Virginia Tech <https://canvas.vt.edu> in which case press Enter')
    
    def translate_input(self):
        super().translate_input()
        
    def get_input(self):
        super().get_input(">>> ", 'https://canvas.vt.edu')
        # Returns if user intends to quit program
        if self.input == 'Quit':
            return self.input
        print('URL: ' + self.input)
        print(dedent("""
        Enter API token. This can be generated in your canvas settings by clicking <New Acces Token> 
        located under <Approved Integrations>. Copy and paste the token (4511~). While creating the 
        token, you may leave the expiration date blank, and that token will work indefinitely or until 
        you delete it."""))
        token = input('>>> ')
        print('TOKEN: ' + token)
        print(dedent("""
                     Make sure the credentials are correct.
                     [CONFIRM] Yes they are CORRECT.
                     [Any other input] No they are NOT CORRECT.
                     """))
        if input('>>> ') == 'CONFIRM':
            self.message = '_load_profile><' + self.input + ':::' + token
        

            
        
    def print_text(self):
        super().print_text(0,3)
        
        