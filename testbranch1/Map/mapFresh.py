import random
import os
import time

from Vars import gameVars
def mapfreshCreator(path):
    #creates a whole new map. as content is added this file will need updating.
    gameVars.forest_appleTree = random.randint(19, 46)
    gameVars.forest_pineTree = random.randint(25, 78)
    gameVars.underground_normalCave = random.randint(1, 5)
    gameVars.pecuary_pig = random.randint(12, 18)
    gameVars.pecuary_cow = random.randint(8, 15)
    gameVars.consumables_food = random.randint(5, 20)
    gameVars.misc_people = random.randint(1, 2)
    #=================================================================================================================#
    atCaller = open(path + "\\MapEntities\\forest_appleTree.txt", "w+")                   
    atStrConv = str(gameVars.forest_appleTree)
    atCaller.write (atStrConv)    
    atCaller.close()
    #=================================================================================================================#
    ptCaller = open(path + "\\MapEntities\\forest_pineTree.txt", "w+")
    ptStrConv = str(gameVars.forest_pineTree)
    ptCaller.write (ptStrConv)
    ptCaller.close()
    #=================================================================================================================#
    ncCaller = open(path + "\\MapEntities\\underground_normalCave.txt", "w+")
    ncStrConv = str(gameVars.underground_normalCave)
    ncCaller.write (ncStrConv)
    ncCaller.close()
    #=================================================================================================================#
    apCaller = open(path + "\\MapEntities\\pecuary_animalPig.txt", "w+")
    apStrConv = str(gameVars.pecuary_pig)
    apCaller.write (apStrConv)
    apCaller.close()
    #=================================================================================================================#
    acCaller = open(path + "\\MapEntities\\pecuary_animalCow.txt", "w+")
    acStrConv = str(gameVars.pecuary_cow)
    acCaller.write (acStrConv)
    acCaller.close()
    #=================================================================================================================#
    cfCaller = open(path + "\\Misc\\foodCons.txt", "w+")
    cfStrConv = str(gameVars.consumables_food)
    cfCaller.write (cfStrConv)
    cfCaller.close()
    #=================================================================================================================#
    mpCaller = open(path + "\\Misc\\peopleAmm.txt", "w+")
    mpStrConv = str(gameVars.misc_people)
    mpCaller.write (mpStrConv)
    mpCaller.close()
    #=================================================================================================================#
    CcFCaller = open(path + "\\MapEntities\\constructions_craftingForge.txt", "w+")
    CcFStrConv = str(gameVars.constructions_craftingForge)
    CcFCaller.write (CcFStrConv)
    CcFCaller.close()
    #=================================================================================================================#
    CpHCaller = open(path + "\\MapEntities\\constructions_pplHouse.txt", "w+")
    CpHStrConv = str(gameVars.constructions_pplHouse)
    CpHCaller.write (CpHStrConv)
    CpHCaller.close()
    #=================================================================================================================#
    CpPCaller = open(path + "\\MapEntities\\constructions_prodPecuary.txt", "w+")
    CpPStrConv = str(gameVars.constructions_prodPecuary)
    CpPCaller.write (CpPStrConv)
    CpPCaller.close()
    #=================================================================================================================#
    CsFCaller = open(path + "\\MapEntities\\constructions_smeltingForge.txt", "w+")
    CsFStrConv = str(gameVars.constructions_smeltingForge)
    CsFCaller.write (CsFStrConv)
    CsFCaller.close()
    #=================================================================================================================#
    UnsSCaller = open(path + "\\misc\\unsStone.txt", "w+")
    UnsSStrConv = str(gameVars.misc_stone)
    UnsSCaller.write (UnsSStrConv)
    UnsSCaller.close()
    #=================================================================================================================#
    UnsICaller = open(path + "\\misc\\unsIron.txt", "w+")
    UnsIStrConv = str(gameVars.misc_iron)
    UnsICaller.write (UnsIStrConv)
    UnsICaller.close()
    #=================================================================================================================#
    SmSCaller = open(path + "\\misc\\smtStone.txt", "w+")
    SmSStrConv = str(gameVars.misc_stoneSm)
    SmSCaller.write (SmSStrConv)
    SmSCaller.close()
    #=================================================================================================================#
    SmICaller = open(path + "\\misc\\smtIron.txt", "w+")
    SmIStrConv = str(gameVars.misc_ironSm)
    SmICaller.write (SmIStrConv)
    SmICaller.close()
    #=================================================================================================================#
    MwCaller = open(path + "\\Misc\\wood.txt", "w+")
    MwStrConv = str(gameVars.misc_wood)
    MwCaller.write (MwStrConv)
    MwCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Stone\\stoneAxeAmm.txt", "w+")
    tStrConv = str(gameVars.misc_stoneAxe[0])
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Stone\\stoneAxeDur.txt", "w+")
    tStrConv = str(gameVars.misc_stoneAxe[1])
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Stone\\stoneSwordAmm.txt", "w+")
    tStrConv = str(gameVars.misc_stoneSword[0])
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Stone\\stoneSwordDur.txt", "w+")
    tStrConv = str(gameVars.misc_stoneSword[1])
    tCaller.write (tStrConv)
    tCaller.close()
    #=================================================================================================================#
    tCaller = open(path + "\\Items\\Stone\\stonePickaxeAmm.txt", "w+")
    tStrConv = str(gameVars.misc_stonePickaxe[0])
    tCaller.write (tStrConv)
    tCaller = open(path + "\\Items\\Stone\\stonePickaxeDur.txt", "w+")
    tStrConv = str(gameVars.misc_stonePickaxe[1])
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
    os.system("cls")
    time.sleep(1)
