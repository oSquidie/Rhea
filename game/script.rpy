define L = Character('Lila', color="#ced0ff", image = "Lila")
define m = Character('Mingluo', color="#87ddfb", image = "Mingluo")
define fa = Character('Emma', color="#73fff0", image = "Emma")
define fb = Character('Liam', color="#a673ff", image = "Liam")
define Q = Character ("?")

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
define Vine_ListenAfterTouch = False

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
label splashscreen:
    with Pause(1)

    show text "Any similarities this game has with real life is purely coincidental." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "This is a work of fiction." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    call screen confirm(message="Rhea contains a lot of bright colors, this may affect individuals who are susceptible to photo sensitivities. Do you want to continue?", yes_action=Return(), no_action=Quit(confirm=False))
    return
######################## Define Audio Files ################################
define audio.RheaSoundtrack ="audio/RheaSoundtrack.wav"
define audio.RheaMain = "audio/RheaMainMenuMusic.wav"
define audio.CrunchCrys = "audio/Crunch.wav"

play music RheaMain


define Choice1 = True
define Choice2 = True
define Choice3 = True

define Affection= False
define Affection_sys.value = 0

#define Path1_Answers = False
#define Qpoints1.value = 0

if Page_TouchAlready = False:
            hide Page

init python:

    def glass_dragged(drags, drop):

        if not drop:
            return

        store.glass = drags[0].drag_name
        store.object = drop.drag_name

        return True

screen slide_glass_screen:
    add "CaveExplore3.png"
    draggroup:
        drag:
            drag_name "You"
            child "MagnifyingGlass.png"
            droppable False
            dragged glass_dragged
            xpos 100 ypos 100

        drag:
            drag_name "Crystal"
            draggable False
            child "Crystal.png"
            xpos 900 ypos 100

        drag:
            drag_name "Vine"
            draggable False
            child "Vine.png"
            xpos 1500 ypos -90

        drag:
            drag_name "Opus"
            draggable False
            child "Opus.png"
            xpos 20  ypos 450

        drag:
            drag_name "Page?"
            draggable False
            child "PageItem.png"
            xpos 1670 ypos 850

#######################START GAME INTRO####################
label start:
    stop music fadeout 1.0
    play music "audio/RheaSoundtrack.wav" fadein 5.0 volume 0.3

    #$persistent.Route1 = True
    #$persistent.Route2 = True

    default preferences.text_cps = 50
    scene Map with fade
    window hide
    pause
    window show
    "Within a place shrouded in darkness..."
    show Map:
        ease 3.0 zoom 2.0
    window hide
    pause 3.5
    window show
    "Far away from Corpinus village"
    show Map at Position (xpos = 0.4,  xanchor=0.5, yanchor= 0.5, ypos= -.1) with pixellate:
        zoom 3.0
    "A group of friends secretly plays hide and seek in Morel Forest."
    "Whispers can be heard as the glimmers of radiance reveals three kids."

        #show Lila happy at flip for flipping the sprite

        #transform my_dissolve(x):
                # alpha 0.0
                # linear x alpha 1.0

       # label transform_test:
        #show image "Forest_Default.png" at truecenter, my_dissolve(.5)

    scene image "Forest_Default.png" with dissolve
    show Lila default at left
    show Liam default at right
    show Emma default at middle
    L "Hey..."
    show Lila surprised at left with dissolve
    L "Have you guys ever wondered what it's like living in a world filled with light?"
    show Emma default at flip with dissolve
    show Emma concern at flip with dissolve
    show Liam surprised at right with dissolve
    "One of her friends gave her a weird look while the other grew curious."
    "The three of them were deciding who to go first when she popped the question."
    show Lila default at left with dissolve
    show Liam sigh at right with dissolve
    fb "We're already living in a world like that."
    show Liam nervous at right with dissolve
    fb "Aren't we?"

    "They have only known the darkness since their existence on Rhea."
    "The only lights that they've seen are the dim glows of natural bioluminescence."

    show Lila nervous at left with dissolve
    L "No!"
    show Lila pout at left with dissolve
    show Liam surprised with dissolve

    L "I don't mean the kind of lights from this world.."
    L "Not just tiny glows here and there."

    show Lila default at left with dissolve
    L "I meant a world where the entire land"

    show Lila eyes closed at left with dissolve
    L "No..."

    show Lila happy at left with dissolve
    L "The entirety of Rhea is filled by a very, very bright light!"

    show Emma angry at flip with dissolve
    fa "What are you suddenly talking about?"
    show Liam nervous with dissolve

    show Lila nervous at left with dissolve
    L "Ummmm...."
    show Lila eyes closed sad with dissolve
    L "How do I explain this?"
    show Lila happy at left
    L "Oh I know!"
    L "It's like something even more blinding than the Enoki mushrooms!"

    show Emma concern with dissolve
    fa "You've lost your head again."
    show Lila surprised with dissolve

    show Emma sigh with dissolve
    fa "Can we just focus the game?"
    show Lilasad at left with dissolve
    hide  Lila surprised

    show Liam wink at right with dissolve
    fb "Patience Emma. We have plenty of time."

    show Emma angry with dissolve
    fa "I'm just saying I'm not interested in her make believe fantasy."

    fb "It may be fantasy but it might not be make-believe."
    hide Lilasad at left
    show Lila surprised at left

    show Emma concern at yflip with dissolve
    fa "Huh?"
    fa "What are you on about?"

    show Emma sigh with dissolve
    fa "If you keep leading her on these crazy daydreams..."
    fa "She'll become even more stu-"
    show  Lila skeptical with dissolve

    show Liam happy at right with dissolve
    fb "I also think we should start playing the game." with hpunch

    show Emma surprised with dissolve
    fb "It's been a while since we've gathered."
    fb "Let's enjoy this rare moment!"
    show Emma pout at emmaflip with dissolve

    "Liam raised his voice but his uplifting tone didn't change."

    show Lila pout at left with dissolve
    L "Oh..."
    L "I guess you guys are getting bored."
    hide Lila pout at left

    show Lilasad at left
    "Lila sounded disappointed at their reactions."
    "But she wasn't disappointed for long."
    hide Lilasad at left
    show Lila smile at left
    "She did miss her friends after all."

    show Emma angry at flip with dissolve
    fa "How are you so thick headed for you to realize that just now?"

    show Lila angry at left with dissolve
    L "Huh? Thick headed?"
    show Lila pout at left with dissolve

    show Liam nervous with dissolve
    fb "Ah!" with hpunch
    fb "Ignore her. Ignore her."
    show Liam wink at right with dissolve
    fb "Let's play!"

    hide Emma angry at flip
    hide Lila pout at left
    hide Liam wink at right
    #"What do you want to be? The seeker or hidder?"

 #######################Start Character Relationship Points####################
    menu:
        "Start Game":
                jump Seeker
       # "Seeker?": #if persistent.Route1 == True:
            #jump Seeker
        #"Hidder?" if persistent.Route2 == True:
            #jump Concealer
return

label Seeker:
    scene image "Forest_Default.png" with fade
    #$persistent.Route1 = False
    #$persistent.value += 1
#if persistent.value >= 2:
        #$persistent.Route1 = True
        #$persistent.Route2  = True
        #$persistent.value = 0

    show bblack with dissolve
    show Lila eyes closed at lilaflip with dissolve
    "I stand there counting."
    "The only kind of warmth I feel is from the glowing fireflies"
    hide bblack with dissolve

    L "55"
    L "54"
    L "53..."

    show bblack with dissolve
    show Lilasad at lilaflip
    "For some reason."
    "I felt more and more lonely as the numbers continue to count down."
    "Is it because of the darkness?"
    "But I grew up in this darkness..."
    "That can't be it."
    "What could it be?"
    "Something didn't feel right."
    "Yet...."
    hide bblack with dissolve
    hide Lilasad
    show Lila eyes closed sad at lilaflip
    L "52"
    L "51..."

    Q "OUCH!" with vpunch
    show Lila surprised at yflip with dissolve
    "Hearing a weird noise I stopped counting."
    "I listened more closely to make sure I wasn't hearing things."
    "There was only silence so I kept counting."
    show Lila eyes closed sad at lilaflip with dissolve
    L "50"
    L "4-!"

    Q "Ouch! What was that for?" with vpunch
    show Lila skeptical at lilaflip with dissolve
    "That sounded like Emma."
    hide Lila skeptical at lilaflip with dissolve
    show Lilasad at left
    "I should go check on her."
    "I know I'm in the middle of a game but I'm worried."

    L "Emma?"
    L "Was that you?"

    "At first there was no response."
    "But when I got a bit closer Emma popped out of her hiding spot along with Liam."
    hide Lilasad at left
    show Lila surprised at left
    show Emma angry at emmaflip with dissolve
    show Liam nervous at right with dissolve
    fa "Nope."
    show Emma embarrassed at emmaflip with dissolve
    fa "Wasn't me."
    show Lila skeptical at left
    show Liam surprised at right with dissolve
    L "If it wasn't Emma then who was it?"
    show Liam embarrassed at right with dissolve
    L "Liam?"
    hide Emma embarrassed at emmaflip
    hide Lila skeptical at left
    hide Liam embarrassed at right
    menu:
        "Ask if Emma is ok.":
            jump EPath1
        "Ask if Liam is ok.":
            jump LPath1
return
#######################Liam VS EMMA Part 1####################
label EPath1:
    "Emma's affection goes up."
    show Lila skeptical at left
    show Emma embarrassed at emmaflip
    show Liam embarrassed at right
    L "Are you sure?"
    show Emma surprised with dissolve
    L "That sounded like you were in pain."
    show Emma blush with dissolve
    show Emma embarrassed with dissolve
    fa "What pain?"
    show Liam nervous with dissolve
    show Lila surprised with dissolve
    show Lila skeptical with dissolve
    "I don't know why Emma is acting like this..."
    hide Lilasurprised at left
    show Lilasad at left
    L "Well..."
    show Liam surprised with dissolve
    hide Lilasad at left
    show Lila eyes closed sad at left
    "Even so if she's hurt she should take care of herself."
    show Lila eyes closed at left with dissolve
    show Lila default at left with dissolve
    show Liam default with dissolve
    L "I have something here that might help y-"
    show Emma sigh at middle with dissolve
    fa "Look." with hpunch
    show Emma angry with dissolve
    show Liam nervous with dissolve
    show Liam sigh with dissolve
    show Lila surprised with dissolve
    fa "Thanks for worrying but can you stop being so annoy-"
    show Lila skeptical with dissolve
    show Liam happy with dissolve
    fb "Ahahahah!"
    show Emma surprised with dissolve
    show Liam smile with dissolve
    fb "You found us!"
    show Emma pout with dissolve
    show Liam wink with dissolve
    fb "Looks like Emma is the seeker next!"
    show Emma surprised with dissolve
    show Emma envy with dissolve
    L "I guess I did."
    show Emma angry with dissolve
    fa "HUh?"
    show Lila surprised with dissolve
    show Liam surprised with dissolve
    show Emma sigh with dissolve
    fa "This round isn't fair for Liam."
    show Liam sigh with dissolve
    show Emma envy with dissolve
    fa "Recount."

    fb "No. No."
    show Liam nervous with dissolve
    fb "It's fine if I am the seeker."
    fb "There's no need for her to reco-"
    show Emma angry with dissolve
    fa "This isn't fair."
    show Liam skeptical with dissolve
    fa "She needs to recount."
    show Liam sigh with dissolve
    "I heard Liam sigh."
    show Lila swirly eyes with dissolve
    "What should I do?"
    hide Emma angry
    hide Liam sigh
    hide Lila swirly eyes
    menu:
        "Tell Emma she's being moronic.":
                jump EPath2
        "Tell Liam he's being irrational":
                jump LPath2
        "Say you want to be hider.":
                jump NPath1
return

################# Liam VS EMMA Part 2 Or Go Your Own Way Part 1 ####################

label LPath1:
    "Liam's affection goes up."
    show Emma embarrassed at emmaflip
    show Lila skeptical at left
    show Liam embarrassed at right
    L "Was that you Liam?"
    show Lilasad at left
    show Emma surprised with dissolve
    show Liam surprised with dissolve
    L "Are you ok?"
    show Emma envy with dissolve
    show Liam smile with dissolve
    fb "Hm?"
    hide Lilasad at left
    show Lila skeptical at left with dissolve
    show Liam content with dissolve
    fb "How kind Lila."
    show Lila surprised with dissolve
    show Liam smile with dissolve
    fb "I'm perfectly fine."
    show Lila happy with dissolve
    "Liam showed me a bright smile. I smiled back with relief."
    show Lila smile with dissolve
    show Emma angry with dissolve
    fa "Of course he's fine!"
    show Lila surprised with dissolve
    show Emma pout with dissolve
    show Liam nervous with dissolve
    fa "I was the one hurt...."
    show Liam embarrassed with dissolve
    show Lila stunned with dissolve
    L "Huh?"
    L "I thought you said it wasn't you..."
    show Emma surprised with dissolve
    show Emma embarrassed with dissolve
    show Emma envy with dissolve
    show Lila swirly eyes with dissolve
    show Liam nervous with dissolve
    "I'm so confused. Didn't she say she wasn't hurt but now she is?"
    show Emma angry with dissolve
    fa "That's it!"
    show Liam surprised with dissolve
    show Lila surprised with dissolve
    fa "You're recounting Lila!"
    show Liam sigh with dissolve
    fa "This round isn't fair!"
    show Liam nervous with dissolve
    show Lila stunned with dissolve
    L "Huh?"
    show Liam sigh with dissolve
    fb "There's no need for that."
    show Emma pout with dissolve
    show Liam nervous with dissolve
    fb "I can do the counting."
    show Emma envy with dissolve
    show Liam smile with dissolve
    fb "Let's just take turns."
    show Emma yell with dissolve
    fa "But that's not fair!"
    show Liam skeptical with dissolve
    show Emma angry with dissolve
    show Lila surprised with dissolve
    fa "You were found because of me."
    show Lila nervous with dissolve
    fa "So she should just recount and start over."
    show Liam sigh with dissolve
    fb "Emma..."
    show Liam angry with dissolve
    fb "Don't be unreasonable."
    show Emma surprised with dissolve
    show Emma envy with dissolve
    show Lila panic with dissolve
    "What's going on now?"
    show Lila swirly eyes with dissolve
    "Should I do something?"
    hide Liam angry
    hide Lila swirly eyes
    hide Emma envy
    menu:
        "Give Emma a hug.":
                jump EPath3
        "Take Liam's hand.":
                jump LPath3
        "Leave the scene.":
                jump NPath2
return

################### Liam VS EMMA Part 3 Or Go you rown way part 2####################

label EPath2:
    "Emma's affection goes down."
    show Emma angry at emmaflip
    show Lila swirly eyes at left
    show Liam sigh at right
    show Lila Sweats at left with dissolve
    L "Emma your being....."
    show Liam surprised with dissolve
    show Emma envy with dissolve
    show Lila eyes closed sad with dissolve
    L "Um..."
    show Lila nervous at left with dissolve
    L "Moronic."
    show Emma shocked with dissolve
    show Liam shocked with dissolve
    fa "W-"
    fa "What did you just say?"
    show Lila Sweats with dissolve
    show Emma embarrassed with dissolve
    show Emma angry with dissolve
    fa "Do you have any idea what that word means?"
    show Lila skeptical with dissolve
    show Liam nervous with dissolve
    L "Not really but you call me that all the time."
    show Emma shocked with dissolve
    show Emma embarrassed with dissolve
    show Emma angry with dissolve
    show Emma panic with dissolve
    show Emma nervous with dissolve
    show Emma dissapointed with dissolve
    show Lila Sweats with dissolve
    fa "She's right."
    fa "You always somehow manage to bring out the ugly in me."
    show Emma panic with dissolve
    fa "I-"
    show Emma nervous with dissolve
    show Emma panic with dissolve
    show Emma yell cry with dissolve
    fa "I don't want to play anymore."
    hide Emma yell cry with fade
    show Liam panic with dissolve
    show Lila shocked with dissolve
    "She runs off."
    "Liam calls out to her but she doesn't look back."
    hide Liam panic with dissolve
    "So he runs after her."
    show Lila Sweats with dissolve
    "I feel a wave of worry and run after them."
    hide Lila Sweats with fade
    scene image "Twopaths.png" with fade
    "But they are too fast and lost them."
    L "Oh no.."
    "I look around."
    "All I see is a cave."
    #"From what I can see there are only two paths from here."
    #"On the left is a cave and on the right is a den."
    "What should I do?"
    menu:
        "Observe the place?":
                jump O1
        #"Go to Den.":
                #jump Den1
        "Go to Cave.":
                jump Cave1
        "Sit and wait.":
                jump SaW1
return

#######################Place Obseveration 1##########################

label LPath2:
    "Liam's affection goes down. Emma's affection goes down."
    show Emma angry at emmaflip
    show Lila swirly eyes at left
    show Liam sigh at right
    show Lila Sweats at left with dissolve
    L "Liam you are irrational."
    show Liam shocked with dissolve
    show Emma shocked with dissolve
    fb "Oh..."
    show Liam embarrassed with dissolve
    show Liam nervous with dissolve
    show Emma envy with dissolve
    show Emma angry with dissolve
    fa "How dare y-"
    show Liam sigh with dissolve
    fb "She's right."
    show Lila shocked with dissolve
    show Emma shocked with dissolve
    show Liam nervous with dissolve
    fb "That was very childish of me."
    show Emma envy with dissolve
    show Emma pout with dissolve
    show Liam sad with dissolve
    fa "Why do you still side with her..."
    show Liam sigh with dissolve
    show Lila Sweats with dissolve
    "Liam lets out a sigh."
    show Liam angry with dissolve
    fb "That's not it."
    fb "I should have asked."
    show Liam nervous with dissolve
    fb "What do you want to be Lila?"
    hide Emma pout
    hide Lila Sweats
    hide Liam nervous
    menu:
        "Seeker again.":
               jump Seeker1
        "Hidder.":
                jump Hidder1
return

#######################Liam And Emma Offended#####################

label Hidder1:
    show Lila Sweats at left
    show Emma pout at emmaflip
    show Liam nervous at right
    L "I want to hide this time."
    show Emma angry with dissolve
    fa "Then say so in the first place."
    hide Lila Sweats at left
    show Lilasad at left
    show Liam sad with dissolve
    "Emma sounds bitter."
    "Liam doesn't say anything and just sliently counts"
    hide Liam sad with fade
    "Soon after Emma starts to run."
    hide Emma angry with fade
    hide Lilasad at left
    show Lila Sweats at left
    "I want to follow Emma but she runs too fast."
    "I couldn't keep up."
    show Lila nervous with dissolve
    "I took a while to catch my breath."
    hide Lila nervous with fade
    scene image "Twopaths.png" with fade
    "When I look around I see that this isn't a place I have been to before."
    #"From what I can see to my left is a cave and my right is a den."
    "All I see is a cave."
    "What should I do?"
    menu:
          "Observe the place?":
                jump O1
          #"Go to Den.":
                #jump Den1
          "Go to Cave.":
                jump Cave1
          "Sit and wait.":
                jump SaW2
return

