﻿define L = Character('Lila', color="#ced0ff", image = "Lila")
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
    
    show text "This all works of fiction." with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    
    call screen confirm(message="Rhea contains a lot of bright colors, this may affect individuals who are susceptible to photo sensitivities. Do you want to continue?", yes_action=Return(), no_action=Quit(confirm=False))
    return
define audio.RheaSoundtrack ="audio/RheaSoundtrack.wav"
define audio.RheaMain = "audio/RheaMainMenuMusic.wav"

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
            child "Opus3.png"
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
    L "Have you guys ever wondered what it's like living in a world filled with light?"
    
    show Emma default at flip with dissolve
    show Emma concern at flip with dissolve
    show Liam surprised at right with dissolve
    
    "One of her friends gave her a weird look while the other grew curious."
    "The three of them were deciding who to go first when she popped the question."
    
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
    
    show Lila surprised at left
    L "Ummmm...."
    hide Lila surprised at left 
    
    show Lilasad at left
    L "How do I explain this?" 
    hide Lilasad at left
    
    show Lila happy at left 
    L "Oh I know!"
    
    L "It's like something even more blinding than the Enoki mushrooms!"
    
    show Emma concern with dissolve
    fa "You've lost your head again."
    show Lila surprised with dissolve
    
    show Emma sigh with dissolve
    fa "Can we just focus the game?"
    
    show Liam wink at right with dissolve
    fb "Patience Emma. We have plenty of time."

    show Emma angry with dissolve
    fa "I'm just saying I'm not interested in her make believe fantasy."

    fb "It may be fantasy but it might not be make-believe."
    
    show Emma concern at yflip with dissolve
    fa "Huh?"
    fa "What are you on about?"
 
    show Emma sigh with dissolve
    fa "If you keep leading her on these crazy daydreams..."
    fa "She'll become even more stu-"
    
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
    
    show Lila surprised at left with dissolve
    L "Huh? Thick headed?"
    show Lila pout at left with dissolve
    
    show Liam nervous with dissolve
    fb "Ah!" with hpunch
    fb "Ignore her. Ignore her."
    fb "Let's play!"
    
    #"What do you want to be? The seeker or hidder?"
    
 #######################Start Character Relationship Points####################        
    show Liam wink at right with dissolve
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
    show Lila eyes closed at lilaflip
    L "52"
    L "51..."

    Q "OUCH!" with vpunch
    show Lila shocked at yflip with dissolve
    "Hearing a weird noise I stopped counting."
    "I listened more closely to make sure I wasn't hearing things."
    "There was only silence so I kept counting."
    show Lila eyes closed at lilaflip with dissolve
    L "50"
    L "4-!"

    Q "Ouch! What was that for?" with vpunch
    show Lila shocked at lilaflip with dissolve
    "That sounded like Emma."
    hide Lila shocked at lilaflip with dissolve
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
    fa "Wasn't me."
    
    L "If it wasn't Emma then who was it?"
    L "Liam?"
    
    menu:
        "Ask if Emma is ok.":
            jump EPath1
        
        "Ask if Liam is ok.":
            jump LPath1
return 
#######################Liam VS EMMA Part 1####################     
label EPath1:
    "Emma's affection goes up."
    
    L "Are you sure?"
    L "That sound like you were in pain."
    show Emma blush with dissolve  
    show Emma pout with dissolve
    fa "What pain?"
 
    "I don't know why Emma is acting like this..."
    
    L "Well..."
    
    "Even so if she's hurt she should take care of herself."
    
    L "I have something here that might help y-"
    
    fa "Look." with hpunch
    fa "Thanks for worrying but can you stop being so annoy-"
    
    fb "Ahahahah!"
    fb "You found us!"
    fb "Looks like Emma is the seeker next!"
    
    L "I guess I did."
    
    fa "HUh?"
    fa "This round isn't fair for Liam."
    fa "Recount."
    
    fb "No. No."
    fb "It's fine if I am the seeker."
    fb "There's no need for her to reco-"
    
    fa "This isn't fair."
    fb "She needs to recount."
    
    "I heard Liam sigh."
    "What should I do?"
    
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
    
    L "Was that you Liam?"
    L "Are you ok?"
    
    fb "Hm?"
    fb "How kind Lila."
    fb "I'm perfectly fine."
    
    "Liam showed me a bright smile. I smiled back with relief."
    
    fa "Of course he's fine!"
    fa "I was the one hurt...."
    
    L "Huh?"
    L "I thought you said it wasn't you..."
    
    "I'm so confused. Didn't she say she wasn't hurt but now she is?"
    
    fa "That's it!"
    fa "You're recounting Lila!"
    fa "This round isn't fair!"
    
    L "Huh?"
    
    fb "There's no need for that."
    fb "I can do the counting."
    fb "Let's just take turns."
    
    fa "But that's not fair!"
    fa "You were found because of me."
    fa "So she should just recount and start over."
    
    fb "Emma..."
    fb "Don't be unreasonable."
    
    "What's going on now?"
    "Should I do something?"
    
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
    
    L "Emma your being....."
    L "Um..."
    L "Moronic."
    
    fa "W-"
    fa "What did you just say?"
    
    "Emma's face is bright red."
    
    fa "Do you have any idea what that word means?"
    
    L "Not really but you call me that all the time."
    
    "Emma stares at me weirdly."
    
    fa "She's right."
    fa "You always somehow manage to bring out the ugly in me."
    fa "I-"
    
    fa "I don't want to play anymore."
    
    "She runs off."
    "Liam calls out to her but she doesn't look back."
    "So he runs after her."
    "I feel a wave of worry and run after them."
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
    
    L "Liam you are irrational."
    
    "Both Liam and Emma give her a weird look."
    
    fb "Oh..."
    
    "Liam's face turns red."
    
    fa "How dare y-"
    
    fb "She's right."
    fb "That was very childish of me."
    
    "Emma looks upset puffing up her cheeks."
    
    fa "Why do you still side with her..."
    
    "Liam lets out a sigh."
    
    fb "That's not it."
    fb "I should have asked."
    fb "What do you want to be Lila?"
    
    menu:
        "Seeker again.":
               jump Seeker1
        "Hidder.":
                jump Hidder1
return

#######################Liam And Emma Offended#####################

