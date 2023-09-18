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
for course in gradebook_courses:
    course.print()




