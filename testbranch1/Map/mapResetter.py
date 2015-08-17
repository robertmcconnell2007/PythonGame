import random
import time
import os
from Vars import gameVars
#
def mapCreator(path):
    #recreates the map
    gameVars.forest_appleTree = random.randint(19, 46)
    gameVars.forest_pineTree = random.randint(25, 78)
    gameVars.underground_normalCave = random.randint(1, 5)
    gameVars.pecuary_pig = random.randint(12, 18)
    gameVars.pecuary_cow = random.randint(8, 15)
    #=================================================================================================================#
    atCaller = open(path + "\\MapEntities\\forest_appleTree.txt", "r+")                   
    atStrConv = str(gameVars.forest_appleTree)
    atCaller.write (atStrConv)    
    atCaller.close()
    #=================================================================================================================#
    ptCaller = open(path + "\\MapEntities\\forest_pineTree.txt", "r+")
    ptStrConv = str(gameVars.forest_pineTree)
    ptCaller.write (ptStrConv)
    ptCaller.close()
    #=================================================================================================================#
    ncCaller = open(path + "\\MapEntities\\underground_normalCave.txt", "r+")
    ncStrConv = str(gameVars.underground_normalCave)
    ncCaller.write (ncStrConv)
    ncCaller.close()
    #=================================================================================================================#
    apCaller = open(path + "\\MapEntities\\pecuary_animalPig.txt", "r+")
    apStrConv = str(gameVars.pecuary_pig)
    apCaller.write (apStrConv)
    apCaller.close()
    #=================================================================================================================#
    acCaller = open(path + "\\MapEntities\\pecuary_animalCow.txt", "r+")
    acStrConv = str(gameVars.pecuary_cow)
    acCaller.write (acStrConv)
    acCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Stone\\stoneAxeAmm.txt", "w+")
    tStrConv = str(1)
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Stone\\stoneAxeDur.txt", "w+")
    tStrConv = str(6)
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Stone\\stoneSwordAmm.txt", "w+")
    tStrConv = str(1)
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Stone\\stoneSwordDur.txt", "w+")
    tStrConv = str(2)
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Stone\\stonePickaxeAmm.txt", "w+")
    tStrConv = str(1)
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Stone\\stonePickaxeDur.txt", "w+")
    tStrConv = str(10)
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Iron\\ironAxeAmm.txt", "w+")
    tStrConv = str(gameVars.misc_ironAxe[0])
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Iron\\ironAxeDur.txt", "w+")
    tStrConv = str(gameVars.misc_ironAxe[1])
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Iron\\ironSwordAmm.txt", "w+")
    tStrConv = str(gameVars.misc_ironSword[0])
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Iron\\ironSwordDur.txt", "w+")
    tStrConv = str(gameVars.misc_ironSword[1])
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Iron\\ironPickaxeAmm.txt", "w+")
    tStrConv = str(gameVars.misc_ironPickaxe[0])
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Iron\\ironPickaxeDur.txt", "w+")
    tStrConv = str(gameVars.misc_ironPickaxe[1])
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    print("Files created!")
    os.system("cls")
