label Cave1:
    play sound Walk
    stop music fadeout 1.0
    play music NormalCaveMusic fadein 5.0 volume 0.3 loop
    window show
    scene image "Cave.png" with dissolve
    show Lila default at MoveUp
    show Lila default at middle
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaLeft
    show Emma default at emmaMoveUp
    show Lila surprised at PopUp with dissolve
    stop sound
    L "Oh my!"
    show Liam surprised with dissolve
    show Emma surprised with dissolve
    show Lila happy with dissolve
    L "There's so much stuff here to explore!"
    show Liam nervous with dissolve
    show Lila happy at MoveUp with dissolve
    show Emma sigh at PopUp with dissolve
    E "Yeah..."
    show Emma concern with dissolve
    E "{color=#00ffe8}Dangerous stuff{/color} too."
    show Emma concern at emmaMoveUp with dissolve
    show Lila surprised with dissolve
    show Liam default at LiamPopUp with dissolve
    L2 "I agree with Emma."
    show Liam nervous with dissolve
    show Lila nervous with dissolve
    show Emma smug with dissolve
    L2 "It's best if you {color=#00ffe8}stick to us{/color} ."
    hide Emma smug with fade
    hide Lila nervous with fade
    hide Liam nervous with fade
    window hide
    menu:
        "I'm counting on you guys!":
            jump CountingOnYou
        "I don't really need you guys.":
            jump DoNotNeed
        "I'm sure there's nothing that dangerous in here.":
            jump NothingDan
    window hide
return

######For relationship points#########

label CountingOnYou:
    window show
    scene image "Cave.png" with dissolve
    show Lila default at MoveUp
    show Lila default at middle
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaLeft
    show Emma default at emmaMoveUp
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $liam_points += 1
    show Emma surprised with dissolve
    show Liam surprised with dissolve
    show Emma happy at PopUp with dissolve
    E "You can count on us!"
    hide screen positive_affection
    show Emma happy at emmaMoveUp with dissolve
    show Lila surprised with dissolve
    show Lila smile with dissolve
    show Liam smile with dissolve
    show Emma excited at PopUp with dissolve
    E "I'll make sure a weakling like you will live through this."
    show Emma excited at emmaMoveUp with dissolve
    show Liam content at LiamPopUp with dissolve
    L "You're adorable Lila."
    show Liam content at LiamMoveUp with dissolve
    show Lila surprised with dissolve
    show Lila blush with dissolve
    show Emma surprised with dissolve
    show Emma envy at PopUp with dissolve
    E "Ado-!"
    show Emma pout with dissolve
    E "This is the only time I'm letting this go."
    $renpy.notify("Drag the magnifying glass to interact with objects.")
    hide Emma pout with dissolve
    hide Lila blush with dissolve
    hide Liam content with dissolve
    window hide
    jump drag_glass
return

label DoNotNeed:
    window show
    scene image "Cave.png" with dissolve
    show Lila Sweats at MoveUp
    show Lila Sweats at middle
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaLeft
    show Emma default at emmaMoveUp
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    show Emma shocked at PopUp with dissolve
    show Liam shocked with dissolve
    E "What was that?"
    hide screen negative_affection
    show Liam sad with dissolve
    show Emma concern at emmaMoveUp with dissolve
    show Lila panic with dissolve
    show Lila Sweats with dissolve
    show Lila eyes closed sad at PopUp with dissolve
    L "..."
    show Lila eyes closed sad at MoveUp with dissolve
    show Emma angry at PopUp with dissolve
    E "I can't believe you actually had the nerve to say that."
    show Lila Sweats with dissolve
    show Emma dissapointed with dissolve
    E "I don't care if you feel this way about me..."
    show Emma yell with dissolve
    show Lila sad with dissolve
    E "But how can you include Liam-"
    show Liam sigh at LiamPopUp with dissolve
    L "It's fine Emma."
    show Emma shocked at emmaMoveUp with dissolve
    show Liam nervous with dissolve
    show Emma pout with dissolve
    L "I'm sure she meant it as a joke."
    show Lila Sweats with dissolve
    show Liam nervous at LiamMoveUp with dissolve
    show Emma envy at PopUp with dissolve
    E "Well it wasn't funny..."
    show Emma angry with dissolve
    E "I didn't get labeled as an outcast to protect an ungrateful brat."
    show Emma angry at emmaMoveUp with dissolve
    show Liam sigh with dissolve
    show Liam angry at LiamPopUp with dissolve
    L "Ok enough."
    show Lila shocked with dissolve
    show Emma shocked with dissolve
    show Emma pout with dissolve
    show Lila eyes closed sad with dissolve
    show Liam nervous  with dissolve
    L "No more before we start to regret our actions and words."
    $renpy.notify("Drag the magnifying glass to interact with objects.")
    hide Emma pout with dissolve
    hide Lila eyes closed sad with dissolve
    hide Liam nervous with dissolve
    window hide
    jump drag_glass
return

label NothingDan:
    window show
    scene image "Cave.png" with dissolve
    show Lila default at MoveUp
    show Lila default at middle
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaLeft
    show Emma default at emmaMoveUp
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $liam_points += 1
    show Emma envy at PopUp with dissolve
    E "How oblivious can you get?"
    hide screen positive_affection
    show Lila stunned with dissolve
    show Emma sigh with dissolve
    E "There's a limit to how stupid you can be."
    show Lila angry with dissolve
    show Liam sigh with dissolve
    show Liam angry at LiamPopUp with dissolve
    show Emma sigh at emmaMoveUp with dissolve
    L2 "Ok enough Emma."
    show Lila surprised with dissolve
    show Liam angry at LiamMoveUp with dissolve
    show Emma surprised with dissolve
    show Emma pout with dissolve
    show Liam smile at LiamPopUp with dissolve
    L2 "Just stay close to us, ok Lila?"
    show Liam smile at LiamMoveUp with dissolve
    show Lila smile at PopUp with dissolve
    L "Ok?"
    show Lila smile at MoveUp with dissolve
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    show Emma envy at PopUp with dissolve
    E "Ugh."
    hide screen negative_affection
    show Emma pout with dissolve
    E "Favoritism..."
    show Lila stunned with dissolve
    show Liam nervous with dissolve
    show Liam embarrassed with dissolve
    $renpy.notify("Drag the magnifying glass to interact with objects.")
    hide Emma pout with fade
    hide Lila stunned with fade
    hide Liam embarrassed with fade
    window hide
    jump drag_glass
return


######If Players been to cave once already###############
label Cave2:
    window hide
    scene image "Cave.png" with dissolve
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
    window show
return

##########The Door Options##########

