import tkinter as tk

import program_data as PD
from login import LoginWidgets
from utils import _from_rgb

screen_stack = [] 

class MAIN_APP():
        
       
    
    def __init__(self) -> None:
        
        self.color_1 = _from_rgb([72, 52, 52])
        self.color_2 = _from_rgb([107, 79, 79])
        self.color_3 = _from_rgb([238, 214, 196])
        self.color_4 = _from_rgb([255, 243, 228])

        
        self.root = tk.Tk()
        self.root.title = 'Test'
        self.root.geometry('400x300')
        self.root.config(bg= self.color_2)
        
        self.show_main_menu()
        
        self.root.mainloop()
    
    """
    FUNCTION >> show_main_menu
    
    creates and displays the main menu and all objects contained within.
    
    <PACK>(Frame<GRID>(Label, Label), Button, Button, Button)
    """
    def show_main_menu(self):
        self.mm_text_frame = tk.Frame(master= self.root, bg=self.color_2) 
        self.title = tk.Label(
            master= self.mm_text_frame, 
            text= 'Grade Fetch', 
            font=('Lucida Calligraphy', 24), 
            bg= self.color_2
            )
        self.title.grid()
        self.version = tk.Label(
            master= self.mm_text_frame, 
            text= 'version 0.1', 
            font=('Lucida Calligraphy', 12), 
            bg= self.color_2
            )
        self.version.grid()           
        self.mm_text_frame.pack(pady=10)
        
        self.new_profile_btn = tk.Button(
            master= self.root, 
            text= 'New Profile', 
            font=('Lucida Calligraphy', 16),
            bg= self.color_1, 
            command= self.to_new_profile)
        self.new_profile_btn.place(x=40, y=100, width=175, height=60)
        self.load_profile_button = tk.Button(
            master= self.root, 
            text= 'Load Profile', 
            font=('Lucida Calligraphy', 16), 
            bg= self.color_1)
        self.load_profile_button.place(x=115, y=140, width=175, height=60)
        self.close_button = tk.Button(
            master= self.root, 
            text= 'Exit', 
            font=('Lucida Calligraphy', 16), 
            bg= self.color_1, 
            command= self.quit_app)
        self.close_button.place(x=190, y=180, width=175, height=60)
    
    """
    FUNCTION >> to_new_profile
    
    navigates to the new profile screen.
    destroys the main menu.  
    """
    def to_new_profile(self):
        self.new_profile_btn.destroy()
        self.load_profile_button.destroy()
        self.close_button.destroy()
        
        self.show_new_profile_input()
        
    def show_new_profile_input(self):
        self.np_input_frame = tk.Frame(
            master= self.root,
            bg= self.color_2,
        )
        self.np_url_label = tk.Label(
            master= self.np_input_frame,
            text= 'API URL: '
        )
        self.np_url_input = tk.Entry(
            master= self.np_input_frame,
            textvariable= tk.StringVar(master= self.root, value= 'https://canvas.vt.edu')
        )
        self.np_token_label = tk.Label(
            master= self.np_input_frame,
            text= 'API TOKEN'
        )
        self.np_token_input = tk.Entry(
            master= self.np_input_frame,
            textvariable= tk.StringVar(master= self.root, value= 'Enter canvas token (found in canvas settings)')
        )
        self.load_new_profile_button = tk.Button(
            master= self.root,
            text= 'SUBMIT'
        )
        self.np_url_label.grid(column= 0, row= 0)
        self.np_token_label.grid(column= 0, row= 1)
        self.np_url_input.grid(column= 1, row= 0, pady= 2)
        self.np_token_input.grid(column= 1, row= 1, pady= 2)
        self.np_input_frame.pack()
        self.load_new_profile_button.pack()
            
    def quit_app(self):
        """
        Button Command
        ::Trigger -> close_button is pressed
        ::Function -> quits the app from main menu
        """
        self.root.quit()
        
APP = MAIN_APP()