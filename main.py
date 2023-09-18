from canvasapi import Canvas
from collections import deque

from course_gradebook import CourseGradebook

API_URL = "https://canvas.vt.edu" # vt canvas API url
API_KEY = "4511~4s8DAnuzIEWSRTXryIYItXlkWscvzT0ijh9SlxlsnBRlUGaj7I0Ds7AFVaYAOadG" # Evan Finger Canvas API token

canvas = Canvas(API_URL, API_KEY)

c_user = canvas.get_current_user()  # fetches current canvas user
u_enrollment_list = c_user.get_enrollments()  # fetches current user's enrollment data
u_course_list = canvas.get_courses()  # fetches the current user's courses

gradebook_courses = []

for course in u_course_list:
    gradebook_courses.append(CourseGradebook(c_user.id, course))

    assignment_list = course.get_assignments()
    assignment_groups = course.get_assignment_groups()
    for group in assignment_groups:
        total_group_points = 0
        max_group_points = 0
        use_for_final = False

        for assignment in assignment_list:
            if assignment.assignment_group_id == group.id:
                try:
                    max_group_points += assignment.points_possible
                except:
                    pass

                submission = assignment.get_submission(canvas.get_current_user().id)
                if submission.workflow_state == "graded":
                    try:
                        total_group_points += submission.score
                    except:
                        pass
                else:
                    try:
                        max_group_points -= assignment.points_possible
                    except:
                        pass

        print("-------------------------------")
        print(group.name + " " + str(group.group_weight) + "% of final grade")
        print(str(total_group_points) + "/" + str(max_group_points))
    print("FINAL GRADE: ")