label Hidder1:
    L "I want to hide this time."
    
    fa "Then say so in the first place."
    
    "Emma sounds bitter."
    "Liam doesn't say anything and just sliently counts"
    "Soon after Emma starts to run."
    "I want to follow Emma but she runs too fast."
    "I couldn't keep up."
    "I took a while to catch my breath."
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
    L "I want to seek again."
    
    fa "Then say so in the first place."
    
    "Emma sounds bitter."
    "Liam doesn't say anything and just quietly went to hide."
    "Soon after Emma followed behind."
    "I look on as the backs of my friends dissappear into the woods."
    "My heart started to hurt."
    "Feeling awful I decided to follow them."
    "But I can't catch up."
    "I took a while to catch my breath."
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
    
    L "I also want Liam to be the seeker this time!"
    
    "Emma eyes widen."
    
    fa "I just said that it was unfair for Liam."
    fa "Are you de-"
    
    "For a second I thought that Emma is going to blow up."
    "Yet Liam's calm voice settled my nerves."
    
    fb "It's ok Emma. "
    fb "It would be more fair if I play as the seeker next."
   
    fa "I guess it's only fair."
    fa "You're so obvious..."
    
    "I watch as Emma leaves."
    "I've known her for some time now."
    "I have no clue when she became like this."
    "It almost feels bitter."
    "Did something happen to cause her to be like this?"
    
    fb "Aren't you going to hide?"
    
    "Liam asks me."
    "But I don't want to hide yet."
    "I want to sort something out."
    "But should I wait till the game is over?"
    
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
      "I didn't say anything."
      "I just walked up to Emma and gave her a tight hug."
      
      fa "W-What?!"
      
      "Emma looks at me puzzled."
      "Liam seems to have the same look as her."
      
      fa "What are you doing?"
      
      L "I don't know."
      L "Just felt like you need a hug."
      
      fa "Get off me."
      
      "Emma says with her face bright red."
      
      L "No."
      L "I want to stick with you."
      
      fa "What are you? A kid?"
      
      "Emma says still trying to push me away."
      "Liam laughed."
      
      fb "Look at you guys!"
      fb "Being so cute."
      
      "Emma's face turns to a brighter red."
      
      fa "C-cut-cu."
      
      "Emma doesn't seem to know what to say."
      
      fb "Looks like it's decided!"
      fb "You guys should go hide together."
      
      fa "What?!"
      fa "Who said I want to hide wi-"
      
      "Emma looks at me."
      "I look back."
      "She stares at me for a bit."
      "Then she sighs."
      
      fa "Come on let's go."
      "She said as she dragged me away from Liam."
      
      fb "Have fun!"
      "Liam shouts."
      
      fa "Shut up and start counting!"
      
      "Emma shouts back."
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
    "I puffed my chest and walked up to Liam."
    "I grabbed his hand as his eyes widened."
    
    fb "Uh..."
    fb "Lila? W-W-What a-are-"
    
    "Liam's face is bright red but before he can finish his sentence Emma shouts."
    
    fa "WHAT ARE YOU DOING?"
    
    "Her face is also bright red but she looks pissed."
    
    fa "Take your han-"
    
    "I grab her hand next and put it on top of Liam's."
    "The red on their faces fade."
    "They both look at me weridly."
    
    L "Let's stop playing..."
    L "Let's go exploring instead!"
    
    fa "What?"
    
    "I take them into the forrest with me."
    
    fa "But why?"
    
    "Liam stays quiet."
    
    L "I just felt like it."
    L "I didn't like how you guys were acting."
    
    "Emma and Liam looked at each other."
    "They blush."
    "After a while they start to laugh."
    
    L "What's so funny?"
    
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
    
    "I do not like how the two of them are acting."
    "So while they were busy doing that I decided to wonder on my own."
    "I think it's best to give them so space."
    "I'll come back after they have cooled down."
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
    L "I'm going!"
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
    "I don't think Emma will answer me if I asked her."
    "I'll ask just ask Liam."
    L "I have a question Liam."
    fb "Hm?"
    fa "About the game?"
    L "No..."
    L "It's about Emma."
    fa "Emma?"
    L "Yeah."
    L "Why does she talk to me that way?"
    fb "What way?"
    "Liam has a smile on his face but I sense an some kind of other emotion in his eyes."
    L "I don't know."
    L "It's hard to explain it."
    fb "I think you're overthinking again."
    fb "It's ok not to think about it.."
    L "I guess so..."
    "I guess even Liam doesn't know."
    L "Thanks for talking to me!"
    L "I'll go hide now!"
    "I said running away."
    fb "Have fun and don't get lost!"
    L "Got it!"
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
    "I think I'm overthinking again."
    "As I heard Liam's coutdown I started to run."
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
    "Just thinking about the atmosphere within the cave sent a silver down Lila’s spin."
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
    show Lilasad at middle with dissolve
    L "Oh..."
    L "Looks like there's alot stuff in the cave that I've never seen before."
    L "I guess I can explore for a bit..."
    "I'm curious about finding new things."
    "But what happened to me and my friends still bothers me."
    "Drag the magnifying glass to the objects you wish to interact with."
    
label drag_glass:
    call screen slide_glass_screen   
    "[glass] picked the [object]. Do you want to take a closer look at the object?"
    
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

#######Object Drag 1############
######Start of Crystal 1#########

label Crystal1:
    "The crystal glows brightly within the dark cave."
    "It's edges glistens just like Liam's pocket knife."
    "Even so there seems to be more to the crystal."
    $MPath1Points.value += 1
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
    "I tried to bite the crystal but the minute my tongue touched it I felt a sharp pain."
    "There was a taste of iron in my mouth."
    "It seems like there's a warm liquid dripping."
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
     "I bite into the crystal."
     "I felt it slice my tongue."
     "I quickly pulled back."
     
     L "Ow-"
     
     "When I open my mouth I felt the pain again."
     "I think it's best to not talk for now."
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
    "My nose barely touched the edge of the crystal."
    "I sniffed it."
    "It smells like nothing."
    $Crystal_SmellNormal = False
jump menu_Crystal1
return

label SmellAfterTaste :
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
    "I poked the Vine."
    "It sways back and forth."
    "Then it starts to shake."
    "After a while alot of eyes appeared."
    "All of them were staring at me."
    "I felt scared even after the eyes all closed again."
    $Vine_NormalTouch = False
    $VineTouchPoints.value += 1
    if VineTouchPoints.value >= 1:
        $Vine_TouchWithEyes = False
        $Vine_SmellWithEyes = True
        $Vine_SmellNormal = False
        $Vine_BiteWithEyes = True
        $Vine_NormalBite = False
    jump menu_Vine1     
    
label TouchVineBleed:
     "I poked the Vine."
     "The blood on my hands stained it's green color."
     "It sways back and forth."
     "Then it starts to shake."
     "After a while alot of eyes appeared."
     "All of them were staring at me."
     "The blood that was on it got sucked in by the vine."
     "I felt scared."
     "There was an urge to run."
     "Yet when I turned around to leave I fall flat on my face."
     "Vines with eyes have wrapped around on my leg."
     "The only thing I remember seeing was the large mouth that has appeared."
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
    L "Dear god..."
    "I prayed and poked the vine."
    "It started to shake again even harder this time."
    "I close my eyes and felt myself shake."
    "{cps=2}...{/cps}"
    "{cps=2}...{/cps}"
    "Nothing happened."
    "When I open my eyes again I felt like I was being mocked by the eyes."
    "I frowned after the eyes disappeared."
    $VineTouchPoints.value += 1
    if VineTouchPoints.value >=1:
        $Vine_SmellNormal = False
        $Vine_BiteWithEye = True
        $Vine_NormalBite = False
    jump menu_Vine1  
return 

label VineNo1:
    $Vine_TouchWithEyes = False
    "I let out a breath of relief."
    jump menu_Vine1  

label SmellVineNormal:
    $Vine_SmellNormal = False
    "I leaned in to smell the vine."
    "It smelled like fresh grass."
    jump menu_Vine1 
 
label SmellVineWithEyes:
    $Vine_SmellWithEyes = False
    "I lean in to smell the vine."
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
    "I sniffed the vine."
    "It was a very sweet smell."
    "It made me feel hungry..."
    "Very hungry."
    jump menu_Vine1 
return 

label VineNo2:
    "I felt a sense of relief."
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
    "I took a bite of the vine."
    "There was a fresh feeling in my mouth."
    "It didn't taste bad."
    "But it didn't take long for me to regret doing that."
    "I nearly choked on what I was chewing."
    "I saw a bunch of eyes on the vine staring at me."
    "Even after they closed back up I felt a chill down my spin."
    jump menu_Vine1
    
