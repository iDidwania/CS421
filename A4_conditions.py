# ask user for the day of the week
day = input("What day is it?")

# convert day to uppercase
day = (day.upper())

# take the first three letters only
day = (day[0:3])

# compare the input string with days of the week
if day == "MON":
    print("Martial Arts @ 6:30", "\n"
          "Distance Learning")
    
elif day == "TUE":
    print("BASE meeting @ 3:00", "\n"
          "Flute lesson @ 3:45", "\n"
          "At school")
    
elif day == "WED":
    print("Martial Arts @ 6:30", "\n"
          "Distance learning")
    
elif day == "THU":
    print("Interact meeting @ 3:00", "\n"
          "Jazz @ 8:00", "\n"
          "At school")
    
elif day == "FRI":
    print("CS421@SILC assignment due", "\n"
          "STEM Meeting @ 3:00", "\n"
          "Distance Learning")
    
elif day == "SAT":
    print("Hindi Class @ 10:00", "\n"
          "CS421 @ 11:00", "\n"
          "Dog training @ 3:00", "\n"
          "CS421@SILC assignment due with late penalty")
    
elif day == "SUN":
    print("CS421@SILC assignment is published)", "\n")
    
else:
    print("Sorry! I don't understand what you are saying")
