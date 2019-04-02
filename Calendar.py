"""
Calendar
"""
from time import sleep, strftime
USER_FIRST_NAME = "Sergiy"
calendar = {}
def welcome():
  print "Welcome to MyCalendar %s" %(USER_FIRST_NAME)
  print "Calendar launching..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "Time is: " + strftime("%H:%M:%S")
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
    elif user_choice == "A":
      event = raw_input("Enter event:")
      date = raw_input("Enter the date(MM/DD/YYYY):")
      if (len(date) > 10) or int(date[6:]) < int(strftime("%Y")):
        print "Date is invalid!"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "New event successfully created"
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("Calendar is empty")
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print("The event was successfully deleted")
            print(calendar)
          else:
            print("An incorrect event was specified")
    elif user_choice == "X":
      start = False
    else:
      print("An invalid command was entered")
      start = False
start_calendar()
      