label BiteVineWithEyes:
    $Vine_BiteWithEyes = False
    $VineTastePoints.value += 1
    
    if VineTastePoints.value >= 1:
        $Vine_NormalTouch = False
        $Vine_SmellNormal = False
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
    "I gluped and took a bite of the vine."
    "Even though it tasted pretty good it was hard to shallow."
    "I felt it wiggle as it enters my mouth."
    "Besides feeling pretty grossed out nothing major happened..."
    jump menu_Vine1
    
label Vine_No3:
    "I felt a sense of relief."
    L "Huh?"
    "Is it just me or did the vine look upset..."
    "What was the word?"
    "Disappointed?"
    jump menu_Vine1

label BiteVineWithBlood:
    $Vine_BiteBleed = False
    "This gives me a unsettling feeling."
    "But I still bit into the vine."
    "The moment my mouth touched the vine a very sweet scent knocked my senses numb."
    "I felt the cuts inside my mouth painful yet I couldn't move."
    "More like I didn't want too."
    "I felt unwanted tears flow down my eyes."
    "The last thing I saw was a bunch of eyes staring down at me."
    "A gaint mouth opening before the tears over took my sight."
return 

label ListenVine:
    $Vine_ListenVine = False
    "I leaned in close to listen."
    "There was this knot in my stomach when I heard werid noise coming from the vine."
    "It sounded like something wet was moving around."
    "I think I might just faint if I stay here any longer then I should."
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
    "I poked the blob."
    "It felt slimy."
    "It's just contuines to bobble in the water."
    $Opus_NormalTouch = False
    $OpusTouchPoints.value += 1
    if OpusTouchPoints.value >= 1:
        $Opus_Listen = False
        $Opus_ListenAfterTouch = True
    jump menu_Opus1
return 
    
label TouchOpusBlood:
    $Opus_TouchBleed = False
    "I wanted to poke the blob."
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
    "I felt a wave of nerves as my hand touched the blob."
    "Before I know it my hand was no longer in sight."
    "The last thing I saw before everything faded to black..."
    "Was a gaint mouth soaked in the color red."
    "Lila route end."
    "No pages found."
return    

label OpusNo1:
    "I pulled my hand back in relief."
    "The eyeball on the blob that was staring at me was no longer there."
    L "Ew."
    "I shiver at how gross it was."
    jump menu_Opus1   
return 

label SmellOpusNormal:
    $Opus_NormalSmell = False
    "I leaned in close to smell the blob."
    "It kind of reminds me of the sea."
    "Fresh and salty."
    jump menu_Opus1  
return 

label SmellOpusBlood:
    $Opus_SmellBleed = False
    "I leaned in close to smell the blob."
    "A drop of the blood from my mouth dripped onto the blob."
    "It started to shake and I felt my legs gave in."
    "I don't care about how it smells like."
    "I stared at it's third eye and gaint mouth."
    "I wanted to scream but the pain in my mouth stop me from doing so."
    "Pain was all I remember when it dragged me into the water."
    jump menu_Opus1  
return 

label BiteOpusNormal:
    $Opus_Normalbite = False
    "I was feeling a bit hungry."
    "I stared at the Blob that seemed harmless."
    "Won't hurt if I took a bit right?"
    "I leaned in to take a bite."
    "Before my mouth can touch the blob I lost all of my senses."
    "The only thing I felt was pain."
    "Lila route end."
    "No pages found."
return 

label BiteOpusBleed:
    $Opus_BiteBleed = False
    "I was going to lean in to bite the blob."
    "Yet when I opened my mouth I felt a sharp pain and pulled back."
    "Seems like the inside of my mouth is really hurt."
    L "?"
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
    "I leaned in to bite the blob even with the pain in my mouth."
    "Before my mouth can touch the blob I lost all of my sense."
    "The only thing I felt was pain."
    "Lila route end."
    "No pages found."
return    

label OpusNo2:
    "I quickly leaned back from the blob."
    "I felt a wave of relief."
    jump menu_Opus1  
return     

label ListenOpusNormal:
    $Opus_Listen = False
    "I listened to the blob."
    "I think I'm hearing some kind of bubble?"
    "Maybe soft popping sounds?"
    jump menu_Opus1  
return     
 
label ListenOpusAfterTouch:
    $Opus_ListenAfterTouch = False
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
    "It felt just like paper."
    "But it wasn't smooth."
    L "What's so special about this paper?"
    Q "It's more significant then you."
    Q "That's for sure."
    "HUH?"
    "I jumped when I heard a voice."
    "I when I turned around I found out it was from my spirit."
    L "MINGLOU!"
    L "You came out again without my spiritual energy."
    m "I'm surprised you even know what that means."
    L "I'm not that dumb."
    m "At least you are aware of that."
    "I was speachless."
    m "Anyways"
    m "what are you doing here by yourself?"
    m "You usually stick to those two unbearably suffocating brats."
    L "I-"
    "I didn't want to tell her about my fight with my friends."
    m "I guess you don't want to tell me."
    L "It's not like that."
    L "I-"
    m "Well it's not my concern."
    "Then why did she ask?"
    m "I'm more interested in that treasure you're holding."
    L "What?"
    "She pointed to the page."
    L "This???"
    m "That's right."
    m "'This'."
    "She said as she takes the paper from my hands."
    L "What can be interesting about this?"
    m "Hmmmm I do wonder..."
    L "Can't you just tell me?"
    m "Nope."
    L "Then what should I do with it?"
    m "Think about it yourself."
    "She said as she gave the paper back to me."
    L "Huh?"
    L "But how-"
    "Before I can even question she was gone again."
    L "I hate it when she leaves me off like this."
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
    "I was about to pick up the paper but a forced pulled my hand back."
    Q "Don't You Dare Touch That!"
    L "Ouch!"
    "They pulled my hand back with such force that it hurts."
    "I turned to see Minglou with a very scary face expression."
    "I shivered as she lets go of me and grabs the paper like an animal."
    L "Minglou????"
    "What is she doing here?"
    "She didn't even pay attention to me and only focuses on the paper."
    L "H-hey..."
    L "What are you doing?"
    "I asked as she glared at me."
    m "Nothing..."
    "That did not look like nothing..."
    "After she checked the over until she's satisfied she picked it up."
    m "You are not touching this sacrad treasure with those filthy hands."
    L "Huh?"
    "I was so confused by her action and words."
    L "I won't touch it if you tell me not too..."
    "She looks at me with doubt."
    "But she sighs after a long silence between us."
    m "Listen closely Lila."
    L "Yeah?"
    "I asked trying to break this tension."
    m "I need you to go to the village to heal up-"
    L "Are you worried for me?!"
    "I asked in excitement."
    "Despite being with me since I was a kid"
    "She's never been worried about me before."
    "This is a first."
    m "Uh- Y-Yeah I'm worried."
    m "So get cleaned up and come find me ok?"
    L "Ok!"
    L "Wait for me I'll be right back!"
    "I shouted and headed back to the village."
    "Wait..."
    "She wanted to me to find her afterwards but why?"
    "Oh well."
    "Either way I'll think about it later."
    "Let's get cleaned up first and then go find her."
    "Lila's route end."
    "Page 1 found."
    "Meanwhile..."
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
    L "Hmmmm."
    L "I can't really see much from here."
    fa "Not sure what's there to see."
    fa "Looks like a normal cave to me."
    fa "Wait..."
    fa "I guess the amount of crystals formulated is a bit werid."
    
    $C_Sight1 = False
jump menu_OC2
return 

label Smell2:
    L "Do you smell anything but fresh grass?"
    fa "Nope."
    
    $C_Smell1 = False
jump menu_OC2
return 

