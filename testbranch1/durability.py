from Vars import gameVars

def decreaseDurability(durabilityLoss, stoneSword, ironSword, stoneAxe, ironAxe, stonePickaxe, ironPickaxe):
	if stoneSword == 1:
		#print("Stone sword Durability Check!");
		#print(gameVars.misc_stoneSword[0]);
		#print(gameVars.misc_stoneSword[1]);
		#Do I have a stoneSword?
		if(gameVars.misc_stoneSword[0] >0):
			#reduce durability by 1
			print("Old stone sword durability: " + str(gameVars.misc_stoneSword[1]))
			gameVars.misc_stoneSword[1] -= durabilityLoss
			print("new stone sword durability: " + str(gameVars.misc_stoneSword[1]))
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_stoneSword[1] <= 0):
				print("Stone sword has broke!")
				gameVars.misc_stoneSword[1] = gameVars.misc_stoneSwordDurSet
				gameVars.misc_stoneSword[0] -= 1
				print("Stone swords remaining: " + str(gameVars.misc_stoneSword[0]))
			return True;
		else:
			print("False!")
			return False
		
	elif ironSword == 1:
		#print("iron sword Durability Check!");
		#print(gameVars.misc_ironSword[0]);
		#print(gameVars.misc_ironSword[1]);
		#Do I have a ironSword?
		if(gameVars.misc_ironSword[0] >0):
			#reduce durability by 1
			print("Old iron sword durability: " + str(gameVars.misc_ironSword[1]))
			gameVars.misc_ironSword[1] -= 1
			print("New iron sword durability: " + str(gameVars.misc_ironSword[1]))
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_ironSword[1] <= 0):
				print("Iron sword has broke!")
				gameVars.misc_ironSword[1] = gameVars.misc_ironSwordDurSet
				gameVars.misc_ironSword[0] -= 1;
				print("Iron swords remaining: " + str(gameVars.misc_ironSword[0]))
			return True;
		else:
			return False
		
	elif stoneAxe == 1:
		#print("Stone axe Durability Check!");
		#print(gameVars.misc_stoneAxe[0]);
		#print(gameVars.misc_stoneAxe[1]);
		#Do I have a stoneAxe?
		if(gameVars.misc_stoneAxe[0] >0):
			#reduce durability by 1
			print("Old stone axe durability: " + str(gameVars.misc_stoneAxe[1]))
			gameVars.misc_stoneAxe[1] -= durabilityLoss
			print("New stone axe durability: " + str(gameVars.misc_stoneAxe[1]))
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_stoneAxe[1] <= 0):
				print("Stone axe has broken!")
				gameVars.misc_stoneAxe[1] = gameVars.misc_stoneAxeDurSet
				gameVars.misc_stoneAxe[0] -= 1;
				print("Stone axes remaining: " + str(gameVars.misc_stoneAxe[0]))
			return True;
		else:
			return False
	
	elif ironAxe == 1:
		#print("Iron axe Durability Check!");
		#print(gameVars.misc_ironAxe[0]);
		#print(gameVars.misc_ironAxe[1]);
		#Do I have a ironAxe?
		if(gameVars.misc_ironAxe[0] >0):
			#reduce durability by 1
			print("Old iron axe durability: " + str(gameVars.misc_ironAxe[1]))
			gameVars.misc_ironAxe[1] -= durabilityLoss
			print("Old iron axe durability: " + str(gameVars.misc_ironAxe[1]))
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_ironAxe[1] <= 0):
				print("Iron pickaxe has broken!")
				gameVars.misc_ironAxe[1] = gameVars.misc_ironAxeDurSet
				gameVars.misc_ironAxe[0] -= 1;
				print("Iron pickaxes remaining: " + str(gameVars.misc_ironAxe[0]))
			return True;
		else:
			return False
	
	elif stonePickaxe == 1:
		#print("Stone Pickaxe Durability Check!");
		#print(gameVars.misc_stonePickaxe[0]);
		#print(gameVars.misc_stonePickaxe[1]);
		#Do I have a stonePickaxe?
		if(gameVars.misc_stonePickaxe[0] >0):
			#reduce durability by 1
			print("Old stone pickaxe durability: " + str(gameVars.misc_stonePickaxe[1]))
			gameVars.misc_stonePickaxe[1] -= durabilityLoss
			print("Old stone pickaxe durability: " + str(gameVars.misc_stonePickaxe[1]))
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_stonePickaxe[1] <= 0):
				print("Stone pickaxe has broken!")
				gameVars.misc_stonePickaxe[1] = gameVars.misc_stonePickaxeDurSet
				gameVars.misc_stonePickaxe[0] -= 1;
				print("Stone pickaxes remaining: " + str(gameVars.misc_stonePickaxe[0]))
			return True;
		else:
			return False
	
	elif ironPickaxe == 1:
		#print("Iron Pickaxe Durability Check!");
		#print(gameVars.misc_ironPickaxe[0]);
		#print(gameVars.misc_ironPickaxe[1]);
		#Do I have a ironPickaxe?
		if(gameVars.misc_ironPickaxe[0] >0):
			#reduce durability by 1
			print("Old iron pickaxe durability: " + str(gameVars.misc_ironPickaxe[1]))
			gameVars.misc_ironPickaxe[1] -= durabilityLoss
			print("New iron pickaxe durability: " + str(gameVars.misc_ironPickaxe[1]))
			#if durability is <= 0...need to break the weapon...
			if(gameVars.misc_ironPickaxe[1] <= 0):
				print("Iron pickaxe has broken!")
				gameVars.misc_ironPickaxe[1] = gameVars.misc_ironPickaxeDurSet
				gameVars.misc_ironPickaxe[0] -= 1;
				print("Iron pickaxes remaining: " + str(gameVars.misc_ironPickaxe[0]))
			return True;
		else:
			return False
	
	

		
