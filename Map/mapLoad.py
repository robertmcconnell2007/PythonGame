import os
from Vars import gameVars



def load(path):
	print("Loading...")
	loadAt = open(path + "\\MapEntities\\forest_appleTree.txt", "r+")
	loadPt = open(path + "\\MapEntities\\forest_pineTree.txt", "r+")
	loadNc = open(path + "\\MapEntities\\underground_normalCave.txt", "r+")
	loadAp = open(path + "\\MapEntities\\pecuary_animalPig.txt", "r+")
	loadAc = open(path + "\\MapEntities\\pecuary_animalCow.txt", "r+")
	loadFd = open(path + "\\Misc\\foodCons.txt", "r+")
	loadMp = open(path + "\\Misc\\peopleAmm.txt", "r+")
	loadUnsS = open(path + "\\Misc\\unsStone.txt", "r+")
	loadUnsI = open(path + "\\Misc\\unsIron.txt", "r+")
	loadSmS = open(path + "\\Misc\\smtStone.txt", "r+")
	loadSmI = open(path + "\\Misc\\smtIron.txt", "r+")
	loadMw = open(path + "\\Misc\\wood.txt", "r+")
	loadIpA = open(path + "\\Items\\Iron\\ironPickaxeAmm.txt", "r+")
	loadIaA = open(path + "\\Items\\Iron\\ironAxeAmm.txt", "r+")
	loadIsA = open(path + "\\Items\\Iron\\ironSwordAmm.txt", "r+")
	loadIpD = open(path + "\\Items\\Iron\\ironPickaxeDur.txt", "r+")
	loadIaD = open(path + "\\Items\\Iron\\ironAxeDur.txt", "r+")
	loadIsD = open(path + "\\Items\\Iron\\ironSwordDur.txt", "r+")
	loadSpA = open(path + "\\Items\\Stone\\stonePickaxeAmm.txt", "r+")
	loadSaA = open(path + "\\Items\\Stone\\stoneAxeAmm.txt", "r+")
	loadSsA = open(path + "\\Items\\Stone\\stoneSwordAmm.txt", "r+")
	loadSpD = open(path + "\\Items\\Stone\\stonePickaxeDur.txt", "r+")
	loadSaD = open(path + "\\Items\\Stone\\stoneAxeDur.txt", "r+")
	loadSsD = open(path + "\\Items\\Stone\\stoneSwordDur.txt", "r+")
	loadCcF = open(path + "\\MapEntities\\constructions_craftingForge.txt", "r+")
	loadCpH = open(path + "\\MapEntities\\constructions_pplHouse.txt", "r+")
	loadCpP = open(path + "\\MapEntities\\constructions_prodPecuary.txt", "r+")
	loadCsF = open(path + "\\MapEntities\\constructions_smeltingForge.txt", "r+")
	At_loadedInf = int(loadAt.readlines()[0])
	Pt_loadedInf = int(loadPt.readlines()[0])
	Nc_loadedInf = int(loadNc.readlines()[0])
	Ap_loadedInf = int(loadAp.readlines()[0])
	Ac_loadedInf = int(loadAc.readlines()[0])
	Fd_loadedInf = int(loadFd.readlines()[0])
	Mp_loadedInf = int(loadMp.readlines()[0])
	UnsS_loadedInf = int(loadUnsS.readlines()[0])
	UnsI_loadedInf = int(loadUnsI.readlines()[0])
	SmS_loadedInf = int(loadSmS.readlines()[0])
	SmI_loadedInf = int(loadSmI.readlines()[0])
	IpA_loadedInf = int(loadIpA.readlines()[0])
	IaA_loadedInf = int(loadIaA.readlines()[0])
	IsA_loadedInf = int(loadIsA.readlines()[0])
	SpA_loadedInf = int(loadSpA.readlines()[0])
	SaA_loadedInf = int(loadSaA.readlines()[0])
	SsA_loadedInf = int(loadSsA.readlines()[0])
	IpD_loadedInf = int(loadIpD.readlines()[0])
	IaD_loadedInf = int(loadIaD.readlines()[0])
	IsD_loadedInf = int(loadIsD.readlines()[0])
	SpD_loadedInf = int(loadSpD.readlines()[0])
	SaD_loadedInf = int(loadSaD.readlines()[0])
	SsD_loadedInf = int(loadSsD.readlines()[0])
	Mw_loadedInf = int(loadMw.readlines()[0])
	CcF_loadedInf = int(loadCcF.readlines()[0])
	CpH_loadedInf = int(loadCpH.readlines()[0])
	CpP_loadedInf = int(loadCpP.readlines()[0])
	CsF_loadedInf = int(loadCsF.readlines()[0])
	gameVars.forest_appleTree = At_loadedInf
	gameVars.forest_pineTree = Pt_loadedInf
	gameVars.underground_normalCave = Nc_loadedInf
	gameVars.pecuary_pig = Ap_loadedInf
	gameVars.pecuary_cow = Ac_loadedInf
	gameVars.consumables_food = Fd_loadedInf
	gameVars.misc_people = Mp_loadedInf
	gameVars.misc_iron = UnsI_loadedInf
	gameVars.misc_stone = UnsS_loadedInf
	gameVars.misc_ironSm = SmI_loadedInf 
	gameVars.misc_stoneSm = SmS_loadedInf
	gameVars.misc_wood = Mw_loadedInf
	gameVars.misc_stonePickaxeAmm = SpA_loadedInf
	gameVars.misc_stoneAxeAmm = SaA_loadedInf
	gameVars.misc_stoneSwordAmm = SsA_loadedInf
	gameVars.misc_ironPickaxeAmm = IpA_loadedInf
	gameVars.misc_ironAxeAmm = IaA_loadedInf
	gameVars.misc_ironSwordAmm = IsA_loadedInf
	gameVars.constructions_craftingForge = CcF_loadedInf
	gameVars.constructions_pplHouse = CpH_loadedInf
	gameVars.constructions_prodPecuary = CpP_loadedInf
	gameVars.constructions_smeltingForge = CsF_loadedInf
	loadAt.close
	loadPt.close
	loadNc.close
	loadAp.close
	loadAc.close
	loadFd.close
	loadMp.close
	loadUnsS.close
	loadUnsI.close
	loadSmS.close
	loadSmI.close
	loadMw.close
	loadIpA.close
	loadIaA.close
	loadIsA.close
	loadSpA.close
	loadSaA.close
	loadSsA.close
	loadIpD.close
	loadIaD.close
	loadIsD.close
	loadSpD.close
	loadSaD.close
	loadSsD.close
	loadCcF.close
	loadCpH.close
	loadCpP.close
	loadCsF.close
	os.system("cls")	