label drag_glass:
    play sound Walk
    window hide
    stop sound
    call screen slide_glass_screen
    hide CloseupBerry
    hide CloseupCrystal
    hide CloseupCrystalBlood
    hide CloseupCrystalHandPrint
    hide CloseupOpus
    hide CloseupPageCave
    hide CloseupPageDen
    hide CloseupVine
    hide CloseupWyrm
    hide CloseupRock
    hide CloseupDoor
    hide OpusDistract
    hide OpusDistract2
    hide OpusDistract3
    hide OpusDistract4
    hide OpusDistract5
    hide Vina neutral
    hide Vina death
    hide VineHurt
    hide VineBurn
    hide VineWall
    hide LilaTouchCrystal
    hide LilaSharpRock
    hide LilaandEmmaOpus
    hide LilaCatchPage
    hide LilaThrowDrumstick
    hide LilaThrowDrumstick2
    "[glass] picked the [object]"
    menu:
        "{color=#fb92ff}Go through the Crystal Door?{/color}" if store.object == "Crystal Door.":
            jump CrystalDoor
        "{color=#4000ff}Go through the Opus Door?{/color}" if store.object == "Opus Door.":
            jump OpusDoor
        "{color=#c8c8ff}Go through the Treasure Door?{/color}" if store.object == "Treasure Door.":
            jump TreasureDoor
        "{color=#4469ff}Look at rock?{/color}" if store.object == "Rock.":
            jump RockByCrystal
        "{color=#58f7ff}Look at the vine?" if store.object == "vine?":
            jump VineWall
        "Go back":
            jump drag_glass
    window hide
return
######Rock by Crystal was found.#########
label drag_glass2:
    play sound Walk
    window hide
    stop sound
    call screen slide_glass_screen2
    hide CloseupBerry
    hide CloseupCrystal
    hide CloseupCrystalBlood
    hide CloseupCrystalHandPrint
    hide CloseupOpus
    hide CloseupPageCave
    hide CloseupPageDen
    hide CloseupVine
    hide CloseupWyrm
    hide CloseupRock
    hide CloseupDoor
    hide CaveEntrance
    hide Vina neutral
    hide Vina death
    hide VineHurt
    hide VineBurn
    hide VineWall
    hide LilaTouchCrystal
    hide LilaSharpRock
    hide LilaandEmmaOpus
    hide LilaCatchPage
    hide LilaThrowDrumstick
    hide LilaThrowDrumstick2
    "[glass] picked the [object]"
    menu:
        "{color=#fb92ff}Go through the Crystal Door?{/color}" if store.object == "Crystal Door.":
            jump CrystalDoor
        "{color=#4000ff}Go through the Opus Door?{/color}" if store.object == "Opus Door.":
            jump OpusDoor
        "{color=#c8c8ff}Go through the Treasure Door?{/color}" if store.object == "Treasure Door.":
            jump TreasureDoor
        "{color=#58f7ff}Look at the vine?{/color}" if store.object == "vine?":
            jump VineWall
        "Go back":
            jump drag_glass2
    window hide
return
##########Crystal Door###########
label CrystalDoor:
    window hide
    menu:
        "Look at pretty crystal?" if CrystalLooked == True:
            jump LookAtCrystal
        "Look at pretty crystal?" if CrystalLooked == False:
            jump Crystal_menu
        "Back Away" if GotRock == False:
            jump drag_glass
        "Back Away" if GotRock == True:
            jump drag_glass2
    window hide
label Crystal_menu:
    play sound Walk
    window hide
    if emma_points >= 2:
        if thing == True:
            $TouchCrystal_EmmaCare = True
            $TouchCrystal_EmmaDoNotCare = False
    if GotRock2 == True:
        if SawVine == True:
            $GotRock1 = False
    menu:
        "Rub hand on crystal." if TouchCrystal_EmmaCare == True:
            jump TouchCrystal1
        "Rub hand on crystal." if TouchCrystal_EmmaDoNotCare == True:
            jump TouchCrystal2
        "Rub hand on crystal." if CrystalTouched == True:
            jump TouchCrystal3
        "Rub the rock on the crystal." if GotRock1 == True:
            jump EarnedSharpRock
        "Rub the rock on the crystal." if GotRock2 == True & SawVine == True:
            jump EarnedSharpRock2
        "Back Away" if GotRock == False:
            jump drag_glass
        "Back Away" if GotRock == True:
            jump drag_glass2
    window hide
return

label LookAtCrystal:
    window hide
    show CloseupCrystal
    pause 1
    window show
    show Lila surprised at left with moveinleft
    L "Whoa!"
    show Lila smile with dissolve
    L "This crystal is huge!"
    hide Lila smile with moveoutleft
    show Emma sigh at left with moveinleft
    E "Yeah."
    show Emma smug with dissolve
    E "Huge and sharp."
    hide Emma smug with moveoutleft
    show Liam dark smile at right with moveinright
    L2 "Sooooo sharp it'll slice right through your skin."
    hide Liam dark smile with moveoutright
    show Emma sly at left with moveinleft
    E "{color=#00ffe8}It's how my dagger is made.{/color}"
    E "{color=#00ffe8}Sharpening minerals on this exact type crystal.{/color}"
    hide Emma sly at left with moveoutleft
    show Lila shocked at left with moveinleft
    show Lila Sweats with dissolve
    L "..."
    hide Lila Sweats with moveoutleft
    $CrystalLooked = False
    window hide
    jump Crystal_menu
return

label TouchCrystal1:
    E "Wha-!"
    E "Stop!" with vpunch
    window hide
    play sound EmmaSlash
    show LilaTouchCrystal with dissolve
    pause 1
    window show
    #show Emma shocked at left with moveinleft
    #hide Emma shocked at left with moveoutleft
    play sound Ouch
    L "Ouch!" with hpunch
    stop sound
    hide LilaTouchCrystal with dissolve
    show CloseupCrystalBlood
    show Emma angry at left with moveinleft
    E "You idiot!"
    show Emma concern with dissolve
    E "What in the world are you doing?"
    show Emma envy with dissolve
    E "I just said it's sharp."
    show Emma angry with dissolve
    E "Why don't you ever listen?"
    hide Emma angry with moveoutleft
    show Lila Sweats at left with moveinleft
    L "..."
    hide Lila Sweats with moveoutleft
    show Emma angry at left with moveinleft
    E "Liam!"
    show Emma concern with dissolve
    E "Why didn't you stop her?"
    hide Emma concern with moveoutleft
    show Liam dark smile at right with moveinright
    L "She has to learn somehow."
    hide Liam dark smile at right with moveoutright
    show Emma sigh at left with moveinleft
    show Emma dissapointed with dissolve
    E "You chose the weridest times to be strict..."
    hide Emma dissapointed with moveoutleft
    show Lila shocked at left with moveinleft
    L "..."
    hide Lila shocked at left with moveoutleft
    show Emma sigh at left with moveinleft
    E "Come here."
    show Emma soft with dissolve
    E "Let's patch you up."
    hide Emma soft with moveoutleft
    $TouchCrystal_EmmaCare = False
    $TouchCrystal_EmmaDoNotCare = False
    $CrystalTouched = True
    $LilaBleed = False
    $LilaDoNotBleed = True
    $thing = False
    window hide
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
return

label TouchCrystal2:
    window hide
    play sound EmmaSlash
    show LilaTouchCrystal with dissolve
    pause 1
    window show
    play sound Ouch
    L "Ouch!" with hpunch
    stop sound
    hide LilaTouchCrystal with dissolve
    show CloseupCrystalBlood
    show Emma sigh at left with moveinleft
    E "I just told you not to yet you went and did it."
    show Emma envy with dissolve
    E "Serves you right."
    hide Emma envy with moveoutleft
    show Liam nervous at right with moveinright
    L2 "Don't look at me that way Lila..."
    show Liam sigh with dissolve
    L2 "You have to understand how to take care of yourself."
    show Liam nervous with dissolve
    L2 "What would happen if we weren't here with with you?"
    hide Liam nervous with moveoutright
    show Emma sigh at left with moveinleft
    E "Stop wasting your breath on her."
    show Emma envy with dissolve
    E "Let's move on."
    hide Emma sigh with moveoutleft
    $TouchCrystal_EmmaDoNotCare = False
    $TouchCrystal_EmmaCare = False
    $CrystalTouched = True
    $LilaBleed = True
    $LilaDoNotBleed = False
    $LilaBleed2 = True
    $thing = False
    window hide
