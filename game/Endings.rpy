label NearbyVillage:
    hide image "black.png" with fade
    show Cave with fade
    show Lila angry cry at MoveUp
    show Emma dissapointed at emmaMoveUp
    show Emma dissapointed at emmaflip
    show Emma dissapointed at emmaRight
    show Emma sigh at PopUp with dissolve
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
    E "When I'm back and I found out your gone..."
    E "I won't think twice and ditch you."
    hide Emma intimidating with fade
    $renpy.notify("Emma left to find a village.")
    show Lila sad at middle with dissolve
    L "You always leave me behind..."
    show Lila eyes closed sad with dissolve
    L "Why?"
    L "Being alone in this cave feels so lonely and dark."
    show Lila tears with dissolve
    L "Very Dark."
    hide Lila tears with fade
    hide Cave with fade
    show image "black.png" with fade
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting."
    "No Pages Obtained."
return

label EmmaGoGetHelp:
    hide image "black.png" with fade
    show Cave with fade
    show Lila angry cry at MoveUp
    show Emma dissapointed at emmaMoveUp
    show Emma dissapointed at emmaflip
    show Emma dissapointed at emmaRight
    show Emma concern at PopUp with dissolve
    E "I can turst you to keep him safe?"
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
    E "I'll turst you one last time."
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
    show Emma soft at emmaMoveUp with dissolve
    show Lila sad at PopUp with dissolve
    L "Ok..."
    hide Emma soft with fade
    hide Lila sad with dissolve
    hide Cave with fade
    show image "black.png" with fade
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting Together."
    "No Pages Obtained."
return

label EmmaGoGetHelp2:
    hide image "black.png" with fade
    show Cave with fade
    show Lila angry cry at MoveUp
    show Emma envy at emmaMoveUp
    show Emma envy at emmaflip
    show Emma envy at emmaRight
    show Emma envy at PopUp with dissolve
    E "As if I can turst you again."
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
    E "When I'm back and I found out your gone..."
    E "I won't think twice and ditch you."
    hide Emma angry with fade
    $renpy.notify("Emma left to find a village.")
    show Lila sad at middle with dissolve
    L "You always leave me behind..."
    show Lila eyes closed sad with dissolve
    L "Why?"
    L "Being alone in this cave feels so lonely and dark."
    show Lila tears with dissolve
    L "Very Dark."
    hide Lila tears with fade
    hide Cave with fade
    show image "black.png" with fade
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting."
    "No Pages Obtained."
return

label BadEnd1:
    hide image "black.png" with fade
    show Cave with fade
    show Lila panic at MoveUp
    show Emma shocked at emmaMoveUp
    show Emma shocked at emmaflip
    show Emma shocked at emmaRight
    show Emma angry at PopUp with dissolve
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
    E "Don't know when I started to dislike you."
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
    show image "black.png" with fade
    show text '{color=#00ffcd}{size=100}"She left..."{/size}{/color}' at text_effect
    $ renpy.pause()
    hide text '{color=#00ffcd}{size=100}"She left..."{/size}{/color}' at text_effect
    show FadeGlitchBlack with fade

    show text '{color=#00ffcd}{size=100}"She left me...all by myself."{/size}{/color}' at text_effect
    $ renpy.pause()
    hide text '{color=#00ffcd}{size=100}"She left me...all by myself."{/size}{/color}' at text_effect
    hide FadeGlitchBlack with fade

    show text '{color=#00ffcd}{size=100}"How could she..."{/size}{/color}' at text_effect
    $ renpy.pause()
    hide text '{color=#00ffcd}{size=100}"How could she..."{/size}{/color}' at text_effect

    show Lila panic at middle with moveinleft
    L "..."
    show Lila eyes closed sad with dissolve
    L "I-"
    hide Lila eyes closed sad fade
    show White with fade
    RV "How absurd..."
    hide White with fade
    show "black.png" with fade
    RV2 "More like pitful."
    RV "To think a lunic like her was living with us."
    L "I'm not crazy!"
    L "The sun really does exist!"
    RV "What rubbish!"
    RV "Just take her to the mental ward."
    L "NO!" with vpunch
    L "Don't touch me!"
    L "I'm not crazy!"
    L "Stop-"
    hide "black.png" with fade
    show EmmaLiamProtect with fade
    E "Do you adults have no shame?!"
    E "She still just a kid!"
    RV3 "It because she's a kid she needs treatment right now!"
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
    hide EmmaLiamProtect
    show TearsEmmaLiamProtect
    L "They were all I need..."
    L "They were all I had."
    show bblack
    L "What have I done?"
    hide FriendBackTears with fade
    hide bblack with fade
    show image "black.png" with fade
    "Mission failed."
    "Hurt status: Liam is hurt."
    "Ending Achieved: Bad end 1(Overloaded)."
    "No Pages Obtained."
