import datetime
import math

def duedateCalc(year, month, day, hour):
    timeRemaining = datetime.datetime(year=year, month=month, day=day, hour=hour) - datetime.datetime.now()
    return timeRemaining
def TKalgorithm(due, size):
    due = 0
    size = 0

duedateCalc(2014, 11, 2, 12)