jump drag_glass
return

label TouchCrystal3:
    window hide
    show CloseupCrystalBlood
    pause 1
    window show
    show Emma intimidating at left with moveinleft
    E "Don't even think about it."
    hide Emma intimidating with moveoutleft
    show Lila Sweats at left with moveinleft
    L "..."
    hide Lila Sweats with moveinleft
    $TouchCrystal_EmmaDoNotCare = False
    $TouchCrystal_EmmaCare = False
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
    window hide
return

label EarnedSharpRock:
    window hide
    show LilaSharpRock
    pause 1
    window show
    #show Emma concern at left with moveinleft
    E "What are you are doing?"
    #hide Emma concern with moveoutleft
    L "?"
    hide LilaSharpRock with fade
    show CloseupCrystal with fade
    show Lila smile at left with moveinleft
    L "Sharpening the rock?"
    hide Lila smile with moveoutleft
    show Emma surprised with moveinleft
    E "But why?"
    hide Emma surprised with moveoutleft
    show Lila skeptical with moveinleft
    L "Not sure."
    hide Lila skeptical with moveoutleft
    show Emma sigh with moveinleft
    E "Why don't you ever think about your actions?"
    hide Emma sigh with moveoutleft
    show Liam nervous at right with moveinright
    L2 "It's alright Emma."
    show Liam smile with dissolve
    L2 "Might be useful to have a sharp weapon on her."
    hide Liam smile with moveoutright
    show Emma pout at left with moveinleft
    E "Hmf."
    show Emma sigh with dissolve
    E "Guess you're right."
    hide Emma sigh with moveoutleft
    show Lila happy at left with moveinleft
    L "Look."
    show screen inventory_button
    $inventory.add(Sharprock)
    $inventory.drop(dullrock)
    $renpy.notify("Lila sharpened her dull rock.")
    show Lila smile at left with moveinleft
    L "It's so sharp!"
    hide screen inventory_button
    hide Lila smile with moveoutleft
    $GotRock1 = False
    $GotRock2 = False
    $thing3 = False
    $GotSharpRock = True
    window hide
    jump drag_glass2
return

label EarnedSharpRock2:
    window hide
    show LilaSharpRock
    pause 1
    window show
    show Emma concern at left with moveinleft
    E "What are you are doing?"
    hide Emma concern with moveoutleft
    L "?"
    hide LilaSharpRock with fade
    show CloseupCrystal with fade
    show Lila smile at left with moveinleft
    L "Sharpening the rock?"
    hide Lila smile with moveoutleft
    show Emma surprised at left with moveinleft
    E "Oh!"
    show Emma excited with dissolve
    E "Is this for the vine?"
    hide Emma excited with moveoutleft
    show Lila smile at left with moveinleft
    L "..."
    show Lila blush with dissolve
    show Lila panic with dissolve
    show Lila swirly eyes with dissolve
    show Lila Sweats with dissolve
    L "Y-Yeah!"
    show Lila nervous with dissolve
    L "Look."
    show screen inventory_button
    $renpy.notify("Lila sharpened her dull rock.")
    $inventory.add(Sharprock)
    $inventory.drop(dullrock)
    show Lila smile with dissolve
    L "It's so sharp!"
    hide screen inventory_button
    hide Lila smile with moveoutleft
    show Emma sly at left with moveinleft
    E "..."
    show Emma sigh with dissolve
    E "You're so bad at lying..."
    hide Emma sigh with moveoutleft
    $GotRock1 = False
    $GotRock2 = False
    $GotSharpRock = True
    $thing3 = False
    window hide
    jump drag_glass2
###########Opus Door##############

label OpusDoor:
    play sound Walk
    window hide
    show CloseupOpus
label Opus_Menu:
    play sound Opus fadein 5.0
    menu:
        "Look at this blob!" if LookAtOpus == True:
            jump Opus
        "Look at the Opus." if LookAtOpus == False:
            jump Opus2
        "Pick up a rock by the floor." if RockFound_Opus == True:
            jump Rock
        "Pick up a rock by the floor." if RockFound_Opus2 == True:
            jump Rock_menu
        "Back Away" if GotRock == False:
            jump drag_glass
        "Back Away" if GotRock == True:
            jump drag_glass2
    window hide
return

label Opus:
    play sound Walk
    window hide
    show LilaandEmmaOpus with dissolve
    pause 1
    window show
    #show Lila smile at left with moveinleft
    L "Look at this cute little thing!"
    #hide Lila smile with moveoutleft
    #show Emma nervous at left with moveinleft
    E "Cute thing?"
    #show Emma sigh at left with dissolve
    E "Where?"
    #hide Emma sigh with moveoutleft
    #show Lila confused at left with moveinleft
    L "?"
    #show Lila skeptical with dissolve
    L "The blob right here."
    #hide Lila skeptical with moveoutleft
    #show Emma shocked at left with moveinleft
    E "The Opus?"
    #hide Emma shocked with moveoutleft
    #show Lila smile at left with moveinleft
    L "Is that what it's called?"
    #hide Lila smile at left with moveoutleft
    #show Liam smile at right with moveinright
    L2 "Yep."
    #show Liam default with dissolve
    L2 "As cute as it looks {color=#00ffe8}don't go near it.{/color}"
    #hide Liam default with moveoutright
    #show Lila confused at left with moveinleft
    L "Why?"
    #hide Lila confused with moveoutleft
    #show Liam dark smile at right with moveinright
    L2 "You'll lose a finger or two."
    #hide Liam dark smile with moveoutright
    #show Lila panic at left with moveinleft
    #show Lila Sweats with dissolve
    L "Oh..."
    #hide Lila Sweats with moveoutleft
    $LookAtOpus = False
    hide LilaandEmmaOpus
    window hide
    jump Opus_Menu
return

label Opus2:
    play sound Walk
    window hide
    show LilaandEmmaOpus with dissolve
    window show
    #show Lila smile at left with moveinleft
    L "Hehe."
    L "Look at it just bobble."
    #hide Lila smile with moveoutleft
    #show Emma sigh at left with moveinleft
    E "..."
    #hide Emma sigh with moveoutleft
    $LookAtOpus = False
    hide LilaandEmmaOpus
    window hide
    jump Opus_Menu
return

