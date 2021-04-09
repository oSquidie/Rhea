define L = Character('Lila', color="#ced0ff", image = "Lila")
define M = Character('Mingluo', color="#87ddfb", image = "Mingluo")
define E = Character('Emma', color="#73fff0", image = "Emma")
define L2 = Character('Liam', color="#a673ff", image = "Liam")
define Q = Character ('?')
define RV = Character ('Random Villager 1')
define RV2 = Character ('Random Villager 2')
define RV3 = Character ('Random Villager 3')

######## Stops AutoSave #########
define config.has_autosave = False

##################Defining Audio#######################
define audio.RheaSoundtrack ="audio/RheaSoundtrack.wav"
define audio.RheaMain = "audio/RheaMainMenuMusic.wav"
define audio.LilaIntro = "audio/Lila Intro 4.wav"
define audio.CaveBattleMusic = "audio/CaveMusic.wav"

##################Defining Movies#############
image opening movie = Movie(channel="movies", play="Movies/Test2.mpg")

###################For Senses in Cave##################
define C_Sight1 = True
define C_Smell1 = True
define C_Feel1 = True
define C_Sound1 = True

#################For sitting and waiting##########
define sitWait = True

############Affection points#####################
define Affection= False
define Affection_sys.value = 0


############Affection points/changed paths(Crystal)#####################
define CrystalTouched = False
define LilaBleed = False
define LilaBleed2 = False #Helps turn off options
define LilaDoNotBleed = True
define CrystalLooked = True
define TouchCrystal_EmmaCare = False ####BUG fixed###
define TouchCrystal_EmmaDoNotCare = True

############Affection points/changed paths(Opus)#####################
define LookOpus_EmmaCare = False
define LookOpus_EmmaDoNotCare = True
define LookAtOpus = True
define JustReachForRock = True

############Affection playing an effect/changed paths(Rock)#####################
define RockFound_Opus = True ###When Lila learns about the rock
define RockFound_Opus2 = False #So she isn't surprised when seeing the rock again.
define TakeRock_EmmaCare = False #Emma will get rock with enough affection points
define TakeRock_EmmaDoNotCare = True #Emma will not get rock.
define SaveLiam_EmmaCare = False #Leading to one of the different endings
define SaveLiam_EmmaDoNotCare = True #Leading to one of the different endings

###########Affection playing an effect/changed paths(Vine)####
define LookAtVine = True
define Distract_EmmaAndLiamCare = False
define Distract_EmmaAndLiamDoNotCare = True
define AskLiamForInfo = True
define NoDaggerInfo = True
define SawVine = False

##################Information gained/Items path unlocked######################
define DaggerInfo = False ###When Lila Learn about the Dagger
define GotDrumStick = False ###When Lila Gets Drumstick
define GotRock_Crystal = True ###When Lila Get Rock by Crystal
define GotRock_Opus = True ##When Lila Get Rock by Opus
define GotRock = False ###Just to Tell renpy rock is already got
define GotRock1 = False ####To change the outcomes when vine is seen
define GotRock2 = False ####To change the outcomes when vine is seen
define GotSharpRock = False ###### If Lila got sharp rock.
define NoRockFound = True ###If no rock has been got yet.

#######################Different ending affection points involved#############
define SaveMe_AllCare = False
define SaveMe_DoNotCare = True
define SaveLiam_AllCare = False
define SaveLiam_DoNotCare = True
define SaveYourSelf_AllCare = False
define SaveYourSelf_DoNotCare = True

#######Making a statment stop####
define thing = True
define thing2 = True
define thing3 = True
define thing4 = True


######################### Mouse #####################
define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }

########## Text Effect #####
transform text_effect: #Shaky text
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2
            linear 0.1 xoffset 3 yoffset -3
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat
