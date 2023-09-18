from canvasapi import canvas


class AssignmentGroup:

    uid = 0
    assignments = []

    def __init__(self, uid, group, assignments):
        self.uid = uid
        self.group = group
        self.assignments = assignments

