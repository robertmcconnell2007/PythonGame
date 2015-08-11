from Vars import gameVars

def decreaseDurability(stoneSword, ironSword, stoneAxe, ironAxe, stonePickaxe, ironPickaxe):
	if stoneSword == 1:
		print("Stone sword Durability Check!");
		print(gameVars.misc_stoneSword[0]);
		#Do I have a stoneSword?
		if(gameVars.misc_stoneSword[0] >0):
			#reduce durability by 1
			gameVars.misc_stoneSword[1] -= 1
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_stoneSword[1] <= 0):
				gameVars.misc_stoneSword[1] = gameVars.misc_stoneSwordDurSet
				gamevars.misc_stoneSword[0] -= 1;
				return True;
		else:
			print("False!")
			return False
		
	elif ironSword == 1:
		#Do I have a stoneSword?
		if(gameVars.misc_ironSword[0] >0):
			#reduce durability by 1
			gameVars.misc_ironSword[1] -= 1
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_ironSword[1] <= 0):
				gameVars.misc_stoneSword[1] = gameVars.misc_ironSwordDurSet
				gamevars.misc_ironSword[0] -= 1;
				return True;
		else:
			return False
		
	elif stoneAxe == 1:
		#Do I have a stoneSword?
		if(gameVars.misc_stoneAxe[0] >0):
			#reduce durability by 1
			gameVars.misc_stoneAxe[1] -= 1
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_stoneAxe[1] <= 0):
				gameVars.misc_stoneSword[1] = gameVars.misc_stoneAxeDurSet
				gamevars.misc_stoneAxe[0] -= 1;
				return True;
		else:
			return False
	
	elif ironAxe == 1:
		#Do I have a stoneSword?
		if(gameVars.misc_ironAxe[0] >0):
			#reduce durability by 1
			gameVars.misc_ironAxe[1] -= 1
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_ironAxe[1] <= 0):
				gameVars.misc_stoneSword[1] = gameVars.misc_ironAxeDurSet
				gamevars.misc_ironAxe[0] -= 1;
				return True;
		else:
			return False
	
	elif stonePickaxe == 1:
		#Do I have a stoneSword?
		if(gameVars.misc_stonePickaxe[0] >0):
			#reduce durability by 1
			gameVars.misc_stonePickaxe[1] -= 1
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_stonePickaxe[1] <= 0):
				gameVars.misc_stoneSword[1] = gameVars.misc_stonePickaxeDurSet
				gamevars.misc_stonePickaxe[0] -= 1;
				return True;
		else:
			return False
	
	elif ironPickaxe == 1:
		#Do I have a stoneSword?
		if(gameVars.misc_ironPickaxe[0] >0):
			#reduce durability by 1
			gameVars.misc_ironPickaxe[1] -= 1
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_ironPickaxe[1] <= 0):
				gameVars.misc_stoneSword[1] = gameVars.misc_ironPickaxeDurSet
				gamevars.misc_ironPickaxe[0] -= 1;
				return True;
		else:
			return False
	
	

		
