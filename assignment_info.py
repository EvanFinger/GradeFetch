from canvasapi import canvas


class AssignmentInfo:

    uid = 0

    def __init__(self, uid, assignment):
        self.name = ""
        self.points_possible = 0
        self.score = -1
        self.grade_percent = -1.
        self.grade_ratio = "-/"

        self.uid = uid
        self.assignment = assignment
        self.submission = assignment.get_submission(uid)
        self.__init_variables__()

    def __init_variables__(self):
        # print("_INIT_ASSIGNMENT_")
        self.name = self.assignment.name
        self.points_possible = self.assignment.points_possible

        if self.submission.workflow_state == "graded":
            try:
                self.score = self.submission.score
                if self.points_possible > 0:
                    self.grade_percent = (self.score / self.points_possible) * 100
                else:
                    self.grade_percent = 100 * self.score
                self.grade_ratio = str(self.score) + "/" + str(self.points_possible)
            except:
                self.grade_ratio = str(self.grade_ratio) + str(self.points_possible)
                pass