#######################Place Obseveration 2##########################
label Seeker1:
    show Lila Sweats at left
    show Emma pout at emmaflip
    show Liam nervous at right
    L "I want to seek again."
    show Emma angry with dissolve
    fa "Then say so in the first place."
    hide Lila Sweats at left
    show Lilasad at left
    show Liam sad with dissolve
    "Emma sounds bitter."
    "Liam doesn't say anything and just quietly went to hide."
    hide Liam sad with fade
    "Soon after Emma followed behind."
    hide Emma angry with fade
    "I look on as the backs of my friends dissappear into the woods."
    "My heart started to hurt."
    "Feeling awful I decided to follow them."
    hide Lilasad at left
    show Lila Sweats at left
    "But I can't catch up."
    show Lila nervous with dissolve
    "I took a while to catch my breath."
    scene image "Twopaths.png" with fade
    "When I look around I see that this isn't a place I have been to before."
    "All I see is a cave."
    #"From what I can see to my left is a cave and my right is a den."
    "What should I do?"
    menu:
          "Observe the place?":
                jump O1
          #"Go to Den.":
                #jump Den1
          "Go to Cave.":
                jump Cave1
          "Sit and wait.":
                jump SaW2
return

#######################Place Obseveration 2##########################
label NPath1:
    "Liam's affection goes up. Emma's affection goes down."
    show Emma angry at emmaflip
    show Lila swirly eyes at left
    show Liam sigh at right
    show Lila happy at left with dissolve

    L "I also want Liam to be the seeker this time!"
    show Liam surprised with dissolve
    show Liam smile with dissolve
    show Emma surprised with dissolve
    show Emma angry with dissolve
    fa "I just said that it was unfair for Liam."
    fa "Are you de-"
    show Lila nervous with dissolve
    "For a second I thought that Emma was going to blow up."
    "Yet Liam's calm voice settled my nerves."
    show Liam nervous with dissolve
    fb "It's ok Emma. "
    show Lila Sweats with dissolve
    show Emma surprised with dissolve
    show Emma pout with dissolve
    show Liam happy with dissolve
    fb "It would be more fair if I play as the seeker next."
    show Emma embarrassed with dissolve
    show Emma pout with dissolve
    show Emma sigh with dissolve
    fa "I guess it's only fair."
    show Lila relieved with dissolve
    show Emma dissapointed with dissolve
    fa "You're so obvious..."
    show Lila skeptical
    show Liam sad with dissolve
    hide Emma dissapointed with fade
    "I watch as Emma leaves."
    "I've known her for some time now."
    show Liam sigh with dissolve
    show Lilasad at left
    "I have no clue when she became like this."
    "It almost feels bitter."
    show Liam surprised with dissolve
    "Did something happen to cause her to be like this?"
    show Liam smile with dissolve
    fb "Aren't you going to hide?"
    hide Lilasad at left
    show Lila surprised at left with dissolve
    "Liam asks me."
    "But I don't want to hide yet."
    show Lila Sweats with dissolve
    "I want to sort something out."
    "But should I wait till the game is over?"
    hide Lila Sweats
    hide Liam smile
    menu:
        "Go talk to Emma.":
                jump EPath4
        "Ask Liam about Emma":
                jump LPath4
        "Ignore. Just go hide.":
                jump NPath3
return

################### Liam VS EMMA Part 4 Or Go you rown way part 3####################

label EPath3:
      "Emma's affection goes up."
      show Emma envy at emmaflip
      show Lila swirly eyes at left
      show Liam angry at right
      show Lila Sweats with dissolve
      show Lila pout with dissolve
      "I didn't say anything."
      "I just walked up to Emma and gave her a tight hug."
      show Emma shocked with dissolve
      show Liam shocked with dissolve
      show Liam surprised with dissolve
      show Emma blush with dissolve
      show Emma embarrassed with dissolve
      show Lila embarrassed with dissolve
      fa "W-What?!"

      show Emma nervous with dissolve
      show Emma panic with dissolve

      fa "What are you doing?"
      show Lila laugh with dissolve
      show Liam nervous with dissolve
      L "I don't know."
      show Lila embarrassed with dissolve
      show Emma surprised with dissolve
      L "Just felt like you need a hug."
      show Liam content with dissolve
      show Lila blush with dissolve
      show Emma nervous with dissolve
      show Emma panic with dissolve
      show Emma embarrassed with dissolve
      show Emma yell with dissolve
      fa "Get off me."
      show Liam nervous with dissolve
      show Emma nervous with dissolve
      show Emma embarrassed with dissolve
      show Lila embarrassed with dissolve
      L "No."
      show Lila nervous with dissolve
      show Liam surprised with dissolve
      L "I want to stick with you."
      show Emma panic with dissolve
      show Emma nervous with dissolve
      fa "What are you? A kid?"
      "Emma says still trying to push me away."
      show Lila pout with dissolve
      show Liam laugh with dissolve
      show Emma blush with dissolve
      show Emma embarrassed with dissolve

      fb "Look at you guys!"
      show Liam happy with dissolve
      show Lila surprised with dissolve
      show Emma surprised with dissolve
      fb "Being so cute."
      show Liam content with dissolve
      show Emma embarrassed with dissolve
      show Lila Sweats with dissolve
      show Lila blush with dissolve

      fa "C-cut-cu."
      show Emma nervous with dissolve
      show Emma panic with dissolve
      show Emma embarrassed with dissolve
      show Emma blush with dissolve
      show Liam surprised with dissolve
      show Liam smug with dissolve
      show Liam smirk with dissolve
      "Emma doesn't seem to know what to say."
      show Lila stunned with dissolve
      show Lila happy with dissolve
      show Liam happy with dissolve
      fb "Looks like it's decided!"
      show Lila surprised with dissolve
      show Emma surprised at yflip with dissolve
      show Liam wink with dissolve
      fb "You guys should go hide together."
      show Emma shocked with dissolve
      fa "What?!"
      show Liam surprised with dissolve
      show Emma panic with dissolve
      show Emma envy with dissolve
      fa "Who said I want to hide wi-"
      show Liam nervous with dissolve
      show Emma nervous at emmaflip with dissolve
      "Emma looks at me."
      show Lila stunned with dissolve
      show Liam surprised with dissolve
      "I look back."
      show Emma panic with dissolve
      "She stares at me for a bit."
      show Emma blush with dissolve
      show Emma nervous with dissolve
      show Liam smug with dissolve
      show Liam smirk with dissolve
      show Emma sigh with dissolve
      show Emma concern with dissolve
      show Liam happy with dissolve
      show Emma dissapointed with dissolve
      fa "Come on let's go."
      show Emma envy with dissolve
      show Lila surprised with dissolve
      "She said as she dragged me away from Liam."
      show Liam content with dissolve
      fb "Have fun!"
      "Liam shouts."
      show Emma blush with dissolve
      show Emma envy with dissolve
      fa "Shut up and start counting!"
      "Emma shouts back."

      hide Liam content with fade
      hide Emma envy with dissolve
      hide Lila surprised with dissolve
      scene image "Twopaths.png" with fade
      #"Soon we came across two branching paths."
      "Soon we hit an dead end."
      "What's ahead of us is a cave."
      #"To the left is a cave and to the right is a Den."

      fa "What should we do?"
      "Emma asks."
      menu:
          "Observe the place?":
                jump O2
          #"Go to Den.":
                #jump Den2
          "Go to Cave.":
                jump Cave2
          "Sit and wait.":
                jump SaW3
return

#######################Place Obseveration 3##########################

label LPath3:
    "Emma's affection goes up. Liam's affection goes up."
    show Emma envy at middle
    show Lila swirly eyes at left
    show Liam angry at right
    show Lila pout with dissolve
    "I puffed my chest and walked up to Liam."
    show Emma surprised at emmaflip with dissolve
    show Liam surprised with dissolve
    "I grabbed his hand as his eyes widened."
    show Emma shocked with dissolve
    show Emma envy with dissolve
    show Liam shocked with dissolve
    fb "Uh..."
    show Liam blush with dissolve
    show Liam embarrassed with dissolve
    fb "Lila? W-W-What a-are-"
    show Lila Sweats with dissolve
    "Liam's face is bright red but before he can finish his sentence Emma shouts."

    fa "WHAT ARE YOU DOING?"
    show Lila surprised with dissolve
    show Liam shocked with dissolve
    show Liam panic with dissolve
    show Liam nervous with dissolve
    show Emma blush with dissolve
    show Emma angry with dissolve
    "Her face is also bright red but she looks pissed."
    show Emma yell with dissolve
    fa "Take your han-"
    show Lila pout with dissolve
    show Lila blush with dissolve
    show Liam shocked with dissolve
    show Emma shocked with dissolve
    "I grab her hand next and put it on top of Liam's."
    "The red on their faces fade."
    show Emma surprised with dissolve
    show Liam surprised with dissolve
    "They both look at me weridly."
    show Lila pout with dissolve
    L "Let's stop playing..."
    show Lila happy with dissolve
    L "Let's go exploring instead!"
    show Emma nervous with dissolve
    show Liam nervous with dissolve
    fa "What?"

    "I take them into the forest with me."
    show Emma surprised with dissolve
    show Liam surprised with dissolve
    fa "But why?"
    show Liam skeptical with dissolve
    "Liam stays quiet."
    show Lila embarrassed with dissolve
    L "I just felt like it."
    show Lila Sweats with dissolve
    show Liam surprised with dissolve
    L "I didn't like how you guys were acting."
    show Liam embarrassed with dissolve
    show Emma embarrassed with dissolve
    "Emma and Liam looked at each other."
    show Liam nervous with dissolve
    show Liam smile with dissolve
    show Liam happy with dissolve
    show Emma nervous with dissolve
    show Emma smile with dissolve
    show Emma happy with dissolve
    "After a while they start to laugh."
    show Lila stunned with dissolve
    L "What's so funny?"
    hide Liam happy with dissolve
    hide Emma happy with dissolve
    hide Lila stunned with dissolve
    scene image "Twopaths.png" with fade
    "The two don't say anything."
    "They laughed until we noticed we are lost."

    #"They laugh until we reach two branching paths."
    #"At this point I've stopped questioning them."
    #"Instead I focus on the path before me."
    #"Which way should I go?"
    "All I see is a cave."
    "Hmmm."
    "It's too early to go back."
    menu:
          "Observe the place?":
                jump O3
          #"Go to Den.":
                #jump Den3
          "Go to Cave.":
                jump Cave3
return

#######################Place Obseveration 4##########################

label NPath2:
    "Emma's affection goes down. Liam's affection goes down."
    show Emma envy at middle
    show Lila swirly eyes at left
    show Liam angry at right
    hide Lila swirly eyes at left
    show Lilasad at left
    "I do not like how the two of them are acting."
    "So while they were busy doing that I decided to wonder on my own."
    hide Emma envy with dissolve
    hide Liam angry with dissolve
    hide Lilasad at left with dissolve
    show Lilasad at middle with dissolve
    "I think it's best to give them so space."
    "I'll come back after they have cooled down."
    hide Lilasad at middle with fade
    scene image "Twopaths.png" with fade
    "Not paying attention to where I was going."
    "I got lost."

    L "Uh oh..."

    "I have no clue where to go from here."
    menu:
          "Observe the place?":
                jump O1
          #"Go to Den.":
               #jump Den1
          "Go to Cave.":
                jump Cave1
          "Sit and wait.":
                jump SaW1
return

label EPath4:
    "Emma's affection goes up."
    show Lila Sweats at left
    show Liam smile at right
    show Lila nervous with dissolve
    L "I'm going!"
    hide Liam smile with dissolve
    hide Lila nervous with dissolve
    scene image "Twopaths.png" with fade
    "I shouted to Liam but my goal is actually to find Emma."
    "I couldn't wait around to see Liam's reaction and just ran for it."
    "After running for a while I noticed I was lost."
    "I have no clue what to do from here."
    menu:
          "Observe the place?":
                jump O1
          #"Go to Den.":
               #jump Den1
          "Go to Cave.":
                jump Cave1
return

label LPath4:
    "Liam's affection goes up. Emma's affection goes down."
    show Lila Sweats at left
    show Liam smile at right
    show Lilasad at left
    "I don't think Emma will answer me if I asked her."
    "I'll ask just ask Liam."
    L "I have a question Liam."
    show Liam surprised with dissolve
    fb "Hm?"
    show Liam nervous with dissolve
    fb "About the game?"
    L "No..."
    L "It's about Emma."
    show Liam surprised with dissolve
    show Liam nervous with dissolve
    fb "Emma?"
    L "Yeah."
    L "Why does she talk to me that way?"
    fb "What way?"
    hide Lilasad at right
    show Lila nervous at left
    L "I don't know."
    hide Lila nervous at left
    show Lilasad at left
    show Liam surprised with dissolve
    L "It's hard to explain it."
    show Liam nervous with dissolve
    show Liam sigh with dissolve
    fb "I think you're overthinking again."
    show Liam nervous with dissolve
    show Liam smile with dissolve
    fb "It's ok not to think about it.."
    hide Lilasad at left
    show Lila nervous at left with dissolve
    L "I guess so..."
    show Lila eyes closed sad with dissolve
    "I guess even Liam doesn't know."
    show Lila swirly eyes with dissolve
    show Lila Sweats with dissolve
    show Lila happy with dissolve
    L "Thanks for talking to me!"
    show Liam blush with dissolve
    show Liam nervous with dissolve
    L "I'll go hide now!"
    show Lila smile with dissolve
    "I said running away."
    show Liam smile with dissolve
    fb "Have fun and don't get lost!"
    show Liam nervous with dissolve
    show Lila happy with dissolve
    L "Got it!"
    hide Liam nervous with dissolve
    hide Lila happy with dissolve
    scene image "Twopaths.png" with fade
    "He sounded a bit worried...."
    "But for a good reason."
    L "He just said not to..."
    "It seems I'm lost..."
    "But I do see a cave I've never been to before."
    menu:
          "Observe the place?":
                jump O1
          #"Go to Den.":
               #jump Den2
          "Go to Cave.":
                jump Cave1
return

label NPath3:
    show Lila Sweats at left
    hide Liam smile with dissolve
    hide Lila Sweats at left with dissolve
    show Lilasad at middle with dissolve
    "I think I'm overthinking again."
    "As I heard Liam's coutdown I started to run."
    hide Lilasad at middle with dissolve
    scene image "Twopaths.png" with fade
    "Before I know it I hit a dead end."
    "Where is this?"
    "There seems to be this cave I've never seen before..."
    menu:
          "Observe the place?":
                jump O1
          #"Go to Den.":
               #jump Den2
          "Go to Cave.":
                jump Cave1

#######################Place Obseveration 5##########################

#Calling Emma Childish result:
label O1:
    "Which place do you want to Observe first?"
    menu:
        "Cave.":
                jump OC1
        #"Den.":
                #jump OD1
return

label OC1:
    "What would you like to check out first?"
label menu_OC1:
    menu:
        "Sight." if C_Sight1 == True:
                jump Sight1

        "Smell." if C_Smell1 == True:
                jump Smell1

        "Feel." if C_Feel1 == True:
                jump Feel1

        "Sound." if C_Sound1 == True:
                jump Sound1

        #"Observe the Den.":
                #jump OD1

        "Go to Cave.":
                jump Cave1
return

#######################Place Sense Observation 1 ##########################

label Sight1:
    "The cave is a bit too far to see the details up close but from this distance you can definitely see how spacious it is."
    "Besides that only the crystals surrounding the cave stood out."

    $C_Sight1 = False
jump menu_OC1
return

label Smell1:
    "There's nothing but the scent of the fresh grass."

    $C_Smell1 = False
jump menu_OC1
return

label Feel1:
    "Just thinking about the atmosphere within the cave sent a shiver down Lila's spin."
    "It just felt dark, gloomy, and a bit creepy."

    $C_Feel1 = False
jump menu_OC1
return

label Sound1:
    "The only sounds heard are from the insects nearby."

    $C_Sound1 = False
jump menu_OC1

######Start Of Cave Exploring(Emma and Liam Bad terms)#########
label Cave1:
    scene image "Cave.png" with dissolve
    hide Emma pout
    hide Liam nervous
    show Lila surprised at middle with dissolve
    L "Oh..."
    L "Looks like there's alot stuff in the cave that I've never seen before."
    hide Lila surprised at middle
    show Lilasad at middle
    L "I guess I can explore for a bit..."
    "I'm curious about finding new things."
    "But what happened to me and my friends still bothers me."
    hide Lilasad at middle
    "Drag the magnifying glass to the objects you wish to interact with."

label drag_glass:
    call screen slide_glass_screen
    scene image "Cave.png"
    hide image "CloseupOpus.png"
    hide image "CloseupVine.png"
    hide image "CloseupPageCave.png"
    hide image "Opus1.png"
    hide image "Opus2.png"
    hide image "VinaPlant.png"
    "[glass] picked the [object]. Do you want to take a closer look at the object?"
    window hide
    menu:
        "Observe the crystal?" if store.object == "Crystal":
            jump Crystal1
        "Observe the vine?" if store.object == "Vine":
            jump Vine1
        "Observe the Opus?" if store.object == "Opus":
            jump Opus1
        "Observe the page?" if store.object == "Page?":
            jump Page1
        "Go Back":
            jump drag_glass
        "Done Exploring." if MPath1 == True:
            jump NextStory
return
window show
#######Object Drag 1############
######Start of Crystal 1#########

label Crystal1:
    scene image "CloseupCrystal.png"
    $MPath1Points.value += 1
    "The crystal glows brightly within the dark cave."
    "It's edges glistens just like Liam's pocket knife."
    "Even so there seems to be more to the crystal."
label menu_Crystal1:
    menu:
        "Touch it." if Crystal_TouchNormal == True:
                jump TouchNormal
        "Touch it." if Crystal_TouchAfterTaste == True:
                jump TouchAfterTaste
        "Listen to it." if Crystal_Listen1 == True:
                jump Listen1
        "Taste it." if Crystal_TasteNormal == True:
                jump TasteNormal
        "Taste it." if Crystal_TasteAfterTouch == True:
                jump TasteAfterTouch
        "Smell it." if Crystal_SmellNormal == True:
                jump SmellNormal
        "Smell it." if Crystal_SmellAfterTaste  == True:
                jump SmellAfterTaste
        "Don't do anything.":
                jump drag_glass
return

label TouchNormal:
    "I reached out my hand and rubbed the edge of the crystal."
    "Like the it's cold touch I felt a sharp pain through the tips of my finger."
    "Looking at the cut on my finger I felt my entire body freeze."
    "That was a very bad idea..."
    scene image "CloseupCrystalBlood.png" with fade
    $Crystal_TouchNormal = False
    $TouchBleed.value += 1
    $Touch_Points.value += 1

    if Touch_Points.value >= 1:
        $Crystal_TasteAfterTouch = True
        $Crystal_TasteNormal = False
        $Crystal_TouchNormal = False
    jump menu_Crystal1
return

label TouchAfterTaste:
    scene image "CloseupCrystalBlood.png" with fade
    "As my hands reached out to the crystal I felt a sharp pain in my mouth."
    "There is an awful feeling in my stomach."
    "I don't feel like touching the crystal."
    $Crystal_TouchAfterTaste = False
    menu:
        "Touch it anyways.":
                jump yes1
        "Don't touch it.":
                jump no1
return

label yes1:
    scene image "CloseupCrystalBlood.png" with fade
    "I reached out to touch the edge of the crystal."
    "Like the it's cold touch I felt a sharp pain through the tips of my finger."
    "This is the worst."
    "I can't talk and now my finger hurts."
    $TouchBleed.value += 1
    jump menu_Crystal1

label no1:
    "I pulled my hand back with relief."
    jump menu_Crystal1

label Listen1:
    "I put my ears near the crystal."
    "It didn't make any sounds."
    $Crystal_Listen1 = False
jump menu_Crystal1
return

label TasteNormal:
    play sound CrunchCrys volume 0.5
    "I tried to bite the crystal but the minute my tongue touched it I felt a sharp pain."
    "There was a taste of iron in my mouth."
    "It seems like there's a warm liquid dripping."
    scene image "CloseupCrystalBlood.png" with fade
    $Crystal_TasteNormal = False
    $TasteBleed.value += 1
    $Taste_Points.value += 1
    if Taste_Points.value >= 1:
        $Crystal_SmellAfterTaste  = True
        $Crystal_TouchAfterTaste = True
        $Crystal_TasteNormal = False
        $Crystal_TouchNormal = False
        $Crystal_SmellNormal = False
    jump menu_Crystal1

