import tkinter as tk
from utils import _from_rgb

class MAIN_APP:
    def __init__(self) -> None:
        
        tk_col_1 = _from_rgb([72, 52, 52])
        tk_col_2 = _from_rgb([107, 79, 79])
        tk_col_3 = _from_rgb([238, 214, 196])
        tk_col_4 = _from_rgb([255, 243, 228])

        
        self.app = tk.Tk()
        self.app.geometry('400x300')
        self.app.maxsize(400, 300)
        self.app.config(bg= tk_col_3)
        
        # LABEL FRAME
        self.mm_text_frame = tk.Frame(self.app, bg=tk_col_3)
        
        self.title = tk.Label(self.mm_text_frame, text= 'Grade Fetch', font=('Lucida Calligraphy', 24), bg= tk_col_3)
        self.title.grid()
        
        self.version = tk.Label(self.mm_text_frame, text= 'version 0.1', font=('Lucida Calligraphy', 12), bg= tk_col_3)
        self.version.grid()
        
        self.mm_text_frame.pack(pady=10)
        # END LABEL FRAME
        
        # BUTTON FRAME        
        self.new_profile_btn = tk.Button(self.app, text= 'New Profile', font=('Lucida Calligraphy', 16), bg= tk_col_2)
        self.new_profile_btn.place(x=40, y=100, width=175, height=60)
        
        self.load_profile_button = tk.Button(self.app, text= 'Load Profile', font=('Lucida Calligraphy', 16), bg= tk_col_2)
        self.load_profile_button.place(x=115, y=140, width=175, height=60)
        
        self.close_button = tk.Button(self.app, text= 'Exit', font=('Lucida Calligraphy', 16), bg= tk_col_1)
        self.close_button.place(x=190, y=180, width=175, height=60)
        # END BUTTON FRAME
        
        self.app.mainloop()
        
    def test(self):
        print('test')
        
        
APP = MAIN_APP()