return

label MysteriesAwait:
    window show
    scene image "CaveEntrance.png" with dissolve
    show Lila happy at MoveUp
    show Lila happy at middle
    show Liam happy at LiamRight
    show Liam happy at LiamMoveUp
    show Emma nervous at emmaLeft
    show Emma nervous at emmaMoveUp
    show Lila happy at PopUp with dissolve
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
    E "Just need a second...to breath."
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
    show Lila Lila swirly eyes with dissolve
    show Emma sigh with dissolve
    show Emma dissapointed with dissolve
    show Liam default with dissolve
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
    L "I wonder what adventurous awaits us next!"
    hide Emma sigh with fade
    hide Lila happy with fade
    hide Liam smile with fade
    hide image "CaveEntrance.png" with dissolve
    show image "black.png" with fade
    "Mission Success."
    "Hurt status: No one is hurt."
    "Ending Achieved: Mysteries Await."
    "First Page obtained."
return

label SaveMe1:
    window show
    show image "Vina death.png" with fade
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
    show Emma yell with at left with moveinleft
    E "AHHHHHHHHHHH!" with hpunch
    $renpy.notify("Emma cuts the vines on you.")
    show Emma envy with dissolve
    E "This is why you shouldn't have touched the crytsal!"
    $renpy.notify("Emma picks up your sharp rock.")
    show Emma yell with dissolve
    E "Take this you dumb Vina Plant!"
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    show Emma envy with dissolve
    hide image "Vina death.png" with fade
    show image VineHurt with fade
    E "Let's get out of here now!"
    $renpy.notify("Stunned by the pain the Vina plant freed Liam.")
    hide VineHurt with fade
    show image "CaveEntrance.png" with dissolve
    show Emma nervous with dissolve
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
    show image "black.png" with fade
    "Mission failed."
    "Hurt status: No one is hurt."
    "Ending Achieved: Mysteries Await."
    "No Page obtained."
return

label SaveMe2:
    show image "Vina death.png" with fade
    show Emma yell at left with moveinleft
    E "AHHHHHHHHHHH!" with hpunch
    $renpy.notify("Emma choose to save Liam.")
    show Emma panic with dissolve
    E "I-"
    show Emma dissapointed with dissolve
    $renpy.notify("All you can see is the look of guilt.")
    E "I'm sorry..."
    hide Emma dissapointed with moveoutleft
    "Mission failed."
    "Hurt status: unknown."
    "Ending Achieved: Results Of Being Selfish."
    "No Page obtained."
return