###########Still part of Opus Door but For rock options########
label Rock:
    play sound Opus fadein 5.0
    window hide
    show CloseupRock
    pause 1
    window show
    show Emma concern at left with moveinleft
    E "What are you doing?"
    hide Emma concern with moveoutleft
    show Lila default at left with moveinleft
    L "Trying to get this rock."
    hide Lila default with moveoutleft
    show Emma envy at left with moveinleft
    E "Don't put your hand near it idiot."
    hide Emma envy with moveoutleft
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    window hide
label Rock_menu:
    if emma_points >= 2:
        if thing2 == True:
            $LookOpus_EmmaCare = True
            $LookOpus_EmmaDoNotCare = False
            $TakeRock_EmmaCare = True
            $TakeRock_EmmaDoNotCare = False
    elif GotRock == True:
        $TakeRock_EmmaDoNotCare = False
        $TakeRock_EmmaCare = False
    window hide
    show CloseupRock
    menu:
        "Can we distract it somehow?" if LookOpus_EmmaDoNotCare == True:
            jump InformationOnOpus
        "Can we distract it somehow?" if LookOpus_EmmaCare == True:
            jump InformationOnOpus2
        "Can I feed it the dead bird?" if GotDrumStick == True:
            jump FeedingDeadBird
        "Can you or Liam get it for me?" if TakeRock_EmmaDoNotCare == True:
            jump LiamOrYou
        "Can you or Liam get it for me?" if TakeRock_EmmaCare == True:
            jump LiamOrYou2
        "Can you or Liam get it for me?" if GotRock == True:
            jump LiamOrYou3
        "Just Reach for the rock." if JustReachForRock == True:
            jump ReachForIt
        "Just Reach for the rock." if GotRock == True:
            jump ReachForIt2
        "Guess I'll come back for it later." if GotRock == False:
            jump drag_glass
        "Back away from it." if GotRock == True:
            jump drag_glass2
    window hide
return

#######Hints for Player######

label InformationOnOpus:
    play sound Opus fadein 5.0
    window hide
    show CloseupOpus
    pause 1
    window show
    show Emma dissapointed at left with moveinleft
    E "Not sure."
    show Emma default with dissolve
    E "If we have some kind of {color=#00ffe8}meat{/color} we can feed it."
    show Emma smug with dissolve
    E "While it's eating we can grab one of the rocks nearby."
    hide Emma smug with moveoutleft
    show Liam smile at right with moveinright
    L "{color=#00ffe8}I'm sure Emma will be glad to help you too if you get along with her{/color}."
    show Liam nervous with dissolve
    L "Right Emma?"
    hide Liam nervous with moveoutright
    show Emma pout at left with moveinleft
    E "...Right."
    hide Emma pout with moveoutleft
    $LookOpus_EmmaCare = False
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    hide CloseupOpus
    window hide
    jump Rock_menu
return

label InformationOnOpus2:
    play sound Opus fadein 5.0
    window hide
    show CloseupOpus
    pause 1
    window show
    show Emma dissapointed at left with moveinleft
    E "Hmmmmmm."
    show Emma sly with dissolve
    E "It does like {color=#00ffe8}meat{/color}."
    hide Emma sly with moveoutleft
    show Liam smile at right with moveinright
    L "{color=#00ffe8}I'm sure Emma will be glad to help you too if you get along with her{/color}."
    show Liam default with dissolve
    L "Right Emma?"
    hide Liam with moveoutright
    show Emma soft at left with moveinleft
    E "Of course."
    hide Emma soft with moveoutleft
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    $LookOpus_EmmaDoNotCare = False
    window hide
    jump Rock_menu
return

##########Interactions for rock#########
label FeedingDeadBird:
    play sound Opus fadein 5.0
    window hide
    show CloseupRock
    pause 1
    window show
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    show Emma excited at left with moveinleft
    E "That's a great idea!"
    hide screen positive_affection
    show Emma smug with dissolve
    E "You go ahead and toss the meat to it."
    show Emma sly with dissolve
    E "I'll swoop in and grab the rock."
    hide Emma sly with moveoutleft
    show Lila smile at left with moveinleft
    L "Ok!"
    hide Lila smile with moveoutleft
    show Emma excited at left with moveinleft
    E "On the count of 3!"
    E "3!"
    E "2!"
    E "1!" with vpunch
    hide Emma excited with moveoutleft
    window hide
    show LilaThrowDrumstick
    play sound Whoosh
    pause .4
    hide LilaThrowDrumstick
    show LilaThrowDrumstick2
    play sound Crunch
    pause 1
    hide LilaThrowDrumstick2
    stop sound
    show screen inventory_button
    $renpy.notify("Drumstick has been tossed.")
    $inventory.drop(drumstick)
    window show
    show Emma happy at left with moveinleft
    E "Got it!"
    hide screen inventory_button
    show Emma smug with dissolve
    E "Here you go."
    show screen inventory_button
    $renpy.notify("You gained a Dull Rock.")
    $inventory.add(dullrock)
    hide Emma smug with moveoutleft
    show Lila smile at left with moveinleft
    L "Thanks Emma!"
    hide screen inventory_button
    show Lila happy with dissolve
    L "You're the best."
    hide Lila happy with moveoutleft
    show Emma surprised at left with moveinleft
    show Emma embarrassed with dissolve
    show Emma blush with dissolve
    E "It's no big deal!"
    show Emma smug with dissolve
    E "But what do you plan to do with it?"
    hide Emma smug with moveoutleft
    show Lila skeptical at left with moveinleft
    L "Hmmmm...."
    show Lila dumbfounded with dissolve
    L "Good question."
    hide Lila dumbfounded with moveoutleft
    show Liam smile at right with moveinright
    show Liam wink with dissolve
    L2 "{color=#00ffe8}We might be able to something with it or use it for something{/color}."
    hide Liam wink with moveoutright
    show Lila confused at left with moveinleft
    L "?"
    hide Lila confused with moveoutleft
    $GotDrumStick = False
    $GotRock_Opus = True
    $GotRock_Crystal = False
    $EorL_GetIt = False
    $JustReachForRock = False
    $TakeRock_EmmaDoNotCare = False
    $TakeRock_EmmaCare = False
    $GotRock = True
    $GotRock1 = True
    $GotRock2 = True
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    $thing2 = False
    window hide
    jump drag_glass2
return

label LiamOrYou:
    play sound Opus fadein 5.0
    window hide
    show CloseupRock
    pause 1
    window show
    show Emma concern at left with moveinleft
    E "You must be joking."
    show Emma envy with dissolve
    E "I'm not risking my life for your stupid whims."
    show Emma dissapointed with dissolve
    E "I know what you are thinking."
    show Emma sigh with dissolve
    E "Don't even think about it."
    show Emma angry with dissolve
    E "I'm not letting Liam get hurt either."
    hide Emma angry with moveoutleft
    $TakeRock_EmmaDoNotCare = False
    $TakeRock_EmmaCare = False
    $thing2 = False
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    hide CloseupRock
    jump Rock_menu
return