label TasteAfterTouch:
    scene image "CloseupCrystalBlood.png" with fade
    "I was about to bite the crystal but there was this sudden sting on my finger."
    "I thought to myself of a moment."
    "Is this really a good idea?"
    $Crystal_TasteAfterTouch = False

    menu:
        "Bite it anyways.":
                jump yes2
        "Don't bite it.":
                jump no2
return

label yes2:
     play sound CrunchCrys volume 0.5
     "I bite into the crystal."
     "I felt it slice my tongue."
     "I quickly pulled back."

     L "Ow-"

     "When I open my mouth I felt the pain again."
     "I think it's best to not talk for now."
     scene image "CloseupCrystalBlood.png" with fade
     $TasteBleed.value += 1
     $Taste_Points.value += 1
     if Taste_Points.value >= 1:
        $Crystal_SmellAfterTaste = True
        $Crystal_SmellNormal = False
        $Crystal_TasteNormal = False
jump menu_Crystal1

label no2:
    "I sighed with relief."
jump menu_Crystal1

label SmellNormal:
    scene image "CloseupCrystal.png" with fade
    "My nose barely touched the edge of the crystal."
    "I sniffed it."
    "It smells like nothing."
    $Crystal_SmellNormal = False
jump menu_Crystal1
return

label SmellAfterTaste :
    scene image "CloseupCrystalBlood.png" with fade
    "My nose barely touched the edge of the crystal."
    "I sniffed it."
    "There was a rotten smell of iron."
    $Crystal_SmellAfterTaste  = False
jump menu_Crystal1
return

#######Start of Vine 1###########

label Vine1:
    "This is werid."
    "Do plants grow in caves?"
    "It also glowing a healthy color."
    $MPath1Points.value += 1
label menu_Vine1:
    if TouchBleed.value >= 1:
        $Vine_TouchBleed = True
        $Vine_NormalTouch = False
    if TasteBleed.value >= 1:
        $Vine_NormalBite = False
        $Vine_BiteBleed = True
        $Vine_BiteWithEyes = False
    menu:
        "Touch it." if Vine_NormalTouch == True:
                jump TouchVineNormal
        "Touch it." if Vine_TouchBleed == True:
                jump TouchVineBleed
        "Touch it." if Vine_TouchWithEyes == True:
                jump TouchVineWithEyes
        "Smell it." if Vine_SmellNormal == True:
                jump SmellVineNormal
        "Smell it." if Vine_SmellWithEyes == True:
                jump SmellVineWithEyes
        "Bite it." if Vine_NormalBite == True:
                jump BiteVineNormal
        "Bite it." if Vine_BiteWithEyes == True:
                jump BiteVineWithEyes
        "Bite it." if Vine_BiteBleed == True:
                jump BiteVineWithBlood
        "Listen to it." if Vine_ListenVine == True:
                jump ListenVine
        "Listen to it." if Vine_ListenAfterTouch == True:
                jump ListenOpusAfterTouch
        "Don't do anything.":
                jump drag_glass
return

label TouchVineNormal:
    scene image "CloseupVine.png" with fade
    "I poked the Vine."
    "It sways back and forth."
    "Then it starts to shake."
    scene image "VinaPlant.png" with fade
    "After a while alot of eyes appeared."
    "All of them were staring at me."
    "I felt scared even after the eyes all closed again."
    scene image "CloseupVine.png" with fade
    $Vine_NormalTouch = False
    $Vine_NormalBite = False
    $VineTouchPoints.value += 1
    if VineTouchPoints.value >= 1:
        $Vine_TouchWithEyes = False
        $Vine_SmellWithEyes = True
        $Vine_SmellNormal = False
        $Vine_BiteWithEyes = True
        #$Vine_NormalBite = False
    jump menu_Vine1

label TouchVineBleed:
     scene image "CloseupVine.png" with fade
     "I poked the Vine."
     "The blood on my hands stained it's green color."
     "It sways back and forth."
     "Then it starts to shake."
     "After a while alot of eyes appeared."
     scene image "VinaPlant.png" with fade
     "All of them were staring at me."
     "The blood that was on it got sucked in by the vine."
     "I felt scared."
     "There was an urge to run."
     "Yet when I turned around to leave I fall flat on my face."
     scene image "VinaPlantDeath.png" with fade
     "Vines with eyes have wrapped around on my leg."
     "The only thing I remember seeing was the large mouth that has appeared."
     scene image "black.png" with fade
     "{cps=2}...{/cps}"
     "{cps=2}...{/cps}"
     "Lila's route ends"
     "No pages found."
return

label TouchVineWithEyes:
    $Vine_TouchWithEyes = False
    "I didn't like the way it was looking at me."
    "It looks like it watching my every move."
    "Do I still want to touch it?"
    menu:
        "Yes.":
            jump VineYes1
        "No.":
            jump VineNo1
return

label VineYes1:
    scene image "CloseupVine.png" with fade
    L "Dear god..."
    "I prayed and poked the vine."
    scene image "VinaPlant.png" with fade
    "It started to shake again even harder this time."
    "I close my eyes and felt myself shake."
    scene image "black.png" with fade
    "{cps=2}...{/cps}"
    "{cps=2}...{/cps}"
    "Nothing happened."
    scene image "VinaPlant.png" with fade
    "When I open my eyes again I felt like I was being mocked by the eyes."
    "I frowned after the eyes disappeared."
    scene image "CloseupVine.png" with fade
    $VineTouchPoints.value += 1
    if VineTouchPoints.value >=1:
        $Vine_SmellNormal = False
        $Vine_BiteWithEye = True
        $Vine_NormalBite = False
    jump menu_Vine1
return

label VineNo1:
    $Vine_TouchWithEyes = False
    scene image "CloseupVine.png" with fade
    "I let out a breath of relief."
    jump menu_Vine1

label SmellVineNormal:
    $Vine_SmellNormal = False
    scene image "CloseupVine.png" with fade
    "I leaned in to smell the vine."
    "It smelled like fresh grass."
    jump menu_Vine1

label SmellVineWithEyes:
    $Vine_SmellWithEyes = False
    scene image "CloseupVine.png" with fade
    "I lean in to smell the vine."
    scene image "VinaPlant.png" with fade
    "But I stopped when I noticed eyes looking at me."
    "I felt a bit werid."
    "Do I still smell the vine?"
    menu:
        "Yes.":
                jump VineYes2
        "No.":
                jump VineNo2
return

label VineYes2:
    scene image "VinaPlant.png" with fade
    "I sniffed the vine."
    "It was a very sweet smell."
    "It made me feel hungry..."
    "Very hungry."
    scene image "CloseupVine.png" with fade
    jump menu_Vine1
return

label VineNo2:
    scene image "VinaPlant.png" with fade
    "I felt a sense of relief."
    scene image "CloseupVine.png" with fade
    jump menu_Vine1
return

label BiteVineNormal:
    $Vine_NormalBite = False
    $VineTastePoints.value += 1

    if VineTastePoints.value >= 1:
        $Vine_NormalTouch = False
        $Vine_TouchWithEyes = True
        $Vine_SmellNormal = False
        $Vine_SmellWithEyes = True
        $Vine_BiteBlood = False
    scene image "CloseupVine.png" with fade
    "I took a bite of the vine."
    "There was a fresh feeling in my mouth."
    "It didn't taste bad."
    "But it didn't take long for me to regret doing that."
    "I nearly choked on what I was chewing."
    scene image "VinaPlant.png" with fade
    "I saw a bunch of eyes on the vine staring at me."
    "Even after they closed back up I felt a chill down my spin."
    scene image "CloseupVine.png" with fade
    jump menu_Vine1
##Thisbroke##
label BiteVineWithEyes:
    $Vine_BiteWithEyes = False
    $VineTastePoints.value += 1

    if VineTastePoints.value >= 1:
        $Vine_NormalTouch = False
        $Vine_SmellNormal = False
    scene image "VinaPlant.png" with fade
    "I don't think what I'm doing is a good idea."
    "Have I ever eaten anything alive before??"
    "With it's eyes staring at me?"
    menu:
        "There's a first for everything.":
                jump Vine_Yes3
        "The smarter move is not to.":
                jump Vine_No3
return

label Vine_Yes3:
    scene image "VinaPlant.png" with fade
    "I gluped and took a bite of the vine."
    "Even though it tasted pretty good it was hard to shallow."
    "I felt it wiggle as it enters my mouth."
    "Besides feeling pretty grossed out nothing major happened..."
    scene image "CloseupVine.png" with fade
    jump menu_Vine1

label Vine_No3:
    scene image "VinaPlant.png" with fade
    "I felt a sense of relief."
    L "Huh?"
    "Is it just me or did the vine look upset..."
    "What was the word?"
    "Disappointed?"
    scene image "CloseupVine.png" with fade
    jump menu_Vine1
##break##
label BiteVineWithBlood:
    $Vine_BiteBleed = False
    scene image "CloseupVine.png" with fade
    "This gives me a unsettling feeling."
    "But I still bit into the vine."
    scene image "VinaPlant.png" with fade
    "The moment my mouth touched the vine a very sweet scent knocked my senses numb."
    "I felt the cuts inside my mouth painful yet I couldn't move."
    scene image "VinaPlantDeath.png" with fade
    "More like I didn't want too."
    "I felt unwanted tears flow down my eyes."
    scene image "black.png" with fade
    "The last thing I saw was a bunch of eyes staring down at me."
    "A gaint mouth opening before the tears over took my sight."
return

label ListenVine:
    $Vine_ListenVine = False
    scene image "CloseupVine.png" with fade
    "I leaned in close to listen."
    scene image "VinaPlant.png" with fade
    "There was this knot in my stomach when I heard werid noise coming from the vine."
    "It sounded like something wet was moving around."
    "I think I might just faint if I stay here any longer then I should."
    scene image "CloseupVine.png" with fade
    jump menu_Vine1
return

########Start of Opus 1###########
label Opus1:
    "There was this blob floating in the water."
    "It bobbles there cutely."
    "Yet staring into it's eyes made me feel werid."
    "I also don't like the color of it's skin."
    $MPath1Points.value += 1
label menu_Opus1:
     if TouchBleed.value >= 1:
        $Opus_TouchBleed = True
        $Opus_NormalTouch = False
        $Opus_NormalBite = False
        $Opus_BiteBleed = True
     if TasteBleed.value >= 1:
        $Opus_NormalBite = False
        $Opus_BiteBleed = True
     menu:
        "Touch it." if Opus_NormalTouch == True:
            jump TouchOpusNormal
        "Touch it." if Opus_TouchBleed == True:
            jump TouchOpusBlood
        "Smell it." if Opus_NormalSmell == True:
            jump SmellOpusNormal
        "Smell it." if Opus_SmellBleed == True:
            jump SmellOpusBlood
        "Bite it." if Opus_NormalBite == True:
            jump BiteOpusNormal
        "Bite it." if Opus_BiteBleed == True:
            jump BiteOpusBleed
        "Listen to it." if Opus_Listen == True:
            jump ListenOpusNormal
        "Listen to it." if Opus_ListenAfterTouch == True:
            jump ListenOpusAfterTouch
        "Don't do anything":
            jump drag_glass
return

label TouchOpusNormal:
    scene image "CloseupOpus.png" with fade
    "I poked the blob."
    "It felt slimy."
    scene image "Opus1.png" with fade
    "It's just contuines to bobble in the water."
    $Opus_NormalTouch = False
    $OpusTouchPoints.value += 1
    if OpusTouchPoints.value >= 1:
        $Opus_Listen = False
        $Opus_ListenAfterTouch = True
    jump menu_Opus1
return

label TouchOpusBlood:
    scene image "CloseupOpus.png" with fade
    "I wanted to poke the blob."
    scene image "Opus2.png" with fade
    "But I just notice... another eye has appeared on the blob."
    "It was just staring at the cut on my finger."
    "I felt a bit scared."
    menu:
        "Touch it anways.":
            jump OpusYes1
        "Don't touch it.":
            jump OpusNo1
return

label OpusYes1:
    scene image "Opus2.png" with fade
    "I felt a wave of nerves as my hand touched the blob."
    scene image "black.png" with fade
    "Before I know it my hand was no longer in sight."
    "The last thing I saw before everything faded to black..."
    "Was a gaint mouth soaked in the color red."
    "Lila route end."
    "No pages found."
return

label OpusNo1:
    scene image "Opus2.png" with fade
    "I pulled my hand back in relief."
    scene image "CloseupOpus.png" with fade
    "The eyeball on the blob that was staring at me was no longer there."
    L "Ew."
    "I shiver at how gross it was."
    jump menu_Opus1
return

label SmellOpusNormal:
    $Opus_NormalSmell = False
    scene image "CloseupOpus.png" with fade
    "I leaned in close to smell the blob."
    "It kind of reminds me of the sea."
    "Fresh and salty."
    jump menu_Opus1
return

label SmellOpusBlood:
    $Opus_SmellBleed = False
    scene image "CloseupOpus.png" with fade
    "I leaned in close to smell the blob."
    "A drop of the blood from my mouth dripped onto the blob."
    "It started to shake and I felt my legs gave in."
    "I don't care about how it smells like."
    scene image "Opus2.png" with fade
    "I stared at it's third eye and gaint mouth."
    scene image "black.png" with fade
    "I wanted to scream but the pain in my mouth stop me from doing so."
    "Pain was all I remember when it dragged me into the water."
    jump menu_Opus1
return

label BiteOpusNormal:
    $Opus_Normalbite = False
    scene image "CloseupOpus.png" with fade
    "I was feeling a bit hungry."
    "I stared at the Blob that seemed harmless."
    "Won't hurt if I took a bit right?"
    "I leaned in to take a bite."
    scene image "black.png" with fade
    "Before my mouth can touch the blob I lost all of my senses."
    "The only thing I felt was pain."
    "Lila route end."
    "No pages found."
return

label BiteOpusBleed:
    $Opus_BiteBleed = False
    scene image "CloseupOpus.png" with fade
    "I was going to lean in to bite the blob."
    "Yet when I opened my mouth I felt a sharp pain and pulled back."
    "Seems like the inside of my mouth is really hurt."
    L "?"
    scene image "Opus2.png" with fade
    "After pulling myself together from the pain I saw a third eye appear on the blob."
    "Did it always have a third eye?"
    menu:
        "Try biting it again.":
                jump OpusYes2
        "This is a bad idea.":
                jump OpusNo2
    jump menu_Opus1
return

label OpusYes2:
    scene image "black.png" with fade
    "I leaned in to bite the blob even with the pain in my mouth."
    "Before my mouth can touch the blob I lost all of my sense."
    "The only thing I felt was pain."
    "Lila route end."
    "No pages found."
return

label OpusNo2:
    scene image "CloseupOpus.png" with fade
    "I quickly leaned back from the blob."
    "I felt a wave of relief."
    jump menu_Opus1
return

label ListenOpusNormal:
    $Opus_Listen = False
    scene image "CloseupOpus.png" with fade
    "I listened to the blob."
    "I think I'm hearing some kind of bubble?"
    "Maybe soft popping sounds?"
    jump menu_Opus1
return

label ListenOpusAfterTouch:
    $Opus_ListenAfterTouch = False
    scene image "CloseupOpus.png" with fade
    "I listened to the blob."
    "There was a gruggling sounds."
    "I sounds just like me...hungry."
    jump menu_Opus1
return

##########START OF PAGE 1#########
label Page1:
    "A piece of old crumpled paper sits in the corner."
    "Nothing about it really stood out."
    "The only thing that was not normal was the amount of mushroom around it."
    $MPath1Points.value += 1
label menu_Page1:
    if TouchBleed.value >= 1:
        $Page_TouchBleed = True
        $Page_TouchNormal = False
    if TasteBleed.value >= 1:
        $Page_NormalBite = False
        $Page_BiteBleed = True
    menu:
        "Pick up Page" if Page_TouchNormal == True:
            jump PageFound1
        "Pick up Page" if Page_TouchBleed == True:
            jump TouchPageBleed
        #"Pick up paper" Make Minglou appear
        "Explore some more.":
            jump drag_glass
return

label PageFound1:
    $Page_TouchNormal = False
    scene image "CloseupPageCave.png" with fade
    "It felt just like paper."
    "But it wasn't smooth."
    scene image "Cave.png" with fade
    show Lila skeptical at right with dissolve
    L "What's so special about this paper?"
    Q "It's more significant then you."
    show Lila shocked with dissolve
    Q "That's for sure."
    show Lila swirly eyes with dissolve
    "HUH?"
    "I jumped when I heard a voice."
    "I when I turned around I found out it was from my spirit."
    show Lila surprised at flip with dissolve
    show Lila yell with dissolve
    L "MINGLOU!"
    show Lila swirly eyes with dissolve
    show Mingluo smirk at MingLouFlip with dissolve
    L "You came out again without my spiritual energy."
    show Mingluo default at MingLouFlip with dissolve
    m "I'm surprised you even know what that means."
    show Lila pout with dissolve
    L "I'm not that dumb."
    show Mingluo annoyed with dissolve
    m "At least you are aware of that."
    show Lila swirly eyes with dissolve
    show Lila Sweats with dissolve
    "I was speachless."
    show Mingluo sigh with dissolve
    m "Anyways"
    show Lila surprised with dissolve
    show Mingluo skeptical with dissolve
    m "what are you doing here by yourself?"
    show Mingluo disgust with dissolve
    show Lila Sweats with dissolve
    m "You usually stick to those two unbearably suffocating brats."
    L "I-"
    show Lila swirly eyes with dissolve
    show Lila embarrassed with dissolve
    show Lila Sweats with dissolve
    show Lila eyes closed sad with dissolve
    "I didn't want to tell her about my fight with my friends."
    m "I guess you don't want to tell me."
    show Mingluo annoyed with dissolve
    show Lila Sweats with dissolve
    L "It's not like that."
    L "I-"
    show Lila eyes closed sad with dissolve
    show Mingluo sigh with dissolve
    m "Well it's not my concern."
    show Lila surprised with dissolve
    show Lila pout with dissolve
    "Then why did she ask?"
    show Mingluo smirk with dissolve
    m "I'm more interested in that treasure you're holding."
    show Lila surprised with dissolve
    show Mingluo annoyed with dissolve
    L "What?"
    show Mingluo sigh with dissolve
    "She pointed to the page."
    show Lila swirly eyes with dissolve
    L "This???"
    show Mingluo smirk with dissolve
    m "That's right."
    show Mingluo evil with dissolve
    m "'This'."
    show Lila Sweats with dissolve
    "She said as she takes the paper from my hands."
    hide Lila Sweats with dissolve
    hide Mingluoevil with dissolve
    #####NOTE TO AMBER THIS IMAGE IS TOO BIG##############
    scene image "MingluoBurnCG.png" with fade
    window hide
    pause
    window show
    L "What can be interesting about this?"
    m "Hmmmm I do wonder..."
    L "Can't you just tell me?"
    m "Nope."
    L "Then what should I do with it?"
    m "Think about it yourself."
    "She said as she gave the paper back to me."
    scene image "Cave.png" with fade
    show Lila Sweats at middle with dissolve
    L "Huh?"
    show Lila surprised with dissolve
    L "But how-"
    show Lila pout with dissolve
    "Before I can even question she was gone again."
    L "I hate it when she leaves me off like this."
    hide Lila pout with dissolve
    scene image "black.png" with fade
    "I guess I'll just ask Liam..."
    "Will he even want to tell me?"
    "Either way it's better then staying here wondering all day..."
    "I hope there's some kind of meaning to this paper."
    "Otherwise I feel like I just wasted my energy."
    "I sighed at the thought of it being useless."
    "Lila's route end."
    "Page 1 found"