label Feel2:
    L "I don't like this feeling."
    fa "What feeling?"
    L "You don't feel it?"
    L "Something about this cave is very werid."
    fa "I have no clue what you are on about."
    "I guess it's just me."
    
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
    fa "Nothing..."
    fa "Just explore no worries."
    L "Oh ok..."
    "Well since Emma said so I might as well."
    "Drag the magnifying glass to the objects you wish to interact with."
    
label drag_glass2:
    call screen slide_glass_screen   
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
    "I reached out my hand to touch the crystall."
    "But before my finger even came close to touching it Emma stopped me."
    fa "Just what do you think you're doing."
    L "Touching the crystal..."
    fa "I know that!"
    fa "Are you dumb?"
    fa "I just said this thing is sharp."
    "Oh no."
    "Looks like Emma's mad."
    "What should I do?"
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
    "I slapped away Emma's hand and grabbed the crystal."
    L "OW!"
    "I pulled back right after grabbing it."
    "My whole hand is in pain."
    fa "YOU IDIOT."
    "Emma shouted and grabbed my hand."
    fa "Where's your medication case?"
    "I felt tears at the edge of my eyes as I start to sob."
    fa "Forget it."
    fa "I also carry some first aid on me."
    "Emma said as she whipe something cold on my cuts and wraps a white rope around me."
    fa "This should do for now."
    fa "Why don't you ever listen."
    fa "Geez."
    L "Thank you."
    fa "Instead of saying thank you and sorry learn not to be so stupid."
    "She said as she knocked me on the head."
    L "Ouch."
    fa "Hmf."
    "Emma sighed."
    "This kind of feels familiar."
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
    L "I'm sorry."
    "I said as she let's go of my hand."
    fa "I wish you stopped this foolish act instead of always saying sorry this and sorry that."
    L "So-" 
    fa "Ok stop."
    fa "Go on have your fun."
    fa "Who knows how long we have until we have to leave."
    L "Ok."
    "At least she's not as harsh before."
    jump menu_Crystal2 
return 

label CrystalTasteStopped:
    $Crystal2_TasteStopped = False
    "Feeling guilty I wanted to slice my finger too."
    "Maybe she'll feel less mad if I share my pain with her..."
    fa "Don't even think about it."
    L "?"
    fa "I see the that glitter in your eyes."
    fa "I just stopped you from biting this crap and you want to touch it now?"
    fa "I just showed you what happens if you touch this."
    fa "Want me to show you again?"
    "Emma showed me her wrapped bloody finger."
    L "No..."
    L "Sorry.."
    "I truely felt bad."
    fa "For god's sake."
    "She sighed again."
    jump menu_Crystal2 
return     
    
label Listen2:
    $Crystal_Listen1 = False
    "I leaned in to listen to the crystal."
    fa "{cps=2}...{/cps}"
    fa "What are you doing?"
    L "Shhhhh. "
    L "I listening to the crystal."
    L "If you talk I can't hear."
    fa "I swear you were dropped as a baby."
    L "Hm?"
    L "You said something."
    fa "Nothing."
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
    
    "I wanted to lean in to bite the crystal but Emma pulled me back by my hair."
    L "Ow! Ow! Ow!"
    L "Emma you are hurting me!"
    L "Please stop!"
    fa "You think this is painful?"
    "She said as she lets go."
    fa "You were about to do something even more painful."
    L "Huh?"
    "I questioned rubbing my head."
    fa "UGHHHHHHHH."
    fa "I don't understand how you can be so airheaded."
    fa "Watch this you idiot."
    "Emma stated and bit her lips."
    "Then she took her finger and slices it on the crystal."
    fa "Look."
    "I felt pale as Emma shoved her bleeding bleeding finger to me."
    L "Emma!"
    L "You're bleeding!"
    "I wanted to reach out to help her but stopped after seeing how she's already preparing to take care of the cut."
    fa "Worry about yourself."
    fa "To think you were gonna bite that."
    fa "Idiotic."
    "Emma said frowing."
    "I felt an awful feeling rising in me."
    L "Sorry..."
    "Emma didn't say anything."
    "She only let out a sigh."
    jump menu_Crystal2  
return

label TasteAfterTouchBleed:
    $Crystal2_TouchBleed = False
    fa "After all of that drama if you even dare to think about biting this."
    fa "I swear I'll leave the cave and you can get lost forever here."
    "I rather not be alone."
    "And the pain in my hands is stinging really bad."
    "So I am not going to bite that."
    jump menu_Crystal2  
return    

label CrystalTouchStopped:
    $Crystal2_TouchStopped = False
    "Emma's affection goes down."
    fa "What were just sorry for..."
    L "Trying to touch the crystal?"
    fa "What are you about to do?"
    L "{cps=2}...{/cps}"
    L "Sorr-"
    fa "Don't bother."
    fa "You never seem to learn..."
    "Emma looks didn't look happy."
    jump menu_Crystal2 
return     

label SmellNormal2:
    $Crystal_SmellNormal = False
    "I leaned in to sniff the crystal."
    "But I felt a force pull me back."
    "I turned to see Emma's hand on my shoulder."
    fa "What do you think you are doing?"
    L "?"
    L "Smelling the crystal?"
    "Emma looked shocked."
    fa "Is that all you are going to do?"
    L "For now yeah?"
    fa "Ok..."
    "Emma said as she let's go of her hand."
    "Still confused I still sniffed the crystal."
    "Smells like nothing."
    fa "Werido."
    L "?"
    fa"..."
    jump menu_Crystal2 
return      

label SmellAfterTouch2:
    $Crystal2_SmellAfterTouch = False
    "I leaned in to sniff the crystal."
    "But I felt a force pull me back."
    "I turned to see Emma's hand on my shoulder."
    fa "Are you for real?!"
    fa "What on earth do you think you are doing?"
    L "?"
    L "Smelling the crystal?"
    "Emma looked shocked."
    fa "Is that all you are going to do?"
    L "For now yeah?"
    fa "Ok..."
    "Emma said as she let's go of her hand."
    "Still confused I still sniffed the crystal."
    "Smells like there's a hint iron"
    fa "I swear..."
    fa "One day you are going to be the cuase of my death."
    L "What?"
    fa"..."
    "Well that felt...Not good."
    jump menu_Crystal2 
return

#######Start of Vine 2###########

label Vine2:
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
    fa "Don't touch that."
    L "But why can't I touch it."
    "Emma sighs."
    "She picked up a pebbled and tosses it at the vine."
    "The vine started to shake and many eyes appeared on it."
    "I felt a shiver go down my spin when the eyes started to move around."
    "After a while the eyes shut back down."
    L "What was that?!"
    "I asked and Emma shooked her head."
    fa "Didn't you learn about this in Bio?"
    L "What?"
    fa "Forget it."
    menu:
        "Touch it anyways.":
                jump TouchVineAnyways
        "Leave it alone.":
                jump LeftVineAlone
                
jump menu_Vine2
return 

label TouchVineAnyways:
    "Emma's affection goes down."
    "I poked the vine when Emma wasn't looking."
    "I started to shake just like before."
    "This time the eyes stared at me and me only."
    "It's like it was making sure I was there before closing again."
    "There wasn't even time to think about what I saw before I felt a hard thob on my head."
    fa "I just told you not to touch it!"
    fa "Are you death?"
    L "But nothing happened!"
    fa "Even so something could have."
    fa "I can't believe you."
    L "I'm sorry..."
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
    "I didn't bother reaching out to the vine."
    "Emma was already glaring at me."
    fa "Don't touch that."
    "The vine started to shake and many eyes appeared on it."
    "I felt a shiver go down my spin when the eyes started to move around."
    "The eyes just stared at us..."
    "Wait no."
    "It was staring mainly at me."
    fa "I'll say it one more time."
    fa "Don't you dare touch it."
    menu:
        "Touch it anyways.":
                jump TouchVineAnyways2
        "Leave it alone.":
                jump LeftVineAlone2
