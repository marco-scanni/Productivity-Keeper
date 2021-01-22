# -*- coding: utf-8 -*-
"""
Day Keeper Schedule Creator

@author: Marco Scanni marco.scanni2020@gmail.com

Note:
Line 51: Replace directory with your own directory. Ensure DayKeeper.py is in it's own folder.

"""
import datetime

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle
    
from os import listdir
from os.path import isfile, join


class Event:
    
    def  __init__(self, eventName, time):
        self.eventName = eventName
        self.time = time
      

class DayStack:
    
    def __init__(self, date):
        self.date = date
        self.schedule = []
        
    def getDate(self):
        OFormatDate = str(self.date)
        return str(OFormatDate[5:7]) +"-"+ str(OFormatDate[8::]) +"-"+ str(OFormatDate[0:4])
        
    def addEvent(self, event):
        self.schedule.append(event)
        self.schedule.sort(key = lambda t: t.time)
    
    def viewSchedule(self):
         print("\n\nYour Schedule for " + self.getDate() + ":\n------------------------------------------")
         for i in range (len(self.schedule)):
             print("%-35s %s" %(self.schedule[i].eventName,"at " + str(self.schedule[i].time)))    
         print("\n")
        
    def saveStack(self,dayStack):
        pickle_out = open(str(dayStack.getDate()),"wb")
        pickle.dump(dayStack,pickle_out)
        pickle_out.close()
        
    def giveAllStacks():
        onlyFiles = [f for f in listdir(r'C:\Users\Marco\Documents\School\Non-class Items\Personal Projects\Productivity Keeper') if str(f) != "DayKeeper.py" and isfile(join(r'C:\Users\Marco\Documents\School\Non-class Items\Personal Projects\Productivity Keeper', f))]
        if len(onlyFiles) == 0:
            print("It doesn't seem like there are any saved schedules. Returning to main menu...")
            UserInput.mainMenu()
        else: 
            return onlyFiles
        

class UserInput:
    
    def askforEvent():
        evName = input("Enter the name of your event, then press Enter. ")
        while evName == "" or evName.isspace():
            print("Please ensure you are entering an event.")
            evName = input("Enter the name of your event, then press Enter. \n")
        return evName
    
    def askforTime():
        hourStr = input("Enter the hour of your event, then press Enter.")
        while (not hourStr.isdigit()
               or int(hourStr) < 0
               or int(hourStr) > 24):
            print("Please ensure you are entering a valid hour between 0-24.")
            hourStr = input("Enter the hour of your event, then press Enter.\n")
                
        minStr = input("Enter the minute of your event, then press Enter.")
        while (not minStr.isdigit()
               or int(minStr) < 0
               or int(minStr) > 59):
            print("Please ensure you are entering a minute between 0-59.")
            minStr = input("Enter the minute of your event, then press Enter.\n")
            
        return datetime.time(int(hourStr),int(minStr),0,0)
    
    def chooseExistingSchedule():
        for file in DayStack.giveAllStacks():
            print("\n" + str(file))
        chosenSched = input("Enter the date for the schedule you would like to see.")
        for file in DayStack.giveAllStacks():
            if file != "DayKeeper.py":
                if(chosenSched == file):
                    pickle_in = open(file,"rb")
                    openedStack = pickle.load(pickle_in)
                    openedStack.viewSchedule()
        print("returning to main menu......")
        UserInput.mainMenu()
            
            
    def mainMenu():
        mainMenuSelection = input("Welcome to Day Keeper!\n\nPlease select one of the options below.\n" 
                                  + "Enter 1 to view your existing schedules.\n"
                                         + "Enter 2 to create a new schedule.\n"
                                          + "Enter 3 to exit Day Keeper.\n")
                
        while mainMenuSelection != "1" and mainMenuSelection != "2" and mainMenuSelection != "3":
            print("Please enter a valid selection.")
            mainMenuSelection = input("Enter 1 to view your existing schedules.\n"
                                      + "Enter 2 to create a new schedule.\n"
                                      + "Enter 3 to exit Day Keeper.\n")
        if mainMenuSelection == "1":
                UserInput.chooseExistingSchedule()
                    
        elif mainMenuSelection == "2":
                UserInput.makeSchedule()
        elif mainMenuSelection == "3":
            return
                    
    
    
    def makeSchedule():
            uInDate = input("Great! Enter a date in the form of MM-DD-YYYY to create a schedule for that day.")
            while(not uInDate[6::].isdigit() or not int(uInDate[6::]) > 1000 #year conditions 
                  or not uInDate[0:2].isdigit() or not int(uInDate[0:2]) > 0 or not int(uInDate[0:2]) < 13
                  or not uInDate[3:5].isdigit() or not int(uInDate[3:5]) > 0 or not int(uInDate[3:5]) < 32
                  or int(uInDate[0:2]) == 1 and not int(uInDate[3:5]) <= 31 #month-specific conditions for day dates
                  or int(uInDate[0:2]) == 2 and not int(uInDate[3:5]) <= 29
                  or int(uInDate[0:2]) == 3 and not int(uInDate[3:5]) <= 31
                  or int(uInDate[0:2]) == 4 and not int(uInDate[3:5]) <= 30
                  or int(uInDate[0:2]) == 5 and not int(uInDate[3:5]) <= 31
                  or int(uInDate[0:2]) == 6 and not int(uInDate[3:5]) <= 30
                  or int(uInDate[0:2]) == 7 and not int(uInDate[3:5]) <= 31
                  or int(uInDate[0:2]) == 8 and not int(uInDate[3:5]) <= 31
                  or int(uInDate[0:2]) == 9 and not int(uInDate[3:5]) <= 30
                  or int(uInDate[0:2]) == 10 and not int(uInDate[3:5]) <= 31
                  or int(uInDate[0:2]) == 11 and not int(uInDate[3:5]) <= 30
                  or int(uInDate[0:2]) == 12 and not int(uInDate[3:5]) <= 31
                  or len(uInDate) != 10):
                print("Ensure that you are entering a valid date in the form of MM-DD-YYYY.")
                uInDate = input("Enter a date in the form of MM-DD-YYYY to create a schedule for that day.\n")
                
            tempStack = DayStack(datetime.date(int(uInDate[6::]),int(uInDate[0:2]),int(uInDate[3:5])))
            
            unFinished = True
            while True:
                if len(tempStack.schedule) > 0 and unFinished == True:
                    addMore = input("Enter 1 to continue adding to this schedule, \n"
                                    + "Enter 2 to save this schedule and return to the main menu.\n"
                                    + "Enter 3 to scrap this schedule and return to the main menu. \n")
                    if addMore == "1":
                        unFinished = False
                    elif addMore == "2":
                        tempStack.saveStack(tempStack)
                        UserInput.mainMenu()
                        break
                    elif addMore == "3":
                        UserInput.mainMenu()
                        break
                    
                unFinished = True
                tempStack.addEvent(Event(UserInput.askforEvent(),UserInput.askforTime()))
                tempStack.viewSchedule()
            
        
        




UserInput.mainMenu() #Begin the program using user input from console

