label NearbyVillage:
    show Cave
    window show
    show Lila angry cry at MoveUp
    show Emma dissapointed at emmaMoveUp
    show Emma dissapointed at emmaflip
    show Emma dissapointed at emmaRight
    show Emma sigh at PopUp with dissolve
    stop music fadeout 1.0
    play music BadEnd fadein 5.0 volume 0.3
    E "You stay here."
    show Emma envy with dissolve
    E "You might just cause more trouble if you tagged along."
    show Emma sigh at emmaMoveUp with dissolve
    show Lila panic at PopUp with dissolve
    L "But I'm worried."
    show Lila panic at MoveUp with dissolve
    show Emma angry at PopUp with dissolve
    E "Too late to be saying that now."
    show Emma sigh with dissolve
    show Lila shocked with dissolve
    show Lila sad with dissolve
    E "I can't trust you to watch him."
    show Emma dissapointed with dissolve
    E "And can't trust you to find a village either..."
    show Lila Sweats with dissolve
    show Emma envy with dissolve
    E "What good are you for?"
    show Emma envy at emmaMoveUp with dissolve
    show Lila eyes closed sad at PopUp with dissolve
    L "I'm sorry..."
    show Emma sigh at PopUp with dissolve
    E "Forget it."
    show Emma dissapointed with dissolve
    E "I'll carry him on my shoulder and look for a nearby villiage."
    show Emma concern with dissolve
    E "While I'm gone..."
    show Emma envy with dissolve
    E "Don't you dare touch anything."
    E "Or go anywhere."
    show Emma envy at emmaMoveUp with dissolve
    show Lila sad at PopUp with dissolve
    L "Ok..."
    show Lila sad at MoveUp with dissolve
    show Emma sigh at PopUp with dissolve
    E "Wait for us to come back."
    show Emma intimidating with dissolve
    E "When I'm back and I find out you're gone..."
    E "I won't think twice and ditch you."
    hide Emma intimidating with fade
    play sound Walk
    $renpy.notify("Emma left to find a village.")
    show Lila sad at middle with dissolve
    L "You always leave me behind..."
    show Lila eyes closed sad with dissolve
    L "Why?"
    L "Being alone in this cave feels so lonely and dark."
    show Lila tears with dissolve
    L "Very dark."
    hide Lila tears with fade
    window hide
    hide Cave with fade
    show image "black.png"
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting."
    "No Pages Obtained."
    show Cave with fade
    window show
    show Mingluo no eyes at right with moveinright
    play sound Walk
    Q "If you have chosen your actions more wisely this wouldn't have happened."
    hide Mingluo no eyes with moveoutright
    show Lila shocked at left with moveinleft
    L "Who's there!"
    show Lila surprised with dissolve
    L "!"
    show Lila panic with dissolve
    L "You're..."
    hide Lila surprised with moveoutleft
    window hide
    hide Cave with fade
    show image "black.png"
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label EmmaGoGetHelp:
    show Cave
    window show
    show Lila angry cry at MoveUp
    show Emma dissapointed at emmaMoveUp
    show Emma dissapointed at emmaflip
    show Emma dissapointed at emmaRight
    show Emma concern at PopUp with dissolve
    stop music fadeout 1.0
    play music GoodEnd fadein 5.0 volume 0.3
    E "I can trust you to keep him safe?"
    show Lila shocked with dissolve
    show Emma dissapointed with dissolve
    E "He's defenseless right now."
    show Emma dissapointed at emmaMoveUp with dissolve
    show Lila yell at PopUp with dissolve
    L "I promise I won't leave his side."
    show Lila yell at MoveUp with dissolve
    show Emma sigh at PopUp with dissolve
    E "Fine."
    show Lila relieved with dissolve
    show Emma soft with dissolve
    E "I'll trust you one last time."
    show Lila smile with dissolve
    show Emma intimidating with dissolve
    E "Don't make me regret this choice."
    show Emma intimidating at emmaMoveUp with dissolve
    show Lila Sweats at PopUp with dissolve
    show Lila Sweats at MoveUp with dissolve
    show Emma surprised at PopUp with dissolve
    E "Also."
    show Emma concern with dissolve
    E "Take this."
    show screen inventory_button
    $renpy.notify("You now have Emma's dagger.")
    $inventory.add(Dagger)
    show Emma angry with dissolve
    E "Don't hesitate to kill."
    show Lila panic with dissolve
    hide screen inventory_button
    show Emma sigh with dissolve
    E "The things in this world aren't forgiving."
    show Emma sigh at emmaMoveUp with dissolve
    show Lila Sweats at PopUp with dissolve
    L "?"
    show Lila Sweats at MoveUp with dissolve
    show Emma dissapointed at PopUp with dissolve
    E "Forget it."
    show Emma sigh with dissolve
    E "Just don't go anywhere."
    show Emma soft with dissolve
    E "Wait for me to come back."
    play sound Walk
    show Emma soft at emmaMoveUp with dissolve
    show Lila sad at PopUp with dissolve
    L "Ok..."
    hide Emma soft with fade
    hide Lila sad with dissolve
    window hide
    hide Cave with fade
    show image "black.png"
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting Together."
    "No Pages Obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label EmmaGoGetHelp2:
    show Cave with fade
    window show
    show Lila angry cry at MoveUp
    show Emma envy at emmaMoveUp
    show Emma envy at emmaflip
    show Emma envy at emmaRight
    show Emma envy at PopUp with dissolve
    stop music fadeout 1.0
    play music BadEnd fadein 5.0 volume 0.3
    E "As if I can trust you again."
    show Emma concern with dissolve
    show Lila shocked with dissolve
    show Lila sad with dissolve
    E "I can't trust you to watch him."
    show Emma angry with dissolve
    E "And can't trust you to find a village either..."
    show Lila Sweats with dissolve
    show Emma envy with dissolve
    E "What good are you for?"
    show Emma envy at emmaMoveUp with dissolve
    show Lila eyes closed sad at PopUp with dissolve
    L "I'm sorry..."
    show Emma angry at PopUp with dissolve
    E "Forget it."
    show Emma envy with dissolve
    E "I'll carry him on my shoulder and look for a nearby villiage."
    show Emma concern with dissolve
    E "While I'm gone..."
    show Emma envy with dissolve
    E "Don't you dare touch anything."
    E "Or go anywhere."
    show Emma envy at emmaMoveUp with dissolve
    show Lila sad at PopUp with dissolve
    L "Ok..."
    show Lila sad at MoveUp with dissolve
    show Emma sigh at PopUp with dissolve
    E "Wait for us to come back."
    show Emma angry with dissolve
    E "When I'm back and I find out you're gone..."
    E "I won't think twice and ditch you."
    hide Emma angry with fade
    play sound Walk
    $renpy.notify("Emma left to find a village.")
    show Lila sad at middle with dissolve
    L "You always leave me behind..."
    show Lila eyes closed sad with dissolve
    L "Why?"
    L "Being alone in this cave feels so lonely and dark."
    show Lila tears with dissolve
    L "Very dark."
    hide Lila tears with fade
    hide Cave with fade
    show image "black.png"
    window show
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting."
    "No Pages Obtained."
    window show
    show Mingluo no eyes at right with moveinright
    Q "If you have chosen your actions more wisely this wouldn't have happened."
    hide Mingluo no eyes with moveoutright
    show Lila shocked at left with moveinleft
    L "Who's there!"
    show Lila surprised with dissolve
    L "!"
    show Lila panic with dissolve
    L "You're..."
    hide Lila surprised with moveoutleft
    window hide
    hide Cave with fade
    show image "black.png"
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label BadEnd1:
    show Cave with fade
    window show
    show Lila panic at MoveUp
    show Emma shocked at emmaMoveUp
    show Emma shocked at emmaflip
    show Emma shocked at emmaRight
    show Emma angry at PopUp with dissolve
    stop music fadeout 1.0
    play music BadEnd fadein 5.0 volume 0.3
    E "Are you serious?"
    show Emma envy with dissolve
    E "Feel your chest."
    show Emma concern with dissolve
    E "Is there still a heart inside of there?"
    show Emma dissapointed at emmaMoveUp with dissolve
    show Lila Sweats at PopUp with dissolve
    L "Wait-I.."
    show Lila panic with dissolve
    show Lila pain with dissolve
    show Lila Sweats with dissolve
    L "I said that without thinking-"
    show Lila panic at MoveUp with dissolve
    show Emma angry at PopUp with dissolve
    E "Enough." with vpunch
    show Emma sigh with dissolve
    E "I don't know when I started to dislike you."
    show Emma dissapointed with dissolve
    E "But I was right."
    show Emma concern with dissolve
    E "I told him so many times you aren't worth our time."
    show Emma angry with dissolve
    E "I'm taking Liam."
    E "As for you..."
    show Emma cry with dissolve
    show Emma dissapointed with dissolve
    E "Your safety no long concerns me."
    play sound Walk
    show Emma dissapointed at emmaMoveUp with dissolve
    hide Emma dissapointed with fade
    show Lila panic at middle with dissolve
    L "Emma!"
    show Lila yell with dissolve
    L "Don't Leave!"
    show Lila angry cry with dissolve
    L "Listen to me!"
    L "Emma!"
    show Lila shocked with dissolve
    hide Lila shocked with fade
    hide Cave with fade
    window hide
    show image "black.png"
    show static
    show text '{color=#00ffcd}{size=100}"She left..."{/size}{/color}' at text_effect
    $ renpy.pause()
    hide text '{color=#00ffcd}{size=100}"She left..."{/size}{/color}' at text_effect
    show static
    show FadeGlitchBlack with fade
    show static
    show text '{color=#00ffcd}{size=100}"She left me...all by myself."{/size}{/color}' at text_effect
    show static
    $ renpy.pause()
    hide text '{color=#00ffcd}{size=100}"She left me...all by myself."{/size}{/color}' at text_effect
    show static
    hide FadeGlitchBlack with fade
    show static
    show text '{color=#00ffcd}{size=100}"How could she..."{/size}{/color}' at text_effect
    $ renpy.pause()
    hide text '{color=#00ffcd}{size=100}"How could she..."{/size}{/color}' at text_effect
    hide static
    window show
    show Lila panic at middle with moveinleft
    L "..."
    show Lila eyes closed sad with dissolve
    L "I-"
    hide Lila eyes closed sad fade
    show White with fade
    RV "How absurd..."
    hide White with fade
    window hide
    show Riot with fade
    pause 1
    window show
    RV2 "More like pitful."
    RV "To think a lunatic like her was living with us."
    L "I'm not crazy!"
    L "The sun really does exist!"
    RV "What rubbish!"
    RV "Just take her to the mental ward."
    L "NO!" with vpunch
    L "Don't touch me!"
    L "I'm not crazy!"
    L "Stop-"
    hide image "black.png" with fade
    window hide
    show TearsEmmaLiamProtect with fade
    pause 1
    window show
    E "Do you adults have no shame?!"
    E "She still just a kid!"
    RV3 "It because she's a kid she needs treatment right now!"
    window hide
    show EmmaLiamProtect with fade
    pause 1
    window show
    E "Ridiculous!"
    E "Go on Liam."
    E "Let's take her out of here."
    RV "How insolent!"
    RV3 "We try to help and they act like such rebels."
    RV2 "Go on!"
    RV2 "Leave!"
    RV2 "Once you do."
    RV2 "Don't you dare come back!"
    L2 "Trust me."
    L2 "I won't."
    show static2 with fade
    show bblack
    L "They are all I need..."
    L "They were all I had."
    L "What have I done?"
    show image "black.png"
    "Mission failed."
    "Hurt status: Liam is hurt."
    "Ending Achieved: Bad end 1(Overloaded)."
    "No Pages Obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label MysteriesAwait:
    play sound Run
    scene image "CaveEntrance.png" with dissolve
    window show
    show Lila happy at MoveUp
    show Lila happy at middle
    show Liam happy at LiamRight
    show Liam happy at LiamMoveUp
    show Emma nervous at emmaLeft
    show Emma nervous at emmaMoveUp
    show Lila happy at PopUp with dissolve
    play music RheaSoundtrack fadein 5.0 volume 0.3
    L "We did it!"
    show Lila happy at MoveUp with dissolve
    show Emma nervous at PopUp with dissolve
    E "N-Nice..."
    show Emma nervous at emmaMoveUp with dissolve
    show Lila swirly eyes at PopUp with dissolve
    L "Emma are you ok?"
    show Liam surprised with dissolve
    show Lila swirly eyes at MoveUp with dissolve
    show Emma smile at PopUp with dissolve
    E "Y-yeah."
    show Emma nervous with dissolve
    show Liam content with dissolve
    show Liam smile with dissolve
    E "Just need a second...to breathe."
    show Emma nervous at emmaMoveUp with dissolve
    show Lila surprised at PopUp with dissolve
    L "Oh ok..."
    show Lila skeptical with dissolve
    L "Hmmm..."
    L "What does this say??"
    show Lila skeptical at MoveUp with dissolve
    show Emma surprised with dissolve
    show Liam surprised at LiamPopUp with dissolve
    L2 "Let me take a look."
    show Liam skeptical with dissolve
    L2 "Hmmmm..."
    show Liam nervous with dissolve
    L2 "It's a bit complicated to decode."
    show Lila swirly eyes with dissolve
    show Emma sigh with dissolve
    show Emma dissapointed with dissolve
    show Liam default with dissolve
    stop music fadeout 1.0
    play music GoodEnd fadein 5.0 volume 0.3
    L2 "Let's find a nearby library where I can focus and do some research."
    show Liam default at LiamMoveUp with dissolve
    show Lila happy at PopUp with dissolve
    L "Ok!"
    show Lila happy at MoveUp with dissolve
    show Emma concern at PopUp with dissolve
    E "Guess we looking for a town next."
    show Emma default with dissolve
    E "Let's go."
    show Emma sigh with dissolve
    E "I'm exhausted."
    show Emma sigh at emmaMoveUp with dissolve
    show Lila smile at PopUp with dissolve
    show Liam smile with dissolve
    L "Ok!"
    show Lila skeptical with dissolve
    show Lila happy with dissolve
    L "I wonder what adventures awaits us next!"
    hide Emma sigh with fade
    hide Lila happy with fade
    hide Liam smile with fade
    #hide image "CaveEntrance.png"
    window hide
    show HandinHand with fade
    pause 1
    window show
    "Mission Success."
    "Hurt status: No one is hurt."
    "Ending Achieved: Mysteries Await."
    "First Page obtained."
    hide HandinHand
    show image "black.png"
    show DefaultForest with fade
    show Mingluo soft at MingLuoUp
    show Mingluo soft at MingLuoMiddle
    Q "Lila."
    Q "I see that you've grown."
    show Mingluo smirk with dissolve
    show Mingluo smile with dissolve
    Q "Keep growing."
    Q "Soften that heart and eventually..."
    show Mingluo evil with dissolve
    show Mingluo happy with dissolve
    Q "You'll be of use to me."
    hide Mingluo happy with dissolve
    window hide
    hide DefaultForest with fade
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label SaveMe1:
    play sound VineEyes
    show Vina death with fade
    window show
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    show Liam panic at right with moveinright
    L2 "Go save her first!"
    hide screen negative_affection
    hide Liam panic with moveoutright
    show Emma panic at left with moveinleft
    E "But!"
    hide Emma panic with moveoutleft
    show Liam panic at right with moveinright
    L2 "I'll be fine!"
    hide Liam with moveoutright
    show Emma yell at left with moveinleft
    E "AHHHHHHHHHHH!" with hpunch
    $renpy.notify("Emma cuts the vines on you.")
    play sound EmmaSlash
    show Emma envy with dissolve
    E "This is why you shouldn't have touched the crytsal!"
    $renpy.notify("Emma picks up your sharp rock.")
    show Emma yell with dissolve
    E "Take this you dumb Vina Plant!"
    play sound Whoosh
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    show Emma envy with dissolve
    hide Vina death
    play sound Squash
    show VineHurt
    E "Let's get out of here now!"
    stop music fadeout 1.0
    $renpy.notify("Stunned by the pain the Vina plant freed Liam.")
    play sound Run
    hide VineHurt with fade
    show image "CaveEntrance.png" with dissolve
    show Emma nervous with dissolve
    play music GoodEnd fadein 5.0 volume 0.3
    E "...."
    show Emma envy with dissolve
    E "Stop weiling you idiot."
    hide Emma envy with moveoutleft
    show Lila angry cry at left with moveinleft
    show Lila pout with dissolve
    L "But what about the page?"
    hide Lila pout with moveoutleft
    show Emma angry at left with moveinleft
    E "Why are you worried about that in this state?"
    show Emma sigh with dissolve
    E "Not even medication can fix that brain of yours."
    hide Emma sigh with moveoutleft
    show Lila Sweats at left with moveinleft
    L "..."
    hide Lila Sweats with moveoutleft
    show Liam sigh at right with moveinright
    L2 "Let's find a place to rest up before we figure out the next step..."
    hide Liam sigh with moveoutright
    show Lila sad at left with moveinleft
    L "Ok..."
    hide Lila sad with moveoutleft
    hide image "CaveEntrance.png" with dissolve
    window hide
    show WalkingHomeNorm
    pause 1
    window show
    stop music fadeout 1.0
    "Mission failed."
    "Hurt status: No one is hurt."
    "Ending Achieved: Mysteries Await."
    "No Page obtained."
    show image "black.png"
    show DefaultForest with fade
    show Mingluo annoyed at MingLuoUp
    show Mingluo annoyed at MingLuoMiddle
    play music BadEnd
    Q "Tch."
    Q "Still as dumb as she always have been."
    show Mingluo smirk with dissolve
    Q "At least she got that page for me."
    show Mingluo sigh with dissolve
    Q "Grow up faster please child."
    show Mingluo evil with dissolve
    show Mingluo happy with dissolve
    Q "Then eventually you'll be of use to me."
    hide Mingluo happy with dissolve
    window hide
    hide WalkingHomeNorm
    hide DefaultForest with fade
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label SaveMe2:
    play sound VineEyes
    show Vina death with fade
    window show
    show Emma yell at left with moveinleft
    E "AHHHHHHHHHHH!" with hpunch
    stop music fadeout 1.0
    play music BadEnd fadein 5.0 volume 0.3
    $renpy.notify("Emma choose to save Liam.")
    play sound EmmaSlash
    hide Vina death with fade
    show image "black.png"
    show Emma panic with dissolve
    E "I-"
    stop sound
    show Emma dissapointed with dissolve
    $renpy.notify("All you can see is the look of guilt.")
    E "I'm sorry..."
    hide Emma dissapointed with moveoutleft
    "Mission failed."
    "Hurt status: unknown."
    "Ending Achieved: Results Of Being Selfish."
    "No Page obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label SaveLiam:
    play sound VineEyes
    show Vina death with fade
    window show
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $liam_points += 1
    show Liam panic at right with moveinright
    L2 "No!"
    hide screen positive_affection
    L2 "Save her first!"
    hide Liam panic with moveoutright
    show Emma panic at left with moveinleft
    E "But you-"
    show Liam panic at right with moveinright
    L2 "I'll be fine!"
    hide Liam panic with moveoutright
    show Emma yell at left with moveinleft
    E "AAAAHHHHH!" with hpunch
    $renpy.notify("Emma cuts the vines on you.")
    play sound EmmaSlash
    show Emma envy with dissolve
    E "This is why you shouldn't have touched the crytsal!"
    $renpy.notify("Emma picks up your sharp rock.")
    show Emma yell with dissolve
    E "Take this you dumb Vina Plant!"
    play sound Whoosh
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    hide Vina death with fade
    play sound Squash
    show VineHurt with fade
    show Emma envy with dissolve
    E "Let's get out of here now!"
    play sound Run
    stop music fadeout 1.0
    $renpy.notify("Stunned by the pain the Vina plant drops Liam.")
    hide Emma envy with moveoutleft
    hide Vinehurt with fade
    show Cave with fade
    show Emma panic at left with moveinleft
    play music RheaSoundtrack fadein 5.0 volume 0.3
    E "...."
    hide Emma panic with moveoutleft
    show Lila tears at left with moveinleft
    show Lila angry cry with dissolve
    L "...."
    hide Lila angry cry with moveoutleft
    show Liam nervous at right with moveinright
    L2 "It's ok..."
    show Liam smile with dissolve
    L2 "It's over now."
    show Liam nervous with dissolve
    L2 "Sorry we couldn't get the page."
    hide Liam nervous with moveoutright
    show Lila angry cry at left with moveinleft
    L "I don't care about that right now..."
    hide Lila angry cry with moveoutleft
    show Mingluo no eyes at right with moveinright
    stop music
    Q "You should care."
    play music BadEnd fadein 5.0 volume 0.3
    hide Mingluo no eyes with moveoutright
    hide Cave with fade
    window hide
    play sound Fire
    show VineBurn with fade
    pause 1
    window show
    $renpy.notify("The wall of vines started to burn.")
    show Emma shocked at left with moveinleft
    E "What-?!"
    hide Emma shocked with moveoutleft
    show Mingluo happy at right with moveinright
    M "Nice to see you guys doing well."
    stop sound
    hide VineBurn with fade
    window hide
    show MingluoBurnPage with fade
    pause 1
    window show
    play sound PaperFall
    $renpy.notify("Mingluo picks up the page.")
    E "..."
    L2 "..."
    hide MingluoBurnPage with fade
    show Cave with fade
    show Lila happy at left with moveinleft
    L "Mingluo!" with vpunch
    play sound hug
    $renpy.notify("You gave Mingluo a hug.")
    show Mingluo disgust at right with moveinright
    show Mingluo happy with dissolve
    M "..." with vpunch
    hide Lila happy with moveoutleft
    show Mingluo smirk with dissolve
    M "Looks like you're friends don't like seeing me."
    show Mingluo sigh with dissolve
    M "Makes me a bit sad."
    hide Mingluo sigh with moveoutright
    show Lila skeptical at left with dissolve
    L "What are you doing here?"
    hide Lila skeptical with moveoutleft
    show Mingluo smile at right with moveinright
    M "To help you of course!"
    hide Mingluo smile with moveoutright
    show Emma intimidating at left with moveinleft
    E "You could have came earlier..."
    hide Emma intimidating with moveoutleft
    show Mingluo skeptical at right with moveinright
    M "But there's no fun in that."
    M "What was the phase?"
    show Mingluo happy with dissolve
    M "The main character never comes on time."
    hide Mingluo happy with moveoutright
    show Emma envy at left with moveinleft
    E "What a load of bull-"
    hide Emma envy with moveoutleft
    show Mingluo smile at right with moveinright
    M "Anyways!"
    show Mingluo page with dissolve
    M "Here you go."
    hide Mingluo page with moveoutright
    play sound PaperFall
    show screen inventory_button
    $renpy.notify("Page Found.")
    $inventory.add(Page1)
    show Lila smile at left with moveinleft
    stop music fadeout 1.0
    play music GoodEnd fadein 5.0 volume 0.3
    L "Thanks Mingluo!"
    show Lila skeptical with dissolve
    L "Hm?"
    hide screen inventory_button
    L "I Don't know what it says."
    show Lila swirly eyes with dissolve
    L "Can you help me Mingluo-"
    show Lila skeptical with dissolve
    L "Huh?"
    show Lila swirly eyes with dissolve
    L "Where did she go?"
    hide Lila swirly eyes with moveoutleft
    show Emma sigh at left with moveinleft
    E "She left after you took the page."
    hide Emma sigh with moveoutleft
    show Liam nervous at right with moveinright
    L2 "Ignore her for now."
    L2 "Let's find a place to rest first."
    L2 "It's been a tough start to our adventure."
    L2 "I'll help you figure out what's written after."
    hide Liam nervous with moveoutright
    show Emma concern at left with moveinleft
    E "I agree with Liam."
    show Emma sigh with dissolve
    E "I feel beat."
    hide Emma sigh with moveoutleft
    show Lila surprised at left with moveoutleft
    L "Oh ok!"
    show Lila swirly eyes with dissolve
    L "I wonder why Mingluo wants this page that bad..."
    hide Lila swirly eyes with moveoutleft
    show Emma intimidating at left with moveinleft
    E "Who knows."
    hide Emma intimidating with moveoutleft
    hide Cave with fade
    window hide
    show WalkingHomeNorm
    pause 1
    window show
    "Mission Success."
    "Hurt status: No one is hurt."
    "Ending Achieved: A 'friend' helps when your in need."
    "First Page obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label SaveLiam2:
    show image "black.png" with fade
    window show
    stop music fadeout 1.0
    play music BadEnd fadein 5.0 volume 0.3
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $liam_points += 1
    show Emma panic at left with moveinleft
    E "AHHHHHHHHHHH!" with hpunch
    hide screen positive_affection
    show Emma dissapointed with dissolve
    E "I-"
    show Emma cry with dissolve
    E "I'm sorry Lila."
    $renpy.notify("Emma choose to free Liam.")
    play sound EmmaSlash
    hide Emma cry with moveoutleft
    show Liam shocked at right with moveinright
    L2 "NO Emma!" with vpunch
    show Liam yell cry with dissolve
    L2 "Lila!"
    $renpy.notify("Liam pushed Emma but Emma hold Liam back.")
    stop music fadeout 1.0
    show Liam shocked with dissolve
    Q "How coldhearted..."
    hide image "black.png" with fade
    window hide
    play sound Fire
    show VineBurn with fade
    pause 1
    window show
    hide Liam shocked with moveoutright
    show Mingluo soft at right with moveinright
    Q "You pitful child."
    stop sound
    hide VineBurn with fade
    hide Mingluo soft with moveoutright
    play music BadEnd
    window hide
    show image "MingluoCatchLila.png" with dissolve
    pause 1
    window show
    L "Ming...lou..."
    $renpy.notify("You listened to her words...")
    M "Shhhhhh"
    M "I'm here now."
    M "So don't worry."
    M "Sleep."
    M "When you wake up again"
    M "Everything will be fine again."
    show image "black.png"
    $renpy.notify("You fell into a deep sleep.")
    "Mission Failed."
    "Hurt status: unknown."
    "Ending Achieved: Mysteries Await."
    "No Page obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label SaveYourself:
    play sound VineEyes
    show Vina death with fade
    window show
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $renpy.notify("Emma choose to save you first.")
    show Emma envy at left with moveinleft
    play sound EmmaSlash
    E "You must be really stupid if you I'll only save myself."
    hide screen positive_affection
    $renpy.notify("Emma picks up your sharp rock.")
    show Emma yell cry with dissolve
    play sound Whoosh
    E "Take this you dumb Vina Plant!"
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    show Emma envy with dissolve
    hide Vina death with fade
    play sound Squash
    show VineHurt with fade
    E "Let's get out of here now!"
    $renpy.notify("Stunned by the pain the Vina plant drops Liam.")
    play sound Run
    stop music fadeout 1.0
    hide Emma envy with moveoutleft
    hide VineHurt with fade
    show image "CaveEntrance.png" with dissolve
    show Emma nervous at left with moveinleft
    E "...."
    play music RheaSoundtrack fadein 5.0 volume 0.3
    E "Stop it you baby."
    show Emma sigh with dissolve
    E "Everything is fine now."
    hide Emma sigh with moveoutleft
    show Lila angry at left with moveinleft
    show Lila relieved with dissolve
    L "...Yeah."
    hide Lila relieved with moveoutleft
    show Emma nervous at left with moveinleft
    E "Look."
    show Emma sigh with dissolve
    E "Stop crying for a bit."
    hide Emma sigh with moveoutleft
    show Lila nervous at left with moveinleft
    L "?"
    hide Lila nervous with moveoutleft
    show Emma embarrassed at left with moveinleft
    E "I'm sorry I could get the page..."
    hide Emma embarrassed with moveoutleft
    show Lila pout at left with moveinleft
    L "I don't care about that!"
    hide Lila pout with moveoutleft
    show Liam laugh at right with moveinright
    L2 "Pft."
    hide Liam laugh with moveoutright
    show Emma embarrassed at left with moveinleft
    E "What's so funny??"
    hide Emma embarrassed with moveoutleft
    show Liam content at right with moveinright
    L "You guys are so cute."
    hide Liam content with moveoutright
    show Emma blush at left with moveinleft
    E "C-"
    show Emma panic with dissolve
    show Emma embarrassed with dissolve
    show Emma nervous with dissolve
    show Emma sigh with dissolve
    E "Forget it."
    show Emma concern with dissolve
    E "What do we do about the page."
    hide Emma concern with moveoutleft
    show Liam smirk at right with moveinright
    L2 "Let's give it another attempt."
    hide Liam smirk with moveoutright
    show Emma shocked at left with moveinleft
    E "What-?"
    hide Emma shocked with moveoutleft
    show Liam wink at right with moveinright
    L2 "But just with you and me this time."
    show Liam smile with dissolve
    L2 "I'll go find another rock to sharpen."
    hide Liam smile at moveoutright
    stop music fadeout 1.0
    window hide
    menu:
        "Don't go. I don't want you to die.":
            jump DoNotDie
        "Please be safe.":
            jump BeSafe
        "Are You sure you don't need me to try again?":
            jump YouSure