return

label TouchPageBleed:
    $Page_TouchBleed = False
    scene image "CloseupPageCave.png" with fade
    "I was about to pick up the paper but a forced pulled my hand back."
    scene image "Cave.png" with fade
    show Lila skeptical at right with dissolve
    Q "Don't You Dare Touch That!"
    show Lila panic with dissolve
    L "Ouch!"
    show Lila pain with dissolve
    "They pulled my hand back with such force that it hurts."
    show Lila Sweats with dissolve
    "I turned to see Minglou with a very scary face expression."
    show Mingluo pyscho at MingLouFlip with dissolve
    "I shivered as she lets go of me and grabs the paper like an animal."
    show Lila shocked at flip with dissolve
    L "Minglou????"
    "What is she doing here?"
    show Lila Sweats with dissolve
    "She didn't even pay attention to me and only focuses on the paper."
    L "H-hey..."
    L "What are you doing?"
    show Mingluo nervous with dissolve
    show Mingluo angry with dissolve
    show Mingluo rage with dissolve
    "I asked as she glared at me."
    m "Nothing..."
    show Lila surprised with dissolve
    show Lila Sweats with dissolve
    "That did not look like nothing..."
    "After she checked the over until she's satisfied she picked it up."
    show Mingluo angry with dissolve
    m "You are not touching this sacrad treasure with those filthy hands."
    show Lila surprised with dissolve
    L "Huh?"
    "I was so confused by her action and words."
    show Lila nervous with dissolve
    L "I won't touch it if you tell me not too..."
    show Mingluo skeptical with dissolve
    "She looks at me with doubt."
    show Lila Sweats with dissolve
    "But she sighs after a long silence between us."
    show Mingluo sigh with dissolve
    m "Listen closely Lila."
    show Mingluo default with dissolve
    L "Yeah?"
    show Lila skeptical with dissolve
    "I asked trying to break this tension."
    show Mingluo nervous with dissolve
    m "I need you to go to the village to heal up-"
    show Mingluo annoyed with dissolve
    L "Are you worried for me?!"
    show Lila happy with dissolve
    "I asked in excitement."
    show Mingluo nervous with dissolve
    "Despite being with me since I was a kid"
    "She's never been worried about me before."
    "This is a first."
    show Mingluo skeptical with dissolve
    show Mingluo nervous with dissolve
    show Mingluo laugh with dissolve
    m "Uh- Y-Yeah I'm worried."
    show Mingluo skeptical with dissolve
    m "So get cleaned up and come find me ok?"
    L "Ok!"
    show Lila smile with dissolve
    L "Wait for me I'll be right back!"
    show Mingluo nervous with dissolve
    "I shouted and headed back to the village."
    hide Mingluo nervous with dissolve
    hide Lila smile with dissolve
    scene image "black.png" with fade
    "Wait..."
    "She wanted to me to find her afterwards but why?"
    "Oh well."
    "Either way I'll think about it later."
    "Let's get cleaned up first and then go find her."
    "Lila's route end."
    "Page 1 found."
    "Meanwhile..."
    scene image "Cave.png" with fade
    show Mingluo nervous at middle with dissolve
    show Mingluo sigh with  dissolve
    show Mingluo evil with dissolve
    m "Dumb kid."
return

##########End Cave Explore Herself############
##########Start MingLou's Apparence 1##########
#Nothing for Minglou yet
#Sticking with emma when there's danger

label O2:
    "Which place should we Observe first?"
    menu:
        "Cave.":
                jump OC2
        #"Den.":
                #jump OD2
return

label OC2:
    "What would you like to check out first?"
label menu_OC2:
    menu:
        "Sight." if C_Sight1 == True:
                jump Sight2

        "Smell." if C_Smell1 == True:
                jump Smell2

        "Feel." if C_Feel1 == True:
                jump Feel2

        "Sound." if C_Sound1 == True:
                jump Sound2

        #"Observe the Den.":
                #jump OD2

        "Go to Cave.":
                jump Cave2
return

#######################Place Sense Observation 2##########################

label Sight2:
    show Lila stunned at left with dissolve
    show Emma default at emmaflip with dissolve
    show Emma default at right with dissolve
    L "Hmmmm."
    L "I can't really see much from here."
    show Emma dissapointed with dissolve
    fa "Not sure what's there to see."
    fa "Looks like a normal cave to me."
    fa "Wait..."
    show Emma nervous with dissolve
    fa "I guess the amount of crystals formulated is a bit werid."
    hide Emma nervous with dissolve
    hide Lila stunned at left with dissolve
    $C_Sight1 = False
jump menu_OC2
return

label Smell2:
    show Lila stunned at left with dissolve
    show Emma default at emmaflip with dissolve
    show Emma default at right with dissolve
    L "Do you smell anything but fresh grass?"
    show Emma sigh with dissolve
    fa "Nope."
    hide Lila stunned at left with dissolve
    hide Emma sigh with dissolve
    $C_Smell1 = False
jump menu_OC2
return

label Feel2:
    show Lila stunned at left with dissolve
    show Lila nervous with dissolve
    show Emma default at emmaflip with dissolve
    show Emma default at right with dissolve
    L "I don't like this feeling."
    show Emma concern with dissolve
    fa "What feeling?"
    show Lila surprised with dissolve
    L "You don't feel it?"
    show Lila nervous with dissolve
    L "Something about this cave is very werid."
    show Emma pout with dissolve
    fa "I have no clue what you are on about."
    "I guess it's just me."
    hide Lila nervous with dissolve
    hide Emma pout with dissolve
    $C_Feel1 = False
jump menu_OC2
return

label Sound2:
    "I don't hear anything but insects."

    $C_Sound1 = False
jump menu_OC2

######Start Of Cave Exploring(With Emma)#########
label Cave2:
    scene image "Cave.png" with dissolve
    hide Emma pout
    hide Liam nervous
    show Emma surprised at right with dissolve
    show Lila happy at left with dissolve
    L "Oh wow!"
    L "There's a ton of stuff in here I've never seen before."
    L "Let's explore of a bit."
    show Emma concern at emmaflip with dissolve
    fa "There's no way I'm letting you get touchy in this cave."
    fa "Thank god I came here with you."
    show Lila surprised with dissolve
    L "huh?"
    show Lila Sweats with dissolve
    fa "Nothing..."
    show Emma dissapointed with dissolve
    fa "Just explore no worries."
    show Lila stunned with dissolve
    L "Oh ok..."
    "Well since Emma said so I might as well."
    hide Emma dissapointed with dissolve
    hide Lila stunned with dissolve
    "Drag the magnifying glass to the objects you wish to interact with."

label drag_glass2:
    call screen slide_glass_screen
    scene image "Cave.png"
    hide image "CloseupOpus.png"
    hide image "CloseupVine.png"
    hide image "CloseupPageCave.png"
    hide image "Opus1.png"
    hide image "Opus2.png"
    hide image "VinaPlant.png"
    "[glass] picked the [object]. Do you want to take a closer look at the object?"

    menu:
        "Observe the crystal?" if store.object == "Crystal":
            jump Crystal2
        "Observe the vine?" if store.object == "Vine":
            jump Vine2
        "Observe the Opus?" if store.object == "Opus":
            jump Opus2
        "Observe the page?" if store.object == "Page?":
            jump Page2
        "Go Back":
            jump drag_glass2
        "Done Exploring." if EaMpath1 == True:
            jump NextStory2
return

#######Start of Crystal 2###########

label Crystal2:
    scene image "CloseupCrystal.png" with fade
    L "Oh my god Emma!"
    fa "What?"
    L "Look at how pretty this crystal is."
    fa "Yeah..."
    fa "Pretty sharp."
    L "Huh?"
    "I looked closer at the crystal."
    "It does remind me of Liam's pocket knife."
    $EaMpath1Points.value += 1

label menu_Crystal2:
    menu:
        "Touch it." if Crystal_TouchNormal == True:
                jump TouchNormal2
        "Touch it." if Crystal2_TasteStopped == True:
                jump CrystalTasteStopped
        "Listen to it." if Crystal_Listen1 == True:
                jump Listen2
        "Taste it." if Crystal_TasteNormal == True:
                jump TasteNormal2
        "Taste it." if Crystal2_TouchBleed == True:
                jump TasteAfterTouchBleed
        "Taste it" if Crystal2_TouchStopped == True:
                jump CrystalTouchStopped
        "Smell it." if Crystal_SmellNormal == True:
                jump SmellNormal2
        "Smell it." if Crystal2_SmellAfterTouch  == True:
                jump SmellAfterTouch2
        "Don't do anything.":
                jump drag_glass2
return

label TouchNormal2:
    $Crystal_TouchNormal = False
    scene image "Cave.png" with fade
    show Emma shocked at emmaflip with dissolve
    show Lila happy at left with dissolve
    "I reached out my hand to touch the crystall."
    "But before my finger even came close to touching it Emma stopped me."
    show Emma concern with dissolve
    show Lila surprised with dissolve
    fa "Just what do you think you're doing."
    show Lila Sweats with dissolve
    L "Touching the crystal..."
    show Emma angry with dissolve
    fa "I know that!"
    fa "Are you dumb?"
    fa "I just said this thing is sharp."
    show Lila shocked with dissolve
    "Oh no."
    "Looks like Emma's mad."
    "What should I do?"
    hide Emma angry with dissolve
    hide Lila shocked with dissolve
    menu:
        "Touch the crytsal anyways.":
                jump TouchCrystalAnyways
        "Say you are sorry.":
                jump SaidSorry
return

label TouchCrystalAnyways:
    $TouchBleed.value += 1
    $LilaBleed.value += 1

    if TouchBleed.value >= 1:
        $Crystal2_TouchBleed = True
        $Crystal_TasteNormal = False
        $Crystal_TouchNormal = False
        $Crystal_SmellNormal = False
        $Crystal2_SmellAfterTouch = True
    scene image "Cave.png" with fade
    show Emma shocked at emmaflip with dissolve
    show Lila pout at left with dissolve
    "I slapped away Emma's hand and grabbed the crystal."
    show Lila panic with dissolve
    show Lila pain with dissolve
    L "OW!"
    "I pulled back right after grabbing it."
    "My whole hand is in pain."
    show Emma angry with dissolve
    fa "YOU IDIOT."
    "Emma shouted and grabbed my hand."
    show Emma concern with dissolve
    fa "Where's your medication case?"
    "I felt tears at the edge of my eyes as I start to sob."
    show Lila tears with dissolve
    show Lila angry cry with dissolve
    show Emma dissapointed with dissolve
    fa "Forget it."
    fa "I also carry some first aid on me."
    show Emma sigh with dissolve
    "Emma said as she whipe something cold on my cuts and wraps a white rope around me."
    show Lila tears with dissolve
    show Emma nervous with dissolve
    fa "This should do for now."
    show Emma angry with dissolve
    fa "Why don't you ever listen."
    fa "Geez."
    show Emma sigh with dissolve
    show Emma dissapointed with dissolve
    show Lila relieved with dissolve
    L "Thank you."
    show Emma embarrassed with dissolve
    fa "Instead of saying thank you and sorry learn not to be so stupid."
    show Emma angry with dissolve
    "She said as she knocked me on the head."
    show Lila swirly eyes with dissolve
    L "Ouch."
    show Emma sigh with dissolve
    fa "Hmf."
    "Emma sighed."
    show Lila surprised with dissolve
    "This kind of feels familiar."
    hide Emma sigh with dissolve
    hide Lila surprised with dissolve
    scene image "CloseupCrystalHandPrint.png" with fade
    jump menu_Crystal2
return

label SaidSorry:
    $Crystal_TouchNormal = False
    $Touch_Points.value += 1

    if Touch_Points.value >= 1:
        $Crystal2_TouchStopped = True
        $Crystal_TasteNormal = False
        $Crystal_TouchNormal = False
    "Emma's affection goes up."
    scene image "Cave.png" with fade
    show Emma shocked at emmaflip with dissolve
    show Lila eyes closed sad at left with dissolve
    L "I'm sorry."
    "I said as she let's go of my hand."
    show Emma sigh with dissolve
    fa "I wish you stopped this foolish act instead of always saying sorry this and sorry that."
    show Lila yell with dissolve
    L "So-"
    show Lila surprised with dissolve
    show Emma embarrassed with dissolve
    fa "Ok stop."
    fa "Go on have your fun."
    show Lila eyes closed sad with dissolve
    show Emma dissapointed with dissolve
    fa "Who knows how long we have until we have to leave."
    hide Lila eyes closed sad
    show Lilasad at left
    L "Ok."
    "At least she's not as harsh before."
    hide Lilasad at left
    hide Emma dissapointed with dissolve
    scene image "CloseupCrystal.png" with fade
    jump menu_Crystal2
return

label CrystalTasteStopped:
    $Crystal2_TasteStopped = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila eyes closed sad at left with dissolve
    "Feeling guilty I wanted to slice my finger too."
    "Maybe she'll feel less mad if I share my pain with her..."
    show Emma angry with dissolve
    fa "Don't even think about it."
    show Lila surprised with dissolve
    L "?"
    show Emma envy with dissolve
    fa "I see the that glitter in your eyes."
    fa "I just stopped you from biting this crap and you want to touch it now?"
    show Emma angry with dissolve
    fa "I just showed you what happens if you touch this."
    fa "Want me to show you again?"
    hide Lila surprised with dissolve
    show Lilasad at left with dissolve
    "Emma showed me her wrapped bloody finger."
    hide Lilsad at left with dissolve
    show Lila eyes closed sad at left
    L "No..."
    L "Sorry.."
    "I truely felt bad."
    show Emma sigh with dissolve
    fa "For god's sake."
    "She sighed again."
    hide Lila eyes closed sad at left
    hide Emma sigh with dissolve
    scene image "CloseupCrystalBlood.png" with fade
    jump menu_Crystal2
return

label Listen2:
    $Crystal_Listen1 = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I leaned in to listen to the crystal."
    fa "{cps=2}...{/cps}"
    fa "What are you doing?"
    show Lila pout with dissolve
    show Emma surprised with dissolve
    L "Shhhhh. "
    L "I listening to the crystal."
    L "If you talk I can't hear."
    show Lila skeptical at left with dissolve
    show Emma concern with dissolve
    fa "I swear you were dropped as a baby."
    show Lila stunned with dissolve
    L "Hm?"
    show Lila skeptical at left with dissolve
    L "You said something."
    show Emma embarrassed with dissolve
    fa "Nothing."
    hide Lila skeptical at left
    hide Emma embarrassed with dissolve
    jump menu_Crystal2
return

label TasteNormal2:
    $Crystal_TasteNormal = False
    $TouchBleed.value += 1
    $EmmaBleed.value += 1

    if TouchBleed.value >= 1:
        $Crystal_TouchNormal = False
        $Crystal2_TasteStopped = True
        $Crystal_SmellNormal = False
        $Crystal2_SmellAfterTouch = True

    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I wanted to lean in to bite the crystal but Emma pulled me back by my hair."
    show Lila pain with dissolve
    show Emma intimidating with dissolve
    L "Ow! Ow! Ow!"
    L "Emma you are hurting me!"
    L "Please stop!"
    show Emma angry with dissolve
    fa "You think this is painful?"
    "She said as she lets go."
    show Emma envy with dissolve
    show Lila pout with dissolve
    fa "You were about to do something even more painful."
    show Lila stunned with dissolve
    L "Huh?"
    "I questioned rubbing my head."
    show Emma angry with dissolve
    fa "UGHHHHHHHH."
    show Lila Sweats with dissolve
    show Emma panic with dissolve
    fa "I don't understand how you can be so airheaded."
    show Emma envy with dissolve
    fa "Watch this you idiot."
    "Emma stated and bit her lips."
    show Emma nervous with dissolve
    show Lila surprised with dissolve
    "Then she took her finger and slices it on the crystal."
    show Lila shocked with dissolve
    fa "Look."
    show Emma panic with dissolve
    show Emma angry with dissolve
    "I felt pale as Emma shoved her bleeding bleeding finger to me."
    show Lila panic with dissolve
    L "Emma!"
    L "You're bleeding!"
    show Lila swirly eyes with dissolve
    "I wanted to reach out to help her but stopped after seeing how she's already preparing to take care of the cut."
    show Emma embarrassed with dissolve
    fa "Worry about yourself."
    show Lila surprised with dissolve
    show Emma concern with dissolve
    fa "To think you were gonna bite that."
    show Lila embarrassed with dissolve
    show Emma angry with dissolve
    fa "Idiotic."
    "Emma said frowing."
    show Lila eyes closed sad with dissolve
    "I felt an awful feeling rising in me."
    L "Sorry..."
    show Emma sigh with dissolve
    "Emma didn't say anything."
    "She only let out a sigh."
    hide Lila eyes closed sad with dissolve
    hide Emma sigh with dissolve
    scene image "CloseupCrystalBlood.png" with fade
    jump menu_Crystal2
return

label TasteAfterTouchBleed:
    $Crystal2_TouchBleed = False
    show Emma angry at emmaflip with dissolve
    show Lila nervous at left with dissolve
    fa "After all of that drama if you even dare to think about biting this."
    fa "I swear I'll leave the cave and you can get lost forever here."
    show Lila panic with dissolve
    "I rather not be alone."
    "And the pain in my hands is stinging really bad."
    "So I am not going to bite that."
    hide Lila panic with dissolve
    hide Emma angry with dissolve
    scene image "CloseupCrystalHandPrint.png" with fade
    jump menu_Crystal2
return

label CrystalTouchStopped:
    $Crystal2_TouchStopped = False
    "Emma's affection goes down."
    scene image "Cave.png" with fade
    show Emma angry at emmaflip with dissolve
    show Lila Sweats at left with dissolve
    fa "What were just sorry for..."
    L "Trying to touch the crystal?"
    fa "What are you about to do?"
    L "{cps=2}...{/cps}"
    show Lila eyes closed sad with dissolve
    L "Sorr-"
    show Emma dissapointed with dissolve
    show Lila shocked with dissolve
    fa "Don't bother."
    show Emma envy with dissolve
    show Lila eyes closed sad with dissolve
    fa "You never seem to learn..."
    "Emma looks didn't look happy."
    hide Emma envy with dissolve
    hide Lila eyes closed sad with dissolve
    jump menu_Crystal2
return

label SmellNormal2:
    $Crystal_SmellNormal = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I leaned in to sniff the crystal."
    "But I felt a force pull me back."
    show Lila surprised with dissolve
    "I turned to see Emma's hand on my shoulder."
    show Emma nervous with dissolve
    fa "What do you think you are doing?"
    show Lila stunned with dissolved
    L "?"
    L "Smelling the crystal?"
    show Emma shocked with dissolve
    show Emma concern with dissolve
    fa "Is that all you are going to do?"
    show Lila skeptical with dissolve
    L "For now yeah?"
    show Emma embarrassed with dissolve
    fa "Ok..."
    "Emma said as she let's go of her hand."
    show Lila eyes closed with dissolve
    "Still confused I still sniffed the crystal."
    "Smells like nothing."
    show Lila skeptical with dissolve
    show Emma concern with dissolve
    fa "Werido."
    show Lila stunned with dissolve
    L "?"
    fa"..."
    hide Emma concern with dissolve
    hide Lila stunned with dissolve
    jump menu_Crystal2
return

