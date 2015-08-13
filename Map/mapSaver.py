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


    saveIpd_conv = str(gameVars.misc_ironPickaxe[1])
    saveIad_conv = str(gameVars.misc_ironAxe[1])
    saveIsd_conv = str(gameVars.misc_ironSword[1])
    saveSpd_conv = str(gameVars.misc_stonePickaxe[1])
    saveSad_conv = str(gameVars.misc_stoneAxe[1])
    saveSsd_conv = str(gameVars.misc_stoneSword[1])
    
    saveIpa_conv = str(gameVars.misc_ironPickaxe[0])
    saveIaa_conv = str(gameVars.misc_ironAxe[0])
    saveIsa_conv = str(gameVars.misc_ironSword[0])
    saveSpa_conv = str(gameVars.misc_stonePickaxe[0])
    saveSaa_conv = str(gameVars.misc_stoneAxe[0])
    saveSsa_conv = str(gameVars.misc_stoneSword[0])


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
    
    
    saverIpd = saveCallerF_Ipd.write (saveIpd_conv)
    saverIad = saveCallerF_Iad.write (saveIad_conv)
    saverIsd = saveCallerF_Isd.write (saveIsd_conv)
    saverSpd = saveCallerF_Spd.write (saveSpd_conv)
    saverSad = saveCallerF_Sad.write (saveSad_conv)
    saverSsd = saveCallerF_Ssd.write (saveSsd_conv)
    
    saverIpa = saveCallerF_Ipa.write (saveIpa_conv)
    saverIaa = saveCallerF_Iaa.write (saveIaa_conv)
    saverIsa = saveCallerF_Isa.write (saveIsa_conv)
    saverSpa = saveCallerF_Spa.write (saveSpa_conv)
    saverSaa = saveCallerF_Saa.write (saveSaa_conv)
    saverSsa = saveCallerF_Ssa.write (saveSsa_conv)
    
    
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
    
    
    saveCallerF_Ipd.close
    saveCallerF_Iad.close
    saveCallerF_Isd.close
    saveCallerF_Spd.close
    saveCallerF_Sad.close
    saveCallerF_Ssd.close
    
    saveCallerF_Ipa.close
    saveCallerF_Iaa.close
    saveCallerF_Isa.close
    saveCallerF_Spa.close
    saveCallerF_Saa.close
    saveCallerF_Ssa.close
    
    
    saveCallerF_CcF.close
    saveCallerF_CpH.close
    saveCallerF_CpP.close
    saveCallerF_CsF.close
