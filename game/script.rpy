play music RheaMain
################ Warning screen #######################
label splashscreen:
    with Pause(1)

    show text "Any similarities this game has with real life is purely coincidental." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "This all works of fiction." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    call screen confirm(message="Rhea contains a lot of bright colors, this may affect individuals who are susceptible to photo sensitivities. Do you want to continue?", yes_action=Return(), no_action=Quit(confirm=False))
    return

#######################START GAME INTRO ####################
label start:
    ############Items for Inven ##############
    python:
        Sharprock = Item("A Sharp Rock", image="gui/inv_sharprock.png")
        drumstick = Item("DrumStick", image="gui/inv_Drumstick.png")
        dullrock = Item("A Dull Rock", image="gui/inv_rock.png")
        LilaMushroom = Item("A Glowing Mushroom", image="gui/inv_LilaMushroom.png")
        Dagger = Item("Emma's Dagger", image="gui/inv_Dagger.png")
        Page1 = Item ("A Mysterious Page.", image= "gui/inv_PageItem.png")
        inventory = Inventory()
    hide screen inventory_button
    stop music fadeout 1.0
    default preferences.text_cps = 50
    play music LilaIntro fadein 5.0 volume 0.3 loop
    window hide
    show LilaIntro1
    pause 1
    window show
    L "I've been told my entire life..."
    L "We live in a world without the existence of light."
    L "There was no such thing as the sun."
    L "Only the soft glows of luminescence lead us through the darkness."
    L "{cps=2}...{/cps}"
    show LilaIntro2
    L "All of that was just a lie." with vpunch
    show LilaIntro3
    hide LilaIntro2
    L "No matter where I went."
    L "Who I asked."
    L "No one was willing to give me an answer."
    hide LilaIntro3 with dissolve
    show LilaIntro1 with dissolve
    L "Where is the sun?"
    L "Why is it gone?"
    L "Why cover the truth?"
    show LilaIntro2
    L "I will dig the truth out of these dirty lies." with vpunch
    show LilaIntro3
    L "I refuse to become the outcast of my village with no clear reason."
    L "I have already found a lead."
    L "Soon I will be able to gave solid proof to the existence called the sun."
    stop music fadeout 1.0
    $renpy.movie_cutscene("Movies/Test2.mpg")
    #############Start Dialogue Cutscene#########
    hide LilaIntro3
    hide LilaIntro2
    hide LilaIntro1
    show image "Forest_Default.png" with dissolve
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila swirly eyes at shake
    $inventory.add(LilaMushroom)
    play music RheaSoundtrack fadein 5.0 volume 0.3
    L "Huh?"
    show Lila swirly eyes at PopUp with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    L "Where is it???"
    show Lila swirly eyes at MoveUp with dissolve
    show Emma concern at PopUp with dissolve
    E "Where is what?"
    show Emma concern at emmaMoveUp with dissolve
    show Lila Sweats at PopUp with dissolve
    L "The old thing we are looking for..."
    show Liam laugh with dissolve
    show Lila Sweats at MoveUp with dissolve
    show Emma intimidating at PopUp with dissolve
    E "If you are talking about the ancient artifact."
    show Emma envy with dissolve
    E "I'll be really mad."
    show Emma envy at emmaMoveUp with dissolve
    show Liam nervous with dissolve
    show Lila panic with dissolve
    show Lila embarrassed with dissolve
    show Lila nervous with dissolve
    show Lila Sweats with dissolve
    show Emma envy at PopUp with dissolve
    E "Didn't you just tell me it's somewhere over here."
    show Emma angry with dissolve
    E "You are just unbelievable..."
    show Emma sigh at emmaMoveUp with dissolve
    show Lila happy at PopUp with dissolve
    L "Thank you!"
    show Lila happy at MoveUp with dissolve
    show Emma envy at PopUp with dissolve
    E "That wasn't a compliment."
    show Emma envy at emmaMoveUp with dissolve
    show Liam sigh with dissolve
    show Liam nervous at LiamPopUp with dissolve
    L2 "I feel relieved we are here with you..."
    show Liam nervous at LiamMoveUp with dissolve
    show Emma surprised with dissolve
    show Lila surprised with dissolve
    show Liam nervous at LiamPopUp with dissolve
    L2 "Who knows what could have happened if you went on this journey by yourself."
    show Liam default at LiamMoveUp with dissolve
    show Emma sigh with dissolve
    show Emma soft with dissolve
    show Lila Sweats with dissolve
    show Liam default at LiamPopUp with dissolve
    L2 "Anyways."
    show Liam happy with dissolve
    L2 "Looks like there's a few branching paths ahead of us."
    L2 "Why don't we go take a look?"
    show Liam happy at LiamMoveUp with dissolve
    hide Lila Sweats with fade
    hide Emma envy with fade
    hide Liam happy with fade
    window hide

