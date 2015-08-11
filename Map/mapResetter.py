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
    print("Files created!")
    os.system("cls")
