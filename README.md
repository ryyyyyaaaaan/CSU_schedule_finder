# CSU_schedule_finder
A tool to help find the best class schedule at CSU

Dependencies: 
Chrome 59 or newer, 
Selenium, 
chromedriver (executable must be in environment path)

I am a student at Colorado State University and this is a script I wrote in python to help me find the perfect schedule every semester. The python script uses selenium webdriver and headless chrome to scrape the class data off of the course registration website and then from there it finds every possible schedule, and prints that to the command line. Currently, you set your classes and other options inside of the settings.py file. In this file, there are 10 lists, one for each class you are taking. Get the CRN numbers of every different option for each of your classes and put them in the lists. Set any list that you arent putting CRN's into to be " ['NULL'] ". If you have a class that requires that you take a specific lab/recitation for each specific lecture, than make sure to put the CRN's for the lab/lecture list in the same order as their corresponding lecture list and then set the linked classes list to be " [list_x, list_y] " where x is the list number of the lecture and y is the list number of the lab/recitation. If you prefer not to have 8 am classes, set the no_8am variable to be 1, otherwise 0. The gap score is a score that is assigned to each schedule based on how large the amount of continous free time it gives you (basically, the higher the score, the fewer gaps you have in your schedule). Setting the gap threshold just tells the program not to print any schedules that dont have a score at least that high. Run the program at least once and see what the gap scores of some of the output schedules are and then maybe run it again with a (non-zero) gap threshold set to in order to narrow it down. Setting days off pref to 1 will double the gap score for any day that has no classes and setting the long weekend pref to 1 will triple the gap score for any monday or friday that doesnt have any classes (3 day weekend!).

NOTE: This is a work in progress and is currently not designed to be used publicly.