label SaveLiam:
    show image "Vina death.png" with fade
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
    hide Liam with moveoutright
    show Emma yell with at left with moveinleft
    E "AAAAHHHHH!" with hpunch
    $renpy.notify("Emma cuts the vines on you.")
    show Emma envy with dissolve
    E "This is why you shouldn't have touched the crytsal!"
    $renpy.notify("Emma picks up your sharp rock.")
    show Emma yell with dissolve
    E "Take this you dumb Vina Plant!"
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    hide image "Vina death.png" with fade
    show Vinehurt with fade
    show Emma envy with dissolve
    E "Let's get out of here now!"
    $renpy.notify("Stunned by the pain the Vina plant drops Liam.")
    hide Vinehurt with fade
    show Cave with fade
    show Emma panic at left with moveinleft
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
    Q "You should care."
    hide Mingluo no eyes with moveoutright
    hide Cave with fade
    window hide
    show VineBurn with fade
    pause
    window show
    $renpy.notify("The wall of vines started to burn.")
    show Emma shocked at left with moveinleft
    E "What-?!"
    hide Emma shocked with moveoutleft
    show Mingluo happy at right with moveinright
    M "Nice to see you guys doing well."
    hide VineBurn with fade
    window hide
    show MingluoBurnPage with fade
    pause
    window show
    $renpy.notify("Minglou picks up the page.")
    E "..."
    L2 "..."
    hide MingluoBurnPage with fade
    show Cave with fade
    show Lila happy at left with moveinleft
    L "Minglou!"
    $renpy.notify("You gave minglou a hug.")
    show Mingluo disgust at right with moveinright
    show Minglou happy with dissolve
    M "..."
    hide Lila happy with moveoutleft
    show Minglou smirk with dissolve
    M "Looks like you're friends don't like seeing me."
    show Minglou sigh with dissolve
    M "Makes me a bit sad."
    hide Minglou sigh with moveoutright
    show Lila skeptical at left with dissolve
    L "What are you doing here?"
    hide Lila skeptical with moveoutleft
    show Minglou smile at right with moveinright
    M "To help you of course!"
    hide Minglou smile with moveoutright
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
    M "Anyways!"
    M "Here you go."
    show screen inventory_button
    $renpy.notify("Page Found.")
    $inventory.add(Page1)
    L "Thanks Minglou!"
    L "Hm?"
    hide screen inventory_button
    L "I Don't know what it says."
    L "Can you help me Minglou-"
    L "Huh?"
    L "Where did she go?"
    E "She left after you took the page."
    L2 "Ignore her for now."
    L2 "Let's find a place to rest first."
    L2 "It's been a tough start to our adventure."
    L2 "I'll help you figure out what's written after."
    E "I agree with Liam."
    E "I feel beat."
    L "Oh ok!"
    L "I wonder why Minglou wants this page that bad..."
    E "Who knows."
    "Mission Success."
    "Hurt status: No one is hurt."
    "Ending Achieved: Mysteries Await."
    "First Page obtained."
return

label SaveLiam2:
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $liam_points += 1
    E "AHHHHHHHHHHH!" with hpunch
    hide screen positive_affection
    E "I-"
    E "I'm sorry Lila."
    $renpy.notify("Emma choose to free Liam.")
    L2 "Emma!" with vpunch
    $renpy.notify("Liam pushed Emma but Emma hold Liam back.")
    Q "How coldhearted..."
    Q "You pitfully child."
    L "Ming...lou..."
    $renpy.notify("You listened to her words...")
    M "I'm here now."
    M "So don't worry."
    M "Sleep peacefully."
    M "When you wake up again"
    M "Everything will be fine again."
    $renpy.notify("And fell into a deep sleep.")
    "Mission Failed."
    "Hurt status: unknown."
    "Ending Achieved: Mysteries Await."
    "No Page obtained."
return

label SaveYourself:
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $renpy.notify("Emma choose to save you first.")
    E "You must be really stupid if you I'll only save myself."
    hide screen positive_affection
    $renpy.notify("Emma picks up your sharp rock.")
    E "Take this you dumb Vina Plant!"
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    E "Let's get out of here now!"
    $renpy.notify("Stunned by the pain the Vina plant drops Liam.")
    E "...."
    E "Stop it you baby."
    E "Everything is fine now."
    L "...Yeah."
    E "Look."
    E "Stop crying for a bit."
    L "?"
    E "I'm sorry I could get the page..."
    L "I don't care about that!"
    L2 "Pft."
    E "What's so funny??"
    L "You guys are so cute."
    E "C-"
    E "Forget it."
    E "What do we do about the page."
    L2 "Let's give it another attempt."
    E "What-?"
    L2 "But just with you and me this time."
    L2 "I'll go find another rock to sharpen."
    menu:
        "Don't go. I don't want you to die.":
            jump DoNotDie
        "Please be safe.":
            jump BeSafe
        "Are You sure you don't need me to try again?":
            jump YouSure