label SmellAfterTouch2:
    $Crystal2_SmellAfterTouch = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I leaned in to sniff the crystal."
    "But I felt a force pull me back."
    show Lila surprised with dissolve
    show Emma nervous with dissolve
    "I turned to see Emma's hand on my shoulder."
    show Emma angry with dissolve
    fa "Are you for real?!"
    fa "What on earth do you think you are doing?"
    show Lila stunned with dissolved
    L "?"
    show Lila skeptical with dissolve
    L "Smelling the crystal?"
    show Emma shocked with dissolve
    show Emma concern with dissolve
    fa "Is that all you are going to do?"
    L "For now yeah?"
    show Emma embarrassed with dissolve
    show Emma sigh with dissolve
    fa "Ok..."
    "Emma said as she let's go of her hand."
    show Lila eyes closed with dissolve
    "Still confused I still sniffed the crystal."
    show Lila eyes closed sad with dissolve
    "Smells like there's a hint iron"
    show Emma dissapointed with dissolve
    fa "I swear..."
    fa "One day you are going to be the cuase of my death."
    show Lila panic with dissolve
    L "What?"
    show Emma embarrassed with dissolve
    show Emma sigh with dissolve
    fa"..."
    hide Lila panic
    show Lilasad at left
    "Well that felt...Not good."
    hide Emma sigh with dissolve
    hide Lilasad at left
    jump menu_Crystal2
return

#######Start of Vine 2###########

label Vine2:
    scene image "CloseupVine.png" with fade
    L "Oh wow!"
    L "Emma come take a look at this."
    L "There's some kind of vine growing here."
    fa "I wouldn't go near that."
    L "Huh?"
    L "Why?"
    fa "Think about it yourself thickhead."
    $EaMpath1Points.value += 1
label menu_Vine2:
    if LilaBleed.value >= 1:
        $Vine2_NormalTouch = False
        $Vine2_TouchVineBleed = True
    if EmmaBleed.value >= 1:
        $Vine2_NormalTouch = False
        $Vine2_TouchVineBleed2 =True
    menu:
        "Touch it." if Vine2_NormalTouch == True:
                jump TouchVineNormal2
        "Touch it." if Vine2_TouchVineBleed == True:
                jump TouchVineBleed2
        "Touch it." if Vine2_TouchVineBleed2 == True:
                jump EmmaBleedTouchVine
        "Touch it." if Vine2_TouchWithEyes == True:
                jump TouchVineWithEyes2
        "Smell it." if Vine2_SmellVineNormal == True:
                jump SmellVineNormal2
        "Smell it." if Vine2_SmellVineEyes == True:
                jump SmellVineWithEyes2
        "Bite it." if Vine2_BiteVineNormal == True:
                jump BiteVineNormal2
        "Bite it." if Vine2_BiteVineWithEyes == True:
                jump BiteVineWithEyes2
        "Listen to it." if Vine2_ListenVine == True:
                jump ListenVine2
        "Don't do anything.":
                jump drag_glass2
return

label TouchVineNormal2:
    $Vine2_NormalTouch = False
    $Vine2_SmellVineNormal = False
    $Vine2_SmellVineEyes = True
    $Vine2_BiteVineNormal = False
    $Vine2_BiteVineWithEyes = True
    $VineTouchPoints.value += 1
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    fa "Don't touch that."
    L "But why can't I touch it."
    show Emma sigh with dissolve
    "She picked up a pebbled and tosses it at the vine."
    hide Emma sigh with dissolve
    hide Lila skeptical at left with dissolve
    scene image "CloseupVine.png" with fade
    scene image "VinaPlant.png" with fade
    "The vine started to shake and many eyes appeared on it."
    "I felt a shiver go down my spin when the eyes started to move around."
    "After a while the eyes shut back down."
    scene image "CloseupVine.png" with fade
    show Emma sigh at emmaflip with dissolve
    show Lila panic at left with dissolve
    L "What was that?!"
    show Emma dissapointed with dissolve
    "I asked and Emma shooked her head."
    show Emma intimidating with dissolve
    fa "Didn't you learn about this in Bio?"
    show Lila Sweats with dissolve
    L "What?"
    show Emma sigh with dissolve
    fa "Forget it."
    hide Lila Sweats with dissolve
    hide Emma sigh with dissolve
    menu:
        "Touch it anyways.":
                jump TouchVineAnyways
        "Leave it alone.":
                jump LeftVineAlone

jump menu_Vine2
return

label TouchVineAnyways:
    "Emma's affection goes down."
    scene image "Cave.png" with fade
    show Emma shocked at emmaflip with dissolve
    show Lila surprised at left with dissolve
    "I poked the vine when Emma wasn't looking."
    hide Emma shocked at emmaflip with dissolve
    hide Lila surprised at left with dissolve
    scene image "CloseupVine.png" with fade
    scene image "VinaPlant.png" with fade
    "It started to shake just like before."
    "This time the eyes stared at me and me only."
    "It's like it was making sure I was there before closing again."
    scene image "CloseupVine.png" with fade
    "There wasn't even time to think about what I saw before I felt a hard thob on my head."
    show Emma intimidating at emmaflip with dissolve
    show Lila pain at left with dissolve
    fa "I just told you not to touch it!"
    fa "Are you deaf?"
    show Lila pout with dissolve
    L "But nothing happened!"
    show Emma angry with dissolve
    fa "Even so something could have."
    show Lila Sweats with dissolve
    show Emma sigh with dissolve
    fa "I can't believe you."
    L "I'm sorry..."
    hide Lila Sweats with dissolve
    hide Emma sigh with dissolve
jump menu_Vine2
return

label LeftVineAlone:
    "I didn't like the way it looked at us."
    "Best to leave it alone."
jump menu_Vine2
return

label TouchVineBleed2:
    $Vine2_NormalTouch = False
    $Vine2_TouchVineBleed = False
    $Vine2_SmellVineNormal = False
    $Vine2_SmellVineEyes = True
    $Vine2_BiteVineNormal = False
    $Vine2_BiteVineWithEyes = True
    $Vine2_ListenVine = False
    $Vine2_ListenAfterTouch = True

    $VineTouchPoints.value += 1
    scene image "Cave.png" with fade
    show Emma intimidating at emmaflip with dissolve
    show Lila Sweats at left with dissolve
    "I didn't bother reaching out to the vine."
    "Emma was already glaring at me."
    show Emma envy with dissolve
    fa "Don't touch that."
    hide Lila Sweats at left with dissolve
    hide Emma envy with dissolve
    scene image "CloseupVine.png" with fade
    scene image "VinaPlant.png" with fade
    "The vine started to shake and many eyes appeared on it."
    "I felt a shiver go down my spin when the eyes started to move around."
    "The eyes just stared at us..."
    "Wait no."
    "It was staring mainly at me."
    scene image "Cave.png" with fade
    show Emma intimidating at emmaflip with dissolve
    show Lila Sweats at left with dissolve
    fa "I'll say it one more time."
    fa "Don't you dare touch it."
    menu:
        "Touch it anyways.":
                jump TouchVineAnyways2
        "Leave it alone.":
                jump LeftVineAlone2
return

label TouchVineAnyways2:
    scene image "VinaPlant.png" with fade
    scene image "VinaPlantDeath.png" with fade
    "I ignored Emma and touched it."
    "As soon as my finger touched the vine it wrapped itself around me."
    "I couldn't even scream through it."
    scene image "black.png" with fade
    "As it keeps twisting and wrapping I saw Emma trying to pull it apart from me."
    "Muffled screams came from Emma as my body pulls towards it."
    "Then all that was left was complete darkness."
    "Compared to the pain on my skin...."
    show Lila pain at middle with dissolve
    "I was more regretful for making her show such a face expression."
    show Lila eyes closed sad with dissolve
    show Lila tears with dissolve
    "I wished I could have at least said sorry."
    show Lila relieved with dissolve
    "I smiled and sobbed at the thought of how I'll be scolded this time."
    hide Lila relieved with dissolve
    "Though that don't seem likely."
    "Lila's route end."
    "No pages found."
return

label LeftVineAlone2:
    scene image "VinaPlant.png" with fade
    "I didn't like the way it looked at us."
    "Best to leave it alone."
    "As I backed away from it the eyes on the vines slowly shuts off."
    scene image "CloseupVine.png" with fade
    scene image "Cave.png" with fade
    show Emma intimidating at emmaflip with dissolve
    show Lila panic at left with dissolve
    fa "Look at it feeling dissappointed."
    show Emma laugh with dissolve
    fa "For once you weren't acting dumb."
    show Lila Sweats with dissolve
    "I guess I wasn't the only one who thought it felt kind of upset."
    hide Emma laugh with dissolve
    hide Lila Sweats with dissolve
jump menu_Vine2
return

label EmmaBleedTouchVine:
    $Vine2_NormalTouch = False
    $Vine2_TouchVineBleed2 = False
    $Vine2_TouchVineBleed = False
    $Vine2_TouchVineBleed2 = False
    $Vine2_TouchWithEyes = False
    $Vine2_SmellVineNormal = False
    $Vine2_SmellVineEyes = False
    $Vine2_BiteVineNormal = False
    $Vine2_BiteVineWithEyes = False
    $Vine2_ListenVine = False
    $Vine2_ListenAfterTouch = False
    $VineTouchPoints.value += 1
    scene image "Cave.png" with fade
    show Emma intimidating at emmaflip with dissolve
    show Lila Sweats at left with dissolve
    "I didn't bother reaching out to the vine."
    "Emma was already glaring at me."
    show Emma envy with dissolve
    fa "Don't touch that."
    show Lila pout with dissolve
    L "But why can't I touch it."
    show Emma sigh with dissolve
    fa "You're such a bother."
    show Emma angry with dissolve
    "She said as picked up a pebbled."
    "A bit of her blood from her finger cute got on to it."
    show Emma nervous with dissolve
    "Making a painful face she tosses it at the vine."
    hide Emma nervous with dissolve
    hide Lila pout with dissolve
    scene image "CloseupVine.png" with fade
    scene image "VinaPlant.png" with fade
    "The vine started to shake and many eyes appeared on it."
    "A giant mouth appeared and shollowed the pebble."
    scene image "VinaPlantDeath.png" with fade
    "After a while it spit out the pebble."
    "It's eyes and mouth was no longer there."
    show Lila panic at left with dissolve
    L "What was that?!"
    show Emma dissapointed at emmaflip with dissolve
    "I asked and but she only looked dissappointed."
    hide Lila panic at left with dissolve
    hide Emma dissapointed at emmaflip with dissolve
jump menu_Vine2
return

label TouchVineWithEyes2:
   $Vine2_TouchWithEyes = False
   "I would but I don't think Emma wants me too."
   "I think I pissed her off enough today."
   scene image "Cave.png" with fade
   show Emma intimidating at emmaflip with dissolve
   show Lila Sweats at left with dissolve
   fa "..."
   "She's already glaring."
   hide Emma intimidating at emmaflip with dissolve
   hide Lila Sweats at left with dissolve
jump menu_Vine2
return

label SmellVineNormal2:
    $Vine2_SmellVineNormal = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila Sweats at left with dissolve
    L "I kind of want to smell this."
    show Emma shocked with dissolve
    fa "Wha-?"
    show Emma concern with dissolve
    fa "I guess smelling it won't hurt..."
    show Emma yell with dissolve
    fa "I GUESS."
    show Lila stunned with dissolve
    "Getting a yes from Emma I leaned in to smell it."
    show Lila eyes closed with dissolve
    show Emma concern with dissolve
    fa "..."
    fa "What does it smell like?"
    show Lila skeptical with dissolve
    L "hmmmmmmmmmmmm..."
    show Lila smile with dissolve
    L "Grass."
    show Emma dissapointed with dissolve
    fa "I don't have words to discribe you anymore."
    show Lila happy with dissolve
    "I smiled back in response to her comment."
    show Emma embarrassed with dissolve
    fa "That was not a complement."
    hide Lila happy with dissolve
    hide Emma embarrassed with dissolve
jump menu_Vine2
return

label SmellVineWithEyes2:
    $Vine2_SmellVineEyes = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila Sweats at left with dissolve
    "After seeing that I don't think that's a good idea."
    show Lila surprised with dissolve
    "I wasn't going to do it but I noticed I have Emma with me."
    show Lila skeptical with dissolve
    L "Can I smell it?"
    show Emma shocked with dissolve
    fa "Wha-?"
    show Emma angry with dissolve
    fa "We just saw how this thing isn't friendly."
    L "Will smelling it hurt me?"
    show Emma nervous with dissolve
    fa "How would I know?"
    show Lila surprised with dissolve
    L "But you sound like you know some things."
    show Emma sigh with dissolve
    fa "I only know that this thing isn't exactly harmless..."
    show Lila shocked with dissolve
    L "Oh...."
    show Lila surprised with dissolve
    L "Should I go for it anyways?"
    show Emma concern with dissolve
    fa "Huh?"
    show Lila smile with dissolve
    L "You'll help me if something happens right?"
    show Emma nervous with dissolve
    fa "I-I'm not sure."
    fa "I'm not as strong as Liam."
    show Lila eyes closed sad with dissolve
    "hmmmmm..."
    hide Emma nervous with dissolve
    hide Lila eyes closed sad with dissolve
    menu:
        "Go ahead and smell it.":
                jump YesSmellWithEyes
        "Don't do it.":
                jump DidntSmell
jump menu_Vine2
return

label YesSmellWithEyes:
    scene image "Cave.png" with fade
    show Emma shocked at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I leaned it to sniff the Vine."
    show Lila eyes closed with dissolve
    show Emma panic with dissolve
    "For a second I thought I saw Emma reach out for me."
    "But when I turned around she only had a worried face."
    show Emma nervous with dissolve
    fa "H-how does it smell like?"
    show Emma concern with dissolve
    show Emma panic with dissolve
    show Emma blush with dissolve
    show Emma embarrassed with dissolve
    show Lila surprised with dissolve
    L "It smelled very sweet."
    show Emma concern with dissolve
    fa "Sweet?"
    show Lila smile with dissolve
    L "Yeah."
    show Lila eyes closed sad with dissolve
    L "Makes me a bit hungry."
    show Emma shocked with dissolve
    show Emma concern with dissolve
    fa "That's very unsettling."
    hide Emma concern with dissolve
    hide Lila eyes closed sad with dissolve
jump menu_Vine2
return

label DidntSmell:
    scene image "Cave.png" with fade
    show Emma shocked at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I decided to pull back."
    show Emma sly with dissolve
    fa "Smart move."
    show Lila pout with dissolve
    L "I don't think hurt me though."
    show Emma sigh with dissolve
    fa "I rather you say 'I know it will not hurt me' before I let you do that."
    show Lila surprised with dissolve
    L "Why are you acting like Liam?"
    show Emma surprised with dissolve
    fa "Huh?"
    show Lila stunned with dissolve
    L "Actually it feels a bit different."
    show Emma concern with dissolve
    fa "What are you on about?"
    show Lila swirly eyes with dissolve
    L "I don't know."
    show Emma sigh with dissolve
    fa "Weirdo."
    hide Lila swirly eyes with dissolve
    hide Emma sigh with dissolve
jump menu_Vine2
return

label BiteVineNormal2:
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    L "Should I eat it?"
    show Emma shocked with dissolve
    L "I am a bit hungry."
    show Lila eyes closed sad with dissolve
    show  Emma concern with dissolve
    fa "If I were you I wouldn't."
    show Lila pout with dissolve
    L "Why?"
    show Emma dissapointed with dissolve
    fa "I don't think this thing is edible."
    show Lila stunned with dissolve
    show Emma concern with dissolve
    L "Wouldn't hurt to try right?"
    show Emma angry with dissolve
    fa "Ha."
    show Emma envy with dissolve
    fa "If you read about it in the books you wouldn't have said that."
    show Lila skeptical with dissolve
    L "What is so dangerous about this vine?"
    L "Is it like...poison?"
    show Emma nervous with dissolve
    fa "I don't think so..."
    show Lila surprised with dissolve
    L "I thought you said you know about it."
    show Emma sigh  with dissolve
    fa "I just know it's not safe."
    hide Lila surprised with dissolve
    hide Emma sigh  with dissolve
    menu:
        "Bite it anyways.":
                jump BiteItAnyways
        "Don't bite it.":
                jump DidntBite2
return

label BiteItAnyways:
    $Vine2_NormalTouch = False
    $Vine2_SmellVineNormal = False
    $Vine2_SmellVineEyes = True
    $Vine2_BiteVineNormal = False
    $Vine2_BiteVineWithEyes = False
    $Vine2_ListenVine = False
    $Vine2_ListenAfterTouch = True
    scene image "Cave.png" with fade
    show Emma panic at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I took a chunck out of the vine."
    show Lila smile at left with dissolve
    "It tasted pretty good..."
    "Like sweetness melting in my mouth."
    show Lila happy at left with dissolve
    L "H-"
    show Emma nervous with dissolve
    "I wanted Emma to try it too but before I can even say anything Emma pulled me back with force."
    show Lila pain at left with dissolve
    "Before I know it I was in her arms."
    show Lila swirly eyes at left with dissolve
    L "Wha-"
    show Lila nervous at left with dissolve
    show Lila shocked at left with dissolve
    show Lila panic at left with dissolve
    hide Lila panic at left with dissolve
    hide Emma nervous with dissolve
    "I stopped questioning her scared face staring at the vine."
    scene image "VinaPlant.png" with fade
    "When I looked over I noticed that the vine had eyes."
    "The eyes rolled and rolled checking the area until it shut back down."
    scene image "CloseupVine.png" with fade
    show Emma panic at emmaflip with dissolve
    show Lila panic at left with dissolve
    L "What was that?"
    "I felt grossed out thinking that this thing is now inside my stomach."
    show Emma nervous at emmaflip with dissolve
    fa "I'm not sure."
    fa "I just know it triggers on touch."
    fa "And it eats other living things."
    show Lila shocked at left with dissolve
    show Lila panic at left with dissolve
    L "Will it eat us too?"
    show Emma sigh with dissolve
    fa "I don't know."
    fa "Don't go near it anymore ok."
    show Lila eyes closed sad with dissolve
    L "..."
    "I shouldn't make a promise I can't keep."
    hide Lila eyes closed sad with dissolve
    hide Emma sigh with dissolve
jump menu_Vine2
return

label DidntBite2:
    $Vine2_BiteVineNormal = False
    $Vine2_BiteVineWithEyes = False
    "I guess it's safer not to eat it."
    "I think Emma let out a breath of relief."
jump menu_Vine2
return

label BiteVineWithEyes2:
    $Vine2_BiteVineNormal = False
    $Vine2_BiteVineWithEyes = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    L "Is this safe to eat?"
    fa "What kind of question is that."
    show Emma shocked with dissolve
    show Emma concern with dissolve
    L "I'm a bit hungry."
    show Lila eyes closed sad with dissolve
    fa "After seeing that you can still think about eating it?"
    show Emma shocked with dissolve
    show Lila skeptical with dissolve
    L "If I won't kill me I might just eat it."
    show Emma nervous with dissolve
    fa "That's the thing."
    fa "I don't know if it can."
    show Lila nervous with dissolve
    L "Doesn't hurt to try... right?"
    show Emma concern with dissolve
    fa "I don't think you should."
    show Lila embarrassed with dissolve
    show  Emma embarrassed with dissolve
    "We heard my stomach grumble."
    show Lila eyes closed sad with dissolve
    L "Emma...."
    show Emma intimidating with dissolve
    "Emma gave me a werid look and sighed."
    show Emma sigh with dissolve
    fa "When you feel like you are done exploring I'll make you something at your house."
    show Emma intimidating with dissolve
    show Lila surprised with dissolve
    show Lila stunned with dissolve
    fa "Hold it in until then."
    show Lila happy with dissolve
    L "Ok!"
    show Emma surprised with dissolve
    show Emma smile with dissolve
    show Emma laugh with dissolve
    "I can't wait since Emma is pretty good at cooking."
    hide Emma laugh with dissolve
    hide Lila happy with dissolve
