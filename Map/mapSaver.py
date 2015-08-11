from Vars import gameVars
#
def saver(path):
    #saves game. as content is added this file will need updating.

    #opens up files for r+
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
    
    saveCallerF_Ipd = open(path + "\\Items\\Iron\\ironPickaxeDur.txt", "r+")
    saveCallerF_Iad = open(path + "\\Items\\Iron\\ironAxeDur.txt", "r+")
    saveCallerF_Isd = open(path + "\\Items\\Iron\\ironSwordDur.txt", "r+")
    saveCallerF_Spd = open(path + "\\Items\\Stone\\stonePickaxeDur.txt", "r+")
    saveCallerF_Sad = open(path + "\\Items\\Stone\\stoneAxeDur.txt", "r+")
    saveCallerF_Ssd = open(path + "\\Items\\Stone\\stoneSwordDur.txt", "r+")

    saveCallerF_Ipa = open(path + "\\Items\\Iron\\ironPickaxeAmm.txt", "r+")
    saveCallerF_Iaa = open(path + "\\Items\\Iron\\ironAxeAmm.txt", "r+")
    saveCallerF_Isa = open(path + "\\Items\\Iron\\ironSwordAmm.txt", "r+")
    saveCallerF_Spa = open(path + "\\Items\\Stone\\stonePickaxeAmm.txt", "r+")
    saveCallerF_Saa = open(path + "\\Items\\Stone\\stoneAxeAmm.txt", "r+")
    saveCallerF_Ssa = open(path + "\\Items\\Stone\\stoneSwordAmm.txt", "r+")
    
    saveCallerF_CcF = open(path + "\\MapEntities\\constructions_craftingForge.txt", "r+")
    saveCallerF_CpH = open(path + "\\MapEntities\\constructions_pplHouse.txt", "r+")
    saveCallerF_CpP = open(path + "\\MapEntities\\constructions_prodPecuary.txt", "r+")
    saveCallerF_CsF = open(path + "\\MapEntities\\constructions_smeltingForge.txt", "r+")    

    #turns integers into strings to write them onto the .txt files    
    
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


    saveIpd_conv = str(gameVars.misc_ironPickaxe)
    saveIad_conv = str(gameVars.misc_ironAxe)
    saveIsd_conv = str(gameVars.misc_ironSword)
    saveSpd_conv = str(gameVars.misc_stonePickaxe)
    saveSad_conv = str(gameVars.misc_stoneAxe)
    saveSsd_conv = str(gameVars.misc_stoneSword)
    
    saveIpa_conv = str(gameVars.misc_ironPickaxe)
    saveIaa_conv = str(gameVars.misc_ironAxe)
    saveIsa_conv = str(gameVars.misc_ironSword)
    saveSpa_conv = str(gameVars.misc_stonePickaxe)
    saveSaa_conv = str(gameVars.misc_stoneAxe)
    saveSsa_conv = str(gameVars.misc_stoneSword)


    saveMw_conv = str(gameVars.misc_wood)
    saveCcF_conv = str(gameVars.constructions_craftingForge)
    saveCpH_conv = str(gameVars.constructions_pplHouse)
    saveCpP_conv = str(gameVars.constructions_prodPecuary)
    saveCsF_conv = str(gameVars.constructions_smeltingForge)
        
    #writes said strings to the .txt file
    
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

    #closes the files
    
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
