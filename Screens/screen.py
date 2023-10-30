import os

class Screen:
    
    title = 'Screen Title'
    input = ''
    
    message = None
    
    def __init__(self, title = None) -> None:
        if title:
            self.title = title
            
        self.text_lines = []
        
    def print_text(self, s_index = None, e_index = None): 
        """Prints the text present within the text_lines list. If both args left to default, prints all lines.
        If s_index is filled, prints text at s_index of self.text_lines. If both args filled, prints lines in
        range from s_index(inclusive) to e_index(exclusive) in self.text_lines.

        Args:
            s_index (int, optional): Starting index of lines in text_lines. Defaults to None.
            e_index (int, optional): Ending index of lines in text_lines. Defaults to None.
        """
        os.system('cls')
        print(self.title)
        if s_index == e_index == None: # Prints all text_lines
            for text in self.text_lines:
                print(text)
        elif s_index != None and e_index == None: # Prints specified single text_line
            print(self.text_lines[s_index])
        elif s_index != None and e_index != None: # Prints text lines from s_index to e_index
            for index in range(s_index, e_index):
                print(self.text_lines[index])
        
            
    def get_input(self, prompt = "Enter Option >>> ", default = None):
        """Waits for an input into the terminal. Sets the input variable to 
        the imput collected from the user and then returns input.

        Args:
            prompt (string, optional): Prompt displayed while waiting for input. 
            Defaults to "Enter Option >>> ".
            
        Returns:
            string: Input recieved from user
        """
        self.input = input(prompt)
        # Default Value if no input entered
        if self.input == '' and default != None:
            self.input = default
        return self.input
    
    def translate_input(self):
        """Translates input into a message usable by the handler. Returns the message.

        Returns:
            string: message tansated from the input
        """
        if self.input == 'Quit':
            self.message = '_quit_app><'
            return self.message
            
    def getMessage(self):
        """Returns message variable

        Returns:
            string: String contained within the message variable
        """
        return self.message