jump menu_Vine2
return

label ListenVine2:
    $Vine2_ListenVine = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    fa "What are you doing?"
    show Emma panic with dissolve
    "When I leaned in to listen to the vine Emma was a bit jumpy."
    show Lila stunned with dissolve
    L "Listening to the Vine."
    show Emma concern with dissolve
    fa "Why?"
    show Lila surprised with dissolve
    L "Just cause."
    show Emma nervous with dissolve
    fa "There's no way a vine will make any kind of sounds."
    show Lila skeptical with dissolve
    L "Actually it kind of sounds like us when we are hungry."
    show Emma shocked with dissolve
    show Emma panic with dissolve
    fa "Wha-"
    "Emma's face looks a bit pale."
    show Lila swirly eyes with dissolve
    L "You know..."
    show Lila skeptical with dissolve
    L "Like a grumble?"
    show Emma panic with dissolve
    show Emma nervous with dissolve
    show Emma concern with dissolve
    fa "Get away from that thing now!"
    "Emma said as she yanked me away for it."
    show Lila pain with dissolve
    L "Ow..."
    show Lila swirly eyes with dissolve
    L "Why did you do that?"
    "I asked as she let go."
    show Emma nervous with dissolve
    fa "Don't go near it."
    show Lila surprised with dissolve
    show Emma sigh with dissolve
    fa "For now."
    show Lila eyes closed sad with dissolve
    "I guess it is unsettling."
    hide Emma sigh with dissolve
    hide Lila eyes closed sad with dissolve
jump menu_Vine2
return

#######Start of Opus  2###########
label Opus2:
    scene image "CloseupOpus.png" with fade
    L "Look at this guy here Emma!"
    L "It's so cute!"
    fa "Ok."
    fa "I know you can be very very dumb."
    fa "But you are not going anywhere near that thing."
    L "Huh?"
    L "Why can't I?"
    fa "It's not as cute as it looks."
    fa "I don't know what it's doing here but it lives in the Ocean."
    L "By the sea?"
    fa "Yeah."
    "Huh...I wonder why it's chilling in a cave."
    $EaMpath1Points.value += 1

label menu_Opus2:
    if LilaBleed.value >= 1:
        $Opus2_NormalTouch = False
        $Opus2_TouchBleed = True
    menu:
        "Touch it." if Opus2_NormalTouch == True:
            jump TouchOpusNormal2
        "Touch it." if Opus2_TouchBleed == True:
            jump TouchOpusBlood2
        "Smell it." if Opus2_NormalSmell == True:
            jump SmellOpusNormal2
        "Bite it." if Opus2_NormalBite == True:
            jump BiteOpusNormal2
        "Listen to it." if Opus2_Listen == True:
            jump ListenOpusNormal2
        "Don't do anything":
            jump drag_glass2
return

label TouchOpusNomral2:
    $Opus2_NormalTouch = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila smile at left with dissolve
    "I wanted to poke the Opus but Emma grabbed my reaching hand."
    show Emma angry with dissolve
    show Lila surprised with dissolve
    fa "Don't think about it..."
    show Lila pout with dissolve
    L "But it's so cute."
    show Emma nervous with dissolve
    fa "If you value your life you'll listen to me."
    hide Lila pout with dissolve
    hide Emma nervous with dissolve
    menu:
        "Ignore Emma.":
            jump IgnoredEmma
        "Listen to Emma.":
            jump ListenToEmma
return

label IgnoredEmma:
    $Opus2_ListenAfterTouch = True
    "Emma's affection goes down."
    scene image "Cave.png" with fade
    show Emma nervous at emmaflip with dissolve
    show Lila smile at left with dissolve
    L "I'm sure you're overthinking again."
    show Emma panic with dissolve
    "I said as I poked the Opus using my other hand."
    show Emma nervous with dissolve
    show Lila nervous with dissolve
    "Although Emma quickly pulled me back afterwards we noticed nothing happned."
    L "See."
    show Lila Sweats with dissolve
    show Emma shocked with dissolve
    show Emma sigh with dissolve
    show Emma intimidating with dissolve
    fa "I really hate you..."
    show Lila embarrassed with dissolve
    show Lila yell with dissolve
    L "EHHHHHHH!"
    show Lila swirly eyes with dissolve
    show Lila pout with dissolve
    show Emma embarrassed with dissolve
    L "Why???"
    show Emma blush with dissolve
    show Emma embarrassed with dissolve
    show Emma angry with dissolve
    fa "Just shut up."
    show Lila angry with dissolve
    L "You are so mean today."
    show Emma envy with dissolve
    fa "I'm like this everyday."
    hide Lila angry with dissolve
    hide Emma envy with dissolve
jump menu_Opus2
return

label ListenToEmma:
   "Emma's affection goes up."
   scene image "Cave.png" with fade
   show Emma nervous at emmaflip with dissolve
   show Lila smile at left with dissolve
   L "Ok."
   show Lila eyes closed with dissolve
   L "I won't touch."
   show Lila smile with dissolve
   L "I'll listen to you."
   show Lila happy with dissolve
   fa "Good."
   show Emma sigh with dissolve
   fa "If only you were like this all the time."
   show Emma smile with dissolve
   fa "That would take the burden off my shoulders."
   show Emma laugh with dissolve
   L "What?"
   show Lila surprised with dissolve
   show Emma embarrassed with dissolve
   show Emma dissapointed with dissolve
   fa "Nevermind."
   hide Lila surprised with dissolve
   hide Emma dissapointed with dissolve
jump menu_Opus2
return

label TouchOpusBlood2:
    $Opus2_NormalTouch = False
    $Opus2_TouchOpusBlood2 = False
    scene image "Cave.png" with fade
    show Emma nervous at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    "I wanted to poke the Opus but Emma grabbed my reaching hand."
    show Emma panic with dissolve
    fa "Don't think about it..."
    show Lila pout with dissolve
    L "But it's so cute."
    show Emma angry with dissolve
    fa "If you value your life you'll listen to me."
    menu:
        "Ignore Emma.":
            jump IgnoredEmma2
        "Listen to Emma.":
            jump ListenToEmma2
return

label IgnoredEmma2:
    "Emma's affection goes down."
    scene image "Cave.png" with fade
    show Emma nervous at emmaflip with dissolve
    show Lila happy at left with dissolve
    L "I'm sure you're overthinking again."
    "I said as I poked the Opus using the hand that had the cuts wounds."
    show Emma panic with dissolve
    fa "Idiot!"
    hide Emma panic with dissolve
    hide Lila happy at left with dissolve
    scene image "Opus2.png" with fade
    scene image "black.png" with fade
    "Emma shouted before pushing me out of the way."
    L "Huh?"
    "When I came back to my senses Emma was no longer in sight."
    L "Emma?"
    "I called out to her but there was no response."
    "I look back at where the blob was floating."
    "It was no longer there..."
    "All that was left was a puddle of red water."
    "I...."
    L "Emma!"
    "I shouted helplessly but there was no response."
    "The lonely darkness enters my sight as I felt myself lossing balance."
    "The cold floor of the cave overtook my body."
    "This must be a dream."
    "I hope I wake up soon."
    "Lila's route end."
    "Emma lost."
    "No pages found."
return

label ListenToEmma2:
   "Emma's affection goes up."
   scene image "Cave.png" with fade
   show Emma nervous at emmaflip with dissolve
   show Lila smile at left with dissolve
   L "Ok."
   show Lila eyes closed with dissolve
   L "I won't touch."
   show Lila smile with dissolve
   L "I'll listen to you."
   show Lila happy with dissolve
   fa "Good."
   show Emma sigh with dissolve
   show Emma smile with dissolve
   fa "Just stay close to me."
   show Emma smile with dissolve
   L "Mhm!"
   show Lila smile with dissolve
   show Lila happy with dissolve
   show Emma embarrassed with dissolve
   show Emma blush with dissolve
   "I nodded with a smile."
   hide Lila happy with dissolve
   hide Emma blush with dissolve
jump menu_Opus2
return

label SmellOpusNormal2:
    $Opus2_NormalSmell = False
    scene image "Cave.png" with fade
    show Emma nervous at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    L "I wonder if it'll smell like salt."
    show Emma concern with dissolve
    fa "Don't tell me..."
    show Emma panic with dissolve
    show Emma nervous with dissolve
    fa "Are you going to attempt to smell it?"
    show Lila happy with dissolve
    L "Yes!"
    show Emma angry with dissolve
    fa "Don't."
    show Lila pout with dissolve
    L "But why not?"
    show Emma sigh with dissolve
    fa "I already told you this thing isn't safe."
    show Lila eyes closed sad with dissolve
    L "Ok..."
    hide Emma sigh with dissolve
    hide Lila eyes closed sad with dissolve
jump menu_Opus2
return

label ListenOpusNormal2:
    $Opus2_Listen = False
    show Emma nervous at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    L "Should I listen to it?"
    show Emma concern with dissolve
    fa "Why?"
    show Lila swirly eyes with dissolve
    L "Just wondering what kind of sounds it'll make."
    show Emma angry with dissolve
    fa "No."
    show Lila eyes closed sad with dissolve
    L"I guess not."
    hide Emma angry with dissolve
    hide Lila eyes closed sad with dissolve
jump menu_Opus2
return

#########START OF PAGE 2########################
label Page2:
    $EaMpath1Points.value += 1
    scene image "CloseupPageCave.png" with fade
    L "Oh my."
    L "Emma look."
    L "What is a paper doing in here?"
    fa "Hm?"
    "We both too a close look at it."
    fa "What the..."
    fa "It looks older than your grandma."
    L "Hey!"
    fa "Ops."
    fa "My bad."
    fa "Anyways."
    fa "You finally asked a good question...."
    L "Should we take this to Liam?"
    fa "Right now?"
    menu:
            "Yes.":
                jump PageFound2
            "Not right now.":
                jump ExploreMore
return

label PageFound2:
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila happy at left with dissolve
    L "Yeah."
    L "Let's go!"
    L "I want to know more about it."
    show Emma dissapointed with dissolve
    fa "I don't know what's there to know more about..."
    show Lila skeptical with dissolve
    show Emma smile with dissolve
    fa "But sure."
    fa "Let's go."
    show Lila happy with dissolve
    L "I wonder what waits ahead of us."
    show Emma dissapointed with dissolve
    fa "I could just be a normal paper."
    show Emma surprised with dissolve
    fa "Then again normal paper wouldn't appear in a cave."
    show Lila surprised with dissolve
    L "Huh?"
    show Lila stunned with dissolve
    L "Then someone put it there?"
    show Emma dissapointed with dissolve
    fa "Maybe."
    show Emma nervous with dissolve
    fa "Who knows."
    show Lila happy with dissolve
    L "Let's find out!"
    show Emma dissapointed with dissolve
    fa "Yeah. Yeah."
    fa "Heard you the first time."
    fa "Let's go."
    hide Lila happy with dissolve
    hide Emma dissapointed with dissolve
    scene image "black.png" with fade
    "Lila's route end."
    "First page found."
return

label ExploreMore:
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila nervous at left with dissolve
    L "Wait no."
    L "I want to see the other things first."
    hide Emma sigh with dissolve
    fa "Suit yourself."
    hide Emma concern at emmaflip with dissolve
    hide Emma sigh with dissolve
jump drag_glass2
return

###############END OF EXPLORING CAVE WITH EMMA#############
###############START APPEARANCE OF MINGLOU 2################
###NOTHING YET FOR MINGLOU
#######Lila is with both of her friends###################

label O3:
    "Which place should we Observe first?"
    menu:
        "Cave.":
                jump OC3
        #"Den.":
                #jump OD3
return

label OC3:
    "What would you like to check out first?"
label menu_OC3:
    menu:
        "Sight." if C_Sight1 == True:
                jump Sight3

        "Smell." if C_Smell1 == True:
                jump Smell3

        "Feel." if C_Feel1 == True:
                jump Feel3

        "Sound." if C_Sound1 == True:
                jump Sound3

        #"Observe the Den.":
                #jump OD3

        "Go to Cave.":
                jump Cave3
return

#######################Place Sense Observation 3##########################

label Sight3:
    show Lila stunned at left with dissolve
    show Emma default at emmaflip with dissolve
    show Liam default at right with dissolve
    L "Hmmmm."
    show Lila skeptical with dissolve
    L "Do you guys see anything from here?"
    show Emma concern with dissolve
    fa "Not sure what's there to see."
    fa "Looks like a normal cave to me."
    fa "Wait..."
    show Emma surprised with dissolve
    show Emma nervous with dissolve
    fa "I guess the amount of crystals formulated is a bit werid."
    show Liam smile with dissolve
    show Liam default with dissolve
    show Emma sigh with dissolve
    fa "Well whatever we do we should be fine since Liam is here."
    show Lila smile with dissolve
    L "True."
    show Emma sly with dissolve
    show Liam blush with dissolve
    show Liam embarrassed with dissolve

    hide Emma sly with dissolve
    hide Lila smile at left with dissolve
    hide Liam embarrassed at left with dissolve
    $C_Sight1 = False
jump menu_OC3
return

label Smell3:
    show Lila skeptical at left with dissolve
    show Emma default at emmaflip with dissolve
    show Liam default at right with dissolve
    L "What do you guys think about the smell of this place?"
    show Emma surprised with dissolve
    fa "You ask the weirdest questions."
    show Lila smile with dissolve
    L "What do you think Liam?"
    show Emma envy with dissolve
    show Liam surprised with dissolve
    fb "Hm?"
    show Liam smile with dissolve
    show Liam default with dissolve
    fb "I'll go with whatever you think."
    show Emma dissapointed with dissolve
    fa "Ugh."
    fa "Favoritism."
    L "Well I think it just smell like grass."
    hide Emma dissapointed with dissolve
    hide Liam default with dissolve
    hide Lila smile with dissolve
    $C_Smell1 = False
jump menu_OC3
return

label Feel3:
    show Lila skeptical at left with dissolve
    show Emma default at emmaflip with dissolve
    show Liam default at right with dissolve
    L "There's something off putting about the cave."
    show Emma surprised with dissolve
    show Liam surprised with dissolve
    fa "Huh?"
    show Emma concern with dissolve
    fa "I have no idea what you are talking about."
    show Liam smile with dissolve
    fb "Hmmmm..."
    show Liam default  with dissolve
    fb "You always did rely on your instincts more then your logic."
    show Liam smile with dissolve
    fb "But you are almost always correct."
    show Lila swirly eyes with dissolve
    L "?"
    show Emma pout with dissolve
    fa "Can't you just speak normally?"
    hide Emma pout with dissolve
    hide Liam smile with dissolve
    hide Lila swirly eyes with dissolve
    $C_Feel1 = False
jump menu_OC3
return

label Sound3:
    show Lila skeptical at left with dissolve
    show Emma default at emmaflip with dissolve
    show Liam default at right with dissolve
    L "I don't think there are any other noise besides the sound of insects."
    show Emma concern with dissolve
    fa "No duh."
    fa "Otherwise we wouldn't be playing in this area."
    show Emma nervous with dissolve
    fa "Who knows what's out there lurking in the dark."
    hide Emma default with dissolve
    hide Lila skeptical at left  with dissolve
    hide Liam default with dissolve
    $C_Sound1 = False
jump menu_OC3

##############Start Of Cave Exploring(With Emma and Liam)#########
label Cave3:
    scene image "Cave.png" with dissolve
    hide Emma pout
    hide Liam nervous
    show Liam shocked at right with dissolve
    show Emma surprised at middle with dissolve
    show Lila happy at left with dissolve
    L "Oh wow!"
    L "There's a ton of stuff in here I've never seen before."
    L "Let's explore of a bit."
    show Emma concern at middle with dissolve
    show Liam nervous with dissolve
    fb "I'm so glad I came with you today."
    fa "For once we agree on something."
    L "Huh?"
    show Emma dissapointed at middle with dissolve
    show Liam smile with dissolve
    fb "Don't worry too much and just explore."
    "Well with Liam and Emma here I'm sure nothing will go wrong."
    "Drag the magnifying glass to the objects you wish to interact with."

label drag_glass3:
    call screen slide_glass_screen
    scene image "Cave.png"
    hide image "CloseupOpus.png"
    hide image "CloseupVine.png"
    hide image "CloseupPageCave.png"
    hide image "Opus1.png"
    hide image "Opus2.png"
    hide image "VinaPlant.png"
    "[glass] picked the [object]. Do you want to take a closer look at the object?"

    menu:
        "Observe the crystal?" if store.object == "Crystal":
            jump Crystal3
        "Observe the vine?" if store.object == "Vine":
            jump Vine3
        "Observe the Opus?" if store.object == "Opus":
            jump Opus3
        "Observe the page?" if store.object == "Page?":
            jump Page3
        "Go Back":
            jump drag_glass3
        "Done Exploring." if  LilaFriendsPlusMPath == True:
            jump NextStory3
return

#########################Start of Crystal 3#######################

label Crystal3:
    scene image "CloseupCrystal.png" with fade
    L "Guys!"
    L "Look at this shiny crystal."
    fa "Yeah shiny and sharp."
    L "It's sharp?!"
    fb "Well it is what my knife is made of."
    fb "It'll slice right through skin."
    L "Oh god."
    $LilaFriendsPlusMPathPoints.value += 1

label menu_Crystal3:
    menu:
        "Touch it." if Crystal3_TouchNormal == True:
                jump TouchNormal3
        "Touch it." if Crystal3_TouchAfterTaste == True:
                jump TouchCrystalEvenAfterBite
        "Listen to it." if Crystal3_Listen1 == True:
                jump Listen3
        "Taste it." if Crystal3_TasteNormal == True:
                jump TasteNormal3
        "Taste it." if Crystal3_TasteAfterTouch == True:
                jump BiteCrystalEvenAfterTouch
        "Smell it." if Crystal3_SmellNormal == True:
                jump SmellNormal3
        "Smell it." if Crystal3_SmellAfterTouch == True:
                jump SmellAfterTouch3
        "Don't do anything.":
                jump drag_glass3
return

label TouchNormal3:
    $Crystal3_TouchNormal = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    show Liam smile at right with dissolve
    "I reached for the Crystal but Emma grabbed my hand."
    show Emma angry with dissolve
    fa "Did you not listen to Liam."
    show Lila surprised with dissolve
    L "?"
    fa "He just said it'll slice through skin."
    show Lila Sweats with dissolve
    show Emma concern with dissolve
    fa "I swear you never learn your lesson."
    hide Emma concern with dissolve
    hide Lila Sweats with dissolve
    hide Liam smile at right with dissolve
    menu:
        "I did but I don't care.":
                jump LilaHandCut
        "Oh right. I forgot.":
                jump LilaDidntGetCut
return

