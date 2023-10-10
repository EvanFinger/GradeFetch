from xml.dom import minidom
import user_buffer

path = str('app_data\\saved_account_data\\u_222254.xml')

mytree = minidom.parse(path)
tagname = mytree.getElementsByTagName('Assignment')
def LoadToDict(tag):
    return_dict = {}
    return_dict['id'] = tag.attributes.item(0).value
    for element in tag.childNodes:
        try:
            
            return_dict[element.localName] = element.firstChild.nodeValue
        except:
            pass
    return return_dict


for semester_tag in mytree.getElementsByTagName('Semester'):
    user_buffer.semesters.append(semester_tag.getAttribute('id'))
    if semester_tag.getAttribute('id') == 'sem_1':
        user_buffer.active_semester = LoadToDict(semester_tag)
        
        for course_tag in semester_tag.getElementsByTagName('Course'):
            user_buffer.courses.append(LoadToDict(course_tag))
            user_buffer.groups.append([])
            user_buffer.assignments.append([])
            
            for group_tag in course_tag.getElementsByTagName('Group'):
                user_buffer.groups[len(user_buffer.groups) - 1].append(LoadToDict(group_tag))
                user_buffer.assignments[len(user_buffer.assignments) - 1].append([])
                
                for assignment_tag in group_tag.getElementsByTagName('Assignment'):
                    user_buffer.assignments[len(user_buffer.assignments) - 1][len(user_buffer.assignments[len(user_buffer.assignments) - 1]) - 1].append(LoadToDict(assignment_tag))


# print(LoadToDict(tagname[0]))

