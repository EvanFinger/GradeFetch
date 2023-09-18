from canvasapi import Canvas

from assignment_group import AssignmentGroup


class CourseGradebook:

    uid = 0

    def __init__(self, uid, course):
        self.groups = []

        self.course = course
        self.uid = uid
        self.course_assignments = self.course.get_assignments()  # fetching assignments from the course
        self.course_assignment_groups = self.course.get_assignment_groups()

        for grp in self.course_assignment_groups:  # Sorts the assignments with their respective groups
            temp = []                                    # list that holds the assignments to be placed in a group
            for assignment in self.course_assignments:
                if assignment.assignment_group_id == grp.id:
                    temp.append(assignment)
            self.groups.append(AssignmentGroup(uid, grp, temp))

    def __calc_final__(self):
        pass

    def print(self):
        print('///////////////////////////////////////////////////' + '\n')
        print(self.course.name + '\n')
        print('///////////////////////////////////////////////////')

        for group in self.groups:
            group.print()