label LiamOrYou2:
    play sound Opus fadein 5.0
    window hide
    show CloseupRock
    pause 1
    window show
    show Emma default at left with moveinleft
    E "We might be able to."
    show Emma smug with dissolve
    E "Pass me that mushroom in your bag."
    hide Emma smug with moveoutleft
    show Lila confused at left with moveinleft
    L "Ok?"
    play sound Whoosh
    show screen inventory_button
    $renpy.notify("You passed the mushroom to Emma.")
    $inventory.drop(LilaMushroom)
    hide Lila confused with moveinleft
    L "?!" with hpunch
    hide screen inventory_button
    window hide
    L "My Mushroom!"
    play sound DeeperThump
    show OpusDistract
    pause 1
    window show
    stop sound
    L "Why did you throw over to the blob!"
    E "Shut up and just watch."
    L "?"
    play music CaveBattleMusic fadein 5.0 volume 0.3
    E "Liam grab the rock!"
    window hide
    hide OpusDistract
    play sound Whoosh
    show OpusDistract2
    pause 1
    window show
    L2 "Got it!"
    stop sound
    E "Nice!"
    E "I'll go take back the mushroom."
    window hide
    hide OpusDistract2
    play sound Whoosh
    show OpusDistract3
    pause 1
    window show
    E "And got that too."
    hide window
    hide OpusDistract3
    show OpusDistract4
    pause 1
    window show
    stop music fadeout 1.0
    L "Whoa!"
    play music RheaSoundtrack fadein 5.0 volume 0.3
    window hide
    hide OpusDistract4
    show OpusDistract5
    pause 1
    window show
    L "You guys are awesome!"
    hide OpusDistract5
    show CloseupOpus
    E "Here take back your mushroom."
    play sound Whoosh
    hide CloseupOpus
    show CloseupRock
    stop sound
    show screen inventory_button
    $renpy.notify("Emma gave back the mushroom.")
    $inventory.add(LilaMushroom)
    show Emma smug at left with moveinleft
    E "Well Liam's got you your rock too."
    hide Emma smug with moveoutleft
    hide screen inventory_button
    show Liam smile at right with moveinright
    L2 "Here you go."
    hide Liam smile with moveoutright
    show screen inventory_button
    $renpy.notify("Liam gave you the dull rock.")
    $inventory.add(dullrock)
    show Lila happy at left with moveinleft
    L "Thanks guys!"
    hide Lila happy with moveoutleft
    hide screen inventory_button
    show Emma concern at left with moveinleft
    E "What do you plan to do with it?"
    hide Emma concern with moveoutleft
    show Lila skeptical at left with moveinleft
    L "Hmmmmm{cps=2}...{/cps}"
    show Lila confused with dissolve
    L "I'm not sure."
    hide Lila confused with moveoutleft
    show Liam nervous at right with moveinright
    L2 "Maybe check around the {color=#00ffe8}other areas{/color}."
    show Liam smile with dissolve
    L2 "{color=#00ffe8}We might be able to something to it or use it for something{/color}."
    hide Liam smile with moveoutright
    show Lila default at left with moveinleft
    L "Ok."
    hide Lila default with moveoutleft
    $GotDrumStick = False
    $GotRock = True
    $GotRock1 = True
    $GotRock2 = True
    $JustReachForRock = False
    $GotRock_Opus = True
    $GotRock_Crystal = False
    $TakeRock_EmmaDoNotCare = False
    $TakeRock_EmmaCare = False
    $thing2 = False
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    hide CloseupRock
    window hide
    jump drag_glass2
return

label LiamOrYou3:
    play sound Opus fadein 5.0
    window hide
    show CloseupRock
    pause
    window show
    show Emma sigh at left with moveinleft
    E "You already have a rock."
    hide Emma sigh with moveoutleft
    show Lila stunned at left with moveinleft
    L "Oh right."
    hide Lila stunned with moveoutleft
    show Emma concern at left with moveinleft
    E "Getting the rock by this opus will be dangerous."
    show Emma envy with dissolve
    E "I'm not going to get another one if you have one already."
    hide Emma envy with moveoutleft
    show Lila pout at left with moveinleft
    L "Ok."
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    hide CloseupRock
    window hide
    jump Rock_menu
return

label ReachForIt:
    play sound Opus fadein 5.0
    window hide
    show CloseupOpus
    pause 1
    window show
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    hide CloseupOpus
    show Emma panic at left with moveinleft
    E "What a sec-"
    hide Emma panic with moveoutleft
    stop music fadeout 1.0
    hide screen negative_affection
    window hide
    hide CloseupOpus
    hide CloseupRock
    show LilaReachForRock with dissolve
    pause 1
    hide LilaReachForRock with dissolve
    play music CaveBattleMusic fadein 5.0 volume 0.3
    show Opus death with dissolve
    pause 1
    window show
    show Liam shocked at right with moveinright
    L2 "Lila!" with vpunch
    hide Liam shocked with moveoutright
    window hide
    hide Opus death with dissolve
    show LilaScareOfOpus with dissolve
    pause 1
    hide LilaScareOfOpus with dissolve
    $renpy.notify("Liam choose to save you.")
    window show
    play sound DeeperThump
    L2 "!" with hpunch
    stop sound
    play sound LiamFaint fadein 5.0
    window hide
    show LiamHurt with dissolve
    stop sound
    pause 1
    window show
    #show Emma panic at left with moveinleft
    E "Liam!"
    #hide Emma panic with moveoutleft
    #show Lila panic at left with moveinleft
    L "Liam!"
    #show Lila angry cry with dissolve
    L "Are you ok?!"
    #hide Lila panic with moveoutleft
    #show Emma yell at left with moveinleft
    E "You!" with vpunch
    #show Emma yell cry with dissolve
    E "Lila!"
    E "This all your fault!"
    #hide Emma yell cry with moveoutleft
    #show Liam nervous at right with moveinright
    L2 "It's ok..."
    #show Liam panic with dissolve
    L2 "I-"
    L2 "I just need to rest for a while."
    #show Liam nervous with dissolve
    L2 "You guys should move on without me."
    #hide Liam nervous with moveoutright
    #show Emma yell cry at left with moveinleft
    E "How can you expect me to leave you by yourself?"
    ##hide Emma yell cry with moveoutleft
    L2 "..."
    ##show Emma panic at left with moveinleft
    E "Liam?"
    hide LiamHurt with dissolve
    window hide
    play sound DeeperThump
    show LiamKnockedOut with dissolve
    pause 1
    window show
    stop sound
    ##hide Emma panic with moveoutleft
    #show Lila panic at left with moveinleft
    L "Liam!"
    #hide Lila panic with moveoutleft
    #show Emma shocked at left with moveoutleft
    E "Liam!" with vpunch
    #show Emma panic with dissolve
    E "..."
    hide LiamKnockedOut with dissolve
    show Cave
    hide Emma with moveoutleft
    show Lila angry cry at MoveUp
    show Emma dissapointed at emmaMoveUp
    show Emma dissapointed at emmaflip
    show Emma dissapointed at emmaRight
    show Lila angry cry at PopUp with dissolve
    L "What happened to him?!"
    show Lila panic at MoveUp with dissolve
    show Emma sigh at PopUp with dissolve
    E "He's just unconscious."
    show Emma sigh at emmaMoveUp
    show Lila tears at PopUp with dissolve
    L "What should we do?"
    show Lila tears at MoveUp with dissolve
    show Emma dissapointed at PopUp with dissolve
    E "..."
    hide Emma dissapointed at MoveUp with dissolve
    hide Lila tears with dissolve
    stop music fadeout 1.0
    window hide
    if emma_points >= 1:
        $SaveLiam_EmmaCare = True
        $SaveLiam_EmmaDoNotCare = False
    menu:
        "Let's go look for a nearby village together.":
            jump NearbyVillage
        "Emma. You should go get help." if SaveLiam_EmmaCare == True:
            jump EmmaGoGetHelp
        "Emma. You should go get help." if SaveLiam_EmmaDoNotCare == True:
            jump EmmaGoGetHelp2
        "Let's just leave Liam here and move on.":
            jump BadEnd1
    window hide
return

