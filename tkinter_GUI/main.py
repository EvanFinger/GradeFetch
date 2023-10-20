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
        self.root.geometry('800x600')
        
        self.mm_text_frame = tk.Frame(master= self.root, bg=self.color_3) 
        self.title = tk.Label(
            master= self.mm_text_frame, 
            text= 'Grade Fetch', 
            font=('Lucida Calligraphy', 24), 
            bg= self.color_3
            )
        self.title.grid()
        self.version = tk.Label(
            master= self.mm_text_frame, 
            text= 'version 0.1', 
            font=('Lucida Calligraphy', 12), 
            bg= self.color_3
            )
        self.version.grid()           
        self.mm_text_frame.pack(pady=10)
        
        new_profile_btn = tk.Button(
            master= self.root, 
            text= 'New Profile', 
            font=('Lucida Calligraphy', 16),
            bg= self.color_3, 
            command= self.to_new_profile)
        new_profile_btn.place(x=40, y=100, width=175, height=60)
        load_profile_button = tk.Button(
            master= self.root, 
            text= 'Load Profile', 
            font=('Lucida Calligraphy', 16), 
            bg= self.color_3)
        load_profile_button.place(x=115, y=140, width=175, height=60)
        close_button = tk.Button(
            master= self.root, 
            text= 'Exit', 
            font=('Lucida Calligraphy', 16), 
            bg= self.color_3, 
            command= self.quit_app)
        close_button.place(x=190, y=180, width=175, height=60)
        
        self.root.mainloop()
    
    def to_new_profile(self):
        self.d_title()
        self.new_profile_btn.destroy()
        self.load_profile_button.destroy()
        self.close_button.destroy()
            
    def quit_app(self):
        """
        Button Command
        ::Trigger -> close_button is pressed
        ::Function -> quits the app from main menu
        """
        self.root.quit()
        
APP = MAIN_APP()