return 

label TouchVineAnyways2:
    "I ignored Emma and touched it."
    "As soon as my finger touched the vine it wrapped itself around me."
    "I couldn't even scream through it."
    "As it keeps twisting and wrapping I saw Emma trying to pull it apart from me."
    "Muffled screams came from Emma as my body pulls towards it."
    "Then all that was left was complete darkness."
    "Compared to the pain on my skin...."
    "I was more regretful for making her show such a face expression."
    "I wished I could have at least said sorry."
    "I smiled and sobbed at the thought of how I'll be scolded this time."
    "Though that don't seem likely."
    "Lila's route end."
    "No pages found."
return

label LeftVineAlone2:
    "I didn't like the way it looked at us."
    "Best to leave it alone."
    "As I backed away from it the eyes on the vines slowly shuts off."
    fa "Look at it feeling dissappointed."
    fa "For once you weren't acting dumb."
    "I guess I wasn't the only one who thought it felt kind of upset."
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
    "I didn't bother reaching out to the vine."
    "Emma was already glaring at me."
    fa "Don't touch that."
    L "But why can't I touch it."
    "Emma sighs."
    fa "You're such a bother."
    "She said as picked up a pebbled."
    "A bit of her blood from her finger cute got on to it."
    "Making a painful face she tosses it at the vine."
    "The vine started to shake and many eyes appeared on it."
    "A giant mouth appeared and shollowed the pebble."
    "After a while it spit out the pebble."
    "It's eyes and mouth was no longer there."
    L "What was that?!"
    "I asked and but she only looked dissappointed."
jump menu_Vine2
return 

label TouchVineWithEyes2:
   $Vine2_TouchWithEyes = False   
   "I would but I don't think Emma wants me too."
   "I think I pissed her off enough today."
   fa "..."
   "She's already glaring."
jump menu_Vine2
return    

label SmellVineNormal2:
    $Vine2_SmellVineNormal = False 
    L "I kind of want to smell this."
    fa "Wha-?"
    fa "I guess smelling it won't hurt..."
    fa "I GUESS."
    "Getting a yes from Emma I leaned in to smell it."
    fa "..."
    fa "What does it smell like?"
    L "hmmmmmmmmmmmm..."
    L "Grass."
    fa "I don't have words to discribe you anymore."
    "I smiled back in response to her comment."
    fa "That was not a complement."
jump menu_Vine2
return 

label SmellVineWithEyes2:
    $Vine2_SmellVineEyes = False
    "After seeing that I don't think that's a good idea."
    "I wasn't going to do it but I noticed I have Emma with me."
    L "Can I smell it?"
    fa "Wha-?"
    fa "We just saw how this thing isn't friendly."
    L "Will smelling it hurt me?"
    fa "How would I know?"
    L "But you sound like you know some things."
    fa "I only know that this thing isn't exactly harmless..."
    L "Oh...."
    L "Should I go for it anyways?"
    fa "Huh?"
    L "You'll help me if something happens right?"
    fa "I-I'm not sure."
    fa "I'm not as strong as Liam."
    "hmmmmm..."
    menu:
        "Go ahead and smell it.":
                jump YesSmellWithEyes
        "Don't do it.":
                jump DidntSmell
jump menu_Vine2
return    

label YesSmellWithEyes:
    "I leaned it to sniff the Vine."
    "For a second I thought I saw Emma reach out for me."
    "But when I turned around she only had a worried face."
    fa "H-how does it smell like?"
    "She said but with a blush for some reason."
    L "It smelled very sweet."
    fa "Sweet?"
    L "Yeah."
    L "Makes me a bit hungry."
    fa "That's very unsettling."
jump menu_Vine2
return     

label DidntSmell:
    "I decided to pull back."
    fa "Smart move."
    L "I don't think hurt me though."
    fa "I rather you say 'I know it will not hurt me' before I let you do that."
    L "Why are you acting like Liam?"
    fa "Huh?"
    L "Actually it feels a bit different."
    fa "What are you on about?"
    L "I don't know."
    fa "Weirdo."
jump menu_Vine2
return 

label BiteVineNormal2: 
    L "Should I eat it?"
    L "I am a bit hungry."
    fa "If I were you I wouldn't."
    L "Why?"
    fa "I don't think this thing is edible."
    L "Wouldn't hurt to try right?"
    fa "Ha."
    fa "If you read about it in the books you wouldn't have said that."
    L "What is so dangerous about this vine?"
    L "Is it like...poison?"
    fa "I don't think so..."
    L "I thought you said you know about it."
    fa "I just know it's not safe."
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
    "I took a chunck out of the vine."
    "It tasted pretty good..."
    "Like sweetness melting in my mouth."
    L "H-"
    "I wanted Emma to try it too but before I can even say anything Emma pulled me back with force."
    "Before I know it I was in her arms."
    L "Wha-"
    "I stopped questioning her scared face staring at the vine."
    "When I looked over I noticed that the vine had eyes."
    "The eyes rolled and rolled checking the area until it shut back down."
    L "What was that?"
    "I felt grossed out thinking that this thing is now inside my stomach."
    fa "I'm not sure."
    fa "I just know it triggers on touch."
    fa "And it eats other living things."
    L "Will it eat us too?"
    fa "I don't know."
    fa "Don't go near it anymore ok."
    L "..."
    "I shouldn't make a promise I can't keep."
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
    L "Is this safe to eat?"
    fa "What kind of question is that."
    L "I'm a bit hungry."
    fa "After seeing that you can still think about eating it?"
    L "If I won't kill me I might just eat it."
    fa "That's the thing."
    fa "I don't know if it can."
    L "Doesn't hurt to try... right?"
    fa "I don't think you should."
    "We heard my stomach grumble."
    L "Emma...."
    "Emma gave me a werid look and sighed."
    fa "When you feel like you are done exploring I'll make you something at your house."
    fa "Hold it in until then."
    L "Ok!"
    "I can't wait since Emma is pretty good at cooking."
jump menu_Vine2
return    

label ListenVine2:
    $Vine2_ListenVine = False
    fa "What are you doing?"
    "When I leaned in to listen to the vine Emma was a bit jumpy."
    L "Listening to the Vine."
    fa "Why?"
    L "Just cause."
    fa "There's no way a vine will make any kind of sounds."
    L "Actually it kind of sounds like us when we are hungry."
    fa "Wha-"
    "Emma's face looks a bit pale."
    L "You know..."
    L "Like a grumble?"
    fa "Get away from that thing now!"
    "Emma said as she yanked me away for it."
    L "Ow..."
    L "Why did you do that?"
    "I asked as she let go."
    fa "Don't go near it."
    fa "For now."
    "I guess it is unsettling."
jump menu_Vine2
return    

#######Start of Opus  2###########
label Opus2:
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
    "I wanted to poke the Opus but Emma grabbed my reaching hand."
    fa "Don't think about it..."
    L "But it's so cute."
    fa "If you value your life you'll listen to me."
    menu:
        "Ignore Emma.":
            jump IgnoredEmma
        "Listen to Emma.":
            jump ListenToEmma
return

