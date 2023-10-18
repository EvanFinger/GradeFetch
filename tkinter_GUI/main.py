import tkinter as tk

import program_data as PD
from main_menu import MainMenu
from utils import _from_rgb


class MAIN_APP():
        
    screen_stack = []    
    
    def __init__(self) -> None:
        
        PD.tk_colors.append(_from_rgb([72, 52, 52]))
        PD.tk_colors.append(_from_rgb([107, 79, 79]))
        PD.tk_colors.append(_from_rgb([238, 214, 196]))
        PD.tk_colors.append(_from_rgb([255, 243, 228]))

        
        self.app = tk.Tk()
        
        self.screen_stack.append(MainMenu(self.app))
        
APP = MAIN_APP()