label LilaHandCut:
     $LiamLetLilaBleed.value += 1
     if LiamLetLilaBleed.value >= 1:
         $Crystal3_SmellNormal = False
         $Crystal3_SmellAfterTouch = True
         $Crystal3_TasteNormal = False
         $Crystal3_TasteAfterTouch = True
     "Emma's affection for Liam goes down. Liam's affection goes down."
     scene image "Cave.png" with fade
     show Emma angry at emmaflip with dissolve
     show Liam default at right with dissolve
     show Lila Sweats at left with dissolve
     "Even though I know I will get hurt..."
     "The shiny crystal is all I can see in my eyes."
     "It was just so pretty."
     "I want it..."
     show Emma panic with dissolve
     show Liam shocked with dissolve
     show Liam nervous with dissolve
     show Liam smile with dissolve
     "I pushed Emma away and grabbed the Crystal."
     show Lila pain with dissolve
     show Lila panic with dissolve
     L "Ouch!"
     show Emma shocked with dissolve
     show Lila nervous with dissolve
     fa "Idiot!"
     show Emma nervous with dissolve
     fa "Look you're bleeding."
     "Emma said as she wrapped a white rag around me."
     show Emma concern with dissolve
     fa "Why didn't you stop her?"
     "Emma asked Liam but he only silently smiled."
     show Emma angry with dissolve
     fb "Sometimes it's good for her to learn a thing or two on her own."
     show Lila shocked with dissolve
     show Lila Sweats with dissolve
     show Emma shocked with dissolve
     show Emma nervous with dissolve
     "Emma gave him a weird look."
     fa "You're not acting like yourself..."
     show Liam surprised with dissolve
     show Liam default with dissolve
     fb "Hm?"
     fb "I've always been like this."
     show Liam smile with dissolve
     show Liam intimidating with dissolve
     show Emma shocked with dissolve
     fa "...."
     show Emma envy with dissolve
     "Emma gave him a glare."
     "Liam is giving off an awful feeling."
     "I felt so bad I found myself clinging onto Emma."
     hide Emma envy with dissolve
     hide Liam intimidating with dissolve
     hide Lila Sweats with dissolve
     scene image "CloseupCrystalHandPrint.png" with fade
jump menu_Crystal3
return

label LilaDidntGetCut:
    "Liam's affection goes up."
    scene image "Cave.png" with fade
    show Emma angry at emmaflip with dissolve
    show Lila Sweats at left with dissolve
    show Liam default at right with dissolve
    L "I rather not do that."
    "I said and pulled my hand away from the crystal."
    show Emma sigh with dissolve
    show Liam smile with dissolve
    show Liam default with dissolve
    show Liam smile with dissolve
    fa "For once you didn't make a dumb choice."
    hide Liam smile with dissolve
    hide Emma sigh with dissolve
    hide Lila Sweats at left with dissolve
jump menu_Crystal3
return

label TouchCrystalEvenAfterBite:
    $Crystal3_TouchAfterTaste = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    show Liam default at right with dissolve
    "I wanted to touch the Crystal but Liam's face popped up in my head."
    show Liam dark smile with dissolve
    show Liam default with dissolve
    show Lila shocked with dissolve
    show Lila Sweats with dissolve
    "I rather not piss him off again."
    hide Lila Sweats with dissolve
    hide Liam default with dissolve
    hide Emma concern at emmaflip with dissolve
jump menu_Crystal3
return

label Listen3:
    $Crystal3_Listen1 = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    show Liam default at right with dissolve
    L "Do you think it'll make some kind of sound?"
    show Liam surprised with dissolve
    show Liam default with dissolve
    fa "What?"
    show Emma sigh with dissolve
    fa "Of course no-"
    show Liam smirk with dissolve
    fb "It does."
    show Lila surprised with dissolve
    show Emma surprised with dissolve
    L "OOOOOOOOOOO!"
    show Lila happy with dissolve
    L "What kind of sound???"
    show Liam smile with dissolve
    fb "Why don't you give it a listen?"
    show Emma concern with dissolve
    show Lila eyes closed with dissolve
    "Getting excited I leaned in to listen."
    show Lila surprised with dissolve
    L "Huh?"
    show Lila swirly eyes with dissolve
    "Am I missing something?"
    "I don't hear anything?"
    show Liam laugh with dissolve
    show Emma nervous with dissolve
    "Also why is Liam laughing?"
    hide Emma nervous with dissolve
    hide Liam laugh with dissolve
    hide Lila swirly eyes with dissolve
jump menu_Crystal3
return

label TasteNormal3:
    $Crystal3_TasteNormal = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    show Liam default at right with dissolve
    show Emma panic with dissolve
    "I wanted to lean in to taste the Crystal but Emma pulled my hair."
    show Liam shocked with dissolve
    show Liam nervous with dissolve
    show Liam smile with dissolve
    show Emma angry with dissolve
    show Lila pain with dissolve
    fa "Oh no you don't."
    L "Ow!"
    show Lila swirly eyes with dissolve
    L "Emma that hurts."
    show Emma envy with dissolve
    fa "You say that yet you were about to do something that will be even more painful."
    show Lila Sweats with dissolve
    L "?"
    hide Lila Sweats with dissolve
    hide Emma envy with dissolve
    hide Liam smile with dissolve
    menu:
        "Don't listen to Emma.":
                jump LiamIsMad
        "Listen to Emma":
                jump LilaDidntBiteIt
return

label LiamIsMad:
    $Crystal3_TouchAfterTaste = True
    $Crystal3_TouchNormal = False
    "Emma's affection goes down. Liam's affection goes down."
    scene image "Cave.png" with fade
    show Emma angry at emmaflip with dissolve
    show Liam default at right with dissolve
    show Lila Sweats at left with dissolve
    L "Ok..."
    show Lila smile with dissolve
    L "You can please let go I promise I won't do it."
    show Lila Sweats with dissolve
    show Emma nervous with dissolve
    fa "You promise?"
    show Lila smile with dissolve
    L "Yeah."
    show Lila Sweats with dissolve
    show Emma sigh with dissolve
    fa "Ok."
    show Emma panic with dissolve
    "Emma said as she lets go but I went for it anyways."
    show Liam shocked with dissolve
    show Liam nervous with dissolve
    show Liam smile with dissolve
    show Emma yell with dissolve
    fa "LILA!"
    "She shouted as my mouth was intches away from the crystal."
    show Emma shocked with disslove
    show Lila shocked with dissolve
    "But before I can bite it I felt an strong force pull me backwards."
    show Lila pain with dissolve
    show Emma nervous with dissolve
    fb "Why do you have to be so stuborn sometimes?"
    show Liam sigh with dissolve
    fb "Try that again and I might have carry you back to the village."
    show Liam dark smile with dissolve
    show Lila shocked with dissolve
    show Lila nervous with dissolve
    "Liam made a scary face and my shoulder where he touched me hurts."
    show Lila pain with dissolve
    fa "Geez."
    show Liam nervous with dissolve
    show Liam smile with dissolve
    show Emma sigh with dissolve
    show Lila nervous with dissolve
    fa "Don't do that again."
    show Emma nervous with dissolve
    fa "I nearly had an heart attack."
    hide Emma nervous with dissolve
    hide Lila nervous with dissolve
    hide Liam smile with dissolve
jump menu_Crystal3
return

label LilaDidntBiteIt:
    "Emma's affection goes up. Liam's affection goes up."
    scene image "Cave.png" with fade
    show Emma angry at emmaflip with dissolve
    show Liam default at right with dissolve
    show Lila Sweats at left with dissolve
    "I just got along well with Emma."
    "Let's not ruin that."
    L "Ok."
    show Liam smile with dissolve
    show Liam default with dissolve
    show Liam smile with dissolve
    show Lila smile with dissolve
    L "I understand."
    show Emma nervous with dissolve
    fa "Do you really?"
    show Lila happy with dissolve
    L "If I don't you can stop me again."
    show Emma embarrassed with dissolve
    fa "I'm not your babysitter."
    show Emma sigh with dissolve
    fa "As long as you understand."
    "She said as she lets go of my hair."
    hide Emma sigh with dissolve
    hide Lila happy with dissolve
    hide Liam smile with dissolve
jump menu_Crystal3
return

label BiteCrystalEvenAfterTouch:
    $Crystal3_TasteAfterTouch = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    show Liam default at right with dissolve
    "I wanted to bite the Crystal but Liam's face popped up in my head."
    show Liam dark smile with dissolve
    show Liam default with dissolve
    show Lila shocked with dissolve
    show Lila Sweats with dissolve
    "I rather not piss him off again."
    hide Lila Sweats with dissolve
    hide Liam default with dissolve
    hide Emma concern at emmaflip with dissolve
jump menu_Crystal3
return

label SmellNormal3:
    $Crystal3_SmellNormal = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    show Liam default at right with dissolve
    L "Will the Crystal smell like anything?"
    show Liam shocked with dissolve
    show Liam smile with dissolve
    show Emma shocked with dissolve
    show Emma concern with dissolve
    fa "What do you think?"
    show Lila swirly eyes with dissolve
    L "Ahhhhhhh..."
    show Lila surprised with dissolve
    L "I will found out!"
    show Lila eyes closed with dissolve
    "I leaned in to sniff it."
    show Liam smirk with dissolve
    fb "What does it smell like?"
    "Liam asked but it does not look like he means it."
    show Lila pout with dissolve
    L "Nothing really."
    show Emma envy with dissolve
    fa "Why do you still entertain her even though you know the answers."
    show Liam wink with dissolve
    fb "Because it's fun."
    show Emma nervous with dissolve
    show Liam laugh with dissolve
    "He started to laugh."
    show Liam surprised with dissolve
    "But it didn't feel bad."
    "It was like a soft laugh."
    hide Liam laugh with dissolve
    hide Emma nervous with dissolve
    hide Lila pout with dissolve
jump menu_Crystal3
return

label SmellAfterTouch3:
    $Crystal3_SmellAfterTouch = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Lila skeptical at left with dissolve
    show Liam sigh at right with dissolve
    L "What will this smell like?"
    show Liam dark smile with dissolve
    show Liam smile with dissolve
    show Lila shocked with dissolve
    show Emma shocked with dissolve
    fb "Your blood."
    "Liam sounded very scary today."
    show Lila nervous with dissolve
    show Emma nervous with dissolve
    "I didn't like that."
    L "Should I still smell it?"
    show Liam dark smile with dissolve
    show Liam intimidating with dissolve
    show Liam smile with dissolve
    fb "I don't know..."
    fb "Why don't you try it?"
    show Emma angry with dissolve
    fa "Knock off Liam."
    show Emma nervous with dissolve
    fa "You're overbearing at the moment."
    hide Emma nervous with dissolve
    hide Liam smile with dissolve
    hide Lila nervous with dissolve
    menu:
        "Smell it anyways.":
                jump SmelledBlood
        "I don't want to piss off Liam more.":
                jump LiamNotPissed
return

label SmelledBlood:
    "I sniffed the Crystal."
    "It smells just like rotten iron."
jump menu_Crystal3
return

label LiamNotPissed:
    "I think it's best if I back off for today."
jump menu_Crystal3
return

#####################Start of Vine 3#########################

label Vine3:
        $LilaFriendsPlusMPathPoints.value += 1
        scene image "CloseupVine.png" with fade
        "Before I could say anything Laim threw a pebble at the vine."
        "The vine started to shake and a lot eyes appeared on it."
        scene image "VinaPlant.png" with fade
        "After the eyes rolled and twisted for a bit it went back to normal."
        scene image "CloseupVine.png" with fade
        "Well..."
        "That was disgusting."
label menu_Vine3:
    scene image "CloseupVine.png" with fade
    $LiamLetLilaBleed.value += 1
    if LiamLetLilaBleed.value >= 1:
        $Vine3_NormalTouch = False
        $Vine3_TouchBleed = True
    menu:
        "Touch it." if Vine3_NormalTouch == True:
                jump TouchVineNormal3
        "Touch it." if Vine3_TouchBleed == True:
                jump TouchVineBleed3
        "Smell it." if Vine3_SmellVineNormal == True:
                jump SmellVineNormal3
        "Bite it." if Vine3_BiteVineNormal == True:
                jump BiteVineNormal3
        "Listen to it." if Vine3_ListenVine == True:
                jump ListenVine3
        "Don't do anything.":
                jump drag_glass3
return

label TouchVineNormal3:
    $Vine3_NormalTouch = False
    scene image "Cave.png" with dissolve
    show Emma surprised at middle with dissolve
    show Lila skeptical at left with dissolve
    show Liam shocked at right with dissolve
    show Liam nervous with dissolve
    show Liam smile with dissolve
    fa "Ew."
    show Emma concern with dissolve
    fa "After seeing that you still want to touch it?"
    fa "Don't."
    show Lila Sweats with dissolve
    L "Why not?"
    L "Will it hurt me?"
    show Liam happy with dissolve
    fb "Maybe?"
    show Lila shocked with dissolve
    L "Huh?"
    show Lila Sweats with dissolve
    "There's no way Liam wouldn't know."
    show Liam smile with dissolve
    show Liam happy with dissolve
    fb "Want to try it for us?"
    show Lila shocked with dissolve
    show Emma shocked with dissolve
    "His smile is almost cruel."
    show Emma angry with dissolve
    fa "I can't believe you'll encourage her to do that."
    menu:
        "Touch it.":
                jump TouchTheGrossVine
        "Grab Emma's hand.":
                jump EmmaProtects
return

label TouchTheGrossVine:
    "Emma's affection goes down."
    scene image "Cave.png" with fade
    show Emma panic at emmaflip with dissolve
    show Liam default at right with dissolve
    show Lila Sweats at left with dissolve
    fa "Wait!"
    "Emma shouted but I still poked the Vine."
    show Emma shocked with dissolve
    show Emma nervous with dissolve
    show Lila panic with dissolve
    show Lila Sweats with dissolve
    hide Lila Sweats with dissolve
    hide Emma nervous with dissolve
    hide Liam default at right with dissolve
    scene image "CloseupVine.png" with fade
    "Both me and Emma braced ourselves for the worst."
    "It started to shake again and eyes appeared again."
    scene image "VinaPlant.png" with fade
    "The eyes looked around once again before closing again."
    scene image "CloseupVine.png" with fade
    show Emma angry at emmaflip with dissolve
    show Liam default at right with dissolve
    show Lila surprised at left with dissolve
    "Hmmm..."
    "It didn't do anything."
    fa "I can't believe you."
    "Emma shouted as she hit me on the head."
    show Lila swirly eyes with dissolve
    L "Ouch!"
    L "I'm sorry!"
    show Lila eyes closed sad with dissolve
    "I shouted back feeling the sting on the top of my head."
    show Emma envy with dissolve
    fa "You better be."
    show Liam laugh with dissolve
    "Liam laughed."
    hide Liam laugh with dissolve
    hide Emma envy with dissolve
    hide Lila eyes closed sad with dissolve
jump menu_Vine3
return

label EmmaProtects:
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Liam default at right with dissolve
    show Lila Sweats at left with dissolve
    "I held onto Emma's hand."
    "At first she was shocked."
    "But then she shocked me by giving me a hug."
    show Emma shocked with dissolve
    show Emma embarrassed with dissolve
    show Lila shocked with dissolve
    show Lila embarrassed with dissolve
    show Emma nervous with dissolve
    fa "I don't know what is up with you today but stop that."
    show Emma angry with dissolve
    fa "You should know this is how she is."
    show Liam blush with dissolve
    show Liam embarrassed with dissolve
    show Liam nervous with dissolve
    fb "I guess I teased a bit too much."
    show Emma concern with dissolve
    fa "Huh?"
    show Emma envy with dissolve
    fa "That was you teasing?"
    show Emma angry with dissolve
    fa "BS."
    show Liam surprised with dissolve
    show Liam nervous with dissolve
    show Liam smile with dissolve
    show Lila happy with dissolve
    "I have no clue what the two were doing but at the moment I felt happy."
    hide Lila happy with dissolve
    hide Liam smile with dissolve
    hide Emma angry with dissolve
jump menu_Vine3
return

label TouchVineBleed3:
    $Vine3_TouchBleed = False
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Liam default at right with dissolve
    show Lila Sweats at left with dissolve
    L "Can I touch this?"
    show Liam intimidating with dissolves
    fb "No."
    show Lila panic with dissolves
    show Lila Sweats at left with dissolves
    show Emma shocked with dissolve
    show Emma nervous with dissolve
    "Liam sounded scary."
    "I think Emma was just as scared because she became very quiet."
    show Liam dark smile with dissolve
    show Liam smile with dissolve
    fb "Is what I want to say but you're going to do it anways... aren't you?"
    "Yet all of a sudden he sounded normal again."
    hide Liam smile with dissolve
    hide Emma nervous with dissolve
    hide Lila Sweats at left with dissolves
    menu:
        "No. I'll listen to you.":
                jump ListenToLiam
        "Yep! I'm going to touch it.":
                jump DidntListenToLiam
return

label ListenToLiam:
    scene image "Cave.png" with fade
    show Emma concern at emmaflip with dissolve
    show Liam default at right with dissolve
    show Lila Sweats at left with dissolve
    L "Nope!"
    show Lila smile with dissolve
    show Emma sigh with dissolve
    L "If you say no touching then I won't touch."
    show Liam happy with dissolve
    fb "Good."
    "Liam said as he smiles."
    hide Liam happy with dissolve
    hide Emma sigh with dissolve
    hide Lila smile with dissolve
jump menu_Vine3
return

label DidtListenToLiam:
    "Emma's affection for Liam goes down. Liam's affection goes down."
    scene image "Cave.png" with dissolve
    show Emma panic at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam dark smile at right with dissolve
    "It was like he read my mind."
    "I reached for the vine."
    hide Liam dark smile at right with dissolve
    hide Lila Sweats at left with dissolve
    hide Emma panic at middle with dissolve
    scene image "CloseupVine.png" with dissolve
    "My blood wrapped hands touched the vine."
    "I felt the vine wrap around me."
    scene image "VinaPlant.png" with dissolve
    "It was so tight breathing became hard."
    "It pulled me closer to it."
    "I suddenly felt very scared."
    scene image "VinaPlantDeath.png" with dissolve
    "Just when I was about to panic Liam cut the vine with his pocket knife."
    scene image "black.png" with dissolve
    "It ripped right through the Vine."
    "The vine screeched making my ears ring."
    "Once I was freed I was so scared I felt my body gave in."
    "I didn't hit the ground because Emma was able to catch me."
    fa "What the hell Liam!?"
    "I heard her shouting."
    fb "She had to learn."
    fa "You could have told her."
    fb "You saw she wouldn't listen."
    fa "Why are you acting like this?"
    "All I heard was them shouting back and forth before my vision faded to black."
    "Lila's route end."
    "Lila fainted."
    "No pages found."
return

label SmellVineNormal3:
    $Vine3_SmellVineNormal = False
    scene image "Cave.png" with dissolve
    show Emma angry at middle with dissolve
    show Lila skeptical at left with dissolve
    show Liam smile at right with dissolve
    L "Can I smell the vine?"
    show Emma surprised with dissolve
    show Emma envy with dissolve
    show Liam surprised with dissolve
    show Liam smile with dissolve
    fa "No-"
    fb "Go ahead."
    show Emma shocked with dissolve
    hide Emma shocked with dissolve
    hide Liam smile with dissolve
    hide Lila skeptical at left with dissolve
    "Liam looks like he's having fun but Emma looks...I don't know to discribe it."
    "I guess since Liam says it's ok...it should be fine to smell it right?"
    menu:
        "Smell it.":
                jump VineSmelled
        "Don't smell it.":
                jump VineNotSmelled
return

label VineSmelled:
    scene image "Cave.png" with dissolve
    show Emma shocked at middle with dissolve
    show Lila skeptical at left with dissolve
    show Liam smile at right with dissolve
    "I sniffed the vine."
    show Lila surprised with dissolve
    L "Oh!"
    show Lila happy with dissolve
    L "It smells so good."
    L "You guys should smell it too."
    show Emma envy with dissolve
    show Emma angry with dissolve
    "Emma was not happy."
    fa "I'll pass..."
    fb "..."
    show Lila pout with dissolve
    "Liam just stood there smiling."
    "I guess that's a no from both ends?"
    hide Lila pout with dissolve
    hide Emma angry with dissolve
    hide Liam smile at right with dissolve
jump menu_Vine3
return

