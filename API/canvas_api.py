from canvasapi import Canvas

class canvas_api:
    
    canvas = None
    user = None
    
    # Account Information
    user_name = ""
    user_id = 0
    
    
    
    def LoadCanvasProfile(self,API_URL, API_TOKEN):
        self.canvas = Canvas(API_URL, API_TOKEN)
        self.user = self.canvas.get_current_user()
        
        self.user_name = self.user.name
        self.user_id = self.user.id
        