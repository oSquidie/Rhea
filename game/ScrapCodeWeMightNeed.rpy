image Page = "PageItem.png"

define bblack = "#000000"

#define persistent.Route1 = True
#define persistent.Route2 = True

define C_Sight1 = True
define C_Smell1 = True
define C_Feel1 = True
define C_Sound1 = True

#define C1_Points.value = 0

#Path for Minglou only
define MPath1 = False
define MPath1Points.value = 0

#Path for Emma plus Minglou
define EaMpath1 = False
define EaMpath1Points.value = 0

#Path for Lila's Friends and Maybe Minglou
define LilaFriendsPlusMPath = False
define LilaFriendsPlusMPathPoints.value = 0

#Explore Cave by herself
define Crystal_TouchNormal = True
define Crystal_TouchAfterTaste = False
define Crystal_Listen1 = True
define Crystal_TasteNormal = True
define Crystal_TasteAfterTouch = False
define Crystal_SmellNormal = True
define Crystal_SmellAfterTaste = False

#Explore cave with Emma
define Crystal2_TouchBleed = False
define Crystal2_TouchStopped = False
define Crystal2_TasteBleed = False
define Crystal2_TasteStopped = False
define Crystal2_SmellAfterTouch = False

#Explore cave With LaimAndEmma
define Crystal3_TouchNormal = True
define Crystal3_TouchAfterTaste = False
define Crystal3_Listen1 = True
define Crystal3_TasteNormal = True
define Crystal3_TasteAfterTouch = False
define Crystal3_SmellNormal = True
define Crystal3_SmellAfterTouch = False

#Explore Cave by herself
define Vine_NormalTouch = True
define Vine_TouchBleed = False
define Vine_TouchWithEyes = False
define Vine_SmellNormal = True
define Vine_SmellWithEyes = False
define Vine_NormalBite = True
define Vine_BiteBleed = False
define Vine_BiteWithEyes = False
define Vine_ListenVine = True

#Explore Cave with Emma
define Vine2_NormalTouch = True
define Vine2_TouchVineBleed = False
define Vine2_TouchWithEyes = False
define Vine2_TouchVineBleed2 = False
define Vine2_SmellVineNormal = True
define Vine2_SmellVineEyes = False
define Vine2_BiteVineNormal = True
define Vine2_BiteVineWithEyes = False
define Vine2_ListenVine = True

#Explore Cave with both of her friends:
define Vine3_NormalTouch = True
define Vine3_TouchVineBleed = False
define Vine3_SmellVineNormal = True
define Vine3_BiteVineNormal = True
define Vine3_ListenVine = True


#Explore Cave by herself
define Opus_NormalTouch = True
define Opus_TouchBleed = False
define Opus_NormalSmell = True
define Opus_SmellBleed = False
define Opus_NormalBite = True
define Opus_BiteBleed = False
define Opus_Listen = True
define Opus_ListenAfterTouch = False

#Explore Cave with Emma
define Opus2_NormalTouch = True
define Opus2_TouchBleed = False
define Opus2_NormalSmell = True
define Opus2_NormalBite = True
define Opus2_Listen = True

#Explore Cave with Lila and friends
define Opus3_NormalTouch = True
define Opus3_TouchBleed = False
define Opus3_NormalSmell = True
define Opus3_NormalBite = True
define Opus3_Listen = True

#Explore Cave by herself
define Page_TouchNormal = True
define Page_TouchBleed = False

#Explore Cave by herself
define TouchBleed.value = 0
define TasteBleed.value = 0

#Exploring Cave with Emma
define LilaBleed.value = 0
define EmmaBleed.value = 0

#Exploring Cave With Both of her friends
define LiamLetLilaBleed.value = 0
define LilaTouchBleedPoints.value = 0

#Explore Cave by herself
define Taste_Points.value = 0
define Touch_Points.value = 0

#Explore Cave by herself
define VineTouchPoints.value = 0
define VineTastePoints.value = 0
define VineSmell_Points.value = 0

