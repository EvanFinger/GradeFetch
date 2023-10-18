import tkinter as tk

import program_data as PD


class WINDOW:
    
    def __init__(self, root, title, geometry, message) -> None:
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        tk.Label(self.root, text= message)
        pass


class MainMenu(WINDOW):
    
    def __init__(self, parent) -> None:
        
        super().__init__(parent, 'TEST', '400x300', 'TESTING')
        
        self.mm_text_frame = tk.Frame(self.root, bg=PD.tk_colors[3])
        
        self.title = tk.Label(self.mm_text_frame, text= 'Grade Fetch', font=('Lucida Calligraphy', 24), bg= PD.tk_colors[3])
        self.title.grid()
        
        self.version = tk.Label(self.mm_text_frame, text= 'version 0.1', font=('Lucida Calligraphy', 12), bg= PD.tk_colors[3])
        self.version.grid()
        
        self.mm_text_frame.pack(pady=10)
        # END LABEL FRAME
        
        # BUTTON FRAME        
        self.new_profile_btn = tk.Button(self.root, text= 'New Profile', font=('Lucida Calligraphy', 16), bg= PD.tk_colors[2], command= self.to_new_profile)
        self.new_profile_btn.place(x=40, y=100, width=175, height=60)
        
        self.load_profile_button = tk.Button(self.root, text= 'Load Profile', font=('Lucida Calligraphy', 16), bg= PD.tk_colors[2])
        self.load_profile_button.place(x=115, y=140, width=175, height=60)
        
        self.close_button = tk.Button(self.root, text= 'Exit', font=('Lucida Calligraphy', 16), bg= PD.tk_colors[2], command= self.quit_app)
        self.close_button.place(x=190, y=180, width=175, height=60)
        # END BUTTON FRAME
        
        self.root.mainloop()
        
    def to_new_profile(self):
        self.mm_text_frame.destroy()
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