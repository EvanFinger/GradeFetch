import tkinter as tk

import program_data as PD



class LoginWidgets:
    
    mm_text_frame = tk.Frame
    title = tk.Label
    version = tk.Label

    def show_title(self, root):
        mm_text_frame = tk.Frame(root, bg=PD.tk_colors[3])
            
        title = tk.Label(mm_text_frame, text= 'Grade Fetch', font=('Lucida Calligraphy', 24), bg= PD.tk_colors[3])
        title.grid()
            
        version = tk.Label(mm_text_frame, text= 'version 0.1', font=('Lucida Calligraphy', 12), bg= PD.tk_colors[3])
        version.grid()
            
        mm_text_frame.pack(pady=10)

    def d_title(self):
        self.mm_text_frame.destroy()
        
    def s_login_buttons(self, root):
        new_profile_btn = tk.Button(root, text= 'New Profile', font=('Lucida Calligraphy', 16), bg= PD.tk_colors[2], command= self.to_new_profile)
        new_profile_btn.place(x=40, y=100, width=175, height=60)
            
        load_profile_button = tk.Button(root, text= 'Load Profile', font=('Lucida Calligraphy', 16), bg= PD.tk_colors[2])
        load_profile_button.place(x=115, y=140, width=175, height=60)
            
        close_button = tk.Button(root, text= 'Exit', font=('Lucida Calligraphy', 16), bg= PD.tk_colors[2], command= self.quit_app)
        close_button.place(x=190, y=180, width=175, height=60)


        
        
            
            
            
            
            
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