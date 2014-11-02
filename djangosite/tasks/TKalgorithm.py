import datetime
import math

def duedateCalc(duedate):
    now = datetime.now()
    daysR = ((duedate.day - now.day) * 24) * 1.01 #everything in hours now
    hoursR = (duedate.hour - now.hour) * 1.01
    timeRemaining = daysR + hoursR
    return timeRemaining

def TKalgorithm(d1): #dictionary contains only one element
    due = 0.0
    size = 0.0
    due = duedateCalc(d1.due)
    size = d1.size
    amazingAlg = due + size
    return amazingAlg

def SortingDict(d2):
    newL = []
    for key in d2:
        priority = TKalgorithm(key)
        newL.append(priority, key)
    return newL

