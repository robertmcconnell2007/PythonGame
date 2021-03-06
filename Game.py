# coding=utf-8
import time
import os
import random
from Map import mapResetter
from Map import mapFresh
from Map import mapSaver
from Map import mapLoad
from Vars import gameVars
import death
import birth
import durability
import clock
import msvcrt as m
def wait():
    m.getch()

Opt = "-1"
while(Opt != '1' and Opt != '2' and Opt != '3'):
	print("1.To change location;\n2.New game\n3.Load game")
	Opt = input()
	if Opt == '1':
		mapResetter.mapCreator(os.getcwd())
		mapLoad.load(os.getcwd())
	elif Opt == '2':
		mapFresh.mapfreshCreator(os.getcwd())
		mapLoad.load(os.getcwd())
	#elif Opt == '3':
	#	retVal = durability.decreaseDurability(1,1,0,0,0,0,0)
	#	if(retVal == True) :
	#		print("we have durability!")
	#	else:
	#		print("no weapon!")
	elif Opt == '3':
		mapLoad.load(os.getcwd())

#	Opt = input()


toSpawn = 0
while gameVars.misc_people > 0:
	os.system("cls")

	if toSpawn == 5:
		typeSpawn = random.randint(0, 1)
		if typeSpawn == 0:
			gameVars.pecuary_pig += 1
			toSpawn = 0
		elif typeSpawn == 1:
			gameVars.pecuary_cow += 1
			toSpawn = 0

	death.whichEvent()
	birth.birth()
	print("\n")

	What_toDo = '-1'
	while What_toDo != '1' and What_toDo != '2' and What_toDo != '3' and What_toDo != '4' and What_toDo != '5' and What_toDo != '6' and What_toDo != '7' and What_toDo != '8' and What_toDo != '9':
		What_toDo = input("Choose with the repective number:\n1.Chop down trees\n2.Slaughter an animal\n3.Go to a cave\n4.Check stats\n5.Save game\n6.Build something\n7.Craft something\n8.Smelt something\n9.Show resources\n0.Next day!")

	#Refactored to use the updated durability function
	#Updated input blocks to use while loops to prevent users from inputting bad values.
	
	if What_toDo == '0':
		clock.nextDay(1)
	
	if What_toDo == '1':

		def treeRewards(wood, tree):
			if(tree == "pine"):
				gameVars.forest_pineTree -= 1
			elif(tree == "apple"):
				gameVars.forest_appleTree -= 1
			gameVars.misc_wood += wood
			toSpawn += 1

		which_treeChoice1 = '-1'
		while which_treeChoice1 != '1' and which_treeChoice1 != '2' and which_treeChoice1 != '3':
			which_treeChoice1 = input("Choose with the respective number:\n1.Chop an apple tree\n2.Chop a pine tree\n3.Cancel\n>>  ")
		if which_treeChoice1 == '1':
			if(gameVars.forest_appleTree > 0):
				tool = '-1'
				while(tool != '1' and tool != '2' and tool != '3'):
					tool = input("Which tool do you wish to use?\n1.Stone axe\n2.Iron axe\n3.Cancel\n>>  ")
				if tool == "1":
					if(durability.decreaseDurability(1,0,0,1,0,0,0) == True):
						print ("You chopped an apple tree, and under the leaves you found 3kgs of apples and 6kgs of wood!")
						treeRewards(6,"apple")
						durability.decreaseDurability(1,0,0,1,0,0,0)
						gameVars.consumables_food += 3
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have a Stone Axe! You need to craft another one.")
				elif tool == "2":
					if(durability.decreaseDurability(1,0,0,0,1,0,0) == True):
						print ("You chopped an apple tree, and under the leaves you found 5kgs of apples and 8kgs of wood!")
						treeRewards(8,"apple")
						durability.decreaseDurability(1,0,0,0,1,0,0)
						gameVars.consumables_food += 5
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have a Iron Axe! You need to craft another one.")
				elif tool == '3':
					print ("Ok...")
			else:
				print("There are no apple trees left!")
			time.sleep(3)
			os.system("cls")

		#still have to fix
		elif which_treeChoice1 == '2':
			if gameVars.forest_pineTree > 0:
				tool = '-1'
				while(tool != '1' and tool != '2' and tool != '3'):
					tool = input("Which tool do you wish to use?\n1.Stone axe\n2.Iron axe\n3.Cancel\n>>  ")
				if tool == "1":
					if(durability.decreaseDurability(1,0,0,1,0,0,0) == True):
						print ("You have successfully chopped a pine tree! You got 7 kgs of wood from it!")
						treeRewards(7, "pine")
						durability.decreaseDurability(1,0,0,1,0,0,0)
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have a Stone Axe! You need to craft another one")
				elif tool == "2":
					if(durability.decreaseDurability(1,0,0,0,1,0,0) == True):
						print ("You have successfully chopped a pine tree! You got 10 kgs wood from it!")
						treeRewards(10, "pine")
						durability.decreaseDurability(1,0,0,0,1,0,0)
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have a Iron Axe! You need to craft another one")
				elif tool == "3":
					print("Ok...")
			else:
				print ("You do not have a pine tree to chop!")

		elif(which_treeChoice1 == '3'):
			print("Ok...")
		time.sleep(3)
		os.system("cls")

	if What_toDo == '2':
		#just to make the code more readable and compact
		#------------------------------------------------
		def killRewards(food, animal):
			if(animal == "pig"):
				gameVars.pecuary_pig -= 1
			elif(animal == "cow"):
				gameVars.pecuary_cow -= 1
			gameVars.consumables_food += food
			toSpawn += 1
		#------------------------------------------------
		animalChoice = '-1'
		while(animalChoice != '1' and animalChoice != '2' and animalChoice != '3'):
			animalChoice = input("Do you want to kill:\n\n1.Pig\n2.Cow\n3.Cancel\n>>  ")
		if(animalChoice == '1'):
			if(gameVars.pecuary_pig > 0):
				weapon = '-1'
				while(weapon != '1' and weapon != '2' and weapon != '3'):
					weapon = input("What weapon would you like to use?\n\n1.Stone sword\n2.Iron sword\n3.Cancel\n>>  ")
				if weapon == "1":
					if durability.decreaseDurability(1,1,0,0,0,0,0) == True:
						print ("You killed a pig and managed to salvage 5kgs of meat!")
						killRewards(5, "pig")
						durability.decreaseDurability(1,1,0,0,0,0,0)
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have a stone sword! You need to craft a new one")
				elif weapon == "2":
					if durability.decreaseDurability(1,0,1,0,0,0,0) == True:
						print ("You killed a pig and managed to salvage 7kgs of meat!")
						killRewards(7, "pig")
						durability.decreaseDurability(1,0,1,0,0,0,0)
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have an iron sword! you need to craft a new one")
				elif weapon == "3":
					print("Ok...")
			else:
				print ("Pigs are extinct!")#or so you say.. :P

		#os.system("cls")
		elif(animalChoice == '2'):
			if gameVars.pecuary_cow > 0:
				weapon = '-1'
				while(weapon != '1' and weapon != '2' and weapon != '3'):
					weapon = input("What weapon would you like to use?\n\n1.Stone sword\n2.Iron sword\n3.Cancel\n>>  ")
				if weapon == "1":
					if(durability.decreaseDurability(1,1,0,0,0,0,0) == True):
						print ("You killed a cow and salvaged 7kgs of meat!")
						killRewards(6, "cow")
						durability.decreaseDurability(1,1,0,0,0,0,0)
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have a stone sword! You need to craft a new one")
				elif weapon == "2":
					if(durability.decreaseDurability(1,0,1,0,0,0,0) == True):
						print ("You killed a cow and salvaged 9kgs of meat!")
						killRewards(8, "cow")
						durability.decreaseDurability(1,0,1,0,0,0,0)
						gameVars.consumables_food -= gameVars.misc_people / 2
					else:
						print("You don't have an iron sword! you need to craft a new one")
				elif weapon == "3":
					print("Ok...")
			else:
				print("Cows are extinct!")#xD
		time.sleep(3)
		os.system("cls")

	if What_toDo == '3':
		which_pick = '-1'
		while which_pick != '1' and which_pick != '2':
			which_pick = input ("Which pick would you like to use?\n1. Stone pickaxe\n2. Iron pickaxe\n")
		if(which_pick == '1'):
			iron_vein = random.randint(10,30)
			stone_vein = random.randint(20,70)
			if(durability.decreaseDurability(1,0,0,0,0,1,0) == True):
				print("Mining...")
				time.sleep(3)
				print ("You have struck " + str(iron_vein) + " iron and " + str(stone_vein) + " stone!")
				gameVars.misc_iron += iron_vein
				gameVars.misc_stone += stone_vein
				gameVars.consumables_food -= 3
				toSpawn += 1
			else:
				print("You don't have a Stone Pickaxe! You need to craft another")
		elif(which_pick == '2'):
			iron_vein = random.randint(2,6)
			stone_vein = random.randint(4,15)
			if(durability.decreaseDurability(1,0,0,0,0,0,1) == True):
				print("Mining...")
				time.sleep(3)
				print ("You have struck " + str(iron_vein) + " iron and " + str(stone_vein) + " stone!")
				gameVars.misc_iron += iron_vein
				gameVars.misc_stone += stone_vein
				gameVars.consumables_food -= 3
				toSpawn += 1
			else:
				print("You don't have a Iron Pickaxe! You need to craft another")
		elif(which_pick == '3'):
			print("Ok...")
		time.sleep(3)
		os.system("cls")


	#Options 4, 5, 6, 7 and 8 have been refactored.
	if What_toDo == '4':
		print ("You have:\nMaterials - ", gameVars.misc_stone, "stone;\n\t    ", gameVars.misc_iron, "iron;\n\t    ", gameVars.misc_ironSm, "smelted iron;\n\t    ", gameVars.misc_stoneSm, "smelted stone;\n\t    ", gameVars.misc_wood, "wood;\nHuman resources - ", gameVars.misc_people, "people;\n\t\t  ", gameVars.consumables_food, "food;\nTools - 1st index is ammount\n\t2nd index is durability\n        ", gameVars.misc_stoneAxe, "stone axe(s);\n\t",
		gameVars.misc_ironAxe, "iron axe(s);\n\t", gameVars.misc_stoneSword, "stone sword(s);\n\t", gameVars.misc_ironSword, "iron sword(s);\n\t", gameVars.misc_stonePickaxe, "stone pickaxe(s);\n\t",
		gameVars.misc_ironPickaxe, "iron pickaxe(s);\nMap - ", gameVars.forest_pineTree, "pine trees;\n      ", gameVars.forest_appleTree, "apple trees;\n      ", gameVars.pecuary_pig,
		"pigs;\n      ", gameVars.pecuary_cow, "cows;\n      ", gameVars.constructions_pplHouse, "house(s);\n      ", gameVars.constructions_craftingForge, "crafting forge(s);\n      ", gameVars.constructions_prodPecuary,
		"pecuary house(s);\n      ", gameVars.constructions_smeltingForge, "smelting forge(s).\n\n")
		input()

	if What_toDo == '5':
		mapSaver.saver(os.getcwd())
		time.sleep(3)
		os.system("cls")

	if What_toDo == '6':
		what_toBuild = '-1'
		while what_toBuild != '1' and what_toBuild != '2' and what_toBuild != '3' and what_toBuild != '4' and what_toBuild != '5':
			  what_toBuild = input ("What do you want to build? (choose with the respective number and dont forget you will perish without enough food):\n1.A house for 30kgs of wood in 4 days;\n"
									"2.An animal house for 60kgs of wood in 7 days;\n3.A furnace for 40kgs of stone in 10 days;\n4.A forge for 50kgs of stone in 10 days.\n5.Cancel\n>>  ")
		if what_toBuild == '1':
			if gameVars.misc_wood >= 30:
				gameVars.constructions_pplHouse += 1
				gameVars.misc_wood -= 30
				print ("Successfully built a house.")
				gameVars.consumables_food -= 4
				toSpawn += 1
			elif gameVars.misc_wood < 30:
				print ("Go get some wood!!!")

		elif what_toBuild == '2':
			if gameVars.misc_wood >= 60:
				gameVars.constructions_prodPecuary += 1
				gameVars.misc_wood -=60
				print ("Successfully built an animal house.")
				gameVars.consumables_food -= 7
				toSpawn += 1
			elif gameVars.misc_wood < 60:
				print ("Go get some wood!!!")

		elif what_toBuild == '3':
			if gameVars.misc_stone >= 40:
				gameVars.constructions_smeltingForge += 1
				gameVars.misc_stone -= 40
				print ("Successfully built a furnace.")
				gameVars.consumables_food -= 10
				toSpawn += 1
			elif gameVars.misc_stone < 40:
				print ("Go get some stone!!!")

		elif what_toBuild == '4':
			if gameVars.misc_stone >= 50:
				gameVars.constructions_craftingForge += 1
				gameVars.misc_stone -= 50
				print ("Successfully built a forge.")
				gameVars.consumables_food -= 10
				toSpawn += 1
			elif gameVars.misc_stone < 50:
				print ("Go get some stone!!!")

		elif what_toBuild == '5':
			print("Ok...")
		time.sleep(3)
		os.system("cls")

	if What_toDo == '7':
		what_toCraft = '-1'
		while what_toCraft != '1' and what_toCraft != '2' and what_toCraft != '3' and what_toCraft != '4' and what_toCraft != '5' and what_toCraft != '6' and what_toCraft != '7':
			what_toCraft = input ("What do you want to craft? (choose with the respective number):\n"
								  "1.A stone sword for 50 smelted stone in 4 days;\n2.An iron sword for 125 smelted iron in 3 days;\n3.A stone axe for 60 smelted stone in 5 days;\n"
								  "4.An iron axe for 80 smelted iron in 4 days;\n5.A stone pickaxe for 130 smelted stone in 8 days;\n6.An iron pickaxe for 180 smelted iron in 7 days.\n"
								  "7.Cancel\n>>  ")
		if what_toCraft == '1' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_stoneSm >= 50:
				gameVars.misc_stoneSword[0] += 1
				gameVars.misc_stoneSword[1] += 5
				gameVars.misc_stoneSwordDurSet += 5
				gameVars.misc_stoneSm -= 50
				gameVars.consumables_food -= 4
				durability.decreaseDurability(True, False, False, False, False, False)
				toSpawn += 1
			elif gameVars.misc_stoneSm < 50:
				print ("Go get more smelted stone!!!")
		if what_toCraft == '2' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_ironSm >= 125:
				gameVars.misc_ironSword[0] += 1
				gameVars.misc_ironSword[1] += 8
				gameVars.misc_ironSwordDurSet += 8
				gameVars.misc_ironSm -= 125
				gameVars.consumables_food -= 3
				durability.decreaseDurability(False, True, False, False, False, False)
				toSpawn += 1
			elif gameVars.misc_ironSm < 125:
				print ("Go get more smelted iron!!!")
		if what_toCraft == '3' and gameVars.constructions_smeltingForge >= 1:
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

		if what_toCraft == '4' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_ironSm >= 80:
				gameVars.misc_ironAxe[0] += 1
				gameVars.misc_ironAxe[1] += 9
				gameVars.misc_ironAxeDurSet += 9
				gameVars.misc_ironSm -= 80
				gameVars.consumables_food -= 4
				durability.decreaseDurability(False, False, False, True, False, False)
				toSpawn += 1
			elif gameVars.misc_ironSm < 80:
				print ("Go smelt iron!!!")

		if what_toCraft == '5' and gameVars.constructions_smeltingForge >= 1:
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

		if what_toCraft == '6' and gameVars.constructions_smeltingForge >= 1:
			if gameVars.misc_ironSm >= 180:
				gameVars.misc_ironPickaxe[0] += 1
				gameVars.misc_ironPickaxe[1] += 15
				gameVars.misc_ironPickaxeDurSet += 15
				gameVars.misc_ironSm -= 180
				gameVars.consumables_food -= 7
				durability.decreaseDurability(False, False, False, False, False, True)
				toSpawn += 1
			elif gameVars.misc_ironSm < 180:
				print ("Go smelt iron!!!")

		if(what_toCraft == '7'):
			print("Ok...")
		time.sleep(3)
		os.system("cls")

	if What_toDo == '8':
		what_toSmelt = '-1'
		while what_toSmelt != '1' and what_toSmelt != '2' and what_toSmelt != '3':
			what_toSmelt = input ("What do you want to smelt?:\n1.Smelt iron;\n2.Smelt stone.\n3.Cancel\n>>  ")


		if what_toSmelt == '1':
			if gameVars.constructions_smeltingForge >= 1:
				if gameVars.misc_iron >= 1:
					howm_ironSmelt = input ("How much iron do you want to smelt in 1 day?\nYou have " + str(gameVars.misc_iron) + "\n>>  ")
					if howm_ironSmelt and int(howm_ironSmelt):
						howm_ironSmelt_int = int(howm_ironSmelt)
						if gameVars.misc_iron >= howm_ironSmelt_int:
							for number in range(howm_ironSmelt_int):
								gameVars.misc_ironSm += 1
								gameVars.misc_iron -= 1
							print("Successfully smelted " + howm_ironSmelt + " iron ore!")
							gameVars.consumables_food -= 1
							toSpawn += 1

						elif gameVars.misc_iron < howm_ironSmelt_int:
							gameVars.misc_ironSm += gameVars.misc_iron
					else:
						print("Enter a number.\n")
				else:
					print("Come back when you have at least 1 iron!!!")
			else:
				print("Come back when you have a furnace...")

		elif what_toSmelt == '2':
			if gameVars.constructions_smeltingForge >= 1:
				if gameVars.misc_stone >= 1:
					howm_stoneSmelt = input ("How much stone do you want to smelt in 1 day?\nYou have " + str(gameVars.misc_stone) + "\n>>  ")
					if howm_ironSmelt and int(howm_stoneSmelt):
						howm_stoneSmelt_int = int(howm_stoneSmelt)
						if gameVars.misc_stone >= howm_stoneSmelt_int:
							for number in range(howm_stoneSmelt_int):
								gameVars.misc_stoneSm += 1
								gameVars.misc_stone -= 1
							print ("Successfully smelted " + howm_ironSmelt + " stone!")
							gameVars.consumables_food -= 1
							toSpawn += 1
						elif gameVars.misc_stone < howm_stoneSmelt_int:
							gameVars.misc_stoneSm += gameVars.misc_stone
					else:
						print("Enter a number.\n")
				else:
					print("Come back when you have at least 1 stone!!!")
			else:
				print("Come back when you have a furnace...")

		elif what_toSmelt == '3':
			print("Ok...")
		time.sleep(3)
		os.system("cls")

	if What_toDo == '9':
		#Need to print out all of the resources to the user
		#Wait for the user to press a key to continue
		print("You have:")
		print("\tEquipment:")
		print("\t\tStone Sword: " + str(gameVars.misc_stoneSword[0]))
		print("\t\tIron Sword: " + str(gameVars.misc_ironSword[0]))
		print("\t\tStone Axe: " + str(gameVars.misc_stoneAxe[0]))
		print("\t\tIron Axe: " + str(gameVars.misc_ironAxe[0]))
		print("\t\tStone Pickaxe: " + str(gameVars.misc_stonePickaxe[0]))
		print("\t\tIron Pickaxe: " + str(gameVars.misc_ironPickaxe[0]))

		print("\tResources:")
		print("\t\tFood: " + str(gameVars.consumables_food))
		print("\t\tWood: " + str(gameVars.misc_wood))
		print("\t\tStone: " + str(gameVars.misc_stone))
		print("\t\tSmelted Stone: " + str(gameVars.misc_stoneSm))
		print("\t\tIron: " + str(gameVars.misc_iron))
		print("\t\tSmelted Iron: " + str(gameVars.misc_ironSm))
		print("Press any key to continue\n>>  ")
		wait()
		os.system("cls")
	
	##if What_toDo == '
	print("\n")
