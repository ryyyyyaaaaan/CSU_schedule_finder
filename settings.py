
# SETTINGS


list_1 = ['NULL']

list_2 = ['NULL']

list_3 = ['NULL']

list_4 = ['NULL']

list_5 = ['NULL']

list_6 = ['NULL']

list_7 = ['NULL']

list_8 = ['NULL']

list_9 = ['NULL']

list_10 = ['NULL']


linked_courses = []  # LEAVE EMPTY IF NO LINKED COURSES
if linked_courses:
    if len(linked_courses[0]) != len(linked_courses[1]):
        print "Error: linked courses lists of unequal length"
        quit()
gap_threshold = 0
days_off_pref = 1
long_weekend_pref = 1
no_8am = 0
