from canvasapi import Canvas


# 4511~cpbf5ZYMyXXDSlU5RKjDD6ZkqLfQl6aULrxe7BYdJvV35q5EtrtWLZQcepxSqgw6
API_URL = "https://canvas.vt.edu"
API_KEY = "4511~4s8DAnuzIEWSRTXryIYItXlkWscvzT0ijh9SlxlsnBRlUGaj7I0Ds7AFVaYAOadG"

canvas = Canvas(API_URL, API_KEY)
user = canvas.get_current_user()
enrollments = user.get_enrollments()
enrollment = enrollments[2]
course = canvas.get_course(enrollment.course_id)
assignment_groups = course.get_assignment_groups()

for group in assignment_groups:
    print(group.id)
    print(group.group_weight)
    print('===============================================================')
assignments = course.get_assignments()
for element in assignments:
    assignment = element

    submission = assignment.get_submission(canvas.get_current_user().id)

    print(course.name)
    print(assignment.name)
    print(assignment.assignment_group_id)
    print(assignment.points_possible)
    if submission.workflow_state == "graded":
        try:
               print(submission.score)
        except:
               print("none")
    print('--------------------------------------')






