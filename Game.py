# coding=utf-8
import time
import os
import random
import sys
import msvcrt
from Map import mapResetter
from Map import mapFresh
from Map import mapSaver
from Map import mapLoad
from Vars import gameVars
import durability

print(os.getcwd())
print("1.To change location;\n2.Create a totally fresh map or any other key to skip it\n  ")

Opt = raw_input()
#while(Opt != '1' or Opt != '2'):
if Opt == '1':
	mapResetter.mapCreator(os.getcwd())
	mapLoad.load(os.getcwd())
elif Opt == '2':
	mapFresh.mapfreshCreator()
	mapLoad.load(os.getcwd())
elif Opt == '3':
	retVal = durability.decreaseDurability(1,0,0,0,0,0)
	if(retVal == True) :
		print("we have durability!")
	else:
		print("no weapon!")
else:
	mapLoad.load(os.getcwd())

#	Opt = raw_input()
	
	
toSpawn = 0
print(Opt);
while gameVars.misc_people > 0:
	if toSpawn == 5:
		typeSpawn = random.randint(0, 1)
		if typeSpawn == 0:
			gameVars.pecuary_pig += 1
			toSpawn == 0
		elif typeSpawn == 1:
			gameVars.pecuary_cow += 1
			toSpawn == 0
	
	os.system("cls")
	What_toDo = raw_input ("Choose with the repective number:\n1.Chop down trees\n2.Slaughter an animal\n3.Go to a cave\n4.Check stats\n"
					   "5.Save game\n6.Build something\n7.Craft something\n8.Smelt something\n")
	if What_toDo == '2':
		animalChoice = raw_input("Do you want to kill:\n\n1.Pig\n2.Cow\n>>  ")
		if gameVars.misc_stoneSword[0] >= 1 or gameVars.misc_ironSword[0] >= 1:
			if gameVars.pecuary_pig >= 1 and animalChoice == '1':
				weapon = raw_input("What weapon would you like to use?\n\n1.Stone sword\n2.Iron sword\n>>")	
				if weapon == "1" and gameVars.misc_stoneSword[0] > 0:	
					print ("You killed a pig and managed to salvage 5kgs of meat!")
					gameVars.consumables_food += 5
					gameVars.pecuary_pig -= 1
					gameVars.consumables_food -= 1
					toSpawn += 1
					time.sleep(3)
					durability.decreaseDurability(1,0,0,0,0,0)
					os.system("cls")
				elif weapon == "2" and gameVars.misc_ironSword[0] > 0:
					print ("You killed a pig and managed to salvage 7kgs of meat!")
					gameVars.consumables_food += 7
					gameVars.pecuary_pig -= 1
					gameVars.consumables_food -= 1
					toSpawn += 1
					time.sleep(3)
					durability.decreaseDurability(0,1,0,0,0,0)
					os.system("cls")
		os.system("cls")
		if gameVars.misc_stoneSword[0] == 0 or gameVars.misc_ironSword[0] == 0:
			if gameVars.pecuary_pig == 0 and animalChoice == '1':
				print ("Go back please, you do not have a sword... or pigs to kill.")
			
		if gameVars.misc_stoneSword[0] >= 1 or gameVars.misc_ironSword[0] >= 1:
			if gameVars.pecuary_cow >= 1 and animalChoice == '2':
				weapon = raw_input("What weapon would you like to use?\n\n1.Stone sword\n2.Iron sword\n>>")
				if weapon == "1" and gameVars.misc_stoneSword[0] > 0:
					print ("You killed a cow and salvaged 7kgs of meat!")
					gameVars.consumables_food += 7
					gameVars.pecuary_cow -= 1
					gameVars.consumables_food -= 1
					toSpawn += 1
					time.sleep(3)
					durability.decreaseDurability(1,0,0,0,0,0)
					os.system("cls")
				if weapon == "2" and gameVars.misc_stoneSword[0] > 0:
					print ("You killed a cow and salvaged 9kgs of meat!")
					gameVars.consumables_food += 9
					gameVars.pecuary_cow -= 1
					gameVars.consumables_food -= 1
					toSpawn += 1
					time.sleep(3)
					durability.decreaseDurability(0,1,0,0,0,0)
					os.system("cls")
		os.system("cls")
		if gameVars.misc_stoneSword[0] == 0 or gameVars.misc_ironSword[0] == 0:
			if gameVars.pecuary_cow == 0 and animalChoice == '2':
				print("Go back please, you do not have a sword... or cows to kill.")
		os.system("cls")

	if What_toDo == '1':
		if gameVars.misc_stoneAxe[0] >= 1 or gameVars.misc_ironAxe[0] >= 1:
			which_treeChoice1 = raw_input ("Click 'a' to chop an apple tree or 'p' to chop a pine tree>>  ")
			if which_treeChoice1 == 'a' and gameVars.forest_appleTree >= 1:
				tool = raw_input("Which tool do you wish to use?\n1.Stone axe\n2.Iron axe")
				if tool == "1" and gameVars.misc_stoneAxe[0] > 0:
					print ("You chopped an apple tree, and from under the leaves you got 1kg of apples and 6kgs of wood from it!")
					gameVars.consumables_food += 3
					gameVars.misc_wood += 6
					gameVars.forest_appleTree -= 1
					gameVars.consumables_food -= 1
					toSpawn += 1
					durability.decreaseDurability(0,0,1,0,0,0)
				elif tool == "2" and gameVars.misc_stoneAxe[0] > 0:
					print ("You chopped an apple tree, and from under the leaves you got 3kgs of apples and 8kgs of wood from it!")
					gameVars.consumables_food += 5
					gameVars.misc_wood += 8
					gameVars.forest_appleTree -= 1
					gameVars.consumables_food -= 1
					toSpawn += 1
					durability.decreaseDurability(0,0,0,1,0,0)
			elif which_treeChoice1 == 'a' and gameVars.forest_appleTree == 0:
				print ("You do not have an apple tree to chop!")
			if which_treeChoice1 == 'p' and gameVars.forest_pineTree >= 1:
				print ("You have successfully chopped a pine tree! You got 7 wood points from it!")
				gameVars.misc_wood += 7
				gameVars.forest_pineTree -= 1
				gameVars.consumables_food -= 1
				toSpawn += 1
			elif which_treeChoice1 == 'p' and gameVars.forest_pineTree == 0:
				print ("You do not have a pine tree to chop!")
			time.sleep(3)
			os.system("cls")
		if gameVars.misc_stoneAxe[0] == 0 and gameVars.misc_ironAxe[0] == 0:
			print ("You do not have an axe to chop a tree!")
			time.sleep(3)
			os.system("cls")
			
	if What_toDo == '3':
		if gameVars.misc_stonePickaxe[0] >= 1 or gameVars.misc_ironPickaxe[0] >= 1:
			gameVars.iron_found = random.randint(4, 9)
			gameVars.stone_found = random.randint(2, 15)
			print ("You have struck", gameVars.iron_found, "iron and", gameVars.stone_found, "stone!")
			gameVars.misc_iron += gameVars.iron_found
			gameVars.misc_stone += gameVars.stone_found
			gameVars.consumables_food -= 3
		elif gameVars.misc_stonePickaxe[0] == 0 or gameVars.misc_ironPickaxe[0] == 0:
			print ("I'm sorry but you don't seem to have any pickaxes!")
		time.sleep(3)
		os.system("cls")
		toSpawn += 1
		
	if What_toDo == '5':
		mapSaver.saver(os.getcwd())
		time.sleep(3)
		os.system("cls")
		
	if What_toDo == '4':
		print ("You have:\nMaterials - ", gameVars.misc_stone, "stone;\n\t    ", gameVars.misc_iron, "iron;\n\t    ", gameVars.misc_ironSm, "smelted iron;\n\t    ", gameVars.misc_stoneSm, "smelted stone;\n\t    ", gameVars.misc_wood, "wood;\nHuman resources - ", gameVars.misc_people, "people;\n\t\t  ", gameVars.consumables_food, "food;\nTools - 1st index is ammount\n\t2nd index is durability\n        ", gameVars.misc_stoneAxe, "stone axe(s);\n\t",
		gameVars.misc_ironAxe, "iron axe(s);\n\t", gameVars.misc_stoneSword, "stone sword(s);\n\t", gameVars.misc_ironSword, "iron sword(s);\n\t", gameVars.misc_stonePickaxe, "stone pickaxe(s);\n\t",
		gameVars.misc_ironPickaxe, "iron pickaxe(s);\nMap - ", gameVars.forest_pineTree, "pine trees;\n      ", gameVars.forest_appleTree, "apple trees;\n      ", gameVars.pecuary_pig,
		"pigs;\n      ", gameVars.pecuary_cow, "cows;\n      ", gameVars.constructions_pplHouse, "house(s);\n      ", gameVars.constructions_craftingForge, "crafting forge(s);\n      ", gameVars.constructions_prodPecuary,
		"pecuary house(s);\n      ", gameVars.constructions_smeltingForge, "smelting forge(s).\n\n")
		raw_input()
	
	if What_toDo == '6':
		what_toBuild = raw_input ("What do you want to build? (choose with the first letter of each word (not numbers)):\n1 A house for 29 wood;\n"
								"2 An animal pecuary house for 60 wood;\n3 A smelting forge for 40 stone;\n4 A crafting forge for 50 stone.\n")
		if what_toBuild == '1':
			if gameVars.misc_wood >= 29:
				gameVars.constructions_pplHouse += 1
				gameVars.misc_wood -= 29
				print ("Successfully built!")
				gameVars.consumables_food -= 4
				toSpawn += 1
			elif gameVars.misc_wood < 29:
				print ("Go get some wood!!!")
				
		if what_toBuild == '2':
			if gameVars.misc_wood >= 60:
				gameVars.constructions_prodPecuary += 1
				gameVars.misc_wood -=60
				gameVars.consumables_food -= 7
				toSpawn += 1
			elif gameVars.misc_wood < 60:
				print ("Go get some wood!!!")
		
		if what_toBuild == '3':
			if gameVars.misc_stone >= 40:
				gameVars.constructions_smeltingForge += 1
				gameVars.misc_stone -= 40
				gameVars.consumables_food -= 10
				toSpawn += 1
			elif gameVars.misc_stone < 40:
				print ("Go get some stone!!!")
		
		if what_toBuild == '4':
			if gameVars.misc_stone >= 50:
				gameVars.constructions_craftingForge += 1
				gameVars.misc_stone -= 50
				gameVars.consumables_food -= 1
				toSpawn += 1
			elif gameVars.misc_stone < 50:
				print ("Go get some stone!!!")
		time.sleep(3)
		os.system("cls")

	if What_toDo == '7':
		what_toCraft = raw_input ("What do you want to craft? (choose with the first letter of each word):\n"
							  "A stone sword for 50 smelted stone;\n An iron sword for 125 smelted iron;\nA stone axe for 60 smelted stone;\n"
							  "An iron axe for 80 smelted iron;\nA stone pickaxe for 130 smelted stone;\nAn iron pickaxe for 180 smelted iron.\n")
		if what_toCraft == 'assfss' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_stoneSm >= 50:
				gameVars.misc_stoneSword[0] += 1
				gameVars.misc_stoneSword[1] += 5
				gameVars.misc_stoneSwordDurSet += 5
				gameVars.misc_stoneSm -= 50
				gameVars.consumables_food -= 10
				durability.decreaseDurability(True, False, False, False, False, False)
				toSpawn += 1
			elif gameVars.misc_stoneSm < 50:
				print ("Go get more smelted stone!!!")
			time.sleep(3)
			os.system("cls")
		if what_toCraft == 'asafss' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_stoneSm >= 60:
				gameVars.misc_stoneAxe[0] += 1
				gameVars.misc_stoneAxe[1] += 6
				gameVars.misc_stoneAxeDurSet += 6
				gameVars.misc_stoneSm -= 60
				gameVars.consumables_food -= 5
				durability.decreaseDurability(False, False, True, False, False, False)
				toSpawn += 1
			elif gameVars.misc_stoneSm < 60:
				print ("Go get more smelted stone!!!")
			time.sleep(3)
			os.system("cls")
		if what_toCraft == 'aspfss' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.gameVars.misc_stoneSm >= 130:
				gameVars.misc_stonePickaxe[0] += 1
				gameVars.misc_stonePickaxe[1] += 10
				gameVars.misc_stonePickaxeDurSet += 10
				gameVars.misc_stoneSm -= 130
				gameVars.consumables_food -= 8
				durability.decreaseDurability(False, False, False, False, True, False)
				toSpawn += 1
			elif gameVars.misc_stoneSm < 130:
				print ("Go get more smelted stone!!!")
			time.sleep(3)
			os.system("cls")

		if what_toCraft == 'aisfsi' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_ironSm >= 125:
				gameVars.misc_ironSword[0] += 1
				gameVars.misc_ironSword[1] += 8
				gameVars.misc_ironSwordDurSet += 8
				gameVars.misc_ironSm -= 125
				gameVars.consumables_food -= 20
				durability.decreaseDurability(False, True, False, False, False, False)
				toSpawn += 1
			elif gameVars.misc_ironSm < 125:
				print ("Go get more smelted iron!!!")
			time.sleep(3)
			os.system("cls")
		if what_toCraft == 'aiafsi' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_ironSm >= 80:
				gameVars.misc_ironAxe[0] += 1
				gameVars.misc_ironAxe[1] += 9
				gameVars.misc_ironAxeDurSet += 9
				gameVars.misc_ironSm -= 80
				gameVars.consumables_food -= 15
				durability.decreaseDurability(False, False, False, True, False, False)
				toSpawn += 1
			elif gameVars.misc_ironSm < 80:
				print ("Go get more smelted iron!!!")
			time.sleep(3)
			os.system("cls")
		if what_toCraft == 'aipfsi' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_ironSm >= 180:
				gameVars.misc_ironPickaxe[0] += 1
				gameVars.misc_ironPickaxe[1] += 15
				gameVars.misc_ironPickaxeDurSet += 15
				gameVars.misc_ironSm -= 180
				gameVars.consumables_food -= 13
				durability.decreaseDurability(False, False, False, False, False, True)
				toSpawn += 1
			elif gameVars.misc_ironSm < 180:
				print ("Go get more smelted iron!!!")
			time.sleep(3)
			os.system("cls")
	
	if What_toDo == '8':
		what_toSmelt = raw_input ("What do you want to smelt?:\n"
							  "1.Smelt iron;\n2.Smelt stone.\n")
		if what_toSmelt == '1':
			if gameVars.constructions_smeltingForge >= 1 and gameVars.misc_iron >= 1:
				howm_ironSmelt = raw_input ("How much iron do you pretend to smelt?")
				howm_ironSmelt_int = int(howm_ironSmelt)
				if misc_iron >= howm_ironSmelt_int:
					for number in range(howm_ironSmelt_int):
						gameVars.misc_ironSm += 1
						gameVars.misc_iron -= 1
						print ("Smelted successfully!")
						gameVars.consumables_food -= 1
						toSpawn += 1
				elif gameVars.misc_iron < howm_ironSmelt_int:
					print("Come back when you have decided to enter less or as many iron as you have!!!")
			elif gameVars.constructions_smeltingForge == 0 or gameVars.misc_iron == 0:
				print("Come back when you have at least 1 iron!!! Or when you have a smelting forge...")
			
		
		if what_toSmelt == '2':
			if gameVars.constructions_smeltingForge >= 1 and gameVars.misc_stone >= 1:
				howm_stoneSmelt = raw_input ("How much stone do you pretend to smelt?")
				howm_stoneSmelt_int = int(howm_stoneSmelt)
				if gameVars.misc_stone >= howm_stoneSmelt_int:
					for number in range(howm_stoneSmelt_int):
						gameVars.misc_stoneSm += 1
						gameVars.misc_stone -= 1
						print ("Smelted successfully!")
						gameVars.consumables_food -= 1
						toSpawn += 1
				elif gameVars.misc_stone < howm_stoneSmelt_int:
					print("Come back when you have decided to enter less or as many stone as you have!!!")
			elif gameVars.constructions_smeltingForge == 0 or gameVars.misc_stone == 0:
				print("Come back when you have at least 1 stone!!! Or when you have a smelting forge...")


	#-----Funcionalidades-----


	#if consumables_food == 0:
		#people
