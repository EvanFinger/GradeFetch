from canvasapi import canvas
from tqdm import tqdm

from GradeFetch.Source.API.assignment_info import AssignmentInfo

class AssignmentGroup:

    uid = 0

    def __init__(self, uid, group, assignments):
        self.gid = 0
        self.assignments = []
        self.name = ""
        self.points_possible = 0
        self.score = 0
        self.grade_percent = -1.
        self.active_weight_on_final = 0.
        self.posted_weight_on_final = 0.

        self.uid = uid
        self.group = group
        self.posted_weight_on_final = group.group_weight

        with tqdm(assignments, desc='Fetching Assignments... ', ncols=100, colour='yellow',  leave=False) as pbar:
            for assignment in pbar:
                pbar.desc = assignment.name
                self.assignments.append(AssignmentInfo(self.uid, assignment))
            pbar.close()
        self.__init_variables__()

    def __init_variables__(self):
        # print("_INIT_GROUP_")
        self.name = self.group.name
        self.gid = self.group.id

        for assignment in self.assignments:
            if assignment.score >= 0:
                self.points_possible += assignment.points_possible
                self.score += assignment.score

        if self.points_possible > 0:
            self.grade_percent = (self.score / self.points_possible) * 100
            self.active_weight_on_final = self.posted_weight_on_final



    def print(self):
        print("----------------------------------")
        print(self.name + ' ' + str(self.posted_weight_on_final) + "% of final")
        print("----------------------------------")
        print("uid : " + str(self.uid))
        print("gid : " + str(self.gid))
        print("active weight : " + str(self.active_weight_on_final) + '%')
        print("size : " + str(len(self.assignments)))
        print("pts possible : " + str(self.points_possible))
        print("group score : " + str(self.score))
        print(str(self.grade_percent) + "%")
