from canvasapi import Canvas
from tqdm import tqdm
import os, time
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
        ## In case courses exist that are inaccessable or hidden/deleted
        ## Skips over courses without a name attribute
        for course in [*self.canvas.get_courses()]:
            try:
                course.name
            except(Exception):
                pass
            else:
                self.courses[course.id] = course
        
        
                
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
        self.get_course_credits_from_input()
        print(self.courses.values())
        print()
        with tqdm(self.courses.values(), colour='blue', desc='Loading...', leave=False) as course_bar:
            for course in course_bar:
                course_bar.desc = course.root.name # name the progress bar
                assignment_groups_api = course.root.get_assignment_groups()
                
                with tqdm(assignment_groups_api, total=len([*assignment_groups_api]), colour='yellow',desc='Loading..',leave=False) as group_bar:
                    for group in group_bar:
                        group_bar.desc = group.name
                        group_obj = AssignmentGroup(group)
                        for assignment in course.root.get_assignments():
                            if assignment.assignment_group_id == group_obj.root.id:
                                group_obj.Assignments[assignment.name] = assignment
                        
                        
                        with tqdm(group_obj.Assignments.values(), colour='red', desc='Loading.', leave=False) as assignment_bar:
                            for assignment in assignment_bar:
                                assignment_bar.desc = assignment.name
                                assignment = Assignment(assignment)
                                time.sleep(0.01)
                        course.AssignmentGroups[group.name] = AssignmentGroup(group)
                                
    def get_course_credits_from_input(self):
        """Prompts the user for input. Asks for credit value of the course object passed
        through course_obj.

        Args:
            course_obj (Course): Course object containing data on the course
            key (string): key for locating the correct course from self.courses
        """
        # Initialize Function-Wide Variables
        ignored_courses = {}
        included_courses = {}
        
        with tqdm(list(self.courses), ncols=100, colour='red', desc='Progress: ', leave=False) as progBar:
            for key in progBar:
                # Initialize a new Course object to store course data
                course_obj = Course(self.courses[key]) 
                print(key)
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
                    ignored_courses[self.courses[key].name] = course_obj
                    print('\033[31m' + course_obj.root.name + ' IGNORED\033[0m')
                else:
                    included_courses[self.courses[key].name] = course_obj
                    print('\033[32m' + course_obj.root.name + ' INCLUDED\033[0m')
                #print(self.courses)
        # Allow user to check entries and make sure no mistakes were made. 
        os.system('cls')
        print('These courses WILL be used ->')
        print('COURSE NAME   [CREDITS]\033[32m')  
        # Display all INCLUDED courses
        for key in included_courses.keys():
            print(included_courses[key].root.name + f'  [{included_courses[key].credit_hours}]')
        print('\033[0m')
        print('These courses WILL NOT be used ->\033[31m')
        # Display all IGNORED courses
        for key in ignored_courses.keys():
            print(ignored_courses[key].root.name)
        print('\033[37m')
        print('Is this CORRECT? [Y/N]')
        cont = True
        # Get input (Y/N)
        while cont:
            match input('>>> '):
                case 'Y': # If 'Y' overrides self.courses with newly created Course objects
                    self.courses = included_courses
                    del ignored_courses
                    cont = False
                case 'N': # If 'N', recursively call function to redo entries
                    self.get_course_credits_from_input() 
                    cont = False
                case _:
                    pass
        
    def processProfileData(self):
        
        
class Course:
    
    def __init__(self, course_api):
        
    # Course in API format
        self.root = course_api
        
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
        self.root = group_api
        """(AssignmentGroup) The assignment group in its native form from the API
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
class Assignment:
    
    def __init__(self, assignment_api):
        pass
        # Assignment in API format
        self.root = assignment_api
        """(Assignment) The assignment in its native form from the API
        """
        
        # Assignment Data
        self.submission = None
        """(Submission) Graded submission for the assignmnet if any
        """
        
        self.id = 0
        """(int) identification number for the assignment generated by canvas
        """
        
        self.name = ''
        """(string) name of the assignment as seen on canvas website
        """
        
        self.possible_pts = 0
        """(int) number of points possible for the assignment
        """
        
        self.earned_pts = 0
        """(int) number of points earned by the user on the assignment
        """
        
        self.grade = 0.0
        """(float) overall grade on the assignment
        """
        
        self.is_Graded = False
        """(boolean) true if assignment has a graded submission, false otherwise.
        """