#Explore Cave by herself
define OpusTouchPoints.value = 0

#define persistent.value = 0

define Choice1 = True
define Choice2 = True
define Choice3 = True

define Affection= False
define Affection_sys.value = 0

#define Path1_Answers = False
#define Qpoints1.value = 0

############Affection stuff############
#$ name_points -= 1
#$ name_points += 1
#show screen inventory_button
#show screen positive_affection
#$affbarposi = True
#$liam_points += 1
#$ emma_points +/-= 0
#$ liam_points +/-=  0
#$ affbarposi = False
#$ affbarnegative = False
#$ affbarposi = True
#$ affbarnegative = True
#$show screen line then $bar line

#hide screen inventory_button
#show screen inventory_button

###For adding points
##$ affbarposi = True
###$ liam_points += 1
#show screen positive_affection

#show screen negative_affection
#$ affbarposi = False
#$ affbarnegative = True
#$ liam_points -= 1

##################### Old Game SYS ####################
    #scene Map with fade
    #window hide
    #pause
    #window show
    #show Map:
        #ease 3.0 zoom 2.0
    #window hide
    #pause 3.5
    #window show
    #show Map at Position (xpos = 0.4,  xanchor=0.5, yanchor= 0.5, ypos= -.1) with pixellate:
        #zoom 3.0

        #show Lila happy at flip for flipping the sprite

        #transform my_dissolve(x):
                # alpha 0.0
                # linear x alpha 1.0

       # label transform_test:
        #show image "Forest_Default.png" at truecenter, my_dissolve(.5)

    #"What do you want to be? The seeker or hidder?"

##################### Old Game SYS ####################
    #menu:
        #"Start Game":
                #jump Seeker
       # "Seeker?": #if persistent.Route1 == True:
            #jump Seeker
        #"Hidder?" if persistent.Route2 == True:
            #jump Concealer

#label Seeker:
    #scene image "Forest_Default.png" with fade
    #$persistent.Route1 = False
    #$persistent.value += 1
#if persistent.value >= 2:
        #$persistent.Route1 = True
        #$persistent.Route2  = True
        #$persistent.value = 0

    #show bblack with dissolve
    #hide bblack with dissolve

    #Q "Ouch! What was that for?" with vpunch

    #label Concealer:
        #"To be contuined"
        #$persistent.Route2 = False
        #$persistent.value +=1
        #if persistent.value >= 2:
            #$persistent.Route1 = True
            #$persistent.Route2 = True
            #$persistent.value = 0
    #return

    #init python: (DON'T OPEN THIS WHEN CONCEALER IS FINSIHED)
        #def reset():
            #persistent.Route1 = True
            #persistent.Route2 = True
            #persistent.value = 0

############For Inventory###########
#label start:
    #python:
        #player = Player("Derp", 100, 50)
        #player.hp = 50
        #player.mp = 10
        #chocolate = Item("Chocolate", hp=40, image="gui/inv_chocolate.png")
        #banana = Item("Banana", mp=20, image="gui/inv_banana.png")
        #gun = Item("Gun", element="bullets", image="gui/inv_gun.png", cost=7)
        #laser = Item("Laser Gun", element="laser", image="gui/inv_laser.png")
        #itemname = Item("Itemname", element = "itemname", image="gui/imagename.png")
        #inventory = Inventory()
        #add items to the initial inventory:
        #inventory.add(chocolate) #What shows in the inventory from the start
        #inventory.add(chocolate)
        #inventory.add(banana)
        #inventory.add(item name)
    #$ inventory.drop(banana) Dropping an item
    #$ inventory.add(banana) adding an item
    #menu:
        #"Go deeper into the forest" if chocolate in inventory.items: #Giving items away through choices
            #"you gave chocolate away"
            #$inventory.drop(chocolate)
            #jump ending1

                #$renpy.notify("Information gained.")
                #$renpy.notify("Emma carries a weapon.")
