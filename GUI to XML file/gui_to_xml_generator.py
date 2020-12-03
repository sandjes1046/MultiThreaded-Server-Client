
#import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element. """
    rough_string = ElementTree.tostring(elem, encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


''' xml creation functions '''
# create functions to work with the collected data and the appropriate node (top, parent, sibling)
# data will be collected from the GUI

def xml_to_file(tree,filename):
    with open(filename,"w+") as f:
        f.write(prettify(tree))
    return f
'''
# version 1       
def insert_semester(tree,semester_name,semester_year):
    return ElementTree.SubElement(tree, 'semester', {'name':semester_name,'year':semester_year}) #attribs as a dictionary
'''
#version 2
def insert_semester2(tree,semester_name,semester_year):
    semester=ElementTree.SubElement(tree, 'semester')
    
    name=ElementTree.SubElement(semester, 'name')
    name.text=semester_name
    
    year=ElementTree.SubElement(semester, 'year')
    year.text=semester_year  
    return semester
'''
# version 1
def insert_studentInfo(tree,f_name,l_name,student_id,faculty_advisor,adv_date):
      return ElementTree.SubElement(tree, 'studentinfo', {'f_name':f_name,'l_name':l_name,'student_id':student_id,'faculty_advisor':faculty_advisor,'adv_date':adv_date}) #attribs as a dictionary
'''
#version 2
def insert_studentInfo2(tree,f_name,l_name,student_id,faculty_advisor,adv_date):
    studentinfo=ElementTree.SubElement(tree, 'studentinfo')
    
    firstname=ElementTree.SubElement(studentinfo, 'f_name')
    firstname.text=f_name
    
    lastname=ElementTree.SubElement(studentinfo, 'l_name')
    lastname.text=l_name
    
    studentid=ElementTree.SubElement(studentinfo, 'student_id')
    studentid.text=student_id
    
    facultyadvisor=ElementTree.SubElement(studentinfo, 'faculty_advisor')
    facultyadvisor.text=faculty_advisor
    
    st_date=ElementTree.SubElement(studentinfo, 'adv_date')
    st_date.text=adv_date
    
    return studentinfo
'''    
#version 1
def insert_course(semester,course_prefix,course_number,course_section, course_hours):
      return ElementTree.SubElement(semester, 'course', {'prefix':course_prefix,'number':course_number,'section':course_section,'hours':course_hours})
'''
#version 2
def insert_course2(semester,course_number,course_section, course_hours):

    course=ElementTree.SubElement(semester, 'course')
    
    number=ElementTree.SubElement(course, 'number')
    number.text=course_number
    
    section=ElementTree.SubElement(course, 'section')
    section.text=course_section
    
    hours=ElementTree.SubElement(course, 'hours')
    hours.text=course_hours 
    return course

# not used
def insert_courses(semester, courses_list_props):
    ''' each course is a dictionary of prefix,number, section, and hours '''
    courses = [ Element('course', courses_list_props[i]) for i in range(len(courses_list_props)) ]
    semester.extend(courses)
 
       
def insert_notes(tree, note_text):
    ''' each course is a dictionary of prefix,number, section, and hours '''
    notes =ElementTree.SubElement(tree, 'notes')
    notes.text = note_text
    
''' xml Parsing functions '''
# create functions to parse xml files...
'''

# Testing  
if __name__ == "__main__":
    
    advisingtree = ElementTree.Element('advising')
    comment = ElementTree.Comment('Generated for MKQ')
    advisingtree.append(comment)
    
#    studentinfo=insert_studentInfo(advisingtree,"MK","Quweider","007","MKQ","00/00/0000")
    studentinfo=insert_studentInfo2(advisingtree,"MK","Quweider","007","MKQ","11-15-2019")

    # create semester
#    semester0 = insert_semester(advisingtree,"Spring","2020")
    semester1 = insert_semester2(advisingtree,"Fall","2019")
 
    # create semester's courses...variable
    course1 = insert_course2(semester1,"CSCI","4301","Computer Science I","3") 
    course2 = insert_course2(semester1,"CSCI","4390","Computer Science II","3") 
    course3 = insert_course2(semester1,"CSCI","4365","Computer Science III","3") 
 
    # create semester
    semester2 = insert_semester2(advisingtree,"Spring","2020")
    
    # create courses
    course1 = insert_course2(semester2,"CSCI","3301","Computer Science I","3") 
    course2 = insert_course2(semester2,"CSCI","3390","Computer Science II","3") 
    course3 = insert_course2(semester2,"CSCI","3365","Computer Science III","3")
    
     # create semester
    semester3 = insert_semester2(advisingtree,"Summer","2020") 
    
    # creat courses
    course1 = insert_course2(semester3,"CSCI","2301","Computer Science I","3") 
    course2 = insert_course2(semester3,"CSCI","2390","Computer Science I","3") 
    course3 = insert_course2(semester3,"CSCI","2365","Computer Science III","3")  

    #insert notes...
    insert_notes(advisingtree, "Calc I and II must be taken in sequence")
    
    # ready to create the xml for the current student
    fname='quweider_mk.xml'
    xml_to_file(advisingtree,fname)
    '''
