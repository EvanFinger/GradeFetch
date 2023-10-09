from xml.dom import minidom
from user_buffer import UserData

path = str('GradeFetch\\app_data\\saved_account_data\\u_222254.xml')

mytree = minidom.parse(path)
tagname = mytree.getElementsByTagName('Assignment')

def LoadToDict(tag):
    return_dict = {}
    for attribute in tag.attributes.items():
        return_dict[attribute[0]] = attribute[1]
    return return_dict

data = UserData

for tag in mytree.getElementsByTagName('Semester'):
    data.AddSemesterFromDict(data, LoadToDict(tag))
    
for tag in mytree.getElementsByTagName('Course'):
    data.AddCourseFromDict(data, LoadToDict(tag))
    
for tag in mytree.getElementsByTagName('Group'):
    data.AddGroupFromDict(data, LoadToDict(tag))
    
for tag in mytree.getElementsByTagName('Assignment'):
    data.AddAssignmentFromDict(data, LoadToDict(tag))

print(tagname[0].attributes.items())
print(LoadToDict(tagname[0]))


