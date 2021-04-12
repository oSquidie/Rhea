
#####For any character########
transform middle:
   xalign .5 #syalign 1.0
   ypos 35

transform flip:
   xzoom -1
   ypos 35

transform MoveUp:
   ypos 35

transform PopUp:
   ypos -50

transform shake:
       ease .06 yoffset 24
       ease .06 yoffset -24
       ease .05 yoffset 20
       ease .05 yoffset -20
       ease .04 yoffset 16
       ease .04 yoffset -16
       ease .03 yoffset 12
       ease .03 yoffset -12
       ease .02 yoffset 8
       ease .02 yoffset -8
       ease .01 yoffset 4
       ease .01 yoffset -4
       ease .01 yoffset 0

transform my_right:
    xalign .9 yalign 1.0

#########For Lila#######
transform lilaflip: ####(Right)#####
   xzoom -1
   xalign -5 #yalign 1.0
   ypos 35

transform yflip: ####(Left)#####
   xzoom 1
   ypos 35

#########For Emma########

transform emmaflip:
   xzoom -1
   xalign .5 #yalign 1.0
   ypos 5

transform emmaflip2:
    xzoom -1

transform emmaFaceRight:
    xzoom 1
    xalign .5 #yalign 1.0
    ypos 5

transform emmaLeft:
   xpos -100

transform emmaRight:
   xpos 1500

transform emmaMoveUp:
   ypos 5

transform emmaMiddle:
   xalign .5
   ypos 5

#######For Liam######
transform LiamMoveUp:
   ypos -200

transform LiamPopUp:
   ypos -250

transform LiamRight:
   xpos 1000

transform Liamflip:
   xzoom -1

#######For MingLou######
transform MingLouFlip:
   xzoom -1
   xalign -5 #yalign 1.0
   ypos 35

#####Pain in my ass(For polish)########
image bblack:
   "black.png"
   alpha .6

define fade = Fade(0.5, 0.0, 0.5) #scene transistions


image static: ##Glitch##
    "FadeGlitchBlack.png" with Dissolve(0.15)
    0.15
    "FadeGlitchBlack2.png" with Dissolve(0.15)
    0.15
    "FadeGlitchBlack3.png" with Dissolve(0.15)
    0.15
    "FadeGlitchBlack4.png" with Dissolve(0.15)
    0.15
    repeat
image static2: ##Glitch with a slight fade/transparency##
    "FadeGlitchBlack5.png" with Dissolve(0.15)
    0.15
    "FadeGlitchBlack6.png" with Dissolve(0.15)
    0.15
    "FadeGlitchBlack7.png" with Dissolve(0.15)
    0.15
    "FadeGlitchBlack8.png" with Dissolve(0.15)
    0.15
    repeat
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
image side Mingluo = im.Scale("images/MingluoIcon.png", 200, 200, xoffset=25, yoffset=-30)
############################################################################
#Lila Sprites##
image Lila happy =  im.Scale("LilaHappy.png", 800, 950)
image Lila sad = im.Scale("LilaSad.png", 800, 950)
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
image Lila dumbfounded = im.Scale("LilaDumbfounded.png", 800, 950)
image Lila confused = im.Scale("LilaConfused.png", 800, 950)
image side Lila = im.Scale("images/LilaIcon.png", 200, 200, xoffset=25, yoffset=-30)
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
image Emma dissapointed = im.Scale("EmmaDissapointed.png", 760, 1000)
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
image Emma soft = im.Scale("EmmaSoft.png", 760, 1000)
image Emma excited = im.Scale("EmmaExcited.png", 760, 1000)
image side Emma = im.Scale("images/EmmaIcon.png", 200, 200, xoffset=25, yoffset=-30)
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
image side Liam = im.Scale("images/LiamIcon.png", 200, 200, xoffset=25, yoffset=-30)
##################################################################################
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
image FadeGlitchBlack = "FadeGlitchBlack.png"
image FadeGlitchBlack2 = "FadeGlitchBlack2.png"
image FadeGlitchBlack3 = "FadeGlitchBlack3.png"
image FadeGlitchBlack4 = "FadeGlitchBlack4.png"
image White = "White.png"
#################################################################################
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
image OpusDistract = "OpusDistract1.png"
image OpusDistract2 = "OpusDistract2.png"
image OpusDistract3 = "OpusDistract3.png"
image OpusDistract4 = "OpusDistract4.png"
image OpusDistract5 = "OpusDistract5.png"
image CloseupRock = "CloseupRock.png"
image CloseupDoor = "CloseupDoor.png"
image CloseupDoor2 = "CloseupDoor2.png"
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
image Vina death = "VinaPlantDeath.png"
image VineHurt = "VinaPlantDeathHurt.png"
image VineBurn = "VineWallBurn.png"
image MingluoBurnPage = "MingluoBurnCG.png"
image LilaIntro1 = "LilaIntro1.png"
image LilaIntro2 = "LilaIntro2.png"
image LilaIntro3 = "LilaIntro3.png"
image LilaReachForRock = "ReachforRock.png"
image LilaScareOfOpus = "LilaScaredOpus.png"
image Emmavsbird = "Emmavsbird.png"
image EmmaLiamProtect = "EmmaLiamProtect.png"
image TearsEmmaLiamProtect = "EmmaLiamProtect2.png"
image Riot = "Riot.png"
image HandinHand = "WalkingHandInHand.png"
image WalkingHomeNorm = "WalkHomeNoHand.png"
image LiamKnockedOut = "LiamKnockedOut.png"
image LiamHurt = "LiamHurt.png"
image MingluoCatchLila ="MingluoCatchLila.png"
image LilaSharpRock = "LilaSharpRock.png"
image LilaTouchCrystal = "LilaTouchCrystal.png"
image LilaandEmmaOpus = "LilaandEmmaOpus.png"
image LilaCatchPage = "LilaCatchPage.png"
image LilaThrowDrumstick = "LilaThrowDrumstick.png"
image LilaThrowDrumstick2 = "LilaThrowDrumstick2.png"
##############################################################
