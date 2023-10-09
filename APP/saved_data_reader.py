from xml.dom import minidom
from user_buffer import UserData

path = str('GradeFetch\\app_data\\saved_account_data\\u_222254.xml')

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
   # print(return_dict)
    return return_dict

data = UserData

for tag in mytree.getElementsByTagName('Semester'):
    data.semesters.append(LoadToDict(tag))
    
for tag in mytree.getElementsByTagName('Course'):
    data.courses.append(LoadToDict(tag))
    
for tag in mytree.getElementsByTagName('Group'):
    data.groups.append(LoadToDict(tag))
    
for tag in mytree.getElementsByTagName('Assignment'):
    data.assignments.append(LoadToDict(tag))

# print(LoadToDict(tagname[0]))


