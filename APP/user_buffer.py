class UserData:
    name = ''
    id = ''
    
    
    _semesters =  []
    _courses = []
    _groups = []
    _assignments = []
    
    def AddSemesterFromDict(self, semester_dict = {}):
        self._semesters.append(_semester)
        wk_sem = self._semesters[len(self._semesters) - 1]
        
        wk_sem.id = semester_dict['id']
        wk_sem.start_date = semester_dict['start_date']
        wk_sem.end_date = semester_dict['end_date']
        wk_sem.credit_hours_taken = semester_dict['credit_hours']
        wk_sem.gpa = semester_dict['gpa']
    
    def GetSemesters(self):
        return self._semesters
    
    def AddCourseFromDict(self, course_dict = {}):
        self._courses.append(_course)
        wk_course = self._courses[len(self._courses) - 1]
        
        wk_course.id = course_dict['id']
        wk_course.name = course_dict['name']
        wk_course.credit_hours = course_dict['credit_hours']
        wk_course.final_grade = course_dict['final_grade']
        
    def GetCourses(self):
        return self._courses
    
    def AddGroupFromDict(self, group_dict = {}):
        self._groups.append(_group)
        wk_grp = self._groups[len(self._groups) - 1]
        
        wk_grp.id = group_dict['id']
        wk_grp.name = group_dict['name']
        wk_grp.points_earned = group_dict['points_earned']
        wk_grp.points_possible = group_dict['points_possible']
        wk_grp.weight = group_dict['weight']
        
    def GetGroups(self):
        return self._groups
    
    def AddAssignmentFromDict(self, assignment_dict = {}):
        self._assignments.append(_assignment)
        wk_asgn = self._assignments[len(self._assignments) - 1]
        
        wk_asgn.id = assignment_dict['id']
        wk_asgn.name = assignment_dict['name']
        wk_asgn.points_earned = assignment_dict['points_earned']
        wk_asgn.points_possible = assignment_dict['points_possible']
        
    def GetAssignments(self):
        return self._assignments
    
class _semester:
    id = ''
    start_date = ''
    end_date = ''
    credit_hours_taken = ''
    gpa = ''
    
class _course:
    id = ''
    name = ''
    credit_hours = ''
    final_grade = ''
    
class _group:
    id = ''
    name = ''
    points_earned = ''
    points_possible = ''
    weight = ''
    
class _assignment:
    id = ''
    name = ''
    points_earned = ''
    points_possible = ''
    