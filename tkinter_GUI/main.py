import tkinter as tk

import program_data as PD
from login import LoginWidgets
from utils import _from_rgb

screen_stack = [] 

class MAIN_APP():
        
       
    
    def __init__(self) -> None:
        
        PD.tk_colors.append(_from_rgb([72, 52, 52]))
        PD.tk_colors.append(_from_rgb([107, 79, 79]))
        PD.tk_colors.append(_from_rgb([238, 214, 196]))
        PD.tk_colors.append(_from_rgb([255, 243, 228]))

        
        self.app = tk.Tk()
        self.app.title = 'Test'
        self.app.geometry('800x600')
        
        self.LW = LoginWidgets()
        
        self.LW.show_title(self.app)
        self.LW.s_login_buttons(self.app)
        
        self.app.mainloop()
        
APP = MAIN_APP()