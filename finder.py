from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import itertools
import sys, os
import operator
import cPickle as pickle
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap



# script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
script_dir = os.path.dirname(os.path.abspath(__file__))



# This if statement here for testing purposes
if "my_settings_copy.py" in os.listdir(script_dir):
    import my_settings_copy as settings
else:
    import settings



#TODO add 'class full' functionality and add time data recieved attribute to class objects
#TODO debug no name problem
#TODO GUI
#TODO lunch hour
#TODO schedule to work around
#     ^^ make gui feature that allows user to edit base schedule (day_dict)





program_start = time.time()




rel_path = "class_objects"
classes_dir = os.path.join(script_dir, rel_path)
if not os.path.exists(classes_dir):
    os.makedirs(classes_dir)



rel_path = "time_dict.p"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path, 'rb') as fp:
    time_dict = pickle.load(fp)
rel_path = "day_dict.p"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path, 'rb') as fp:
    day_dict = pickle.load(fp)

schedules = [] # list of schedule objects
courses = []
crn_dict = {}
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
days_off_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}
color_dict = {0:(8, 87, 214, 190), 1:(8, 87, 214, 190), 2:(173, 247, 37, 190), 3:(247, 117, 36, 190), 4:(36, 236, 247, 190), 5:(255, 76, 213, 190), 6:(252, 242, 95, 190), 7:(194, 244, 66, 190)}

print
# crnInput = raw_input("Enter CRN: ")
# crn_list = [12048	,12051	,12052	,12053	,12054	,12055	,12056	,12057	,12058	,12059	,12078	,12081	,12083	,12084	,12095	,12099	,12100	,12126	,12129	,12133	,12134	,12135	,12137	,12140	,12239	,12246	,12247	,12260	,12261	,12262	,12265	,12301	,16122	,16379	,16467	,18309	,19370	,20642	,20705	,20737	,20738	,20739	,20797	,20798	,20799	,22008	,22876	,24656	,24657	,24659]

list_1 = settings.list_1
list_2 = settings.list_2
list_3 = settings.list_3
list_4 = settings.list_4
list_5 = settings.list_5
list_6 = settings.list_6
list_7 = settings.list_7
list_8 = settings.list_8
list_9 = settings.list_9
list_10 = settings.list_10

crn_list = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8 + list_9 + list_10

#<--------Settings------->

linked_courses = settings.linked_courses
if linked_courses:
    if len(linked_courses[0]) != len(linked_courses[1]):
        print "Error: linked courses lists of unequal length"
        quit()
gap_threshold = settings.gap_threshold
days_off_pref = settings.days_off_pref
long_weekend_pref = settings.long_weekend_pref
no_8am = settings.no_8am

if days_off_pref != 1 and long_weekend_pref == 1:
    days_off_pref = 1

if linked_courses:
    linked_dict = dict(zip(linked_courses[0], linked_courses[1]))



def init(pause):

    # Gets term selection page and clicks drop down menu
    driver.get("https://bannerxe.is.colostate.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search")
    beginning_time = time.time()
    start_time = time.time()
    while "Select a Term" not in driver.find_element_by_xpath("/html/body").text:
        if time.time() - start_time > 15:
            break
        time.sleep(pause)
    driver.find_element_by_xpath("//*[@id='s2id_txt_term']").click()


    # Selects drop down field and inputs search text and then sends ENTER
    start_time = time.time()
    while "Spring Semester 2018" not in driver.find_element_by_xpath("/html/body").text:
        if time.time() - start_time > 15:
            break
    time.sleep(pause)
    term = driver.find_element_by_xpath("//*[@id='s2id_autogen1_search']")
    term.send_keys("spring semester 2018")
    time.sleep(1)
    term.send_keys(Keys.ENTER)
    

    # Clicks 'go'
    start_time = time.time()
    while "selected choice Spring Semester 2018" not in driver.find_element_by_xpath("/html/body").text:
        if time.time() - start_time > 15:
            break
    time.sleep(pause)
    driver.find_element_by_xpath("//*[@id='term-go']").click()
    print "INIT EXEC. TIME :"
    print time.time() - beginning_time