label IgnoredEmma:
    $Opus2_ListenAfterTouch = True
    "Emma's affection goes down."
    L "I'm sure you're overthinking again."
    "I said as I poked the Opus using my other hand."
    "Although Emma quickly pulled me back afterwards we noticed nothing happned."
    L "See."
    fa "I really hate you..."
    L "EHHHHHHH!"
    L "Why???"
    fa "Just shut up."
    L "You are so mean today."
    fa "I'm like this everyday."
jump menu_Opus2
return        

label ListenToEmma:
   "Emma's affection goes up." 
   L "Ok."
   L "I won't touch."
   L "I'll listen to you."
   fa "Good."
   fa "If only you were like this all the time."
   fa "That would take the burden off my shoulders."
   L "What?"
   fa "Nevermind."
jump menu_Opus2
return       

label TouchOpusBlood2:
    $Opus2_NormalTouch = False
    $Opus2_TouchOpusBlood2 = False
    "I wanted to poke the Opus but Emma grabbed my reaching hand."
    fa "Don't think about it..."
    L "But it's so cute."
    fa "If you value your life you'll listen to me."
    menu:
        "Ignore Emma.":
            jump IgnoredEmma2
        "Listen to Emma.":
            jump ListenToEmma2
return 

label IgnoredEmma2:
    "Emma's affection goes down."
    L "I'm sure you're overthinking again."
    "I said as I poked the Opus using the hand that had the cuts wounds."
    fa "Idiot!"
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
   L "Ok."
   L "I won't touch."
   L "I'll listen to you."
   fa "Good."
   fa "Just stay close to me."
   L "Mhm!"
   "I nodded with a smile."
   "Emma face turned red."
jump menu_Opus2
return       

label SmellOpusNormal2:
    $Opus2_NormalSmell = False
    L "I wonder if it'll smell like salt."
    fa "Don't tell me..."
    fa "Are you going to attempt to smell it?"
    L "Yes?"
    fa "Don't."
    L "But why not?"
    fa "I already told you this thing isn't safe."
    L "Ok..."
jump menu_Opus2
return      

label ListenOpusNormal2:
    $Opus2_Listen = False
    L "Should I listen to it?"
    fa "Why?"
    L "Just wondering what kind of sounds it'll make."
    fa "No."
    L"I guess not."
jump menu_Opus2
return       

#########START OF PAGE 2########################
label Page2:
    $EaMpath1Points.value += 1
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
    L "Yeah."
    L "Let's go!"
    L "I want to know more about it."
    fa "I don't know what's there to know more about..."
    fa "But sure."
    fa "Let's go."
    L "I wonder what waits ahead of us."
    fa "I could just be a normal paper."
    fa "Then again normal paper wouldn't appear in a cave."
    L "Huh?"
    L "Then someone put it there?"
    fa "Maybe."
    fa "Who knows."
    L "Let's find out!"
    fa "Yeah. Yeah."
    fa "Heard you the first time."
    fa "Let's go."
    "Lila's route end."
    "First page found."
return 

label ExploreMore:
    L "Wait no."
    L "I want to see the other things first."
    fa "Suit yourself."
    "Emma said with a sigh."
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
    L "Hmmmm."
    L "Do you guys see anything from here?"
    fa "Not sure what's there to see."
    fa "Looks like a normal cave to me."
    fa "Wait..."
    fa "I guess the amount of crystals formulated is a bit werid."
    "Liam didn't say anything and just watched us with a smile on his face."
    fa "Well whatever we do we should be fine since Liam is here."
    L "True."
    "Emma and me smiled watching Liam's face turn red."
    
    $C_Sight1 = False
jump menu_OC3
return 

label Smell3:
    L "What do you guys think about the smell of this place?"
    fa "You ask the weirdest questions."
    L "What do you think Liam?"
    fb "Hm?"
    fb "I'll go with whatever you think."
    fa "Ugh."
    fa "Favoritism."
    L "Well I think it just smell like grass."
    $C_Smell1 = False
jump menu_OC3
return 

label Feel3:
    L "There's something off putting about the cave."
    fa "Huh?"
    fa "I have no idea what you are talking about."
    fb "Hmmmm..."
    fb "You always did rely on your instincts more then your logic."
    fb "But you are almost are always correct."
    L "?"
    fa "Can't you just speak normally?"
    $C_Feel1 = False
jump menu_OC3
return 

label Sound3:
    L "I don't think there are any other noise besides the sound of insects."
    fa "No duh."
    fa "Otherwise we wouldn't be playing in this area."
    fa "Who knows what's out there lurking in the dark."
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
    fa "For once we agree on somthing."
    L "Huh?"
    fb "Don't worry too much and just explore."
    "Well with Liam and Emma here I'm sure nothing will go wrong."
    "Drag the magnifying glass to the objects you wish to interact with."
    
label drag_glass3:
    call screen slide_glass_screen   
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
    "I reached for the Crystal but Emma grabbed my hand."
    fa "Did you not listen to Liam."
    L "?"
    fa "He just said it'll slice through skin."
    fa "I swear you never learn your lesson."
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
     "Even though I know I will get hurt..."
     "The shiny crystal is all I can see in my eyes."
     "It was just so pretty."
     "I want it..."
     "I pushed Emma away and grabbed the Crystal."
     L "Ouch!"
     fa "Idiot!"
     fa "Look you're bleeding."
     "Emma said as she wrapped a white rag around me."
     fa "Why didn't you stop her?"
     "Emma asked Liam but he only silently smiled."
     fb "Sometimes it's good for her to learn a thing or two on her own."
     "Emma gave him a weird look."
     fa "You're not acting like yourself..."
     fb "Hm?"
     fb "I've always been like this."
     fa "...."
     "Emma gave him a glare."
     "Liam is giving off an awful feeling."
     "I felt so bad I found myself clinging onto Emma."
jump menu_Crystal3
return       

label LilaDidntGetCut:
    "Liam's affection goes up." 
    L "I rather not do that."
    "I said and pulled my hand away from the crystal."
    "I felt Emma sigh."
    fa "For once you didn't make a dumb choice."
jump menu_Crystal3
return   

label TouchCrystalEvenAfterBite:
    $Crystal3_TouchAfterTaste = False
    "I wanted to touch the Crystal but Liam's face popped up in my head."
    "I rather not piss him off again."
jump menu_Crystal3
return     

label Listen3:
    $Crystal3_Listen1 = False
    L "Do you think it'll make some kind of sound?"
    fa "What?"
    fa "Of course no-"
    fb "It does."
    L "OOOOOOOOOOO!"
    L "What kind of sound???"
    fb "Why don't you give it a listen?"
    "Getting excited I leaned in to listen."
    L "Huh?"
    "Am I missing something?"
    "I don't hear anything?"
    "Also why is Liam laughing?"
jump menu_Crystal3
return   

label TasteNormal3:
    $Crystal3_TasteNormal = False
    "I wanted to lean in to taste the Crystal but Emma pulled my hair."
    fa "Oh no you don't."
    L "Ow!"
    L "Emma that hurts."
    fa "You say that yet you were about to do something that will be even more painful."
    L "?"
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
    L "Ok..."
    L "You can please let go I promise I won't do it."
    fa "You promise?"
    L "Yeah."
    fa "Ok."
    "Emma said as she lets go but I went for it anyways."
    fa "LILA!"
    "She shouted as my mouth was intches away from the crystal."
    "But before I can bite it I felt an strong force pull me backwards."
    fb "Why do you have to be so stuborn sometimes?"
    fb "Try that again and I might have carry you back to the village."
    "Liam made a scary face and my shoulder where he touched me hurts."
    fa "Geez."
    fa "Don't do that again."
    fa "I nearly had an heart attack."