###########First branching paths###############
label menu_Observe:
    hide image "Forest_Default.png" with dissolve
    show image "Twopaths.png" with dissolve
    menu:
        "Observe the places first?":
                jump ObserveFirst
        "Go to Cave.":
                jump Cave1
        "Sit and wait." if sitWait == True:
                jump SaW1
    window hide
return
###########First branching paths###############
label ObserveFirst:
    window show
    hide image "Forest_Default.png" with dissolve
    show image "Twopaths.png" with dissolve
    show Lila skeptical at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila skeptical at PopUp with dissolve
    L "Which place should I check out first?"
    show Lila skeptical at MoveUp with dissolve
    show Liam default at LiamPopUp with dissolve
    L2 "Up to you."
    show Emma sigh with dissolve
    hide Lila skeptical with dissolve
    hide Liam default with dissolve
    hide Emma sigh with dissolve
    window hide
    menu:
        "Cave.":
            jump OC1
    window hide
return
#######################Cave Observation###########################
label OC1:
    window show
    hide image "Forest_Default.png" with dissolve
    window hide
    show image "CaveEntrance.png" with dissolve
    pause 1.5
    window show
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila skeptical at PopUp with dissolve
    L "What should I do first?"
    show Lila skeptical at MoveUp with dissolve
    show Emma envy at emmaflip with dissolve
    show Emma envy at PopUp with dissolve
    E "Or we could just go to the cave."
    show Emma envy at emmaMoveUp with dissolve
    show Lila surprised with dissolve
    show Lila swirly eyes with dissolve
    show Liam nervous with dissolve
    show Liam sigh with dissolve
    show Liam smile at LiamPopUp with dissolve
    L2 "No harm in being extra cautious."
    show Liam smile at LiamMoveUp with dissolve
    show Liam default with dissolve
    show Emma surprised with dissolve
    show Emma dissapointed with dissolve
    show Emma envy with dissolve
    hide Lila swirly eyes with fade
    hide Liam default with fade
    hide Emma envy with fade
    window hide
label menu_OC1:
    menu:
        "Look at the surroundings." if C_Sight1 == True:
            jump Sight1
        "Feel the surrounding." if C_Feel1 == True:
            jump Feel1
        "Listen to the area." if C_Sound1 == True:
            jump Sound1
        "Check out the scent in the area." if C_Smell1 == True:
            jump Smell1
        "Ready to enter cave.":
            jump Cave1
    window hide
return

label OC2:
    window hide
    hide image "Forest_Default.png" with dissolve
    show image "CaveEntrance.png" with dissolve
    pause 1.5
label menu_OC2:
    menu:
        "Look at the surroundings." if C_Sight1 == True:
            jump Sight2
        "Feel the surrounding." if C_Feel1 == True:
            jump Feel2
        "Listen to the area." if C_Sound1 == True:
            jump Sound2
        "Check out the scent in the area." if C_Smell1 == True:
            jump Smell2
        "Go back to Cave?":
            jump Cave2
    window show
    hide CaveEntrance with dissolve
return

label Sight1:
    window show
    show Lila default at MoveUp
    show Liam default at LiamMoveUp
    show Liam default at LiamRight
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila skeptical at PopUp with dissolve
    L "Do you guys see anything from here?"
    show Lila skeptical at MoveUp with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    show Liam default with dissolve
    show Emma dissapointed at PopUp with dissolve
    E "Hmmmm...."
    show Emma smug with dissolve
    E "Besides the abnormal amount of formulated crystals no I don't see anything else."
    show Emma smug at emmaMoveUp with dissolve
    show Lila surprised at PopUp with dissolve
    L "Those things look familiar..."
    L "Oh right!"
    L "Like your pocket knife."
    show Lila surprised at MoveUp with dissolve
    show Emma sly at PopUp with dissolve
    E "It's called a {color=#00ffe8}dagger{/color} you dense idiot."
    $C_Sight1 = False
    $DaggerInfo = True
    $NoDaggerInfo = False
    hide Lila surprised with fade
    hide Emma sly with fade
    hide Liam default with fade
    window hide
