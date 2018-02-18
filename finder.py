import time
program_start = time.time()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
import sys, os
import operator
import cPickle as pickle
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import Tkinter as tk

# script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
script_dir = os.path.dirname(os.path.abspath(__file__))






schedules = [] # list of schedule objects
courses = []
crn_dict = {}
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
days_off_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}
color_dict = {0:(8, 87, 214, 190), 1:(255, 89, 89, 190), 2:(173, 247, 37, 190), 3:(247, 117, 36, 190), 4:(36, 236, 247, 190), 5:(255, 76, 213, 190), 6:(252, 242, 95, 190), 7:(194, 244, 66, 190)}





#<--------Settings------->
def settings_func():
    global list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10, crn_list, no_8am, long_weekend_pref, days_off_pref, linked_courses, link1, link2, linked_dict
    list_1 = lists[0]
    list_2 = lists[1]
    list_3 = lists[2]
    list_4 = lists[3]
    list_5 = lists[4]
    list_6 = lists[5]
    list_7 = lists[6]
    list_8 = lists[7]
    list_9 = lists[8]
    list_10 = lists[9]

    crn_list = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8 + list_9 + list_10

    days_off_pref = var2.get()
    long_weekend_pref = var3.get()
    no_8am = var1.get()

    if days_off_pref != 1 and long_weekend_pref == 1:
        days_off_pref = 1

    list_dict = {1:list_1, 2:list_2, 3:list_3, 4:list_4, 5:list_5, 6:list_6, 7:list_7, 8:list_8, 9:list_9, 10:list_10}
    if link1 is not "None" and link2 is not "None":
        linked_courses = [list_dict[int(link1.get())], list_dict[int(link2.get())]]
    else:
        linked_courses = []
    if linked_courses:
        if len(linked_courses[0]) != len(linked_courses[1]):
            print "Error: linked courses lists of unequal length"
            quit()



    if linked_courses:
        linked_dict = dict(zip(linked_courses[0], linked_courses[1]))




#TODO add 'class full' functionality and add time data recieved attribute to class objects
#TODO debug no name problem
#TODO lunch hour
#TODO schedule to work around
#     ^^ make gui feature that allows user to edit base schedule (day_dict)
#TODO throw error if # of possible schedules too high
#TODO Switch to python 3
#TODO compile list of all valid CRN's and check user inputs against that



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








#def inclusive():
#    if var2.get() == 0:
#        check2.select()
    

def button_func():
    get_vals()
    settings_func()
    main()


def get_vals():
    global lists
    lists = []
    str_list = [list1.get(), list2.get(), list3.get(), list4.get(), list5.get(), list6.get(), list7.get(), list8.get(), list9.get(), list10.get()]

    for i, string in enumerate(str_list):
        if string == '':
            str_list[i] = 'NULL'


    for n in str_list:
        lists.append(n.split(','))


    for i in range(len(lists)):
        if 'NULL' not in lists[i]:
            lists[i] = [int(x) for x in lists[i]]