jump menu_Crystal3
return      

label LilaDidntBiteIt:
    "Emma's affection goes up. Liam's affection goes up." 
    "I just got along well with Emma."
    "Let's not ruin that."
    L "Ok."
    L "I understand."
    fa "Do you really?"
    L "If I don't you can stop me again."
    fa "I'm not your babysitter."
    fa "As long as you understand."
    "She said as she lets go of my hair."
jump menu_Crystal3
return  

label BiteCrystalEvenAfterTouch:
    $Crystal3_TasteAfterTouch = False
    "I wanted to bite the Crystal but Liam's face popped up in my head."
    "I rather not piss him off again."
jump menu_Crystal3
return 

label SmellNormal3:
    $Crystal3_SmellNormal = False
    L "Will the Crystal smell like anything?"
    fa "What do you think?"
    L "Ahhhhhhh..."
    L "I will found out!"
    "I leaned in to sniff it."
    fb "What does it smell like?"
    "Liam asked but it does not look like he means it."
    L "Nothing really."
    fa "Why do you still entertain her even though you know the answers."
    fb "Because it's fun."
    "He started to laugh."
    "But it didn't feel bad."
    "It was like a soft laugh."
jump menu_Crystal3
return  

label SmellAfterTouch3:
    $Crystal3_SmellAfterTouch = False
    L "What will this smell like?"
    fb "Your blood."
    "Liam sounded very scary today."
    "I didn't like that."
    L "Should I still smell it?"
    fb "I don't know..."
    fb "Why don't you try it?"
    fa "Knock off Liam."
    fa "You're overbearing at the moment."
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
        "Before I could say anything Laim threw a pebble at the vine."
        "The vine started to shake and a lot eyes appeared on it."
        "After the eyes rolled and twisted for a bit it went back to normal."
        "Well..."
        "That was disgusting."
label menu_Vine3:
    if LiamLetLilaBleed.value += 1:
        $Vine3_NormalTouch = False
        $Vine3_TouchBleed = True
    menu:
        "Touch it." if Vine3_NormalTouch == True:
                jump TouchVineNormal3
        "Touch it." if Vine3_TouchBleed == True:
                jump TouchVineBleed3
        "Smell it." if Vine3_SmellNormal == True:
                jump SmellVineNormal3
        "Bite it." if Vine3_NormalBite == True:
                jump BiteVineNormal3
        "Listen to it." if Vine3_ListenVine == True:
                jump ListenVine3     
        "Don't do anything.":
                jump drag_glass3
return

label TouchVineNormal3:
    $Vine3_NormalTouch = False
    fa "Ew."
    fa "After seeing that you still want to touch it?"
    fa "Don't."
    L "Why not?"
    L "Will it hurt me?"
    fb "Maybe?"
    L "Huh?"
    "There's no way Liam wouldn't know."
    fb "Want to try it for us?"
    "His smile is almost cruel."
    fa "I can't believe you'll encourage her to do that."
    menu:
        "Touch it.":
                jump TouchTheGrossVine
        "Grab Emma's hand.":
                jump EmmaProtects
return 

label TouchTheGrossVine:
    "Emma's affection goes down."  
    fa "Wait!"
    "Emma shouted but I still poked the Vine."
    "Both me and Emma braced ourselves for the worst."
    "It started to shake again and eyes appeared again."
    "The eyes looked around once again before closing again."
    "Hmmm..."
    "It didn't do anything."
    fa "I can't believe you."
    "Emma shouted as she hit me on the head."
    L "Ouch!"
    L "I'm sorry!"
    "I shouted back feeling the sting on the top of my head."
    fa "You better be."
    "Liam laughed."
jump menu_Vine3
return      
   
label EmmaProtects:
    "I held onto Emma's hand."
    "At first she was shocked."
    "But then she shocked me by giving me a hug."
    fa "I don't know what is up with you today but stop that."
    fa "You should know this is how she is."
    "Liam smiles with guilt."
    fb "I guess I teased a bit too much."
    fa "Huh?"
    fa "That was you teasing?"
    fa "BS."
    "I have no clue what the two were doing but at the moment I felt happy."
jump menu_Vine3
return         

label TouchVineBleed3:
    $Vine3_TouchBleed = False
    L "Can I touch this?"
    fb "No."
    "Liam sounded scary."
    "I think Emma was just as scared because she became very quiet."
    fb "Is what I want to say but you're going to do it anways... aren't you?"
    "Yet all of a sudden he sounded normal again."
    menu:
        "No. I'll listen to you.":
                jump ListenToLiam
        "Yep! I'm going to touch it.":
                jump DidntListenToLiam
return 
    
label ListenToLiam:
    L "Nope!"
    L "If you say no touching then I won't touch."
    fb "Good."
    "Liam said as he smiles."
jump menu_Vine3
return

label DidtListenToLiam:
    "Emma's affection for Liam goes down. Liam's affection goes down." 
    "It was like he read my mind."
    "I reached for the vine."
    "My blood wrapped hands touched the vine."
    "I felt the vine wrap around me."
    "It was so tight breathing became hard."
    "It pulled me closer to it."
    "I suddenly felt very scared."
    "Just when I was about to panic Liam cut the vine with his pocket knife."
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
    $Vine3_SmellNormal = False
    L "Can I smell the vine?"
    fa "No-"
    fb "Go ahead."
    "Liam looks like he's having fun but Emma looks...I don't know to discribe it."
    "I guess since Liam says it's ok...it should be fine to smell it right?"
    menu:
        "Smell it.":
                jump VineSmelled
        "Don't smell it.":
                jump VineNotSmelled
return 

label VineSmelled:
    "I sniffed the vine."
    L "Oh!"
    L "It smells so good."
    L "You guys should smell it too."
    "Emma was not happy."
    fa "I'll pass..."
    fb "..."
    "Liam just stood there smiling."
    "I guess that's a no from both ends?"
jump menu_Vine3
return   

label VineNotSmelled:
    "I backed away from the vine."
    fb "Hm?"
    fb "You don't want to smell it?"
    L "I think I'm good."
    fb "Well that's a pity..."
    fb "It actually smells amazing."
    "Oh really?"
    fa "I don't know why you're being a prick today."
    fb "My bad."
    "Liam laughed nervously."
jump menu_Vine3
return   

label BiteVineNormal3:
    $Vine3_NormalBite = False
    L "Is this something I can eat?"
    "Both of them looks as me weridly."
    fb "I've never heard of someone wanting to eat that..."
    fb "But sure go for it."
    "Liam sounds like he's faving fun."
    fa "Don't listen to him Lila."
    fa "I have no clue why he being such a dingus..."
    fa "But don't eat that."
    fa "It can't be good for you."
    "It one or the other again..."
    menu:
        "Eat it.":
                jump AteThePlant
        "Don't eat it.":
                jump DontEatPlant
return 

label AteThePlant:
    "I took a bit of the plant."
    "Right when I did Emma pulled me back."
    "The plant shook like crazy but after a while it went back to normal."
    "The part I took a bit off grew back too."
    "The two of us waited for something to happen."
    "But the only thing that happened with Liam's laugher."
    L "It actually taste pretty good."
    L "Want to try it too Emma?"
    "While Liam laughed harder Emma looked pissed."
    "Emma shouted at Liam while I enjoyed the taste of this treat."
jump menu_Vine3
return   

label DontEatPlant:
    L "I think I rather not."
    fb "Well that's disappointing."
    "Emma looks super upset."