label ReachForIt2:
    play sound Opus fadein 5.0
    window hide
    show CloseupRock
    pause 1
    window show
    show Emma intimidating at left with moveinleft
    E "Don't even think about it."
    hide Emma intimidating with moveoutleft
    show Lila Sweats at left with moveinleft
    L "Think about what?"
    hide Lila Sweats with moveoutleft
    show Emma envy at left with moveinleft
    E "Grabbing the rock."
    show Emma angry with dissolve
    E "Leave it."
    show Emma envy with dissolve
    E "You have one already."
    hide Emma envy with moveoutleft
    show Lila pout at left with moveinleft
    L "ok..."
    hide Lila pout with moveoutleft
    $GotRock_Crystal = False
    $RockFound_Opus = False
    $RockFound_Opus2 = True
    window hide
    jump Rock_menu
return

##########For Hidden Door##########

label TreasureDoor:
    play sound Walk
    window hide
    show CloseupDoor
    pause 1
    window show
    show Lila nervous at left with moveinleft
    show Lila swirly eyes with dissolve
    show Lila nervous with dissolve
    show Lila confused with dissolve
    L "Huh?"
    show Lila dumbfounded with dissolve
    L "It won't open."
    hide Lila dumbfounded with moveoutleft
    show Emma surprised at left with moveinleft
    E "She's right."
    show Emma sigh with dissolve
    E "Don't think it'll open anytime soon."
    show Emma dissapointed with dissolve
    E "Maybe there's a trigger somewhere?"
    hide Emma dissapointed with moveoutleft
    show Lila sad at left with moveinleft
    L "Nope."
    hide Lila sad with moveoutleft
    #show Liam surprised at right with moveinright
    L2 "Seems like there's an indent here."
    show CloseupDoor2
    #show Liam skeptical with dissolve
    L2 "There must be an object somewhere that can fit in here."
    #hide Liam skeptical with moveoutright
    #show Emma excited at left with moveinleft
    E "So we need some kind of key?"
    #hide Emma excited with moveoutleft
    #show Liam wink at right with moveinright
    L2 "Correct!"
    #hide Liam wink with moveoutright
    #show Lila confused at left with moveinleft
    L "???"
    hide CloseupDoor2
    hide Lila confused with moveoutleft
    window hide
    menu:
        "Go back to observe outside of the cave?":
            jump OC2
        "Go back away from door." if GotRock == False:
            jump drag_glass
        "Go back away from door." if GotRock == True:
            jump drag_glass2
    window hide
return

#####Rock by Crystal####

label RockByCrystal:
    play sound Walk
    window hide
    show CloseupRock
    pause 1
    window show
    show Lila skeptical at left with moveinleft
    L "?"
    L "There's a rock just lying here..."
    hide Lila skeptical with moveoutleft
    show Emma surprised at left with moveinleft
    E "Oh..."
    show Emma sigh with dissolve
    E "So?"
    hide Emma sigh with moveoutleft
    window hide
label RockMenu_Crystal:
    menu:
        "I'm going to take it with us." if GotRock_Crystal == True:
            jump TakeRock
        "Back Away" if GotRock == False:
            jump drag_glass
        "Back Away" if GotRock == True:
            jump drag_glass2
    window hide
return

label TakeRock:
    window hide
    show CloseupRock
    pause 1
    window show
    show screen inventory_button
    play sound Whoosh
    $renpy.notify("You gained a Dull Rock.")
    $inventory.add(dullrock)
    show Emma concern at left with moveinleft
    E "Why do you need a rock for?"
    hide screen inventory_button
    hide Emma concern with moveoutleft
    show Lila skeptical at left with moveinleft
    L "Hmmmm..."
    show Lila swirly eyes with dissolve
    L "Good question."
    hide Lila swirly eyes with moveoutleft
    show Liam skeptical at right with moveinright
    L2 "{color=#00ffe8}We might be able to something with it or use it for something{/color}."
    hide Liam skeptical with moveoutright
    show Lila skeptical at left with moveinleft
    L "I wonder..."
    hide Lila skeptical with moveoutleft
    $GotRock_Crystal = False
    $GotRock_Opus = False
    $GotRock = True
    $GotRock1 = True
    $GotRock2 = True
    $RockFound_Opus = False
    $RockFound_Opus2 = False
    stop sound
    window hide
    jump drag_glass2
return

########################Vine Wall###########
label VineWall:
    play sound Walk
    window hide
    show VineWall
    menu:
        "Look at Vine" if LookAtVine == True:
            jump ObserveVine
        "Look at Vina Plant." if LookAtVine == False:
            jump Vine_menu
        "Go Back." if GotRock == False:
            jump drag_glass
        "Go Back." if GotRock == True:
            jump drag_glass2
    if emma_points >= 2:
        if liam_points >=1:
            if thing == True:
                $Distract_EmmaAndLiamDoNotCare = False
                $Distract_EmmaAndLiamCare = True
label Vine_menu:
    menu:
        "Emma, can't you cut it with your dagger?" if DaggerInfo == True:
            jump EmmaDaggerInfo
        "Can't you two distract while I get the page?" if Distract_EmmaAndLiamDoNotCare == True:
            jump YouTwoDistract
        "Can't you two distract while I get the page?" if Distract_EmmaAndLiamCare == True:
            jump YouTwoDistract2
        "What can I use to cut the vines?" if DaggerInfo == False:
            jump NoEmmaDaggerInfo
        "Ask Liam for more information." if AskLiamForInfo == True:
            jump LiamInfo
        "Cut it." if GotSharpRock == True & LilaDoNotBleed == True:
            jump CutVine
        "Cut it." if GotSharpRock == True & LilaBleed2 == True:
            jump CutVine2
        "Go back." if GotRock == False:
            jump drag_glass
        "Go back." if GotRock == True:
            jump drag_glass2
    window hide
return

label ObserveVine:
    window hide
    show VineWall
    pause 1
    window show
    $SawVine = True
    show Lila surprised at left with moveinleft
    L "Oh my god!"
    show Lila happy with dissolve
    L "Guys!"
    L "It's in here!"
    show Lila smile with dissolve
    L "The thing we need."
    hide Lila smile with moveoutleft
    show Emma envy at left with moveinleft
    E "What?"
    show Emma angry with dissolve
    E "You made us come all the way out here for a piece of paper??"
    hide Emma angry with moveoutleft
    show Lila happy at left with moveinleft
    L "Yep."
    hide Lila happy with moveoutleft
    show Emma yell at left with moveinleft
    E "What the hell-"
    hide Emma yell with moveoutleft
    show Liam sigh at right with moveinright
    show Liam angry with dissolve
    L2 "Let's argue later."
    show Liam sigh with dissolve
    L2 "It's located by a Vina Plant."
    hide Liam sigh with moveoutright
    show Lila dumbfounded at left with moveinleft
    L "Huh?"
    hide Lila dumbfounded with moveoutleft
    show Liam skeptical at right with moveinright
    L2 "Not only are these some thick vines but it's guarded by a {color=#00ffe8}carnivorous beast...{/color}"
    hide Liam skeptical with moveoutright
    show Lila shocked at left with moveinleft
    L "!" with vpunch
    hide Lila shocked with moveoutleft
    show Vina neutral with fade
    play sound VineEyes
    show Lila panic at left with moveinleft
    L "That looks scary..."
    hide Vina neutral with fade
    stop sound
    hide Lila panic with moveoutleft
    show Liam nervous at right with moveinright
    L2 "Yeah..."
    hide Liam nervouse with moveoutright
    $LookAtVine = False
    window hide
    jump Vine_menu
