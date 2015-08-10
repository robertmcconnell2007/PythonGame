from Vars import gameVars
def attemptDestroy():
	print("Attempting to destroy")
	print(gameVars.misc_stoneAxe[0])
	print(gameVars.misc_stoneAxe[1])
	print(gameVars.misc_stoneAxeDurSet)
	if(gameVars.misc_stoneSword[1] == 0):
		gameVars.misc_stoneSword[0] -= 1
		if gameVars.misc_stoneSword[0] > 0:
			gameVars.misc_stoneSword[1] = gameVars.misc_stoneSwordDurSet
		if(gameVars.misc_stoneSword[0] < 0):
			gameVars.misc_stoneSword[0] = 0
			
	elif (gameVars.misc_ironSword[1] == 0):
		gameVars.misc_ironSword[0] -= 1
		gameVars.misc_ironSword[1] = gameVars.misc_ironSwordDurSet
		if gameVars.misc_ironSword[0] > 0:
			gameVars.misc_ironSword[1] = gameVars.misc_ironSwordDurSet
		if(gameVars.misc_ironSword[0] < 0):
			gameVars.misc_ironSword[0] = 0
	
	elif (gameVars.misc_stoneAxe[1] == 0):
		gameVars.misc_stoneAxe[0] -= 1
		gameVars.misc_stoneAxe[1] = gameVars.misc_stoneAxeDurSet
		if gameVars.misc_stoneAxe[0] > 0:
			gameVars.misc_stoneAxe[1] = gameVars.misc_stoneAxeDurSet
		if(gameVars.misc_stoneAxe[0] < 0):
			gameVars.misc_stoneAxe[0] = 0
			
	elif (gameVars.misc_ironAxe[1] == 0):
		gameVars.misc_ironAxe[0] -= 1
		gameVars.misc_ironAxe[1] = gameVars.misc_ironAxeDurSet
		if gameVars.misc_ironAxe[0] > 0:
			gameVars.misc_ironAxe[1] = gameVars.misc_ironAxeDurSet
		if(gameVars.misc_ironAxe[0] < 0):
			gameVars.misc_ironAxe[0] = 0
			
	elif (gameVars.misc_stonePickaxe[1] == 0):
		gameVars.misc_stonePickaxe[0] -= 1
		gameVars.misc_stonePickaxe[1] = gameVars.misc_stonePickaxeDurSet
		if gameVars.misc_stonePickaxe[0] > 0:
			gameVars.misc_stonePickaxe[1] = gameVars.misc_stonePickaxeDurSet
		if(gameVars.misc_stonePickaxe[0] < 0):
			gameVars.misc_stonePickaxe[0] = 0
			
	elif (gameVars.misc_ironPickaxe[1] == 0):
		gameVars.misc_ironPickaxe[0] -= 1
		gameVars.misc_ironPickaxe[1] = gameVars.misc_ironPickaxeDurSet
		if gameVars.misc_ironPickaxe[0] > 0:
			gameVars.misc_ironPickaxe[1] = gameVars.misc_ironPickaxeDurSet
		if(gameVars.misc_ironPickaxe[0] < 0):
			gameVars.misc_ironPickaxe[0] = 0

def decreaseDurability(stoneSword, ironSword, stoneAxe, ironAxe, stonePickaxe, ironPickaxe):
	if stoneSword == 1:
		gameVars.misc_stoneSword[1] -= 1
		
	elif ironSword == 1:
		gameVars.misc_ironSword[1] -= 1
		
	elif stoneAxe == 1:
		gameVars.misc_stoneAxe[1] -= 1
	
	elif ironSword == 1:
		gameVars.misc_ironAxe[1] -= 1
	
	elif stonePickaxe == 1:
		gameVars.misc_stonePickaxe[1] -= 1
	
	elif ironPickaxe == 1:
		gameVars.misc_ironPickaxe[1] -= 1
	attemptDestroy()
		
