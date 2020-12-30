#************************** CS421: Assignment 5 **************
#
#  There are four sections in this assignment. Each section is worth 5 points.
#  Sections 1 and 2 count towards Assignment 5.
# Sections 3 and 4 count towards Assignment 6.
#  Skeleton code is already given. 
#  You only need to add your code between BEGIN and END lines in each section.
#
# Do NOT hardcode the output; You need to write python code so that it works whether
# you have 10 students in the list OR 1000 students in the list.
#
#  Use pythontutor.com to implement each section.
#  Save the complete implementation to a file called "a5_lists.py" and submit the file to Google Classroom
#
# How to save the code from PythonTutor to a file?
#           Select the entire code (Ctrl + A)
#           Copy the entire code (Ctrl + C)
#           Open notepad or any other editor you use to write text files.
#           Paste the entire code (Ctrl + V)
#           Save the code to a file (Ctrl +S)
# ************************************************************


#----------------------------------------------------------------------------
# A.5.1 --> Assume that some students registered twice for the same class.
# You need to write a program to remove the duplicate registrations from a list
#----------------------------------------------------------------------------

# define students list
students = ["abe", "barb", "chris", "abe", "dan", "chris", "ellie", "peter"]
print("All students --> ", students, "\n")



#=========================================
# BEGIN -- your code

students_temp = []

for x in students:
    if(x not in students_temp):
        students_temp.append(x)
    
students = students_temp

# END -- your code
#=========================================

# print students list. This should NOT contain any duplicates
print("Unique students --> ", students, "\n")


#----------------------------------------------------------------------------
#A.5.2 --> Assume that some students registered both html and python classes
# Find out the list of students who registered for both the classes.
#----------------------------------------------------------------------------


html = [ "barb", "dan", "ellie", "abe", "chris"]    
python = ["henry", "chris", "dan", "ellie", "frank", "gavin"] 
dupe_list = []

#=========================================
# BEGIN -- your code

for x in html:
    if(x in python):
        dupe_list.append(x)

# END -- your code
#=========================================

print("HTML students --> ", html, "\n")
print("Python students --> ", python, "\n")
print("Duplicates --> ", dupe_list, "\n")