def main():
    global script_dir
    global driver
    fit_criteria = []
    crns_to_get = []
    # print "class_objects :", os.listdir('.class_objects')
    for x in crn_list:
        rel_path = "class_objects"
        abs_file_path = os.path.join(script_dir, rel_path)
        crn_file = str(x) + ".p"
        if crn_file not in os.listdir(abs_file_path) and str(x) != 'NULL':
            crns_to_get.append(x)
        #TODO elif str(x) in os.listdir('.class_objects') and data is old


    # checks if crns_to_get is empty
    if crns_to_get:
        #TODO delete this (needed to get data)
        print "Needed to get data"

        # Sets options for chrome driver
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_page_load_timeout(30)


        try:
            init(0)
        except Exception as exception:
            print "EXCEPTION: ", exception.__class__.__name__
            init(0.2)
    for x in crn_list:
        if x not in crns_to_get and x != 'NULL':
            file_name = str(x) + ".p"
            rel_path = ["class_objects", file_name]
            abs_file_path = os.path.join(script_dir, *rel_path)
            with open(abs_file_path, 'rb') as fp:
                courses.append(pickle.load(fp))
        

    
    
    # loop that iterates over crn_list, calling get_data each time with the argument being the crn_list element and a pause.
    # if any exception is raised, the exception is printed and get_data called again, but with a 0.5 second pause argument.
    for x in crns_to_get:
        if x != 'NULL':

            beginning_time = time.time()
            try:
                courses.append(get_data(x,0))
            except Exception as exception:
                print "EXCEPTION: ", exception.__class__.__name__
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print exc_tb.tb_lineno
                print
                try:
                    init(0)
                except Exception as exception:
                    print "EXCEPTION: ", exception.__class__.__name__
                    init(0.2)
                courses.append(get_data(x, 0.5))
            print "TIME TO EXECUTE :",
            print time.time() - beginning_time
            print "\n"

    # creates dictionary with crn values as keys and their respective courses list index values as values
    # this allows course data to be accessed via courses[crn_dict[CRN]]
    i = 0
    for x in courses:
        crn_dict[courses[i].CRN] = i
        i = i+1
    # Stops chrome
    if crns_to_get:
        driver.quit()
    print

    
    for x in range(len(list_1) * len(list_2) * len(list_3) * len(list_4) * len(list_5) * len(list_6) * len(list_7) * len(list_8) * len(list_9) * len(list_10)):
        schedules.append(Schedule(x))
    i = 0
    for x in itertools.product(list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10):
        if linked_courses:
            valid_linked = 0
            for n in linked_courses[0]:
                if n in x and linked_dict[n] in x:
                    scheduler(x, i)
                    valid_linked = 1
            if valid_linked == 0:
                schedules[i].valid = 0
        else:
            scheduler(x, i)
        i = i + 1


    for schedule in schedules:
        if getattr(schedule, 'valid') != 0:
            schedules[getattr(schedule, 'number')].GapScore()





    for schedule in schedules:
        if getattr(schedule, 'valid') == 1:
            for course in schedules[getattr(schedule, 'number')].class_list:
                if getattr(course, 'start_value') <= 23:
                    setattr(schedule, 'has_8am', 1)

    num_valid = 0
    num_fit_criteria = 0
    for schedule in schedules:
        if getattr(schedule, 'valid') == 1:
            if getattr(schedule, 'gap_score') >= gap_threshold:
                if no_8am == 1:
                    if getattr(schedule, 'has_8am') == 0:
                        fit_criteria.append(schedule)
                        num_fit_criteria = num_fit_criteria + 1
                else:
                    fit_criteria.append(schedule)
                    num_fit_criteria = num_fit_criteria + 1
            num_valid = num_valid + 1

    print "# of Valid Schedules: ", num_valid
    print "# of schedules fitting criteria: ", num_fit_criteria

    fit_criteria = sorted(fit_criteria, key=operator.attrgetter('gap_score'), reverse=True)
    del fit_criteria[20:]

    for i, schedule in enumerate(fit_criteria):
        print "---------------------------------------------------------------------------"
        print "---------------------------------------------------------------------------", "\n"
        print "Schedule: ", getattr(schedule, 'number')
        print "Gap Score: ", getattr(schedule, 'gap_score')
        if getattr(schedule, 'days_off') is not None:
            print "Days off: ",
            for day in getattr(schedule, 'days_off'):
                print days_off_dict[day],
            print
        else:
            print "Days off: None", "\n"
        for course in fit_criteria[i].class_list:
            print getattr(course, 'CRN')
            print getattr(course, 'name')
            print getattr(course, 'day_str')
            print getattr(course, 'classTimes')
            print "\n"    

    for schedule in fit_criteria:
        visual_schedule(schedule)








rel_path = "day_pix.p"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path, 'rb') as fp:
    day_pix = pickle.load(fp)

rel_path = "time_pix.p"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path, 'rb') as fp:
    time_pix = pickle.load(fp)

