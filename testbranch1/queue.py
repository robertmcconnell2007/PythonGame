from Vars import gameVars
import durability
import clock


def treeRewards(wood, tree):
	if(tree == "pine"):
		gameVars.forest_pineTree -= 1
	elif(tree == "apple"):
		gameVars.forest_appleTree -= 1
	gameVars.misc_wood += wood
	gameVars.toSpawn += 1

def queue():
	i = 0
	while i <= 5:
		if gameVars.dayCounter[i] == gameVars.dayCounterNeeded[i]:
			if gameVars.dayCounterDetails[i] == "appletree stoneaxe":
				print ("\n\nYou chopped an apple tree, and under the leaves you found 3kgs of apples and 6kgs of wood!\n\n")
				treeRewards(6, "apple")
				durability.decreaseDurability(1,0,0,1,0,0,0)
				gameVars.consumables_food += 3
			elif gameVars.dayCounterDetails[i] == "appletree ironaxe":
				print ("\n\nYou chopped an apple tree, and under the leaves you found 5kgs of apples and 8kgs of wood!\n\n")
				treeRewards(8, "apple")
				durability.decreaseDurability(1,0,0,0,1,0,0)
				gameVars.consumables_food += 5
			clock.resetCounter(i)
			clock.resetCounterDetails(i)
		i += 1