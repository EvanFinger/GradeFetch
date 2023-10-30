from canvasapi import Canvas
from tqdm import tqdm

from Screens.display import Display, handler

Handler = handler()

while not Display.empty():
    
    Display.top().print_text()
    
    Display.top().get_input()
    
    Display.top().translate_input()
    
    Handler.handle(Display.top().getMessage())










# 4511~4s8DAnuzIEWSRTXryIYItXlkWscvzT0ijh9SlxlsnBRlUGaj7I0Ds7AFVaYAOadG EVAN
# 4511~04TztVL41oTJOVWWqriHtG3Jli6OUQxeirOAt902dDZtgkmIqRRD21Pzu9kzGLuZ MAX

# API_URL = "https://canvas.vt.edu"  # vt canvas API url
# API_KEY = input()  # Evan Finger Canvas API token

# with open("app_data/saved_keys.txt", "r+") as file:
#     if API_KEY not in file:
#         file.write(API_KEY)

# canvas = Canvas(API_URL, API_KEY)

# c_user = canvas.get_current_user()  # fetches current canvas user
# u_enrollment_list = c_user.get_enrollments()  # fetches current user's enrollment data
# u_course_list = [*canvas.get_courses()]  # fetches the current user's courses

# gradebook_courses = []

# with tqdm(u_course_list, ncols=100, colour='red', desc='Fetching Courses... ', leave=False) as pbar:
#     for course in pbar:
#         pbar.desc = course.name
#         gradebook_courses.append(
#             CourseGradebook(
#                 c_user.id,
#                 course
#             )
#         )

# for course in gradebook_courses:
#     course.print()




