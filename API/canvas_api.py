from canvasapi import Canvas
from tqdm import tqdm
import os
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
    
    
    
    def LoadCanvasUser(self,API_URL, API_TOKEN):
        self.canvas = Canvas(API_URL, API_TOKEN)
        self.user = self.canvas.get_current_user()
        
        self.user_name = self.user.name
        self.user_id = self.user.id
        self.api_url = API_URL
        self.api_token = API_TOKEN
        
        self.courses = {}
        for course in [*self.canvas.get_courses()]:
            self.courses[course.name] = course
        
        
                
    def UnloadCanvasProfile(self):
        self.canvas = None
        self.user = None
        self.user_name = ""
        self.user_id = 0
        self.api_url = ""
        self.api_token = ""
        
    def loadProfileData(self):
        with tqdm(self.courses.values(), ncols=100, colour='red', desc='Fetching Courses... ', leave=False) as progBar:
            for course_api in progBar:
                # Initialize a new Course object to store course data
                course_obj = Course(course_api) 
                
                # Get credit hour value for the course from user 
                print("\nENTER COURSE CREDIT HOURS (Press enter if course does not contribute to GPA, we will ignore it!)")
                print('This can be edited later, so dont worry if you make a mistake!')
                course_obj.credit_hours = input(course_api.name + '\n>>> ')
                os.system('cls')
                
                # If course is chosen to be ignored, it is removed from the system
                if course_obj.credit_hours == -1:
                    self.courses[course_api.name] = None
                else:
                    pass
                
        
class Course:
    
    def __init__(self, course_api):
        
    # Course in API format
        self.api_form = course_api
        
    # List Items
        self.AssignmentGroups = {}
        
    # Course Data
        self.final_grade = None
        self.course_weight = -1  # defaults to 1
        self.credit_hours = 1   # defaults to 1

class AssignmentGroup:
    
    def __init__(self, group_api):
        
    # Group in API format
        # 'api_form' is the Assignment group in its native format from the API
        self.api_form = group_api
        
    # List Items
        # 'Assignments' is a dictionary containing each assignment in the group
        self.Assignments = {} 
    
    # Group Data
        # 'id' is an identification label for the group
        self.id = None  # 'type' = int
        # 'name' is a string containing the name of the group as seen in Canvas
        self.name = ''  # 'type' = string
        # 'possible_points' is an integer containing the total possible points in group
        self.possible_pts = 0  # 'type' = int
        # 'earned_pts' is a float containing the total earned points in group
        self.earned_pts = 0.0  # 'type' = float
        # 'group_weight' is a float containing the groups effective weight
        self.group_weight = 0.0  # 'type' = float
        # 'has_graded_assignment' is a boolean representing the presence of a graded
        # assignment in the group. Determines whether or not to use the group in final grade
        self.has_graded_assignment = False  # 'type' = boolean
    