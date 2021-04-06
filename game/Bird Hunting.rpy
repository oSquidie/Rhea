label DidNotKill:
    window show
    hide image "CaveEntrance.png"
    hide image "Twopaths.png"
    show image "Forest_Default.png" with dissolve
    show Lila default at MoveUp
    show Liam default at LiamRight
    show Liam default at LiamMoveUp
    show Emma default at emmaMoveUp
    show Emma default at emmaMiddle
    show Lila panic at PopUp with dissolve
    L "No!"
    show Lila panic at MoveUp with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    show Emma concern at PopUp with dissolve
    E "Why not?"
    show Emma concern at emmaMoveUp with dissolve
    show Lila yell at PopUp with dissolve
    L "You'll kill it!"
    show Lila Sweats at MoveUp with dissolve
    show Liam nervous with dissolve
    show Emma envy at PopUp with dissolve
    E "That's what hunting is about."
    show Emma envy at emmaMoveUp with dissolve
    show Lila sad at PopUp with dissolve
    L "Please no..."
    show Lila sad at MoveUp with dissolve
    show Emma nervous with dissolve
    show Emma dissapointed with dissolve
    show Liam sigh with dissolve
    show Liam smile with dissolve
    show Emma sigh at PopUp with dissolve
    E "Ugh."
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    show Emma pout with dissolve
    E "Fine..."
    hide screen negative_affection
    $C_Sound1 = False
    hide Emma pout with fade
    hide Liam smile with fade
    hide Lila sad with fade
    window hide
jump menu_OC1

label KillIt:
    window show
    hide image "CaveEntrance.png"
    hide image "Twopaths.png"
    show image "Forest_Default.png" with dissolve
    show Lila default at MoveUp
    show Liam default at LiamMoveUp
    show Liam default at LiamRight
    show Emma default at emmaMiddle
    show Emma default at emmaMoveUp
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    show Lila Sweats with dissolve
    show Liam surprised at LiamPopUp with dissolve
    L2 "Did you find it?"
    show Liam surprised at LiamMoveUp with dissolve
    show Emma pout at PopUp with dissolve
    hide screen positive_affection
    E "Hmmmmm...."
    E "Almost."
    show Emma pout at emmaMoveUp with dissolve
    show Liam smirk at LiamPopUp with dissolve
    L2 "Try looking over here."
    show Liam smirk at LiamMoveUp with dissolve
    show Emma excited at PopUp with dissolve
    E "Found it!"
    hide Emma excited
    hide Liam smirk
    hide Lila Sweats
    window hide
    show Emmavsbird with dissolve
    pause
    window show
    E "Thanks Liam!"
    L "..."
    E "Aiming."
    E "Got it!"
    hide Emmavsbird with dissolve
    show image "Forest_Default.png" with dissolve
    show Lila Sweats at MoveUp
    show Liam default at LiamMoveUp
    show Liam default at LiamRight
    show Emma default at emmaMiddle
    show Emma default at emmaMoveUp
    show Lila sad at PopUp with dissolve
    L "This makes me a bit upset."
    show Lila sad at MoveUp with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    show Emma sigh at PopUp with dissolve
    E "Well we have to eat somehow."
    show Emma sigh at emmaMoveUp with dissolve
    show Liam sigh with dissolve
    show Liam nervous with dissolve
    show Lila pout at PopUp with dissolve
    L "..."
    show Lila pout at MoveUp with dissolve
    show Emma nervous with dissolve
    show Emma embarrassed with dissolve
    show Emma pout at PopUp with dissolve
    E "Come on!"
    show Emma embarrassed with dissolve
    E "Don't be like that."
    show Emma happy with dissolve
    E "Here."
    show Lila skeptical with dissolve
    show Liam surprised with dissolve
    show Emma default with dissolve
    E "I'll give this to you."
    show Emma default at emmaMoveUp with dissolve
    show Lila swirly eyes at PopUp with dissolve
    L "Huh?"
    show screen inventory_button
    $renpy.notify("Dumbstick added to inventory.")
    $inventory.add(drumstick)
    $GotDrumStick = True
    show Lila dumbfounded with dissolve
    L "Ew!"
    hide screen inventory_button
    show Liam laugh with dissolve
    show Lila yell with dissolve
    L "Why would I want this?"
    show Lila yell at MoveUp with dissolve
    show Emma sly at PopUp with dissolve
    E "Don't be a baby."
    show Emma sly at MoveUp with dissolve
    show Lila pout with dissolve
    show Liam nervous with dissolve
    show Liam smile at LiamPopUp with dissolve
    L2 "Come on now."
    L2 "Let's keep going."
    $C_Sound1 = False
    hide Lila pount with fade
    hide Emma sly with fade
    hide Liam smile with fade
    window hide
jump menu_OC1
