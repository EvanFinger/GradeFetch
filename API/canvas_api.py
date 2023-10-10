from canvasapi import Canvas
import APP.user_buffer

class canvas_api:
    
    canvas = None
    user = None
    
    # Account Information
    user_name = ""
    user_id = 0
    api_url = ""
    api_token = ""
    num_courses = 0
    
    # Fetched Data
    courses = []
    
    
    
    def LoadCanvasProfile(self,API_URL, API_TOKEN):
        self.canvas = Canvas(API_URL, API_TOKEN)
        self.user = self.canvas.get_current_user()
        
        self.user_name = self.user.name
        self.user_id = self.user.id
        self.api_url = API_URL
        self.api_token = API_TOKEN
        
        
                
    def UnloadCanvasProfile(self):
        self.canvas = None
        self.user = None
        self.user_name = ""
        self.user_id = 0
        self.api_url = ""
        self.api_token = ""
        
    def Fetch(self):
        self.LoadCourses()
        
    def LoadCourses(self):
        for course in self.canvas.get_courses():
            self.courses.append(course)    
    
    
    
class FetchedCourse:
    groups = []
    final_grade = 0.0
    total_weight = 0.0
    
    def FetchGrades(self):
        pass
    
class FetchedGroup:
    assignments = []
        
    
    
class FetchedAssignment:
    pass
        