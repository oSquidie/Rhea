transform middle:
    xalign .5 yalign 1.0

transform flip:
    xzoom -1

transform emmaflip:
    xzoom -1
    xalign .5 yalign 1.0
transform yflip:
    xzoom 1

transform lilaflip:
    xzoom -1
    xalign -5 yalign 1.0

transform MingLouFlip:
    xzoom -1
    xalign -5 yalign 1.0

transform slide:
    linear 0.5 xpos 0.85

image bblack:
    "black.png"
    alpha .6


define fade = Fade(0.5, 0.0, 0.5) #scene transistions
#Lila Sprites##
image Lila happy =  im.Scale("LilaHappy.png", 800, 950)
image Lilasad = im.Scale("LilaSad.png", 800, 950)
image Lila angry = im.Scale("LilaAngry.png", 800, 950)
image Lila smile = im.Scale("LilaSmile.png", 800, 950)
image Lila stunned = im.Scale("LilaOFace.png", 800, 950)
image Lila pout = im.Scale("LilaPout.png", 800, 950)
image Lila shocked = im.Scale("LilaShocked.png", 800, 950)
image Lila surprised = im.Scale("LilaSuprised.png", 800, 950)
image Lila tears = im.Scale("LilaTears.png", 800, 950)
image Lila eyes closed = im.Scale("LilaClosedEyes.png", 800, 950)
image Lila default = im.Scale("LilaDefault.png", 800, 950)
image Lila blush =  im.Scale("LilaBlush.png", 800, 950)
image Lila nervous =  im.Scale("LilaArrowFace.png", 800, 950)
image Lila eyes closed sad = im.Scale("LilaClosedEyesSad.png", 800, 950)
image Lila angry cry = im.Scale("LilaCryAngry.png", 800, 950)
image Lila relieved = im.Scale("LilaRelieved.png", 800, 950)
image Lila embarrassed = im.Scale("LilaEmbarrassed.png", 800, 950)
image Lila laugh = im.Scale("LilaLaugh.png", 800, 950)
image Lila panic = im.Scale("LilaPanic.png", 800, 950)
image Lila pain = im.Scale("LilaPain.png", 800, 950)
image Lila swirly eyes = im.Scale("LilaSwirlyEyes.png", 800, 950)
image Lila yell = im.Scale("LilaYell.png", 800, 950)
image Lila skeptical = im.Scale("LilaSkeptical.png", 800, 950)
image Lila Sweats =  im.Scale("LilaNervous.png", 800, 950)
image side Lila = im.Scale("images/LilaSide.png", 400, 400, xoffset=20, yoffset=30)
############################################################################
#BGs#
image BGStart = "BGStart.png"
image DefaultForest = "Forest_Default.png"
image Cave = "Cave.png"
image InsideDen = "InsideDen.png"
image Den = "OutsideDen.png"
image FirstPage = "FirstPage.png"
image TwoPaths = "TwoPaths.png"
image SecondPage = "SecondPage.png"
image Map = "Map.png"
image TwoPaths = "Twopaths.png"
image MingLouSmilesEvil = im.Scale("MingluoBurnCG.png", 1920, 1080)
image CaveExploreMain = "CaveExploreMain.png" #This is the cave explore with the items inside the picture
image CaveExploreMainEmpty = "CaveExploreMainEmpty.png" #Without the items(sprites) on the picture
image CaveEntrance = "CaveEntrance.png"
image VineWall = "VineWall.png"
############################################################################
#Mingluo Sprites#
image Mingluo happy =  im.Scale("MingluoHappy.png", 960, 1000)
image Mingluo angry = im.Scale("MingluoAngry.png", 960, 1000)
image Mingluo default = im.Scale("Mingluodefault.png", 960, 1000)
image Mingluo cry = im.Scale("MingluoCry.png", 960, 1000)
image Mingluo disgust = im.Scale("MingluoDisgust.png", 960, 1000)
image Mingluo annoyed =  im.Scale("MingluoAnnoyed.png", 960, 1000)
image Mingluo no eyes =  im.Scale("MingluoNoEyes.png", 960, 1000)
image Mingluo pyscho =  im.Scale("MingluoPsycho.png", 960, 1000)
image Mingluo skeptical =  im.Scale("MingluoSkeptical.png", 960, 1000)
image Mingluo smile =  im.Scale("MingluoSmile.png", 960, 1000)
image Mingluo soft =  im.Scale("MingluoSoft.png", 960, 1000)
image Mingluo sad = im.Scale("MingluoSad.png", 960, 1000)
image Mingluo mushroom = im.Scale("MingluoMushroom.png", 960, 1000)
image Mingluo page = im.Scale("MingluoPage.png", 960, 1000)
image Mingluo blush = im.Scale("MingluoBlush.png", 960, 1000)
image Mingluo devasted = im.Scale("MingluoDevasted.png", 960, 1000)
image Mingluo done = im.Scale("MingluoDone.png", 960, 1000)
image Mingluo evil = im.Scale("MingluoEvil.png", 960, 1000)
image Mingluo laugh = im.Scale("MingluoLaugh.png", 960, 1000)
image Mingluo nervous = im.Scale("MingluoNervous.png", 960, 1000)
image Mingluo rage = im.Scale("MingluoRage.png", 960, 1000)
image Mingluo sigh = im.Scale("MingluoSigh.png", 960, 1000)
image Mingluo smirk = im.Scale("MingluoSmirk.png", 960, 1000)
image Mingluo smug = im.Scale("MingluoSmug.png", 960, 1000)
image Mingluo threat = im.Scale("MingluoThreat.png", 960, 1000)
image Mingluo yell = im.Scale("MingluoYell.png", 960, 1000)
image side Mingluo = im.Scale("images/MingluoSide.png", 400, 400, xoffset=20, yoffset=30)
############################################################################
#Emma Sprites#
image Emma happy = im.Scale("EmmaHappy.png", 760, 1000)
image Emma angry = im.Scale("EmmaAngry.png", 760, 1000)
image Emma blush = im.Scale("EmmaBlush.png", 760, 1000)
image Emma concern = im.Scale("EmmaConcerned.png", 760, 1000)
image Emma cry = im.Scale("EmmaCry.png", 760, 1000)
image Emma default = im.Scale("EmmaDefault.png", 760, 1000)
image Emma pout = im.Scale("EmmaPout.png", 760, 1000)
image Emma shocked = im.Scale("EmmaShocked.png", 760, 1000)
image Emma surprised = im.Scale("EmmaSurprised.png", 760, 1000)
image Emma sigh = im.Scale("EmmaSigh.png", 760, 1000)
image Emma smile = im.Scale("EmmaSmile.png", 760, 1000)
image Emma smug  = im.Scale("EmmaSmug.png", 760, 1000)
image Emma dissapointed  = im.Scale("EmmaDissapointed.png", 760, 1000)
image Emma embarrassed = im.Scale("EmmaEmbarassed.png", 760, 1000)
image Emma envy = im.Scale("EmmaEnvy.png", 760, 1000)
image Emma intimidating = im.Scale("EmmaIntimidating.png", 760, 1000)
image Emma laugh = im.Scale("EmmaLaugh.png", 760, 1000)
image Emma nervous = im.Scale("EmmaNervous.png", 760, 1000)
image Emma panic = im.Scale("EmmaPanic.png", 760, 1000)
image Emma sly = im.Scale("EmmaSly.png", 760, 1000)
image Emma tease = im.Scale("EmmaTease.png", 760, 1000)
image Emma yell = im.Scale("EmmaYell.png", 760, 1000)
image Emma yell cry = im.Scale("EmmaYellCry.png", 760, 1000)
image side Emma = im.Scale("images/EmmaSide.png", 400, 400, xoffset=20, yoffset=30)
#############################################################################
#Liam Sprites#
image Liam happy = im.Scale("LiamHappy.png", 960, 1200)
image Liam default = im.Scale("LiamDefault.png", 960, 1200)
image Liam nervous = im.Scale("LiamNervous.png", 960, 1200)
image Liam pout = im.Scale("LiamPout.png", 960, 1200)
image Liam sad = im.Scale("LiamSad.png", 960, 1200)
image Liam shocked = im.Scale("LiamShocked.png", 960, 1200)
image Liam sigh = im.Scale("LiamSigh.png", 960, 1200)
image Liam smile = im.Scale("LiamSmile.png", 960, 1200)
image Liam smug = im.Scale("LiamSmug.png", 960, 1200)
image Liam surprised = im.Scale("Liamsurprised.png", 960, 1200)
image Liam wink = im.Scale("LiamWink.png", 960, 1200)
image Liam angry = im.Scale("LiamAngry.png", 960, 1200)
image Liam page = im.Scale("LiamPage.png", 960, 1200)
image Liam closed eyes = im.Scale("LiamClosedEyes.png", 960, 1200)
image Liam content = im.Scale("LiamContent.png", 960, 1200)
image Liam embarrassed = im.Scale("LiamEmbarrassed.png", 960, 1200)
image Liam intimidating = im.Scale("LiamIntimidating.png", 960, 1200)
image Liam laugh = im.Scale("LiamLaugh.png", 960, 1200)
image Liam panic = im.Scale("LiamPanic.png", 960, 1200)
image Liam skeptical = im.Scale("LiamSkeptical.png", 960, 1200)
image Liam smirk = im.Scale("LiamSmirk.png", 960, 1200)
image Liam yell = im.Scale("LiamYell.png", 960, 1200)
image Liam yell cry = im.Scale("LiamYellCry.png", 960, 1200)
image Liam dark smile = im.Scale("LiamDarkSmile.png", 960, 1200)
image Liam blush = im.Scale("LiamBlush.png", 960, 1200)
image side Liam = im.Scale("images/LiamSide.png", 490, 490, xoffset=20, yoffset=30)
##################################################################################
#CloseUp Images#
image CloseupBerry = "CloseupBerry.png"
image CloseupCrystal = "CloseupCrystal.png"
image CloseupCrystalBlood = "CloseupCrystalBlood.png"
image CloseupCrystalHandPrint = "CloseupCrystalHandPrint.png"
image CloseupOpus = "CloseupOpus.png"
image CloseupPageCave = "CloseupPageCave.png"
image CloseupPageDen = "CloseupPageDen.png"
image CloseupVine = "CloseupVine.png"
image CloseupWyrm = "CloseupWyrm.png"
#####################################################
#Selectable Images and Magnifiying Glass#
image Crystal = "Crystal.png"
image Page = "Page.png"
image PageItem = "PageItem.png"
image Vine = "Vine.png"
image Opus = "Opus.png"
image MagnifyingGlass = "MagnifyingGlass.png"
image Berry = "Berry.png"
image WyrmItem = "WyrmSelectable.png"
image HiddenRock = "HiddenRock.png"
###DOORS####
image OpusDoor = "OpusDoor.png"
image CrystalDoor = "CrystalDoor.png"
image VineDoor = "VineDoor.png"
image TreasureDoor = "TreasureDoor.png"
#####################################################
##Cutscenes##
image Opus neutral = "Opus1.png"
image Opus death = "Opus2.png"
image Wyrm neutral = "Wyrm.png"
image Wyrm death = "Wyrm2.png"
image Vina neutral = "VinaPlant.png"
image Vina neutral = "VinaPlantDeath.png"
image MingluoBurnPage = "MingluoBurnCG.png"
image LilaIntro1 = "LilaIntro1.png"
image LilaIntro2 = "LilaIntro2.png"
image LilaIntro3 = "LilaIntro3.png"
##############################################################
