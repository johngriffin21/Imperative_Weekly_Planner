days = {"Monday": None,                             #I decided the best way to implement a appointment scheduler would be a dictionary with lists as keys..
    "Tuesday": None,                                #for potential appointments.
    "Wednesday": None ,
    "Thursday": None,
    "Friday": None,
    "Saturday": None,
    "Sunday": None
}

print("Welcome to the appointment maker, type any key and enter add an appointment or type & enter 'exit' to leave.")
n = input
while input() != "exit":
    print("Please enter the day you want to make an appointment for:")
    day = input()
    if day not in days:                        #user entered a day that isnt in days, therefore they are given the option to add a new day in
        print("That's not a day")
    else:                                      #throughout this code I used print statements to provide an interactive experience for the user.
        print("Thanks, now please enter a start time for your appointment(24hrs ex: 1pm is 1300):")
        stime = input()
        print("Thanks, now please enter an end time for your appointment(24hrs ex: 1pm is 1300):")
        etime= input()
        print("Please enter the details of your appointment:")
        details = input()
        if day not in days:
            print("Sorry, that's not a day.")
        if days[day] != None:  # this checks if the day in question has a list, which means that an appointment has been added.
            for x in range(days[day][0], days[day][1]):  # to check if an time is available, we iterate from the previous appts start time and see if...
                if int(stime) == x:  # any time between that matches the start time of new appt to be added
                    print("The time {} - {} on {} is already taken sorry.".format(stime, etime, day))  # here we have matched it, so the time is unavailable..
                    print("Here is {}'s schedule".format(day))  # a simple output message lets the user know this.
                    print("For {}, you have an appointment of {} from {} to {}.".format(day, days[day][2],days[day][0], days[day][1]))
                    break

            days[day].append(int(stime))  # the list already exist if we're in this loop, so appending each value works.
            days[day].append(int(etime))
            days[day].append(details)
        else:
            days[day] = [int(stime), int(etime), details] #create a list as a value in days
            print("Your appointment is now added. Enter any key to book another or type & enter 'exit' to leave.")
print('-' * 120)
print('-' * 120)
print("Your schedule this week.")                                                          #I used formatting to separate the appointments into something more readable to the user
print("{:<12} {:<40} {:<10} {:<10}".format('Day:', 'Description:', 'Start:', 'End:'))
for i in days:
    if days[i] == None:                                                                    #The day has none as the value so the user hasn't entered any appointments for that day
        print("{:<12} {:<40} {:<10} {:<10}".format(i, 'No appts', 'N/A', 'N/A'))
    elif len(days[i]) == 3:                                                                #If the user only has one appt for that day then where stime, dtime and details are in the list are fixed
        print("{:<12} {:<40} {:<10} {:<10}".format(i, days[i][2], days[i][0],days[i][1]))
    elif len(days[i]) > 3:                                                                 #The user has entered more than one appt for the day so I made something to iterate through the lit
        print("{:<12} {:<40} {:<10} {:<10}".format(i, days[i][2], days[i][0], days[i][1])) #The first appt will always be fixed
        x = len(days[i])
        t = (x/3)                                                                        #We use this to find the index we need to display (I change it later on to y as an index cant be a float)
        am = (x/3) -1                                                                      #We know now how many appts after the first one there is, ie 9 things in list would equal 3 appts therfore giving us a value of two after the first appt.
        amt = int(am)
        y = int(t)
        for q in range(0,amt):
            print("{:<12} {:<40} {:<10} {:<10}".format("     ", days[i][y + 3], days[i][y + 1], days[i][y + 2]))
            y += 3

print("Would you like to remove an appointment ? Type 'Yes' if you do.")
print("Or type 'Day' to receive your schedule for a particular day.")
print('-' * 120)
print('-' * 120)
x = input()
while x == "Yes" or x == "yes":
    print("Please enter the day of the appointment you want to remove:")
    day = input()
    if day not in days:
        print("That's not a day")
    else:
        print("Thanks, now please enter a start time for that appointment(24hrs ex: 1pm is 1300):")
        stime1 = input()
        print("Thanks, now please enter an end time for that appointment(24hrs ex: 1pm is 1300):")
        etime1 = input()
        print("Please enter the details of that appointment:")
        details1 = input()             # We now remove the appt from the dictionary.
        days[day].remove(int(stime1))  # use int stime etime etc in this as they are appended as these types
        days[day].remove(int(etime1))
        days[day].remove(details1)
        print("Your appointment is now removed. Type 'Yes' to remove another or 'No' to leave.")
        x = input()
while x == "Day" or x == "day":
    print("Please type the day you are looking for with a capital.")
    new_day = input()
    if days[i] == None:                                                                    #The day has none as the value so the user hasn't entered any appointments for that day
        print("{:<12} {:<40} {:<10} {:<10}".format(i, 'No appts', 'N/A', 'N/A'))
        print("Here is {}'s schedule".format(new_day))  # a simple output message lets the user know this.
        print("For {}, you have an appointment of {} from {} to {}.".format(new_day, days[new_day][2], days[new_day][0],days[new_day][1]))
        print("Your schedule this week.")
        print("{:<12} {:<40} {:<10} {:<10}".format('Day:', 'Description:', 'Start:', 'End:'))
        for i in days:
            if days[i] == None:
                print("{:<12} {:<40} {:<10} {:<10}".format(i, 'No appts', 'N/A', 'N/A'))
            elif len(days[i]) == 3:
                print("{:<12} {:<40} {:<10} {:<10}".format(i, days[i][2], days[i][0], days[i][1]))
            elif len(days[i]) > 3:
                print("{:<12} {:<40} {:<10} {:<10}".format(i, days[i][2], days[i][0], days[i][1]))
                x = len(days[i])
                t = (x / 3)
                am = (x / 3) - 1
                amt = int(am)
                y = int(t)
                for q in range(0, amt):
                    print("{:<12} {:<40} {:<10} {:<10}".format("     ", days[i][y + 3], days[i][y + 1], days[i][y + 2]))
