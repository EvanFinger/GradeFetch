from canvasapi import Canvas


from assignment_group import AssignmentGroup
from tqdm import tqdm

class CourseGradebook:

    uid = 0

    def __init__(self, uid, course):
        self.groups = []
        self.final_grade = 0
        self.course_weight = 0.
        self.course = course
        self.uid = uid
        self.course_assignments = self.course.get_assignments()  # fetching assignments from the course
        self.course_assignment_groups = []
        for grp in self.course.get_assignment_groups():
            self.course_assignment_groups.append(grp)
        with tqdm(self.course_assignment_groups, ncols=100, colour='blue',  desc='Fetching Assignment Groups... ', leave=False) as pbar:
            for grp in pbar:  # Sorts the assignments with their respective group
                pbar.desc = grp.name
                temp = []  # list that holds the assignments to be placed in a group
                for assignment in self.course_assignments:
                    if assignment.assignment_group_id == grp.id:
                        temp.append(assignment)
                self.groups.append(AssignmentGroup(uid, grp, temp))


        self.__calc_final__()

    def __calc_final__(self):
        for group in self.groups:
            self.course_weight += (group.active_weight_on_final / 100)
        if self.course_weight > 0.0:
            for group in self.groups:
                self.final_grade += (group.grade_percent / 100.0) * (group.active_weight_on_final / 100.0)
            self.final_grade /= self.course_weight
        else:
            pts_possible = 0
            for group in self.groups:
                self.final_grade += group.score
                pts_possible += group.points_possible
            if pts_possible > 0:
                self.final_grade /= pts_possible
            else:
                self.final_grade = -1

    def print(self):
        print('///////////////////////////////////////////////////' + '\n')
        print(self.course.name + ' ' + str(self.course_weight) + ' ' + str(self.final_grade) + '%' + '\n')
        print('///////////////////////////////////////////////////')

        for group in self.groups:
            group.print()


