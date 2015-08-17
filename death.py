from random import randint
from Vars import gameVars
def casualties(x):
	gameVars.misc_people -= x
def wolfpack():
	#wolves are atracted by cattle produced in this building
	if(gameVars.constructions_prodPecuary >= 1):
		#chance = randint(1, 30)
		if(randint(1, 30) == 1):
			casualties(randint(1, 3))
			print("A wolf pack has attacked you and " + str(a) + " people have died!")
	else:
                #chance = randint(1, 40)
		if(randint(1, 40) == 1):
			casualties(randint(0, 2))
			print("A wolf pack has attacked you and " + str(a) + " people have died!")
def whichEvent():
	#checks if starving
	if(gameVars.consumables_food <= 0):
		a = randint(1, 2)
		gameVars.misc_people -= a;
		print("Your colony is starving! " + str(a) + " people have died!")
	a = randint(1, 1)
	#generates events
	if(a == 1):
                wolfpack()