return

label DoNotDie:
    stop music fadeout 1.0
    play music GoodEnd fadein 5.0 volume 0.3
    show image "CaveEntrance.png" with dissolve
    window show
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $liam_points += 1
    show Liam smile at right with moveinright
    L2 "No one is going to die."
    hide screen positive_affection
    show Lila panic at left with moveinleft
    L "No!" with vpunch
    hide Lila panic with moveoutleft
    show Emma sigh at left with moveinleft
    E "I agree with her."
    show Emma dissapointed with dissolve
    E "I don't like this idea."
    hide Emma dissapointed with moveoutleft
    show Liam nervous at right with moveinright
    L2 "I guess we should find a place to rest up first before we make another attempt."
    hide Liam nervous with moveoutright
    show Emma sigh at left with moveinleft
    E "Yeah..."
    show Emma soft with dissolve
    E "Come on Lila."
    E "Let's go."
    E "I'll hold your hand so calm down ok?"
    hide Emma soft with moveoutleft
    show Lila relieved at left with moveinleft
    L "Ok."
    play sound Walk
    hide Lila relieved with moveoutleft
    #hide image "CaveEntrance.png"
    window hide
    show HandinHand with fade
    pause 1
    window show
    "Mission Failed."
    "Hurt status: No one was hurt."
    "Ending Achieved: Learn Through Failure."
    "No Page obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label Besafe:
    stop music fadeout 1.0
    play music GoodEnd fadein 5.0 volume 0.3
    show image "CaveEntrance.png" with dissolve
    window show
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $liam_points += 1
    show Emma envy at left with moveinleft
    E "You're kidding."
    hide screen positive_affection
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    show Emma sigh with dissolve
    E "After all of that I am not letting you do that again."
    hide screen negative_affection
    hide Emma sigh with moveoutleft
    show Liam sigh at right with moveinright
    L2 "Come on."
    show Liam nervous with dissolve
    L2 "Don't be like that."
    L2 "I also hate the idea of being protected all the time."
    hide Liam nervous with moveoutright
    $renpy.notify("Liam found and sharpened a rock.")
    show Emma surprised at left with moveinleft
    E "Wha-"
    show Emma envy with dissolve
    E "Where did you find that?!"
    hide Emma envy with moveoutleft
    show Liam smug at right with moveinright
    L2 "I have my ways."
    hide Liam smug with moveoutright
    show Emma sigh at left with moveinleft
    E "Why do you have to be so stuborn?"
    hide Emma sigh with moveoutleft
    show Liam wink at right with moveinright
    L2 "I just refuse to accept failure{cps=2}...{/cps}at the moment."
    hide Liam wink with moveoutright
    show Emma intimidating at left with moveinleft
    E "Lila."
    hide Emma intimidating with moveoutleft
    show Lila skeptical at left with moveinleft
    L "?"
    hide Lila skeptical with moveoutleft
    show Emma sigh at left with moveinleft
    E "Summon your spirit if things go wrong again."
    show Emma nervous with dissolve
    E "As much as I hate her..."
    show Emma sigh with dissolve
    E "She is undeniably strong."
    hide Emma sigh with moveoutleft
    show Lila default at left with moveinleft
    L "Ok."
    hide Lila default with moveoutleft
    $renpy.notify("Emma and Liam successfully got the page.")
    show Liam nervous at right with moveinright
    L2 "See it wasn't that bad..."
    hide Liam nervous with moveoutright
    show Emma envy at left with moveinleft
    E "Yeah...I wonder why."
    hide Emma envy with moveoutleft
    show Lila stunned at left with moveinleft
    L "...?"
    hide Lila stunned with moveoutleft
    show Liam skeptical at right with moveinright
    L2 "Well we got the page but what's written will take time to decode."
    hide Liam skeptical with moveoutright
    show Emma sigh at left with moveinleft
    E "Let's find an place to rest up first then."
    hide Emma sigh with moveoutleft
    show Liam nervous at right with moveinright
    L2 "I guess we did start this adventure off rough."
    show Liam smile with dissolve
    L2 "I wonder what awaits us after this."
    hide Liam smile with moveoutright
    hide image "CaveEntrance.png" with dissolve
    window hide
    show WalkingHomeNorm
    pause 1
    window show
    "Mission Success."
    "Hurt status: No one was hurt."
    "Ending Achieved: Mysteries Await."
    "First Page obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label YouSure:
    stop music fadeout 1.0
    play music GoodEnd fadein 5.0 volume 0.3
    show image "CaveEntrance.png" with dissolve
    window show
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    show Emma angry at left with moveinleft
    E "I much rather Liam go then you."
    hide Emma angry with moveoutleft
    hide screen negative_affection
    show Liam nervous at right with moveinright
    L2 "That is the first time I agree with something you say."
    hide Liam nervous with moveoutright
    show Emma envy at left with moveinleft
    E "Yeah but you won't be doing that right now."
    hide Emma envy with moveoutleft
    show Liam sigh at right with moveinright
    L2 "You're not letting this one go...are you?"
    hide Liam sigh with moveoutright
    show Emma smug at left with moveinleft
    E "Nope."
    hide Emma smug with moveoutleft
    show Liam angry at right with moveinright
    L2 "Ok. Fine."
    show Liam sigh with dissolve
    L2 "Guess we'll worry about it after we find a place to rest up."
    hide Liam sigh with moveoutright
    show Lila Sweats at left with moveinleft
    L "But-"
    hide Lila Sweats with moveoutleft
    show Emma angry at left with moveinleft
    E "That's enough from you today."
    show Emma sigh with dissolve
    E "We are all exhausted."
    show Emma envy with dissolve
    E "You cause enough trouble today."
    hide Emma envy with moveoutleft
    show Lila sad at left with moveinleft
    L "Ok..."
    hide Lila sad with moveoutleft
    show Liam nervous at right with moveinright
    L2 "We'll get it later...Ok?"
    hide Liam nervous with moveoutright
    show Lila default at left with moveinleft
    L "Ok."
    hide Lila default with moveoutleft
    show Liam sigh at right with moveinright
    L2 "Tough start huh."
    hide Liam sigh with moveoutright
    show Emma sigh at left with moveinleft
    E "Yeah."
    hide Emma sigh with moveoutleft
    show Liam skeptical at right with moveinright
    L "I wonder what awaits us in the future."
    hide Liam skeptical with moveoutright
    show Emma concern at left with moveinleft
    E "Who knows."
    hide Emma concern with moveoutleft
    hide image "CaveEntrance.png" with dissolve
    window hide
    show WalkingHomeNorm
    pause 1
    window show
    "Mission Failed."
    "Hurt status: No one was hurt."
    "Ending Achieved: Learn Through Failure."
    "No Page Obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return

