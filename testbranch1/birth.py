from random import randint
from Vars import gameVars
def amount(x):
	gameVars.misc_people += x
def birth():
	#says if they had children
	a = randint(1, 20)
	b = randint(1, 2)
	if(a == 1) and gameVars.constructions_pplHouse * 5 >= gameVars.misc_people + 2:
		amount(b)
		print("Someone's been bangin'!" + str(b) + " baby(ies) were born!")