return

label EmmaDaggerInfo:
    window hide
    show VineWall
    pause 1
    window show
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    show Emma surprised at left with moveinleft
    show Emma smile with dissolve
    E "You're actually thinking for once."
    hide screen positive_affection
    show Emma laugh with dissolve
    E "Good job!"
    hide Emma laugh with moveoutleft
    show Lila happy at left with moveinleft
    L "Thank you!"
    hide Lila happy with moveoutleft
    show Emma smug at left with moveinleft
    E "Anyways."
    show Emma dissapointed with dissolve
    E "I can but it won't be enough."
    hide Emma dissapointed with moveoutleft
    show Liam sad at right with moveinright
    L2 "Emma's right."
    show Liam skeptical with dissolve
    L2 "Let's look around the cave for more information."
    L2 "{color=#00ffe8}Maybe there's an object or two that can help us get through here{/color}."
    hide Liam skeptical with moveoutright
    $DaggerInfo = False
    $thing = False
    $Distract_EmmaAndLiamDoNotCare == False
    $Distract_EmmaAndLiamCare = False
    $AskLiamForInfo = False
    $LookAtVine = False
    window hide
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
return

label YouTwoDistract:
    window hide
    show VineWall
    pause 1
    window show
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    show Emma sigh at left with moveinleft
    E "Think about this."
    hide screen negative_affection
    show Emma concern with dissolve
    E "Out of all of us only I carry a weapon."
    show Emma angry with dissolve
    E "If I go fight who's going cuts the these thick vines?"
    hide Emma angry with moveoutleft
    show Lila skeptical at left with moveinleft
    L "Then me and Liam will distract while you cut the vines."
    hide Lila skeptical with moveoutleft
    show Emma sigh at left with moveinleft
    E "Did you hear him?"
    show Emma envy with dissolve
    E "It eats {color=#00ffe8}MEAT{/color}."
    hide Emma envy with moveoutleft
    show Lila confused at left with moveinleft
    L "?"
    hide Lila confused with moveoutleft
    show Emma sigh at left with moveinleft
    E "What are you going to do if you're caught by it?"
    hide Emma sigh with moveoutleft
    show Lila Sweats at left with moveinleft
    L "..."
    hide Lila Sweats with moveoutleft
    show Emma concern at left with moveinleft
    E "{color=#00ffe8}I can't save and cut at the same time{/color}."
    show Emma sigh with dissolve
    E "The parts I've cutted will just grow back."
    show Emma angry with dissolve
    E "Not to mention Vina Plants are unpredictable."
    hide Emma angry with moveoutleft
    show Lila dumbfounded at left with moveinleft
    L "Oh..."
    hide Lila dumbfounded with moveoutleft
    $Distract_EmmaAndLiamDoNotCare == False
    $DaggerInfo = False
    $Distract_EmmaAndLiamCare = False
    $AskLiamForInfo = False
    $thing = False
    $LookAtVine = False
    window hide
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
return

label YouTwoDistract2:
    window hide
    show VineWall
    pause 1
    window show
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    show Emma sigh at left with moveinleft
    E "At the moment I can't."
    hide screen negative_affection
    show Emma concern with dissolve
    E "Vina Plants are unpredictable."
    show Emma dissapointed with dissolve
    E "Maybe if you find another tool for cutting we can do somthing about it."
    hide Emma dissapointed with moveoutleft
    show Lila stunned at left with moveinleft
    L "I see..."
    hide Lila stunned with moveoutleft
    $Distract_EmmaAndLiamDoNotCare = False
    $DaggerInfo = False
    $Distract_EmmaAndLiamCare = False
    $AskLiamForInfo = False
    $thing = False
    $LookAtVine = False
    window hide
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
return

label NoEmmaDaggerInfo:
    window hide
    show VineWall
    pause 1
    window show
    show Emma smug at left with moveinleft
    E "Well I do have my dagger."
    hide Emma smug with moveoutleft
    show Liam sigh at right with moveinright
    L2 "That won't be enough."
    hide Liam sigh with moveoutright
    show Emma dissapointed at left with moveinleft
    E "Sadly yeah."
    hide Emma dissapointed with moveoutleft
    show Lila skeptical at left with moveinleft
    L "Why won't it be enough?"
    hide Lila skeptical with moveoutleft
    show Emma dissapointed at left with moveinleft
    E "Because there's only one weapon but three problems."
    hide Emma dissapointed with moveoutleft
    show Lila confused at left with moveinleft
    L "?"
    hide Lila confused with moveoutleft
    show Liam sigh at right with moveinright
    L2 "In other words..."
    show Liam smile with dissolve
    L2 "We need {color=#00ffe8}two tools{/color}."
    L2 "One for cuting regrowable vines."
    show Liam nervous with dissolve
    L2 "One for fighting the monster that guards here."
    hide Liam nervous with moveoutright
    show Lila confused at left with moveinleft
    L "Oh...ok?"
    hide Lila confused with moveoutleft
    show Emma dissapointed at left with moveinleft
    E "Still don't know if we'll succeed or not."
    show Emma sigh with dissolve
    E "Vina Plants are unpredictable."
    hide Emma sigh with moveoutleft
    show Liam nervous at right with moveinright
    L2 "Doesn't hurt to try."
    hide Liam nervous with moveoutright
    show Emma soft at left with moveinleft
    E "Only if we can properly protect ourselves."
    hide Emma soft with moveoutleft
    $Distract_EmmaAndLiamDoNotCare = False
    $DaggerInfo = False
    $Distract_EmmaAndLiamCare = False
    $AskLiamForInfo = False
    $thing = False
    $LookAtVine = False
    window hide
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
return

label LiamInfo:
    window hide
    show VineWall
    pause 1
    window show
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $liam_points += 1
    show Liam skeptical at right with moveinright
    L2 "Right now tha Vina Plant may look peaceful but it triggers on {color=#00ffe8}blood{/color}."
    hide screen positive_affection
    L2 "It's a vicious meat eater that traps living things with it's vine like body."
    hide Liam skeptical with moveoutright
    show Lila skeptical at left with moveinleft
    L "Cutting it won't work?"
    hide Lila skeptical with moveoutleft
    show Liam nervous at right with moveinright
    L2 "With one of us cutting it'll regrows fast."
    hide Liam nervous with moveoutright
    show Lila confused at left with moveinleft
    L "We can't rip it apart with our hands?"
    hide Lila confused with moveoutleft
    show Liam sigh at right with moveinright
    L2 "Unlike it's delicate appearance"
    L2 "It's body is as tough to rip as the clothes we are wearing."
    show Liam nervous with dissolve
    L2 "Ripping it with our hands might wire us down compared to cutting it with a {color=#00ffe8}smooth sharp edge{/color}."
    show Liam skeptical with dissolve
    L2 "So we might need something else besides Emma's dagger."
    L2 "That's all the information I have on it."
    show Liam sigh with dissolve
    L2 "But I know we are missing bits and pieces."
    hide Liam sigh with moveoutright
    show Emma dissapointed at left with moveinleft
    E "Yeah."
    show Emma sigh with dissolve
    E "This thing is unpredictable."
    hide Emma dissapointed with moveoutleft
    show Lila Sweats at left with moveinleft
    L "I see..."
    hide Lila Sweats with moveoutleft
    $Distract_EmmaAndLiamDoNotCare = False
    $DaggerInfo = False
    $Distract_EmmaAndLiamCare = False
    $AskLiamForInfo = False
    $thing = False
    $LookAtVine = False
    window hide
    if GotRock == False:
        jump drag_glass
    if GotRock == True:
        jump drag_glass2
