from Vars import gameVars
#
def saver(path):
    saveCallerF_At = open(path + "\\MapEntities\\forest_appleTree.txt", "r+")
    saveCallerF_Pt = open(path + "\\MapEntities\\forest_pineTree.txt", "r+")
    saveCallerF_Nc = open(path + "\\MapEntities\\underground_normalCave.txt", "r+")
    saveCallerF_Ap = open(path + "\\MapEntities\\pecuary_animalPig.txt", "r+")
    saveCallerF_Ac = open(path + "\\MapEntities\\pecuary_animalCow.txt", "r+")
    saveCallerF_Fd = open(path + "\\Misc\\foodCons.txt", "r+")
    saveCallerF_Mp = open(path + "\\Misc\\peopleAmm.txt", "r+")
    saveCallerF_UnsS = open(path + "\\Misc\\unsStone.txt", "r+")
    saveCallerF_UnsI = open(path + "\\Misc\\unsIron.txt", "r+")
    saveCallerF_SmS = open(path + "\\Misc\\smtStone.txt", "r+")
    saveCallerF_SmI = open(path + "\\Misc\\smtIron.txt", "r+")
    saveCallerF_Mw = open(path + "\\Misc\\wood.txt", "r+")
    saveCallerF_Ip = open(path + "\\Items\\Iron\\ironPickaxe.txt", "r+")
    saveCallerF_Ia = open(path + "\\Items\\Iron\\ironAxe.txt", "r+")
    saveCallerF_Is = open(path + "\\Items\\Iron\\ironSword.txt", "r+")
    saveCallerF_Sp = open(path + "\\Items\\Stone\\stonePickaxe.txt", "r+")
    saveCallerF_Sa = open(path + "\\Items\\Stone\\stoneAxe.txt", "r+")
    saveCallerF_Ss = open(path + "\\Items\\Stone\\stoneSword.txt", "r+")
    saveCallerF_CcF = open(path + "\\MapEntities\\constructions_craftingForge.txt", "r+")
    saveCallerF_CpH = open(path + "\\MapEntities\\constructions_pplHouse.txt", "r+")
    saveCallerF_CpP = open(path + "\\MapEntities\\constructions_prodPecuary.txt", "r+")
    saveCallerF_CsF = open(path + "\\MapEntities\\constructions_smeltingForge.txt", "r+")    
    saveAt_conv = str(gameVars.forest_appleTree)
    savePt_conv = str(gameVars.forest_pineTree)
    saveNc_conv = str(gameVars.underground_normalCave)
    saveAp_conv = str(gameVars.pecuary_pig)
    saveAc_conv = str(gameVars.pecuary_cow)
    saveFd_conv = str(gameVars.consumables_food)
    saveMp_conv = str(gameVars.misc_people)
    saveUnsS_conv = str(gameVars.misc_stone)
    saveUnsI_conv = str(gameVars.misc_iron)
    saveSmS_conv = str(gameVars.misc_stoneSm)
    saveSmI_conv = str(gameVars.misc_ironSm)
    saveIp_conv = str(gameVars.misc_ironPickaxe)
    saveIa_conv = str(gameVars.misc_ironAxe)
    saveIs_conv = str(gameVars.misc_ironSword)
    saveSp_conv = str(gameVars.misc_stonePickaxe)
    saveSa_conv = str(gameVars.misc_stoneAxe)
    saveSs_conv = str(gameVars.misc_stoneSword)
    saveMw_conv = str(gameVars.misc_wood)
    saveCcF_conv = str(gameVars.constructions_craftingForge)
    saveCpH_conv = str(gameVars.constructions_pplHouse)
    saveCpP_conv = str(gameVars.constructions_prodPecuary)
    saveCsF_conv = str(gameVars.constructions_smeltingForge)
    saverAt = saveCallerF_At.write (saveAt_conv)
    saverPt = saveCallerF_Pt.write (savePt_conv)
    saverNc = saveCallerF_Nc.write (saveNc_conv)
    saverAp = saveCallerF_Ap.write (saveAp_conv)
    saverAc = saveCallerF_Ac.write (saveAc_conv)
    saverFd = saveCallerF_Fd.write (saveFd_conv)
    saverMp = saveCallerF_Mp.write (saveMp_conv)
    saverUnsS = saveCallerF_UnsS.write (saveUnsS_conv)
    saverUnsI = saveCallerF_UnsI.write (saveUnsI_conv)
    saverSmS = saveCallerF_SmS.write (saveSmS_conv)
    saverSmI = saveCallerF_SmI.write (saveSmI_conv)
    saverIp = saveCallerF_Ip.write (saveIp_conv)
    saverIa = saveCallerF_Ia.write (saveIa_conv)
    saverSp = saveCallerF_Sp.write (saveSp_conv)
    saverSa = saveCallerF_Sa.write (saveSa_conv)
    saverMw = saveCallerF_Mw.write (saveMw_conv)
    saverCcF = saveCallerF_CcF.write (saveCcF_conv)
    saverCpH = saveCallerF_CpH.write (saveCpH_conv)
    saverCpP = saveCallerF_CpP.write (saveCpP_conv)
    saverCsF = saveCallerF_CsF.write (saveCsF_conv)
    saveCallerF_At.close
    saveCallerF_Pt.close
    saveCallerF_Nc.close
    saveCallerF_Ap.close
    saveCallerF_Ac.close
    saveCallerF_Fd.close
    saveCallerF_Mp.close
    saveCallerF_UnsS.close
    saveCallerF_UnsI.close
    saveCallerF_SmS.close
    saveCallerF_SmI.close
    saveCallerF_Mw.close
    saveCallerF_Ip.close
    saveCallerF_Ia.close
    saveCallerF_Is.close
    saveCallerF_Sp.close
    saveCallerF_Sa.close
    saveCallerF_Ss.close
    saveCallerF_CcF.close
    saveCallerF_CpH.close
    saveCallerF_CpP.close
    saveCallerF_CsF.close
