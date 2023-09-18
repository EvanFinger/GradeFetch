from canvasapi import canvas

from assignment_info import AssignmentInfo

class AssignmentGroup:

    uid = 0


    def __init__(self, uid, group, assignments):
        self.gid = 0
        self.assignments = []
        self.name = ""
        self.points_possible = 0
        self.score = 0
        self.grade_percent = -1.
        self.weight_on_final = 0.

        self.uid = uid
        self.group = group
        for assignment in assignments:
            self.assignments.append(AssignmentInfo(self.uid, assignment))
        self.__init_variables__()

    def __init_variables__(self):
        print("_INIT_GROUP_")
        self.name = self.group.name
        self.gid = self.group.id

        for assignment in self.assignments:
            if assignment.score >= 0:
                self.points_possible += assignment.points_possible
                self.score += assignment.score

        if self.points_possible > 0:
            self.grade_percent = (self.score / self.points_possible) * 100
        else:
            self.grade_percent = 100 * self.score
        self.weight_on_final = self.group.group_weight

    def print(self):
        print("----------------------------------")
        print(self.name + str(self.weight_on_final) + "% of final")
        print("----------------------------------")
        print("uid : " + str(self.uid))
        print("gid : " + str(self.gid))
        print("size : " + str(len(self.assignments)))
        print("pts possible : " + str(self.points_possible))
        print("group score : " + str(self.score))
        print(str(self.grade_percent) + "%")