return

label DoNotDie:
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $liam_points += 1
    L2 "No one is going to die."
    hide screen positive_affection
    L "No!" with vpunch
    E "I agree with her."
    E "I don't like this idea."
    L2 "I guess we should find a place to rest up first before we make another attempt."
    E "Yeah..."
    E "Come on."
    E "Let's go."
    E "I'll hold your hand so calm down ok?"
    L "Ok."
    E "Off we go to find a village."
    "Mission Failed."
    "Hurt status: No one was hurt."
    "Ending Achieved: Learn Through Failure."
    "No Page obtained."
return

label Besafe:
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $liam_points += 1
    E "You must be kidding."
    hide screen positive_affection
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    E "After all of that I am not letting you do that again."
    hide screen negative_affection
    L2 "Come on."
    L2 "Don't be like that."
    L2 "I also hate the idea of being protected all the time."
    $renpy.notify("Liam found and sharpened a rock.")
    E "Wha-"
    E "Where did you find that?!"
    L2 "I have my ways."
    E "Forget it."
    E "Why do you have to be so stuborn?"
    L2 "I just refuse to accept failure{cps=2}...{/cps}at the moment."
    E "Lila."
    L "?"
    E "Summon your spirit if things go wrong again."
    E "As much as I hate her..."
    E "She is undeniablly strong."
    L "Ok."
    $renpy.notify("Emma and Liam successfully got the page.")
    L2 "See it wasn't that bad..."
    E "Yeah...I wonder why."
    L "...?"
    L2 "Well we got the page but what's written will take time to decode."
    E "Let's find an place to rest up first then."
    L2 "I guess we did start this adventure off rough."
    L2 "I wonder what awaits us after this."
    "Mission Success."
    "Hurt status: No one was hurt."
    "Ending Achieved: Mysteries Await."
    "First Page obtained."
return

label YouSure:
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    E "I much rather Liam go then you."
    hide screen negative_affection
    L2 "That is the first time I agree with something you say."
    E "Yeah but you won't be doing that right now."
    L2 "You're not letting this one go...are you?"
    E "Nope."
    L2 "Ok. Fine."
    L2 "Guess we'll worry about it after we find a place to rest up."
    L "But-"
    E "That's enough from you today."
    E "We are all exhausted."
    E "You cause enough trouble today."
    L "Ok..."
    L2 "We'll get it later...Ok?"
    L "Ok."
    L2 "Tough start huh."
    E "Yeah."
    L "I wonder what awaits us in the future."
    E "Who knows."
    "Mission Failed."
    "Hurt status: No one was hurt."
    "Ending Achieved: Learn Through Failure."
    "No Page Obtained."
return

label SaveYourself2:
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $renpy.notify("Emma choose to save Liam first.")
    E "You must be really stupid if you I'll only save myself."
    hide screen positive_affection
    $renpy.notify("Emma rushes to you.")
    L2 "No!"
    $renpy.notify("Liam picks up the sharp rock.")
    L2 "Lila!"
    $renpy.notify("Liam rushes to you.")
    E "I'm sorry!"
    E "I'm sorry!"
    E "Lila!"
    L "..."
    L "Goodbye."
    L "..."
    Q "You pitfully child."
    $renpy.notify("The vines start to burn.")
    L "?!"
    Q "I'm here now so don't worry."
    Q "Go to sleep now."
    Q "Once you're awake."
    Q "Everything will be fine again."
    L "Ming...lou?..."
    $renpy.notify("You eyelids closed listening to her words.")
    "Mission Failed."
    "Hurt status: unknown."
    "Ending Achieved: Mysteries Await."
    "No Page obtained."
return