return

label CutVine:
    window hide
    show VineWall with fade
    pause 1
    window show
    show Emma sly at left with moveinleft
    E "Ok."
    show Emma smile with dissolve
    E "Here's the plan."
    hide Emma Smile at left with moveoutleft
    window hide
    show Vina neutral with fade
    play sound VineEyes
    pause 1
    window show
    show Emma smile at left with moveinleft
    E "Me and Liam will distract the main body of the Vina Plant."
    hide Emma smile with moveoutleft
    window hide
    hide Vina neutral with fade
    window show
    show Emma smile at left with moveinleft
    E "You will go cut the entangled vines around it."
    hide Emma smile with moveoutleft
    window show
    show Emma sly at left with moveinleft
    E "Grab the page and cut your way out."
    hide Emma sly with moveoutleft
    show Lila sad at left with moveinleft
    L "What will happen if Liam gets caught?"
    show Lila eyes closed sad with dissolve
    L "He doesn't have a sharp object on him like I do."
    hide Lila eyes closed sad with moveoutleft
    show Emma smile at left with moveinleft
    E "I'm quick enough to save him."
    show Emma concern with dissolve
    E "You focus on the wall of vines."
    hide Emma concern with moveoutleft
    show Lila nervous at left with moveinleft
    L "Ok!"
    hide Lila nervous with moveoutleft
    show Emma sly at left with moveinleft
    E "Get in action on the count of 3!"
    show Emma yell with dissolve
    hide VineWall with fade
    show image "black.png" with fade
    E "1!"
    E "2!"
    E "3!" with vpunch
    play sound EmmaSlash
    hide Emma yell with moveoutleft
    window hide
    play sound PaperFall
    show LilaCatchPage with fade
    pause 1
    window show
    stop sound
    hide LilaCatchPage with fade
    show Lila happy at left with moveinleft
    L "!" with hpunch
    show Lila laugh with dissolve
    L "Got the page!"
    show screen inventory_button
    $renpy.notify("Page Found.")
    $inventory.add(Page1)
    hide Lila laugh with moveoutleft
    show Emma happy at left with moveinleft
    E "Great!"
    hide screen inventory_button
    show Emma laugh with dissolve
    E "Let's get out of here!"
    hide  Emma laugh with moveoutleft
    window hide
    jump MysteriesAwait
return

label CutVine2:
    window hide
    show VineWall
    pause 1
    window show
    show Emma concern at left with moveinleft
    E "Ok."
    show Emma sigh at left with dissolve
    E "Here's the plan."
    hide Emma sigh with moveoutleft
    window hide
    play sound VineEyes
    show Vina neutral with fade
    pause 1
    window show
    show Emma sigh at left with moveinleft
    E "Me and Liam will distract the main body of the Vina Plant."
    hide Emma sigh with moveoutleft
    window hide
    stop sound
    hide Vina neutral with fade
    pause 1
    window show
    show Emma concern at left with moveinleft
    E "You will go cut the entangled vines around it."
    show Emma angry with dissolve
    E "Grab the page and cut your way out."
    hide Emma angry with moveoutleft
    show Lila sad at left with moveinleft
    L "What will happen if Liam gets caught?"
    show Lila eyes closed sad with dissolve
    L "He don't have an sharp object on him like me."
    hide Lila eyes closed sad with moveoutleft
    show Emma envy at left with moveinleft
    E "I'm quick enough to save him."
    show Emma angry with dissolve
    E "You focus on the wall of vines."
    hide Emma angry with moveoutleft
    show Lila nervous at left with moveinleft
    L "Ok!"
    hide Lila nervous with moveoutleft
    show Emma sigh at left with moveinleft
    E "Get in action on the count of 3!"
    show Emma yell with dissolve
    hide VineWall with fade
    show image "black.png" with fade
    E "1!"
    E "2!"
    E "3!" with vpunch
    play sound EmmaSlash
    hide Emma yell with moveoutleft
    show Lila panic at left with moveinleft
    play music CaveBattleMusic fadein 5.0 volume 0.3
    stop sound
    play sound DeeperThump
    L "!" with vpunch
    stop sound
    hide Lila panic with moveoutleft
    show Emma shocked at left with moveinleft
    E "Crap!"
    show Emma yell with dissolve
    E "Lila it smells the blood on your finger!"
    show Emma nervous with dissolve
    E "Let's pull back-"
    $renpy.notify("The vines entangled you.")
    show Emma panic with dissolve
    E "Lil-!"
    show screen inventory_button
    $renpy.notify("You dropped the sharp rock.")
    show Emma concern with dissolve
    show Emma yell with dissolve
    $renpy.notify("The Vina Plant look at you with hungry eyes.")
    $inventory.drop(Sharprock)
    E "Don't move I'm coming!"
    hide screen inventory_button
    $renpy.notify("Vines entangled Liam.")
    hide Emma yell with moveoutleft
    show Liam shocked at right with moveinright
    play sound DeeperThump
    L2 "!" with vpunch
    stop sound
    hide Liam shocked with moveoutright
    $renpy.notify("Emma is in a state of panic.")
    show Emma panic at left with moveinleft
    hide Emma panic with moveoutleft
    show Lila panic at left with moveinleft
    L "What should I do?"
    hide Lila panic with moveoutleft
    window hide
    if emma_points >= 3:
        if liam_points >= 2:
            $SaveMe_AllCare = True
            $SaveMe_DoNotCare = False
            $SaveLiam_AllCare = True
            $SaveLiam_DoNotCare = False
            $SaveYourSelf_AllCare = True
            $SaveYourSelf_DoNotCare = False
    elif emma_points >= 2:
        if liam_points >= 1:
            $SaveMe_AllCare = False
            $SaveMe_DoNotCare = True
            $SaveLiam_AllCare = True
            $SaveLiam_DoNotCare = False
            $SaveYourSelf_AllCare = True
            $SaveYourSelf_DoNotCare = False
    elif emma_points >= 1:
        if liam_points >= 0:
            $SaveMe_AllCare = False
            $SaveMe_DoNotCare = True
            $SaveLiam_AllCare = False
            $SaveLiam_DoNotCare = True
            $SaveYourSelf_AllCare = False
            $SaveYourSelf_DoNotCare = True
    menu:
        "Save me!" if SaveMe_AllCare == True:
            jump SaveMe1
        "Save me!" if SaveMe_DoNotCare == True:
            jump SaveMe2
        "Save Liam!" if SaveLiam_AllCare == True:
            jump SaveLiam
        "Save Liam!" if SaveLiam_DoNotCare == True:
            jump SaveLiam2
        "Save Yourself!" if SaveYourSelf_AllCare == True:
            jump SaveYourself
        "Save Yourself!" if SaveYourSelf_DoNotCare == True:
            jump SaveYourself2
return