jump menu_OC1
return

label Feel1:
    window show
    show Lila default at MoveUp
    show Liam default at LiamMoveUp
    show Liam default at LiamRight
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila Sweats at PopUp with dissolve
    L "Why does the cave make me feel so weird..."
    show Lila Sweats at MoveUp with dissolve
    show Liam surprised with dissolve
    show Emma surprised at emmaflip with dissolve
    show Emma concern at PopUp with dissolve
    E "What are you on about?"
    show Emma concern at emmaMoveUp with dissolve
    show Lila skeptical at PopUp with dissolve
    show Liam default with dissolve
    L "There's just this bad feeling about it but also feels like something is pulling me in..."
    show Lila skeptical at MoveUp with dissolve
    show Emma sigh at PopUp with dissolve
    show Liam smile with dissolve
    E "I have no clue what you're on about."
    show Liam nervous with dissolve
    show Lila dumbfounded with dissolve
    $C_Feel1 = False
    hide Liam nervous with fade
    hide Lila dumbfounded with fade
    hide Emma sigh with fade
    window hide
jump menu_OC1
return

label Sound1:
    window show
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Emma dissapointed at PopUp with dissolve
    E "I hear nothing but insects."
    show Emma dissapointed at emmaMoveUp with dissolve
    show Lila skeptical at PopUp with dissolve
    play sound Bird fadein 5.0 volume 1
    L "..."
    L "Really?"
    L "I hear some kind of...chirping?"
    show Lila skeptical at MoveUp with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    show Emma happy at PopUp with dissolve
    E "Oh wait!"
    show Lila surprised with dissolve
    show Emma excited with dissolve
    E "You're right!"
    show Emma sly with dissolve
    show Liam nervous with dissolve
    show Liam default with dissolve
    E "It's definitely a {color=#00ffe8}Hercinia{/color}."
    show Emma excited with dissolve
    E "Let's go hunt it down."
    hide Lila surprised with fade
    hide Liam default with fade
    hide Emma excited with fade
    window hide
    menu:
        "What! No! Don't do it!":
            jump DidNotKill
        "Sure? I guess it's ok...":
            jump KillIt
    window hide
return

label Smell1:
    window show
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Emma default at emmaflip
    show Emma surprised at PopUp with dissolve
    E "What are you doing?"
    show Emma surprised at emmaMoveUp with dissolve
    show Lila stunned at PopUp with dissolve
    L "Smelling the the area."
    show Lila stunned at MoveUp with dissolve
    show Lila smile with dissolve
    show Liam laugh with dissolve
    show Liam happy with dissolve
    show Liam default with dissolve
    show Emma concern at PopUp with dissolve
    E "...Why?"
    show Emma concern at emmaMoveUp with dissolve
    show Lila happy at PopUp with dissolve
    L "Just wondering."
    show Lila happy at MoveUp with dissolve
    show Emma envy with dissolve
    show Liam laugh at LiamPopUp with dissolve
    L2 "pft-"
    show Liam laugh at LiamMoveUp with dissolve
    show Lila surprised with dissolve
    show Emma surprised with dissolve
    show Liam smile at LiamPopUp with dissolve
    L2 "What does it smell like?"
    show Liam default at LiamMoveUp with dissolve
    show Emma envy with dissolve
    show Emma sigh with dissolve
    show Lila smile at PopUp with dissolve
    L "Fresh grass."
    $C_Smell1 = False
    hide Lila smile with fade
    hide Emma sigh with fade
    hide Liam smile with fade
    window hide
jump menu_OC2
return

label Sight2:
    window show
    show Lila default at MoveUp
    show Liam default at LiamMoveUp
    show Liam default at LiamRight
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila skeptical at PopUp with dissolve
    L "Do you guys see anything from here?"
    show Lila skeptical at MoveUp with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    show Liam default with dissolve
    show Emma dissapointed at PopUp with dissolve
    E "Hmmmm...."
    show Emma smug with dissolve
    E "Besides the abnormal amount of formulated crystals no I don't see anything else."
    show Emma smug at emmaMoveUp with dissolve
    show Lila surprised at PopUp with dissolve
    L "Those things look familiar..."
    L "Oh right!"
    L "Like your pocket knife."
    show Lila surprised at MoveUp with dissolve
    show Emma sly at PopUp with dissolve
    E "It's called a {color=#00ffe8}dagger{/color} you dense idiot."
    $C_Sight1 = False
    $DaggerInfo = True
    $NoDaggerInfo = False
    hide Lila surprised with fade
    hide Emma sly with fade
    hide Liam default with fade
    window hide