def visual_schedule(schedule):
    base = Image.open('base_calendar.png')
    class_boxes = Image.new('RGBA', base.size, (255,255,255,0))
    boxes = ImageDraw.Draw(class_boxes)


    for course in schedule.class_list:
        for day in course.class_days:
            x1 = day_pix[day][0]
            y1 = time_pix[course.start_value]
            x2 = day_pix[day][1]
            y2 = time_pix[course.end_value]
            tup1 = (x1, y1)
            tup2 = (x2, y2)
            boxes.rectangle([tup1, tup2], fill=course.color)

    # get a font
    fnt = ImageFont.truetype('Ubuntu-R.ttf', 12)
    # draw text, full opacity
    for course in schedule.class_list:
        for day in course.class_days:
            x1 = day_pix[day][0]
            y1 = time_pix[course.start_value]
            for i, line in enumerate(textwrap.wrap(course.name, width=30)):
                if len(textwrap.wrap(course.name, width=30)) > 2 and i == 1:
                    line = line + " " + textwrap.wrap(course.name, width=30)[2][:(27-len(line))] + "..."
                tup1 = (x1, y1+(i*13))
                boxes.text(tup1, line, font=fnt, fill=(0,0,0,255))
                if i >= 1:
                    break

    out = Image.alpha_composite(base, class_boxes)

    rel_path = "schedule_images"
    images_dir = os.path.join(script_dir, rel_path)
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    file_name = str(schedule.number) + ".JPEG"
    rel_path = ["schedule_images", file_name]
    images_dir = os.path.join(script_dir, *rel_path)
    out.save(images_dir)







class Course:
    def __init__(self, CRN, course_name, day_str, classTimes):
        self.CRN = CRN
        self.name = course_name
        self.day_str = day_str
        self.classTimes = classTimes
        self.class_days = day_str.split(",")
        self.times = classTimes.split(" - ")
        self.start_time = self.times[0]
        self.end_time = self.times[1]
        self.start_value = time_dict[self.times[0]]
        self.end_value = time_dict[self.times[1]]
        self.color = color_dict[random.randint(0,7)]


# function that takes a crn and a pause value as arguments and returns a Course object
# pause value is a pause, in seconds, that is evaluated before each click
def get_data(CRN, pause):
    global script_dir

    print "TESTING CRN     :",
    print CRN
    
    

    # Selects keyword field and inputs crn
    start_time = time.time()
    time.sleep(0.1 + pause)
    if pause != 0:
        while "Advanced Search" not in driver.find_element_by_xpath("/html/body").text:
            if time.time() - start_time > 15:
                break
    crn = driver.find_element_by_xpath("//*[@id='txt_keywordlike']")
    crn.clear()
    crn.send_keys(CRN)

    # Clicks 'go'
    start_time = time.time()
    if pause != 0:
        while 'id="search-go"' not in driver.page_source:
            if time.time() - start_time > 15:
                break
    time.sleep(0.1 + pause)
    driver.find_element_by_xpath("//*[@id='search-go']").click()

    # Gets 'title' attribute of the search result table, which contains the times and days of the week of the class
    start_time = time.time()
    if pause != 0:
        while "Records:" not in driver.find_element_by_xpath("/html/body").text:
            if time.time() - start_time > 15:
                print "Error, class does not exist \n"
                break
    time.sleep(0.5 + pause)
    hay = driver.find_element_by_xpath("//*[@id='table1']/tbody/tr/td[8]").get_attribute("title")

    # finds the index of the '-' in the title attribute
    print "INDEX OF '-'    :",
    print hay.find('-')
    
    # Uses index of '-' to get only relavant parts of string
    dash_index = hay.find('-')
    classTimes = hay[(dash_index-10):(dash_index+11)]
    print "CLASS TIMES     : " + classTimes

    day_str = hay[:(dash_index-17)]
    print "CLASS DAYS      :",
    print day_str

    time.sleep(0.2)
    course_name = driver.find_element_by_xpath("//*[@id='table1']/tbody/tr/td[6]").get_attribute("title")
    
    
    # clicks the 'search again' button
    start_time = time.time()
    time.sleep(pause+0.1)

    if pause != 0:
        while "Advanced Search" not in driver.find_element_by_xpath("/html/body").text:
            driver.find_element_by_xpath("//*[@id='search-again-button']").click()
    else:
        driver.find_element_by_xpath("//*[@id='search-again-button']").click()
    
    instance = Course(CRN, course_name, day_str, classTimes)

    file_name = str(CRN) + ".p"
    rel_path = ["class_objects", file_name]
    abs_file_path = os.path.join(script_dir, *rel_path)
    with open(abs_file_path, 'wb') as fp:
        # json.dump(instance, fp)
        pickle.dump(instance, fp)
    return instance