def finder_gui():
    global var1, var2, var3, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, link1, link2
    
    root = tk.Tk()
    root.title("CSU Schedule Finder")
    tk.Label(root, text='CSU Schedule Finder', font=('Ubuntu', 18)).grid(row=0, columnspan=5, sticky='n')
    var1 = tk.IntVar()
    tk.Checkbutton(root, text="No 8 AM Classes:", variable=var1).grid(row=1, column=0, columnspan=5, sticky='W')
    var2 = tk.IntVar()
    check2 = tk.Checkbutton(root, text="Give preference to schedules with entire days off?", variable=var2).grid(row=2,column=0, columnspan=5, sticky='W')
    var3 = tk.IntVar()
    tk.Checkbutton(root, text="Give preference to schedules with mondays or fridays off?", variable=var3).grid(row=3,column=0,columnspan=5, sticky='W')
    tk.Label(root, text="1st Class").grid(row=4, column=0, sticky='w')
    tk.Label(root, text="2nd Class").grid(row=5, column=0, sticky='w')
    tk.Label(root, text="3rd Class").grid(row=6, column=0, sticky='w')
    tk.Label(root, text="4th Class").grid(row=7, column=0, sticky='w')
    tk.Label(root, text="5th Class").grid(row=8, column=0, sticky='w')
    tk.Label(root, text="6th Class").grid(row=9, column=0, sticky='w')
    tk.Label(root, text="7th Class").grid(row=10, column=0, sticky='w')
    tk.Label(root, text="8th Class").grid(row=11, column=0, sticky='w')
    tk.Label(root, text="9th Class").grid(row=12, column=0, sticky='w')
    tk.Label(root, text="10th Class").grid(row=13, column=0, sticky='w')
    list1 = tk.Entry(root, width=70)
    list2 = tk.Entry(root, width=70)
    list3 = tk.Entry(root, width=70)
    list4 = tk.Entry(root, width=70)
    list5 = tk.Entry(root, width=70)
    list6 = tk.Entry(root, width=70)
    list7 = tk.Entry(root, width=70)
    list8 = tk.Entry(root, width=70)
    list9 = tk.Entry(root, width=70)
    list10 = tk.Entry(root, width=70)
    list1.grid(row=4, column=1,columnspan=6, sticky='w')
    list2.grid(row=5,column=1,columnspan=6, sticky='w')
    list3.grid(row=6,column=1,columnspan=6, sticky='w')
    list4.grid(row=7,column=1,columnspan=6, sticky='w')
    list5.grid(row=8,column=1,columnspan=6, sticky='w')
    list6.grid(row=9,column=1,columnspan=6, sticky='w')
    list7.grid(row=10,column=1,columnspan=6, sticky='w')
    list8.grid(row=11,column=1,columnspan=6, sticky='w')
    list9.grid(row=12,column=1,columnspan=6, sticky='w')
    list10.grid(row=13,column=1,columnspan=6, sticky='w')
    tk.Label(root, text="Linked classes:").grid(row=14, column=0, sticky='w')
    tk.Label(root).grid(row=14, column=1, sticky='e')
    tk.Label(root, text="and").grid(row=14, column=3)
    link1 = tk.IntVar()
    link2 = tk.IntVar()
    options = ['None','1','2','3','4','5','6','7','8','9','10']
    link1.set(options[0])
    link2.set(options[0])
    tk.OptionMenu(root, link1, *options).grid(row=14, column=2, sticky='w')
    tk.OptionMenu(root, link2, *options).grid(row=14, column=5, sticky='w')


    tk.Button(root, text='Submit', command=button_func).grid(row=15, column=5, sticky='e', pady=4)
    root.mainloop()













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

    # TODO CHANGE THIS
    for i, course in enumerate(courses):
        crn_dict[course.CRN] = i
    # Stops chrome
    if crns_to_get:
        driver.quit()
    print

    
    for tuplex in itertools.product(list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10):
        x = list(tuplex)
        x = filter(lambda a: a != 'NULL', x)

        if linked_courses and no_8am == 0:
            for crn in linked_courses[0]:
                if crn in x and linked_dict[crn] in x:
                    schedules.append(Schedule(len(schedules)))
                    scheduler(x, len(schedules)-1)
                    break
        elif linked_courses and no_8am == 1:
            combo_8am = 0
            for crn in x:
                if courses[crn_dict[crn]].start_value <= 23:
                    combo_8am = 1
                    break
            for crn in linked_courses[0]:
                if crn in x and linked_dict[crn] in x and combo_8am == 0:
                    schedules.append(Schedule(len(schedules)))
                    scheduler(x, len(schedules)-1)
                    break
        elif not linked_courses and no_8am == 1:
            combo_8am = 0
            for crn in x:
                if courses[crn_dict[crn]].start_value <= 23:
                    combo_8am = 1
                    break
            if combo_8am == 0:
                schedules.append(Schedule(len(schedules)))
                scheduler(x, len(schedules)-1)
        elif not linked_courses and no_8am == 0:
            schedules.append(Schedule(len(schedules)))
            scheduler(x, len(schedules)-1)
    

    for schedule in schedules:
        if schedule.valid != 0:
            try:
                schedule.GapScore()
            except Exception as exception:
                print schedule.number
                print schedule.valid
                print schedule.Monday
                print schedule.Tuesday
                print schedule.Wednesday
                print schedule.Thursday
                print schedule.Friday
                print schedule.class_list
                quit()



    for schedule in schedules:
        if schedule.valid == 1:
            for course in schedule.class_list:
                if course.start_value <= 23:
                    schedule.has_8am = 1


    for schedule in schedules:
        if schedule.valid == 1:
            fit_criteria.append(schedule)
    
    fit_criteria = sorted(fit_criteria, key=operator.attrgetter('gap_score'), reverse=True)
    del fit_criteria[20:]


    for i, schedule in enumerate(fit_criteria):
        print "---------------------------------------------------------------------------"
        print "---------------------------------------------------------------------------", "\n"
        print "Schedule: ", schedule.number
        print "Gap Score: ", schedule.gap_score
        if schedule.days_off is not None:
            print "Days off: ",
            for day in schedule.days_off:
                print days_off_dict[day],
            print
        else:
            print "Days off: None", "\n"
        for course in schedule.class_list:
            print course.CRN
            print course.name
            print course.day_str
            print course.classTimes
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

    for i, course in enumerate(schedule.class_list):
        course.color = color_dict[i]
    
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

    file_name = str(schedule.gap_score) + ".JPEG"
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
        self.color = None


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

        for day in week_days:
            current_high = 0
            count = 0
            for value in getattr(self, day).values():
                if value == 0:
                    count = count + 1
                else:
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
        for day in class_object.class_days:
            i = class_object.start_value
            while i < class_object.end_value:
                if getattr(self, day) is None:
                    setattr(self, day, day_dict.copy())
                current_value = getattr(self, day)[i]
                if current_value == 1:
                    self.valid = 0
                    break
                getattr(self, day)[i] = 1
                i = i + 1
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
        if schedules[its_number].valid == 1:
            schedules[its_number].add_class(courses[crn_dict[a_combo[x]]])
    for i, day in enumerate(week_days):
        if schedules[its_number].valid == 1 and getattr(schedules[its_number], day) is None:
            if schedules[its_number].days_off is None:
                schedules[its_number].days_off = []
            schedules[its_number].days_off.append(i)
            setattr(schedules[its_number], day, day_dict.copy())


finder_gui()

print "TOTAL TIME TO EXECUTE: ", time.time() - program_start
