from canvasapi import Canvas
from tqdm import tqdm
import os
import APP.user_buffer

class canvas_api:
    
    canvas = None
    """Canvas object from canvasapi. Communicates with the API to 'fetch' the data
    """
    user = None
    """(User) Canvas user object sotring the current user's canvas profile
    """
    # Account Information
    user_name = ""
    """(string) User's canvas username from user
    """
    user_id = 0
    """(string) User's canvas userid from user
    """
    api_url = ""
    """(string) URL fed to canvas to link to the proper API
    """
    api_token = ""
    """(string) TOKEN which specifies to the API the correct account to get data from
    """
    num_courses = 0
    """(int) the number of courses saved in the courses dictionary
    """
    
    # Fetched Data
    courses = {}
    """(dict) Dictionary containing each of the user's courses. Begins filled with native formatted course
        objects. These are then replaced with course objects created by this program
    """
    
    
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
        """Deletes all the active variables in the canvas_api object
        """
        self.canvas = None
        self.user = None
        self.user_name = ""
        self.user_id = 0
        self.api_url = ""
        self.api_token = ""
        
    def loadProfileData(self):
        with tqdm(list(self.courses), ncols=100, colour='red', desc='Fetching Courses... ', leave=False) as progBar:
            for key in progBar:
                # Initialize a new Course object to store course data
                course_obj = Course(self.courses[key]) 
                
                
                # Get credit hour value for the course from user 
                print("\nENTER COURSE CREDIT HOURS (Press enter if course does not contribute to GPA, we will ignore it!)")
                print('This can be edited later, so dont worry if you make a mistake!')
                in_ = input(self.courses[key].name + '\n>>> ')
                if in_ == '':
                    course_obj.credit_hours = -1
                else:
                    try:
                        course_obj.credit_hours = int(in_)
                    except(Exception):
                        print("INVALID ENTRY. ENTRY MUST BE AN INTEGER!!")
                os.system('cls')
                
                # If course is chosen to be ignored, it is removed from the system
                if course_obj.credit_hours == -1:
                    del self.courses[self.courses[key].name]
                    print(course_obj.api_form.name + ' IGNORED')
                else:
                    self.courses[self.courses[key].name] = course_obj
                    print(course_obj.api_form.name + ' INCLUDED')
            print(self.courses)
            input()
                
        
class Course:
    
    def __init__(self, course_api):
        
    # Course in API format
        self.api_form = course_api
        
    # List Items
        self.AssignmentGroups = {}
        
    # Course Data
        self.final_grade = None
        self.course_weight = -1  # defaults to 1
        self.credit_hours = -1   # defaults to -1

class AssignmentGroup:
    """A class containing relevant data from the canvas API AssignmentGroup objects.
    Formatted to work within the program.
    """
    
    def __init__(self, group_api):
        
    # Group in API format
        self.api_form = group_api
        """(Assignment) The assignment group in its native form from the API
        """
        
    # List Items
        self.Assignments = {} 
        """(dict) contains all assignments (formatted) from the assignment group
        """
    
    # Group Data
        self.id = None  
        """(int) identification number for the group sourced from canvas.
        """
        self.name = ''
        """(string) name of the group as seen in canvas.
        """
        self.possible_pts = 0
        """(int) number of points possible in the assignment group.
        """
        self.earned_pts = 0.0
        """(float) number of points earned by the user in the assignment group.
        """
        self.group_weight = 0.0
        """(float) weight of the group when calculating parent course's final grade.
        """
        self.has_graded_assignment = False
        """(boolean) True if assignmnet group contains a graded submission. False otherwise.
        """
    