jump menu_Vine3
return 

label ListenVine3:
    $Vine3_ListenVine = False
    L "Can I listen to the vine?"
    fb "Go ahead."
    fa "No."
    fa "Please just don't go near it."
    L "I won't go close I just want to listen to it."
    fa "That is a very contradicting sentence."
    fb "It's ok."
    fb "Let her."
    fb "I won't let her do anything bad."
    fa "Why do I doubt that..."
    L "?"
    L "E-Emma..."
    fa "What?"
    L "It's making a very scary sound."
    fa "Scary?"
    L "Yeah like it's hungry..."
    fa "That's it."
    fa "You are staying right besides me."
    fa "Don't you dare go near it."
jump menu_Vine3
return 

#####################Start Opus 3#####################
label Opus3:
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
    if LiamLetLilaBleed.value += 1:
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
    "I wanted to poke it but Emma grabbed by the hand."
    fa "Don't touch that!"
    L "But why?"
    fa "It'll bite you."
    L "But it doesn't even have a mouth."
    fa "Just because you can't see it doesn't mean it's not there."
    fa "And Liam!"
    fa "Don't just stand there!"
    fa "Help me explain."
    fb "I don't see a problem with her touching that."
    fa "Wha-"
    fa "Are you insane???"
    fb "Trust me."
    fb "It'll be fine."
    fa "Are you sure?"
    fb "Yep."
    "Emma finally let's go."
    fa "If you say so..."
    fa "Just saying I still think it's a good idea."
    menu:
        "Touch it anyways.":
                jump TouchOpusSafe
        "Don't touch it.":
                jump DidtTouchOpus
return 

label TouchOpusSafe:
    "I poked the Opus."
    "It bobbled in the water silently..."
    L "AWWWWWWW."
    "It's so cute!"
    fa "I don't know how you can see that as cute."
    fa "It looks ominous to me."
    L "It at least it's harmless."
    fb "I never said it's wasn't dangerous."
    fa "HA?"
    fa "You still let her touch that despite knowing that?"
    fb "Well at the moment it won't hurt us."
    fa "Is that so?"
    fb "Yep."
    fa "Would you have done the same to me?"
    fb "Hm?"
    fa "Teasing I mean..."
    fb "I'm not so sure."
    fb "You wouldn't be as fun to tease."
    fa "W-Wha"
    fa "Jerk!"
    "As they continue to fight I keep poking the Opus."
jump menu_Opus3
return 

label DidtTouchOpus:
    "I guess it's safer not too."
    "Emma looks relieved."
    "But Liam...looks displeased?"
jump menu_Opus3
return    

label TouchOpusBlood3:
    $Opus3_TouchBleed = False
    "I wanted to poke the Opus but both Liam and Emma grabbed me."
    "At first Emma was shocked but she was back to normal soon after."
    "She pulls her hand away but Liam kept he's on me."
    fb "If you go any further I'll drag you out of the cave."
    fb "And I'm not joking..."
    "He's scaring me."
    L "I-I won't touch it."
    fb "Good."
    "He said with a scary smile."
    "When he let go of his hand I felt a thob on my shoulder."
    "That hurts."
    jump menu_Opus3
return    

label SmellOpusNormal3:
    $Opus3_NormalSmell = False
    L "Can I smell it?"
    fa "What?"
    fa "Why?"
    L "Just wondering how it smells like."
    fa "I guess it should be fine..."
    fa "You really like to be nosy with these things don't you?"
    fa "I can't imagine what would happen if you were in here alone."
    "With Emma and Liam watching I don't think this can go wrong."
    "So I leaned in and sniffed it."
    L "Smells like the Ocean."
    fa "Well that's to be expected."
    fa "It lives in the sea after all."
    L "Why would it be here then?"
    fa "How should I know?"
    "I guess she doesn't know everything when it comes to these things."
    jump menu_Opus3
return    

label BiteOpusNormal3:
    $Opus3_NormalBite = False
    L "Can I eat this?"
    fb "Hmmmm..."
    fb "If you want to drown yeah sure."
    L "I think I wouldn't want that."
    fb "Hmmmmm..."
    fb "Then yeah don't eat it."
    "Sometimes I feel like Liam can be very scary if he wants too."
    jump menu_Opus3
return 

label ListenOpusNormal3: 
    $Opus3_Listen = False
    L "How does this guy sound like?"
    fb "Want to give it a listen?"
    L "Yes!"
    fa "Uh."
    fa "No."
    "Emma said as she pulled me away from leaning into listen to the Opus."
    fb "It'll be fine~"
    fa "Will it?"
    fb "Yes."
    L "If Liam says so it should be fine!"
    fa "Liam can be mischievous at times though."
    L "huh?"
    fa "Nevermind if you want to go for it then go for it."
    L "Oh ok."
    "I don't know why Emma is so worried but I leaned in to listen anyways."
    L "?"
    "I hear gruggling?"
    "On a second thought I wished I didn't have to hear that."
    jump menu_Opus3
return 

######################START OF PAGE 3##########################

label Page3:
    $LilaFriendsPlusMPathPoints.value += 1
    L "Eh?"
    L "Guys there's somthing on the floor here."
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
    "I picked up the page and looked at it closely."
    "It doesn't look like anything special."
    "Wait..."
    "Hold on....there are symbols on here."
    "It kind of feels a bit warmer then normal paper too."
    fb "Let me take a look at it."
    "I handed the paper to Liam."
    fb "Interesting..."
    fb "It's written in ancient language."
    fb "And it seems to be in code too."
    fa "Oh dang."
    fa "It's already werid for this to appear in a cave."
    fa "I wonder what it says."
    fb "Hmmmm..."
    fb "Let's head back to the village and hit the library."
    fb "Maybe I'll be able to decode something out of it."
    fa "I guess that's enough fun today then."
    hide Lila happy with dissolve 
    hide Emma surprised with dissolve 
    hide Liam shocked with dissolve
    show image "Black.png" with dissolve
    "Being drawn to this strange paper we went back to the village."
    "I really wonder what it says...."
    "Lila's route end."
    "Page 1 found."
    "Meanwhile..."
    hide image "Black.png" with dissolve
    show image "Cave.png" with dissolve
    show Mingluo no eyes with dissolve
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
    "I stand there waiting."
    "I have no clue how long I waited."
    "I just know my legs did become tired."
    "My feet was also hurting."
    "Yet I still waited..."
    "{cps=2}...{/cps}"
    "{cps=2}...{/cps}"
    "Listening to only the sound of bugs I feel the need to sob."
    "Just when I thought the darkness will shallow me..."
    "From the distance I heard Liam's voice calling out to me."
    
    "Lila's route end."
    "No pages found."
return    

label  SaW2:
    "I stand there waiting."
    "I have no clue how long I waited."
    "I just know my legs did become tired."
    "My feet was also hurting."
    "Yet I still waited..."
    "{cps=2}...{/cps}"
    "{cps=2}...{/cps}"
    "Listening to only the sound of bugs I feel the need to sob."
    "I stay there by myself in the darkness."
    
    "Lila's route end."
    "No pages found."
return 

label SaW3:
    L "Let's just wait here."
    L "I don't want to go into the cave."
    fa "Hmmmmm...."
    fa "I guess there's nothing wrong with waiting for a bit."
    "I was a bit surpirsed that Emma went along with what I said."
    "The two of us waited there until our we heard gumbles from our stomachs."
    fa "That boy is talking too long."
    "Emma said with upset."
    fa "That's it."
    fa "Let's go find him."
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
