import time
from Vars import gameVars

def nextDay():
	gameVars.totalDayCounter += 1
	gameVars.consumables_food -= gameVars.misc_people / 2
	i = 0
	while i <= 5:
		if gameVars.dayCounterActivated[i] == True:
			gameVars.dayCounter[i] += 1
		i += 1
	
def setCounter(index, days):
	gameVars.dayCounterNeeded[index] = days
	
def setCounterDetails(index, details):
	gameVars.dayCounterDetails[index] = details 
	
def resetCounter(index):
	gameVars.dayCounter[index] = 0
	gameVars.dayCounterNeeded[index] = 0
	gameVars.dayCounterActivated[index] = 0
	
def resetCounterDetails(index):
	gameVars.dayCounterDetails[index] = ""