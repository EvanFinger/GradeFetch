from canvasapi import canvas

from assignment_info import AssignmentInfo

class AssignmentGroup:

    uid = 0
    gid = 0
    assignments = []
    name = ""
    points_possible = 0
    score = 0
    grade_percent = -1.
    weight_on_final = 0.

    def __init__(self, uid, group, assignments):
        self.uid = uid
        self.group = group
        for assignment in assignments:
            self.assignments.append(AssignmentInfo(self.uid, assignment))

    def __init_variables__(self):
        self.name = self.group.name
        self.gid = self.group.id

        for assignment in self.assignments:
            if assignment.score >= 0:
                self.points_possible += assignment.points_possible
                self.score += assignment.score
        self.grade_percent = self.score / self.points_possible
        self.weight_on_final = self.group.group_weight

    def print(self):
        print("----------------------------------")
        print(self.name + str(self.weight_on_final) + "% of final")
        print("----------------------------------")
        print("uid : " + self.uid)
        print("gid : " + self.gid)
        print("size : " + str(len(self.assignments)))
        print("pts possible : " + str(self.points_possible))
        print("group score : " + str(self.score))
        print(str(self.grade_percent) + "%")