label VineNotSmelled:
    scene image "Cave.png" with dissolve
    show Emma sigh at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam smile at right with dissolve
    "I backed away from the vine."
    show Liam surprised with dissolve
    fb "Hm?"
    show Liam smile with dissolve
    fb "You don't want to smell it?"
    L "I think I'm good."
    show Liam nervous with dissolve
    fb "Well that's a pity..."
    show Liam smile with dissolve
    fb "It actually smells amazing."
    show Lila surprised with dissolve
    "Oh really?"
    show Emma envy with dissolve
    show Emma angry with dissolve
    fa "I don't know why you're being a prick today."
    show Liam nervous with dissolve
    fb "My bad."
    hide Liam nervous with dissolve
    hide Emma angry with dissolve
    hide Lila surprised with dissolve
jump menu_Vine3
return

label BiteVineNormal3:
    $Vine3_NormalBite = False
    scene image "Cave.png" with dissolve
    show Emma shocked at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam shocked at right with dissolve
    L "Is this something I can eat?"
    "Both of them looks as me weridly."
    show Liam nervous with dissolve
    show Emma nervous with dissolve
    fb "I've never heard of someone wanting to eat that..."
    fb "But sure go for it."
    show Liam smile with dissolve
    show Emma shocked with dissolve
    show Emma concern with dissolve
    "Liam sounds like he's faving fun."
    fa "Don't listen to him Lila."
    show Emma sigh with dissolve
    fa "I have no clue why he being such a dingus..."
    show Emma concern with dissolve
    fa "But don't eat that."
    show Emma nervous with dissolve
    fa "It can't be good for you."
    "It one or the other again..."
    hide Emma nervous with dissolve
    hide Liam smile with dissolve
    hide Lila Sweats at left with dissolve
    menu:
        "Eat it.":
                jump AteThePlant
        "Don't eat it.":
                jump DontEatPlant
return

label AteThePlant:
    scene image "Cave.png" with dissolve
    show Emma shocked at middle with dissolve
    show Lila skeptical at left with dissolve
    show Liam smile  at right with dissolve
    "I took a bit of the plant."
    show Emma panic with dissolve
    show Lila panic with dissolve
    "Right when I did Emma pulled me back."
    hide Liam smiled  at right with dissolve
    hide Lila panic with dissolve
    hide Emma panic with dissolve
    scene image "CloseupVine.png" with dissolve
    scene image "VinaPlant.png" with dissolve
    scene image "VinaPlantDeath.png" with dissolve
    "The plant shook like crazy but after a while it went back to normal."
    "The part I took a bit off grew back too."
    scene image "CloseupVine.png" with dissolve
    scene image "Cave.png" with dissolve
    show Emma nervous at middle with dissolve
    show Lila nervous at left with dissolve
    show Liam smile at right with dissolve
    "The two of us waited for something to happen."
    "But the only thing that happened with Liam's laugher."
    show Liam laugh with dissolve
    show Emma angry with dissolve
    show Lila happy with dissolve
    L "It actually taste pretty good."
    L "Want to try it too Emma?"
    "While Liam laughed harder Emma looked pissed."
    "Emma shouted at Liam while I enjoyed the taste of this treat."
    hide Lila happy with dissolve
    hide Liam laugh with dissolve
    hide Emma angry with dissolve
jump menu_Vine3
return

label DontEatPlant:
    scene image "Cave.png" with dissolve
    show Emma angry at middle with dissolve
    show Lila skeptical at left with dissolve
    show Liam nervous at right with dissolve
    L "I think I rather not."
    fb "Well that's disappointing."
    show Liam smile with dissolve
    "Emma looks super upset."
    hide Emma angry at middle with dissolve
    hide Lila skeptical at left with dissolve
    hide Liam smile with dissolve
jump menu_Vine3
return

label ListenVine3:
    $Vine3_ListenVine = False
    scene image "Cave.png" with dissolve
    show Emma concern at middle with dissolve
    show Lila skeptical at left with dissolve
    show Liam smile at right with dissolve
    L "Can I listen to the vine?"
    fb "Go ahead."
    show Emma angry with dissolve
    fa "No."
    show Liam surprised with dissolve
    fa "Please just don't go near it."
    show Liam nervous with dissolve
    show Lila pout with dissolve
    L "I won't go close I just want to listen to it."
    show Emma envy with dissolve
    fa "That is a very contradicting sentence."
    show Liam smile with dissolve
    fb "It's ok."
    fb "Let her."
    fb "I won't let her do anything bad."
    show Emma sigh with dissolve
    fa "Why do I doubt that..."
    show Lila nervous with dissolve
    L "?"
    L "E-Emma..."
    fa "What?"
    show Lila panic with dissolve
    L "It's making a very scary sound."
    show Emma concern with dissolve
    fa "Scary?"
    show Lila nervous with dissolve
    L "Yeah like it's hungry..."
    show Emma panic with dissolve
    fa "That's it."
    show Emma angry with dissolve
    fa "You are staying right besides me."
    fa "Don't you dare go near it."
    hide Emma angry with dissolve
    hide Lila nervous with dissolve
    hide Liam smile with dissolve
jump menu_Vine3
return

#####################Start Opus 3#####################
label Opus3:
    scene image "CloseupOpus.png" with dissolve
    L "Awwww!"
    L "Look at this guy here!"
    L "He's so cute!"
    fa "Yeah there's no way you are going anywhere near it."
    L "But why?"
    L "He's so cute!"
    fa "I can't be bothered to explain."
    "Since Emma don't want to explain I look at Liam for answers."
    "Yet Liam only smiles and says nothing..."
label menu_Opus3:
    $LiamLetLilaBleed.value += 1
    if LiamLetLilaBleed.value >= 1:
        $Opus3_NormalTouch = False
        $Opus3_TouchBleed = True
    menu:
        "Touch it." if Opus3_NormalTouch == True:
            jump TouchOpusNormal3
        "Touch it." if Opus3_TouchBleed == True:
            jump TouchOpusBlood3
        "Smell it." if Opus3_NormalSmell == True:
            jump SmellOpusNormal3
        "Bite it." if Opus3_NormalBite == True:
            jump BiteOpusNormal3
        "Listen to it." if Opus3_Listen == True:
            jump ListenOpusNormal3
        "Don't do anything":
            jump drag_glass3
return

label TouchOpusNormal3:
    $Opus3_NormalTouch = False
    scene image "Cave.png" with dissolve
    show Emma panic at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam smile at right with dissolve
    "I wanted to poke it but Emma grabbed by the hand."
    show Emma angry with dissolve
    fa "Don't touch that!"
    show Lila pout with dissolve
    L "But why?"
    fa "It'll bite you."
    show Lila nervous with dissolve
    L "But it doesn't even have a mouth."
    show Emma envy with dissolve
    fa "Just because you can't see it doesn't mean it's not there."
    show Emma angry with dissolve
    fa "And Liam!"
    fa "Don't just stand there!"
    fa "Help me explain."
    show Liam surprised with dissolve
    show Lila surprised with dissolve
    show Liam smile with dissolve
    fb "I don't see a problem with her touching that."
    show Emma shocked with dissolve
    fa "Wha-"
    show Emma Angry with dissolve
    show Lila panic with dissolve
    show Lila Sweats with dissolve
    fa "Are you insane???"
    show Liam nervous with dissolve
    show Liam smile with dissolve
    fb "Trust me."
    fb "It'll be fine."
    show Emma concern with dissolve
    fa "Are you sure?"
    show Liam wink with dissolve
    fb "Yep."
    show Emma nervous with dissolve
    "Emma finally let's go."
    fa "If you say so..."
    fa "Just saying I still think it's a not good idea."
    hide Emma nervous with dissolve
    hide Liam wink with dissolve
    hide Lila Sweats with dissolve
    menu:
        "Touch it anyways.":
                jump TouchOpusSafe
        "Don't touch it.":
                jump DidtTouchOpus
return

label TouchOpusSafe:
    scene image "Opus.png" with dissolve
    "I poked the Opus."
    "It bobbled in the water silently..."
    L "AWWWWWWW."
    "It's so cute!"
    fa "I don't know how you can see that as cute."
    fa "It looks ominous to me."
    L "It at least it's harmless."
    scene image "Cave.png" with dissolve
    show Emma concern at middle with dissolve
    show Lila Smiles at left with dissolve
    show Liam dark smile at right with dissolve
    fb "I never said it's wasn't dangerous."
    show Liam smile with dissolve
    show Emma shocked with dissolve
    fa "HA?"
    show Emma envy with dissolve
    fa "You still let her touch that despite knowing that?"
    show Liam nervous with dissolve
    show Liam smile with dissolve
    fb "Well at the moment it won't hurt us."
    show Emma concern with dissolve
    fa "Is that so?"
    show Liam happy with dissolve
    fb "Yep."
    show Emma embarrassed with dissolve
    fa "Would you have done the same to me?"
    show Liam nervous with dissolve
    fb "Hm?"
    show Emma blush with dissolve
    fa "Teasing I mean..."
    fb "I'm not so sure."
    show Liam wink with dissolve
    fb "You wouldn't be as fun to tease."
    show Emma surprised with dissolve
    show Emma embarrassed  with dissolve
    show Emma nervous with dissolve
    show Emma yell with dissolve
    show Liam happy with dissolve
    fa "W-Wha"
    fa "Jerk!"
    show Lila happy with dissolve
    "As they continue to fight I keep poking the Opus."
    hide Lila happy with dissolve
    hide Emma yell with dissolve
    hide Liam happy with dissolve
jump menu_Opus3
return

label DidtTouchOpus:
    scene image "Cave.png" with dissolve
    show Emma smiles at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam sad at right with dissolve
    "I guess it's safer not too."
    "Emma looks relieved."
    "But Liam...looks displeased?"
    hide Liam sad at right with dissolve
    hide Lila Sweats at left with dissolve
    hide Emma smiles at middle with dissolve
jump menu_Opus3
return

label TouchOpusBlood3:
    $Opus3_TouchBleed = False
    scene image "Cave.png" with dissolve
    show Emma panic at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam intimidating at right with dissolve
    "I wanted to poke the Opus but both Liam and Emma grabbed me."
    show Emma shocked with dissolve
    "At first Emma was shocked but she was back to normal soon after."
    show Emma nervous with dissolve
    "She pulls her hand away but Liam kept he's on me."
    fb "If you go any further I'll drag you out of the cave."
    show Lila panic with dissolve
    fb "And I'm not joking..."
    show Emma panic with dissolve
    show Emma nervous with dissolve
    "He's scaring me."
    L "I-I won't touch it."
    show Liam dark smile with dissolve
    fb "Good."
    "He said with a scary smile."
    show Liam smile with dissolve
    show Lila pain with dissolve
    show Lila Sweats with dissolve
    "When he let go of his hand I felt a thob on my shoulder."
    "That hurts."
    hide Liam smile with dissolve
    hide Lila Sweats with dissolve
    hide Emma nervous with dissolve
    jump menu_Opus3
return

label SmellOpusNormal3:
    $Opus3_NormalSmell = False
    scene image "Cave.png" with dissolve
    show Emma shocked at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam surprised at right with dissolve
    L "Can I smell it?"
    show Liam smile with dissolve
    show Emma concern with dissolve
    fa "What?"
    fa "Why?"
    show Lila laugh with dissolve
    L "Just wondering how it smells like."
    show Emma surprised with dissolve
    fa "I guess it should be fine..."
    show Emma dissapointed with dissolve
    fa "You really like to be nosy with these things don't you?"
    show Emma panic with dissolve
    show Lila pout with dissolve
    fa "I can't imagine what would happen if you were in here alone."
    show Emma concern with dissolve
    show Lila smile with dissolve
    "With Emma and Liam watching I don't think this can go wrong."
    show Lila eyes closed with dissolve
    "So I leaned in and sniffed it."
    show Lila surprised with dissolve
    L "Smells like the Ocean."
    show Emma dissapointed with dissolve
    fa "Well that's to be expected."
    fa "It lives in the sea after all."
    show Lila skeptical with dissolve
    L "Why would it be here then?"
    show Emma nervous with dissolve
    fa "How should I know?"
    "I guess she doesn't know everything when it comes to these things."
    hide Liam smile with dissolve
    hide Emma nervous with dissolve
    hide Lila skeptical with dissolve
    jump menu_Opus3
return

label BiteOpusNormal3:
    $Opus3_NormalBite = False
    scene image "Cave.png" with dissolve
    show Emma shocked at middle with dissolve
    show Lila Sweats at left with dissolve
    show Liam smile at right with dissolve
    L "Can I eat this?"
    fb "Hmmmm..."
    show Liam happy with dissolve
    fb "If you want to drown yeah sure."
    show Lila panic with dissolve
    show Emma angry with dissolve
    L "I think I wouldn't want that."
    show Liam smile with dissolve
    fb "Hmmmmm..."
    show Liam happy with dissolve
    show Emma sigh with dissolve
    fb "Then yeah don't eat it."
    "Sometimes I feel like Liam can be very scary if he wants too."
    hide Emma sigh with dissolve
    hide Lila panic with dissolve
    hide Liam happy with dissolve
    jump menu_Opus3
return

label ListenOpusNormal3:
    $Opus3_Listen = False
    scene image "Cave.png" with dissolve
    show Emma surprised at middle with dissolve
    show Liam smile at left with dissolve
    show Lila skeptical at right with dissolve
    L "How does this guy sound like?"
    show Liam happy with dissolve
    fb "Want to give it a listen?"
    show Lila happy with dissolve
    show Emma envy with dissolve
    L "Yes!"
    fa "Uh."
    fa "No."
    show Lila surprised with dissolve
    show Lila pout with dissolve
    show Emma nervous with dissolve
    show Liam surprised with dissolve
    "Emma said as she pulled me away from leaning into listen to the Opus."
    show Liam smirk with dissolve
    fb "It'll be fine~"
    show Emma panic with dissolve
    show Emma nervous with dissolve
    fa "Will it?"
    show Liam wink with dissolve
    fb "Yes."
    show Lila happy with dissolve
    L "If Liam says so it should be fine!"
    show Liam surprised with dissolve
    show Liam smile with dissolve
    show Emma dissapointed with dissolve
    fa "Liam can be mischievous at times though."
    show Lila Sweats with dissolve
    L "huh?"
    show Emma sigh with dissolve
    fa "Nevermind if you want to go for it then go for it."
    show Lila surprised with dissolve
    show Lila skepticalwith dissolve
    L "Oh ok."
    "I don't know why Emma is so worried but I leaned in to listen anyways."
    L "?"
    "I hear gruggling?"
    show Lila panic with dissolve
    "On a second thought I wished I didn't have to hear that."
    hide Lila panic with dissolve
    hide Emma sigh with dissolve
    hide Liam smile with dissolve
    jump menu_Opus3
return

######################START OF PAGE 3##########################

label Page3:
    $LilaFriendsPlusMPathPoints.value += 1
    scene image "CloseupPageCave.png" with fade
    L "Eh?"
    L "Guys there's something on the floor here."
    fa "Huh?"
    "Even Liam looks interested."
    L "A paper?"
    menu:
        "Pick it up.":
                jump PageFound3
        "Explore more first.":
                jump drag_glass3
return

label PageFound3:
    scene image "CloseupPageCave.png" with fade
    "I picked up the page and looked at it closely."
    "It doesn't look like anything special."
    "Wait..."
    "Hold on....there are symbols on here."
    "It kind of feels a bit warmer then normal paper too."
    scene image "Cave.png" with fade
    show Lila skeptical at left with dissolve
    show Emma surprised at emmaflip with dissolve
    show Liam surprised at right with dissolve
    fb "Let me take a look at it."
    "I handed the paper to Liam."
    show Liam smile with dissolve
    fb "Interesting..."
    fb "It's written in ancient language."
    fb "And it seems to be in code too."
    show Emma envy with dissolve
    show Lila surprised with dissolve
    fa "Oh dang."
    fa "It's already werid for this to appear in a cave."
    show Emma concern with dissolve
    fa "I wonder what it says."
    fb "Hmmmm..."
    fb "Let's head back to the village and hit the library."
    fb "Maybe I'll be able to decode something out of it."
    show Emma dissapointed with dissolve
    fa "I guess that's enough fun today then."
    hide Emma dissapointed with dissolve
    hide Lila surprised with dissolve
    hide Liam smile with dissolve
    show image "Black.png" with dissolve
    "Being drawn to this strange paper we went back to the village."
    "I really wonder what it says...."
    "Lila's route end."
    "Page 1 found."
    "Meanwhile..."
    hide image "Black.png" with dissolve
    show image "Cave.png" with dissolve
    show Mingluo evil with dissolve
    Q "Guess I didn't have to show you after all..."
    show image "Black.png" with dissolve
    Q "The ugly side of your kind."
    Q "It truly disgust me."
    Q "Don't disappoint me..."
    Q "Lila."
return

##############END OF PAGE 3######################
#############END OF CAVE EXPLORING WITH LILA AND FRIENDS############

#label OD1:
    #"Incomplete."
#jump menu_OC1
#return

#label Den1:
      #"Incomplete."
#return

label  SaW1:
    show image "Twopaths.png" with dissolve
    show Lila eyes closed sad at middle with dissolve
    "I stand there waiting."
    "I have no clue how long I waited."
    hide Lila eyes closed sad at middle
    show Lilasad at middle
    "I just know my legs did become tired."
    "My feet was also hurting."
    hide Lilasad at middle
    show Lila eyes closed sad at middle
    "Yet I still waited..."
    "{cps=2}...{/cps}"
    "{cps=2}...{/cps}"
    "Listening to only the sound of bugs I feel the need to sob."
    show Lila tears with dissolve
    "Just when I thought the darkness will shallow me..."
    "From the distance I heard Liam's voice calling out to me."
    show Lila surprised with dissolve
    show Lila relieved with dissolve
    show image "Black.png" with dissolve
    "Lila's route end."
    "No pages found."
return

label  SaW2:
    show image "Twopaths.png" with dissolve
    show Lila eyes closed sad at middle with dissolve
    "I stand there waiting."
    "I have no clue how long I waited."
    "I just know my legs did become tired."
    hide Lila eyes closed sad at middle
    show Lilasad at middle
    "My feet was also hurting."
    "Yet I still waited..."
    hide Lilasad at middle
    show Lila eyes closed sad at middle
    "{cps=2}...{/cps}"
    "{cps=2}...{/cps}"
    "Listening to only the sound of bugs I feel the need to sob."
    "I stay there by myself in the darkness."
    show Lila tears with dissolve
    show image "Black.png" with dissolve
    "Lila's route end."
    "No pages found."
return

label SaW3:
    show image "Twopaths.png" with dissolve
    show Lila happy at left with dissolve
    show Emma concern at emmaflip with dissolve
    L "Let's just wait here."
    show Lila eyes closed sad with dissolve
    L "I don't want to go into the cave."
    show Emma surprised with dissolve
    fa "Hmmmmm...."
    show Emma dissapointed with dissolve
    fa "I guess there's nothing wrong with waiting for a bit."
    show Lila surprised with dissolve
    show Lila blush with dissolve
    "I was a bit surpirsed that Emma went along with what I said."
    "The two of us waited there until our we heard gumbles from our stomachs."
    show Emma embarrassed with dissolve
    show Emma intimidating with dissolve
    show Lila embarrassed with dissolve
    show Lila eyes closed sad with dissolve
    fa "That boy is talking too long."
    show Emma envy with dissolve
    "Emma said with upset."
    show Emma angry with dissolve
    fa "That's it."
    fa "Let's go find him."
    hide Emma angry with dissolve
    hide Lila eyes closed sad with dissolve
    show image "Black.png" with dissolve
    "She said as she grabbed my hand and dragged me along."
    "I let her drag me while I watch her expressions change."
    "I felt this happy feeling."
    "I guess I somehow made up with Emma."
    "The whole way we walked together hand in hand until we found Liam."
    "Lila's route end."
    "No Pages found."
return


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
return
