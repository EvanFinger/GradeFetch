from canvasapi import Canvas

from assignment_group import AssignmentGroup


class CourseGradebook:

    uid = 0
    groups = []

    def __init__(self, uid, course):
        self.course = course
        self.uid = uid
        self.course_assignments = self.course.get_assignments()  # fetching assignments from the course

        for grp in self.course.get_assignment_groups():
            temp = []
            for assignment in self.course_assignments:
                if assignment.assignment_group_id == grp.id:
                    temp.append(assignment)
            self.groups.append(AssignmentGroup(uid, grp, temp))