jump menu_OC2
return

label Feel2:
    window show
    show Lila default at MoveUp
    show Liam default at LiamMoveUp
    show Liam default at LiamRight
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila Sweats at PopUp with dissolve
    L "Why does the cave make me feel so weird..."
    show Lila Sweats at MoveUp with dissolve
    show Liam surprised with dissolve
    show Emma surprised at emmaflip with dissolve
    show Emma concern at PopUp with dissolve
    E "What are you on about?"
    show Emma concern at emmaMoveUp with dissolve
    show Lila skeptical at PopUp with dissolve
    show Liam default with dissolve
    L "There's just this bad feeling about it but also feels like something is pulling me in..."
    show Lila skeptical at MoveUp with dissolve
    show Emma sigh at PopUp with dissolve
    show Liam smile with dissolve
    E "I have no clue what you're on about."
    show Liam nervous with dissolve
    show Lila dumbfounded with dissolve
    $C_Feel1 = False
    hide Liam nervous with fade
    hide Lila dumbfounded with fade
    hide Emma sigh with fade
    window hide
jump menu_OC2
return

label Sound2:
    window show
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Emma dissapointed at PopUp with dissolve
    E "I hear nothing but insects."
    show Emma dissapointed at emmaMoveUp with dissolve
    show Lila skeptical at PopUp with dissolve
    play sound Bird fadein 5.0 volume 1
    L "..."
    L "Really?"
    L "I hear some kind of...chirping?"
    show Lila skeptical at MoveUp with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    show Emma happy at PopUp with dissolve
    E "Oh wait!"
    show Lila surprised with dissolve
    show Emma excited with dissolve
    E "You're right!"
    show Emma sly with dissolve
    show Liam nervous with dissolve
    show Liam default with dissolve
    E "It's definitely a {color=#00ffe8}Hercinia{/color}."
    show Emma excited with dissolve
    E "Let's go hunt it down."
    hide Lila surprised with fade
    hide Liam default with fade
    hide Emma excited with fade
    window hide
    menu:
        "What! No! Don't do it!":
            jump DidNotKill2
        "Sure? I guess it's ok...":
            jump KillIt2
    window hide
return

label Smell2:
    window show
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Emma default at emmaflip
    show Emma surprised at PopUp with dissolve
    E "What are you doing?"
    show Emma surprised at emmaMoveUp with dissolve
    show Lila stunned at PopUp with dissolve
    L "Smelling the the area."
    show Lila stunned at MoveUp with dissolve
    show Lila smile with dissolve
    show Liam laugh with dissolve
    show Liam happy with dissolve
    show Liam default with dissolve
    show Emma concern at PopUp with dissolve
    E "...Why?"
    show Emma concern at emmaMoveUp with dissolve
    show Lila happy at PopUp with dissolve
    L "Just wondering."
    show Lila happy at MoveUp with dissolve
    show Emma envy with dissolve
    show Liam laugh at LiamPopUp with dissolve
    L2 "pft-"
    show Liam laugh at LiamMoveUp with dissolve
    show Lila surprised with dissolve
    show Emma surprised with dissolve
    show Liam smile at LiamPopUp with dissolve
    L2 "What does it smell like?"
    show Liam default at LiamMoveUp with dissolve
    show Emma envy with dissolve
    show Emma sigh with dissolve
    show Lila smile at PopUp with dissolve
    L "Fresh grass."
    $C_Smell1 = False
    hide Lila smile with fade
    hide Emma sigh with fade
    hide Liam smile with fade
    window hide
jump menu_OC2
return

label SaW1:
    window show
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila default at PopUp with dissolve
    L "Let's just sit and wait it out."
    show Lila default at MoveUp with dissolve
    show Liam surprised with dissolve
    show Liam laugh with dissolve
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    show Emma angry at PopUp with dissolve
    E "That is the dumbest idea I've ever heard."
    show Emma angry at emmaMoveUp with dissolve
    show Liam surprised with dissolve
    show Liam nervous with dissolve
    hide screen negative_affection
    show Lila dumbfounded at PopUp with dissolve
    L "..."
    show Lila Sweats with dissolve
    L "Sorry."
    $sitWait = False
    hide Lila dumbfounded with fade
    hide Emma angry with fade
    hide Liam nervous with fade
    window hide
jump menu_Observe
return
