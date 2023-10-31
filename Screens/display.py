from Resources.stack import Stack
from Screens.mainmenu import MainMenu
from Screens.newprofile import NewProfile


Display = Stack(MainMenu())

class handler:
    
    working = False
    
    def handle(self, message = '><'):
        """Handles the given message if message is recognized.
        Otherwise returns -1.

        Args:
            message (string): message to be handled
        """
        if not message:
            message = '><'
        # Splits the message provided message into a key and usable parameter
        message_key, parameter = message.split('><')
        # takes action based on the key provided by the message
        match message_key:
            case '_quit_app': # Quits the application (pops all screens off the stack)
                for screen in range(0, Display.size()):
                    Display.pop()
            case '_nav_back': # Pops the top screen off the Display stack
                Display.pop()
            case '_nav_new_profile':
                Display.push(NewProfile())
            case '_load_profile':
                print(parameter.split(':::'))
                input()