# CSU_schedule_finder
A tool to help find the best class schedule at CSU

Dependencies: 
Chrome 59 or newer, 
Selenium, 
chromedriver (executable must be in environment path)

This is a tool that finds the best possible class schedule for any Colorado State University student. To use, enter the CRN's of each option for every class in a comma seperated list. ie  1st class: 1234, 5678, 9012.... where each entry in a list is the CRN of a different possible time for that class.  If you have any classes that require you to be in a specific lab section/recitation for every specific lecture section, denote which lists correspond to the lecture and the lab/recitation with the linked class selection. Make sure that the two lists are ordered such that the n'th entry in the lecture list corresponds to the n'th entry in the lab/recitation list. After the program is done, a folder inside of the programs directory with pictures of the 20 best possible schedules.
