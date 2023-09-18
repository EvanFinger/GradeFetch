from canvasapi import canvas


class AssignmentInfo:

    uid = 0
    name = ""
    points_possible = 0
    score = 0
    grade_letter = ""
    grade_percent = 0.
    grade_ratio = ""

    def __init__(self, uid, assignment):
        self.uid = uid
        self.assignment = assignment
        self.submission = assignment.get_submission(uid)
        self.__init_variables__()

    def __init_variables__(self):
        self.name = self.assignment.name
        self.points_possible = self.assignment.points_possible

        if self.submission.workflow_state == "graded":
            try:
                self.score = self.submission.score
            except:
                pass