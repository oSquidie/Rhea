label NearbyVillage:
    E "You stay here."
    E "You might just cause more trouble if you tagged along."
    L "But I'm worried."
    E "Too late to be saying that now."
    E "I can't trust you to watch him."
    E "And can't trust you to find a village either..."
    E "What good are you for?"
    L "I'm sorry..."
    E "Forget it."
    E "I'll carry him on my shoulder."
    E "While I'm gone..."
    E "Don't you dare touch anything."
    L "Ok..."
    E "Wait for us to come back."
    E "When I'm back and I found out your gone..."
    E "I won't think twice and ditch you."
    L "Looks like she's gone."
    L "Being alone in this cave feels lonely and dark."
    L "Very Dark."
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting."
    "No Pages Obtained."
return

label EmmaGoGetHelp:
    E "I can turst you to keep him safe?"
    E "He's defenseless right now."
    L "I promise I won't leave his side."
    E "Fine."
    E "I'll turst you one last time."
    E "Don't make me regret this choice."
    E "Take this."
    show screen inventory_button
    $renpy.notify("You now have Emma's dagger.")
    $inventory.add(Dagger)
    E "Don't hesitate to kill."
    hide screen inventory_button
    E "The things in this world aren't forgiving."
    L "?"
    E "Forget it."
    E "Just don't move."
    E "Wait for me to come back."
    L "Ok..."
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting Together."
    "No Pages Obtained."
return

label EmmaGoGetHelp2:
    E "As if I can turst you again."
    E "I can't trust you to watch him."
    E "And can't trust you to find a village either..."
    E "What good are you for?"
    L "I'm sorry..."
    E "Forget it."
    E "I'll carry him on my shoulder."
    E "While I'm gone..."
    E "Don't you dare touch anything."
    L "Ok..."
    E "Wait for us to come back."
    E "When I'm back and I found out your gone..."
    E "I won't think twice and ditch you."
    L "Looks like she's gone."
    L "Being alone in this cave feels lonely and dark."
    L "Very Dark."
    "Mission failed."
    "Hurt status: Liam was hurt."
    "Ending Achieved: Waiting."
    "No Pages Obtained."
return

label BadEnd1:
    show image "black.png"
    E "Are you serious?"
    E "Feel your chest."
    E "Is there still a heart inside of there?"
    L "Wait-I.."
    L "I said that without thinking-"
    E "Enough." with vpunch
    E "Don't know when I started to dislike you."
    E "But I was right."
    E "I told him so many times you aren't worth our time."
    E "I'm taking Liam."
    E "As for you..."
    E "Your safety no long concerns me."
    L "Emma!"
    L "Don't Leave!"
    L "Listen to me!"
    L "Emma!"
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

    L "..."
    L "I-"
    show White with fade
    RV "How absurd..."
    hide White with fade
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
    show FriendBack
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
    hide FriendBack
    show FriendBackTears
    show bblack
    L "They were all I need..."
    hide FriendBackTears with fade
    hide bblack with fade
    show image "black.png"
    "Mission failed."
    "Hurt status: Liam is hurt."
    "Ending Achieved: Bad end 1(Overloaded)."
    "No Pages Obtained."
return

label MysteriesAwait:
    L "We did it!"
    E "N-Nice..."
    L "Emma are you ok?"
    E "Y-yeah."
    E "Just need a second...to breath."
    L "Oh ok..."
    L "Hmmm..."
    L "What does this say??"
    L2 "Let me take a look."
    L2 "Hmmmm..."
    L2 "It's a bit complicated to decode."
    L2 "Let's find a nearby library where I can focus and do some research."
    L "Ok!"
    E "Guess we looking for a town next."
    E "Let's go."
    E "I'm exhausted."
    L "Ok!"
    L "I wonder what adventurous awaits us next!"
    "Mission Success."
    "Hurt status: No one is hurt."
    "Ending Achieved: Mysteries Await."
    "First Page obtained."
return

label SaveMe1:
    show screen negative_affection
    $affbarposi = False
    $affbarnegative = True
    $emma_points -= 1
    $liam_points -= 1
    L2 "Go save her first!"
    hide screen negative_affection
    E "But!"
    L2 "I'll be fine!"
    E "AHHHHHHHHHHH!" with hpunch
    $renpy.notify("Emma cuts the vines on you.")
    E "This is why you shouldn't have touched the crytsal!"
    $renpy.notify("Emma picks up your sharp rock.")
    E "Take this you dumb Vina Plant!"
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    E "Let's get out of here now!"
    $renpy.notify("Stunned by the pain the Vina plant drops Liam.")
    E "...."
    E "Stop weiling you idiot."
    L "But what about the page?"
    E "Why are you worried about that in this state?"
    E "Not even medication can fix that brain of yours."
    L "..."
    L2 "Let's find a place to rest up before we figure out the next step..."
    L "Ok..."
    "Mission failed."
    "Hurt status: No one is hurt."
    "Ending Achieved: Mysteries Await."
    "No Page obtained."
return

label SaveMe2:
    E "AHHHHHHHHHHH!" with hpunch
    E "I-"
    $renpy.notify("All you can see is the look of guilt.")
    E "I'm sorry..."
    "Mission failed."
    "Hurt status: unknown."
    "Ending Achieved: Results Of Being Selfish."
    "No Page obtained."
return

label SaveLiam:
    show screen positive_affection
    $affbarposi = True
    $affbarnegative = False
    $emma_points += 1
    $liam_points += 1
    L2 "No!"
    hide screen positive_affection
    L2 "Save her first!"
    E "But you-"
    E "AAAAHHHHH!"
    $renpy.notify("Emma cuts the vines on you.")
    E "This is why you shouldn't have touched the crytsal!"
    $renpy.notify("Emma picks up your sharp rock.")
    E "Take this you dumb Vina Plant!"
    $renpy.notify("Emma throws it at one of the eyes on the Vina Plant.")
    E "Let's get out of here now!"
    $renpy.notify("Stunned by the pain the Vina plant drops Liam.")
    E "...."
    L2 "It's ok..."
    L2 "It's over now."
    L2 "Sorry we couldn't get the page."
    L "I don't care about that right now..."
    Q "You should care."
    $renpy.notify("The wall of vines started to burn.")
    E "What-?!"
    M "Nice to see you guys doing well."
    $renpy.notify("Minglou picks up the page.")
    E "..."
    L2 "..."
    L "Minglou!"
    $renpy.notify("You gave minglou a hug.")
    M "Looks like you're friends don't like seeing me."
    M "Makes me a bit sad."
    L "What are you doing here?"
    M "To help you of course!"
    E "You could have came earlier..."
    M "What was the phase?"
    M "The main character never comes on time."
    E "What a load of bull-"
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