label SaveYourself2:
    show image "black.png"
    window show
    stop music fadeout 1.0
    play music GoodEnd fadein 5.0 volume 0.3
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $renpy.notify("Emma choose to save Liam first.")
    show Emma envy at left with moveinleft
    E "You must be really stupid if you think I'll only save myself."
    hide screen positive_affection
    hide Emma sigh with moveoutleft
    $renpy.notify("Emma rushes to you.")
    show Liam panic at right with moveinright
    L2 "No!"
    $renpy.notify("Liam picks up the sharp rock.")
    show Liam yell cry with dissolve
    L2 "Lila!"
    hide Liam yell cry with moveoutright
    $renpy.notify("Liam rushes to you.")
    show Emma panic at left with moveinleft
    E "I'm sorry!"
    show Emma cry with dissolve
    E "I'm sorry!"
    show Emma yell cry with dissolve
    E "Lila!"
    hide Emma yell cry with moveoutleft
    stop music fadeout 1.0
    show Lila eyes closed sad at left with moveinleft
    L "..."
    show Lila tears with dissolve
    show Lila relieved with dissolve
    L "Goodbye."
    show Lila eyes closed sad with dissolve
    L "..."
    hide Lila eyes closed sad with moveoutleft
    Q "You pitful child."
    hide image "black.png" with fade
    window hide
    play sound Fire
    show VineBurn with fade
    pause 1
    window show
    stop sound
    hide VineBurn with fade
    window hide
    show image "MingluoCatchLila.png" with dissolve
    pause 1
    window show
    #show Mingluo soft at right with moveinright
    Q "Shhhhhh"
    $renpy.notify("You listened to her words...")
    #hide Mingluo soft with moveoutright
    L "?!"
    Q "I'm here now so don't worry."
    Q "Go to sleep."
    Q "Once you're awake."
    Q "Everything will be fine again."
    L "Ming...lou?..."
    L "I suddenly feel very tired"
    show image "black.png"
    $renpy.notify("You eyelids closed listening to her words.")
    "Mission Failed."
    "Hurt status: unknown."
    "Ending Achieved: Mysteries Await."
    "No Page obtained."
    #$renpy.movie_cutscene("Movies/End Page.mpg")
return