class Schedule(object):
    def __init__(self, number):
        self.number = number
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.valid = 1
        self.class_list = None
        self.gap_score = 0
        self.has_8am = 0
        self.days_off = None
    
    def GapScore(self):

        current_high = 0
        count = 0

        for value in self.Monday.values():
            if value == 0:
                count = count + 1
            else:
                if count > current_high:
                    current_high = count
                count = 0
            if count > current_high:
                current_high = count
        self.gap_score = self.gap_score + current_high

        current_high = 0
        count = 0
        for value in self.Tuesday.values():
            if value == 0:
                count = count + 1
            elif value == 1:
                if count > current_high:
                    current_high = count
                count = 0
        if count > current_high:
            current_high = count
        self.gap_score = self.gap_score + current_high

        current_high = 0
        count = 0
        for value in self.Wednesday.values():
            if value == 0:
                count = count + 1
            elif value == 1:
                if count > current_high:
                    current_high = count
                count = 0
        if count > current_high:
            current_high = count
        self.gap_score = self.gap_score + current_high

        current_high = 0
        count = 0
        for value in self.Thursday.values():
            if value == 0:
                count = count + 1
            elif value == 1:
                if count > current_high:
                    current_high = count
                count = 0
        if count > current_high:
            current_high = count
        self.gap_score = self.gap_score + current_high

        current_high = 0
        count = 0
        for value in self.Friday.values():
            if value == 0:
                count = count + 1
            elif value == 1:
                if count > current_high:
                    current_high = count
                count = 0
        if count > current_high:
            current_high = count
        self.gap_score = self.gap_score + current_high
        if days_off_pref == 1:
            if self.days_off is not None:
                for day in self.days_off:
                    self.gap_score = self.gap_score + 180
        if long_weekend_pref == 1:
            if self.days_off is not None:
                for day in self.days_off:
                    if day == 0 or day == 4:
                        self.gap_score = self.gap_score + 180

            


    def add_class(self, class_object): 
        if self.class_list is None:
            self.class_list = []
        self.class_list.append(class_object)
        for x in class_object.class_days:
            i = class_object.start_value
            while i < class_object.end_value:

                if x == 'Monday':
                    if self.Monday is None:
                        self.Monday = day_dict.copy()
                    current_value = self.Monday[i]
                    if current_value == 1:
                        self.valid = 0
                        break
                    self.Monday[i] = 1
                elif x == 'Tuesday':
                    if self.Tuesday is None:
                        self.Tuesday = day_dict.copy()
                    current_value = self.Tuesday[i]
                    if current_value == 1:
                        self.valid = 0
                        break
                    self.Tuesday[i] = 1
                elif x == 'Wednesday':
                    if self.Wednesday is None:
                        self.Wednesday = day_dict.copy()
                    current_value = self.Wednesday[i]
                    if current_value == 1:
                        self.valid = 0
                        break
                    self.Wednesday[i] = 1
                elif x == 'Thursday':
                    if self.Thursday is None:
                        self.Thursday = day_dict.copy()
                    current_value = self.Thursday[i]
                    if current_value == 1:
                        self.valid = 0
                        break
                    self.Thursday[i] = 1
                elif x == 'Friday':
                    if self.Friday is None:
                        self.Friday = day_dict.copy()
                    current_value = self.Friday[i]
                    if current_value == 1:
                        self.valid = 0
                        break
                    self.Friday[i] = 1
                i = i+1
            if self.valid == 0:
                self.Monday = None
                self.Tuesday = None
                self.Wednesday = None
                self.Thursday = None
                self.Friday = None
                self.has_8am = None
                self.class_list = None
                self.gap_score = None
                break

           
        



def scheduler(a_combo, its_number):
    for x in range(len(a_combo)):
        if a_combo[x] != 'NULL' and schedules[its_number].valid == 1:
            schedules[its_number].add_class(courses[crn_dict[a_combo[x]]])
    for i, day in enumerate(week_days):
        if schedules[its_number].valid == 1 and getattr(schedules[its_number], day) is None:
            if schedules[its_number].days_off is None:
                schedules[its_number].days_off = []
            schedules[its_number].days_off.append(i)
            setattr(schedules[its_number], day, day_dict.copy())





main()

print "TOTAL TIME TO EXECUTE: ", time.time() - program_start
