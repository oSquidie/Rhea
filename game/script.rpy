define L = Character(_("Lila"), color="#ced0ff")
define m = Character(_("Mingluo"), color="#2e37ff")
define fa = Character(_("Emma"), color="#73fff0")
define fb = Character(_("Liam"), color="#a673ff")
define Q = Character ("?")

#define persistent.Route1 = True
#define persistent.Route2 = True

#define persistent.value = 0

define audio.RheaSoundtrack ="audio/RheaSoundtrack.wav"
define audio.RheaMain = "audio/RheaMainMenuMusic.wav"

play music RheaMain

init:
    transform flip:
        xzoom -1

label start:
    stop music fadeout 1.0
    play music "audio/RheaSoundtrack.wav" fadein 5.0 volume 0.3
    
    #$persistent.Route1 = True
    #$persistent.Route2 = True
    
    default preferences.text_cps = 50
    "Within a planet shrouded by darkness..."
    "In a forest far away from the nearest village."
    "A group of friends gathers to play hide and seek."
    "Whispers can be heard as glimmers of radiance reveals three kids."
    #show Lila happy at flip for flipping the sprite
    
    scene image "Forest_Default.png"
    L "Hey...Have you guys ever wondered what it's like living in a world filled with light?"

    "The three of them was deciding who to go first when Lila popped the question."

    fb "We're already living in a world that’s like that. Aren't we?"

    "Liam seems to be a bit confused on the kind of world Lila envisoned."

    L "No. I don’t mean a world like this one."
    L "Not just tiny slopts of glow here and there."
    L "A world where the entire land, no, the entirety of Rhea is filled by a very, very bright light."

    fa "What are you suddenly talking about?"

    L "You know! Something even more blinding than the glows from an Enoki mushroom!"

    fa "You’ve lost your head again. Can we just focus the game?"

    fb "Patience Emma. We have plenty of time."

    fa "I’m just saying I’m not interested in her make believe fantasy."

    fb "It may be fantasy but it might not be make-believe."

    fa "Huh? What are you on about? If you keep leading her on these crazy daydreams..."
    fa "She’ll become even more stu-"

    fb "I also think we should start playing the game."
    fb "It's been a while since we've gathered. Let's enjoy this rare moment!"

    "Laim did raise his voice but his uplifting tone didn’t change."

    L "Oh... I guess you guys are getting bored."

    "Lila sounded disappointed at their reactions." 
    "But she wasn't disappointed for long."
    "She did miss her friends after all."

    fa "How are you so thick headed for you to realize that just now?"

    L "Huh? Thick headed?"

    "She hates it when Emma uses words she don't understand. It always leave an awful feeling in her."

    fb "Ah! Ignore her. Ignore her. Let's play! What do you want to be Lila? The seeker or hidder?"

    menu:
        "Seeker?": #if persistent.Route1 == True:
            jump Seeker
        #"Hidder?" if persistent.Route2 == True:
            #jump Concealer
return

label Seeker:
    #$persistent.Route1 = False
    #$persistent.value += 1
    #if persistent.value >= 2:
        #$persistent.Route1 = True
        #$persistent.Route2  = True
        #$persistent.value = 0
    "Surrounded by tall trees Lila stood there counting in the dark."
    "The warm glows from the fireflies engulfs her mind as she slowly loses herself in her thoughts." 

    L "55"
    L "54"
    L "53"

    "Each time the numbers go down she feels a bit more lonely than before."
    "Is it because of the darkness?"
    "That can’t be it...She grew up in such an environment." 
    
    L "52"
    L "51..."
    
    Q "OUCH!" with vpunch
    show Lila shocked at left with dissolve
    "Startled, she lost her thought process."
    "She faced the direction where the loud noise came from. "
    "She waited for a few more moments for any kinds of other movement but all she heard was silence."
    "Thinking she may have misheard she went back to counting."
    show Lila eyes closed at left with dissolve
    L "50"
    L "4-!"

    Q "Ouch! What was that for?" with vpunch
    show Lila pout at left with dissolve
    "Once again grabbing her attention she observes from a distance."
    "She was a bit conflicted as to rather or not she should go check up on her friend."
    "After all, She is still in the middle of a game."
    "After thinking for a while, her concerns overpowered her determination to win."
    "She went to investigate the noise."
    show Lila surprised at left with dissolve
    L "Emma?"
    L "Are you ok?"

    fa "I'm fine!"

    "Soon after Emma popped up her other friend Liam popped up as well"
    menu:
        "Are you sure? You sounded like you were in pain.":
            jump YouSure
        "Oh... Are you ok Liam?":
            jump LiamOk
return

label YouSure:
    
    fa "I already said I'm fine."
    hide Lila surprised at left
    show Liladefault at left
    L "I have some medication on me if you nee-"

    fa "Enough! I'm not that weak. Why are you so annoy-!"

    fb "Ahaha! You found us! Looks like Emma is the seeker next."

    "Liam cut Emma off mid-sentence."
    
    L "I guess I did."
    L "But Emma you should still put some ointment on just in case..."

    fa "UGH! I don't need anything."
    fa "Just listen to me."
    fa "This round isn't fair for Liam."
    fa " You should recount!"

    "Although the two should already be used to Emma’s behavior they couldn’t help but be a little bewildered."

    fb "No. no."
    fb "It’s fine."
    fb "I can be the seeker."
    fb "No need for Lila to re-"

    fa "This isn't fair. She needs to recount."

    "Liam sighed."

menu:
    "But I already found you guys":
        jump SeekerL

    "Oh ok! I can be seeker again!":
        jump SeekerLila

return

label SeekerL:
    fb "Lila's right."
    fb "She's already found us."
    fb "It would be more fair if one of us plays as the seeker next."

    fa "..."
   
    "Lila anxiously wondered what she had done this time to bother Emma {cps=2}...{/cps} again. "
   
    fa "Fine."
    fa "But I'm not being 'it'"

    fb "That’s ok. I'll be 'it'. You guys should hide. "
   
    L "I'm sorry Liam..."
   
    "Lila suddenly felt a sense of guilt yet she doesn't know why."
   
    fb "Hm?"
    fb "Why do you feel sorry?"
    fb "Don’t worry." 
    fb "There's nothing to be sorry about."
    fb "You should instead focus on hiding."
   
    "Lila felt conflicted on how to explain this feeling."
    "Before she can even formulate words Liam started to count."
    fb "Are you ready! I’m starting to count!"
   
    "After leaving her with a wink he left her standing there"
   
    fb "100!"
    fb "99!"
    fb "98!"
    hide Liladefault at left with dissolve
   
    "Panicking she went to find a hiding spot."
    "Even after she has left the two of them she couldn’t help but feel a bit awful."
    "Distracted by this feeling, she realized that she may have gone a bit too far."
    "Before she realized she was in an unfamiliar place."
   
    show Lila surprised at left with easeinleft
    L "Oh no...I-I don't remember seeing these paths."
    show Lila pout at left with dissolve
   
    "Catching her breath, she took a moment to frantically look around."
    "From what she could see, to her left was a cave covered in transparent crystals and tiny little glowing fungi."
    "The cave seems endless and very spacious."
    "Besides the cave, to her right was some kind of animal den."
    "Though pitched black inside, the outside is swarmed with fireflies and different kinds of glowing mushrooms."
    "She can't tell what kind of animal made this den but she knows she's big enough to fit through."

    L "Which way should I hide?"

menu:
    "The endless cave":
        jump Cave
    "The animal Den":
        jump Den

return

label SeekerLila:

    fa "See! She wants to be the seeker!"
    
    "Liam looks shocked. While Emma Smirks"
    
    fb "Are you sure? You don’t have to force yourself."
    
    "Lila smiled."
    
    L "I’m not forcing myself."
    L "I just love playing with you guys."
    L "As long as I can play with you guys...I don’t mind what I am."
    
    "Liam’s smile dropped."
    "He thought deeply for a moment while Emma's face showed panic."
    
    fa "Hey Liam."
    fa "She already-"
    
    fb "What if I wanted to be the seeker and I really want to be ‘it’"
    
    "Emma frowned."
    "She knew Liam was going to play with Lila’s heart strings."
    "Even so, she doesn't want to push him any further."
    "Even she knows she’s being childish."
    "She can only pray Lila will reject that idea."
     
    L "Oh {cps=2}...{/cps}Do you really want to be 'it'?"
    
    "Liam smiled."
    
    fa "I definitely do!"
    
    "Lila innocently smiled back."
    
    L "Whatever makes you happy!"
    
    "Emma frowned."
    
    fa "Your favoritism is so obvious and I hate it…"
    
    "Emma grumbled but it was so quiet the other two didn’t hear her."
    
    fb "Ok! I’ll start counting now! Go hide!"
    
    L "Ok!"
    
    "With that the three scattered."
    "Emma and Lila went in opposite directions."
    "Lila continued to explore until she ended up in a place she’s unfamiliar with."
    
    L "I don’t think I’ve been here before."
    
    "Catching her breath, she took a moment to frantically look around."
    "From what she could see, to her left was a cave covered in transparent crystals and tiny little glowing fungi."
    "The cave seems endless and very spacious."
    "Besides the cave, to her right was some kind of animal den."
    "Though pitched black inside, the outside is swarmed with fireflies and different kinds of glowing mushrooms."
    "She can't tell what kind of animal made this den but she knows she's big enough to fit through."
    
    "Despite the danger these do look like good hiding places."
    
    L "Which way should I go"
    
menu:
    "The endless cave":
        jump Cave
    
    "The animal Den":
        jump Den

return

label LiamOk:
    fb "Hm? How kind Lila."
    fb "Don’t worry."
    fb "I’m perfectly fine."
    
    fa "Of course he's fine!"
    fa "I was the one hurt…."
    
    "Emma responded with a frown as she grinded her teeth."
    
    L "But I thought you said you are fine Emma?"
    
    "Lila said with no hostility."
    "She was actually just confused and puzzled."
    "However, for some reason Emma looks even more menacing."
    
    fa "That’s it!"
    fa "You’re recounting Lila!"
    fa "This round isn’t fair!"
    
    L "Huh?"
    
    fb "Now, now."
    fb "There’s no need for that."
    fb "I can do the counting."
    fb "Let’s take turns being the seeker."
    
    fa "But that's not fair!"
    fa "You got found because of me."
    fa "So she should just recount and start over."
    
    fb "Emma, don’t be unreasonable."
    fb " I really don’t mind being the seeker."
    fb "Let’s not fight over something so small."
    
    "Liam explained but he didn't even sound a bit annoyed."
    "Instead, he handled it with patience and sternness."
    "Still Emma refuses to back down."
    "What should Lila do?"
    menu:
        "I’m ok with being seeker again.":
            jump OkSeeker
        
        "I also want Liam to be the seeker this time!":
            jump LiamSeeker
            
label LiamSeeker:
    "Just as the two were about to get heated Lila broke the tension."
    
    fa "I just said that it was unfair for Liam. Are you de-"
    
    "Emma seems like she’ll explode but Liam stopped her with a very calm voice."
    
    fb "It’s ok Emma. It would be more fair if I play as the seeker next." 
    
    fa "...."
    
    "Lila anxiously wondered what she had done this time to bother Emma {cps=2}...{/cps}again."
    
    fa "Fine."
    "Emma grumbled. Her voice sent a bit of fear down Lila’s spin. "
    
    L "I'm sorry Emma...I’m sorry Liam..."
    
    "Lila felt a sense of guilt yet she doesn't know why. "
    
    fb "Hm?"
    fb "Why do you feel sorry?"
    fb "Don’t worry."
    fb "There's nothing to be sorry about."
    fb "You should instead focus on hiding."
    
    "Emma didn’t say anything."
    "She just stood there with a very scary face."
    "Lila felt conflicted on how to explain this feeling."
    
    fb "Are you ready! I’m starting to count!"
    
    "Before she can even explain anything Liam started to count."
    "Panicking she went to find a hiding spot."
    
    fb "100!"
    fb "99!"
    fb "98!"
    
    show Lila surprised at left with easeinleft
    L "Oh no...I-I don't remember seeing these paths."
    show Lila pout at left with dissolve
   
    "Catching her breath, she took a moment to frantically look around."
    "From what she could see, to her left was a cave covered in transparent crystals and tiny little glowing fungi."
    "The cave seems endless and very spacious."
    "Besides the cave, to her right was some kind of animal den."
    "Though pitched black inside, the outside is swarmed with fireflies and different kinds of glowing mushrooms."
    "She can't tell what kind of animal made this den but she knows she's big enough to fit through."

    L "Which way should I hide?"

menu:
    "The endless cave":
        jump Cave
    "The animal Den":
        jump Den

return

label OkSeeker:
    fa "See! She wants to be the seeker!"
    
    "Liam looks shocked. While Emma Smirks"
    
    fb "Are you sure? You don’t have to force yourself."
    
    "Lila smiled."
    
    L "I’m not forcing myself."
    L "I just love playing with you guys."
    L "As long as I can play with you guys...I don’t mind what I am."
    
    "Liam’s smile dropped."
    "He thought deeply for a moment while Emma's face showed panic."
    
    fa "Hey Liam."
    fa "She already-"
    
    fb "What if I wanted to be the seeker and I really want to be ‘it’"
    
    "Emma frowned."
    "She knew Liam was going to play with Lila’s heart strings."
    "Even so, she doesn't want to push him any further."
    "Even she knows she’s being childish."
    "She can only pray Lila will reject that idea."
     
    L "Oh {cps=2}...{/cps}Do you really want to be 'it'?"
    
    "Liam smiled."
    
    fa "I definitely do!"
    
    "Lila innocently smiled back."
    
    L "Whatever makes you happy!"
    
    "Emma frowned."
    
    fa "Your favoritism is so obvious and I hate it…"
    
    "Emma grumbled but it was so quiet the other two didn’t hear her."
    
    fb "Ok! I’ll start counting now! Go hide!"
    
    L "Ok!"
    
    "With that the three scattered."
    "Emma and Lila went in opposite directions."
    "Lila continued to explore until she ended up in a place she’s unfamiliar with."
    
    L "I don’t think I’ve been here before."
    
    "Catching her breath, she took a moment to frantically look around."
    "From what she could see, to her left was a cave covered in transparent crystals and tiny little glowing fungi."
    "The cave seems endless and very spacious."
    "Besides the cave, to her right was some kind of animal den."
    "Though pitched black inside, the outside is swarmed with fireflies and different kinds of glowing mushrooms."
    "She can't tell what kind of animal made this den but she knows she's big enough to fit through."
    
    "Despite the danger these do look like good hiding places."
    
    L "Which way should I go"
    
menu:
    "The endless cave":
        jump Cave
    
    "The animal Den":
        jump Den

return

label Cave:
    L "At least it has more room to breath then the den."
    
    scene Cave
    with dissolve
    show Liladefault at left with dissolve
    "Making up her mind Lila chose to hide inside the cave."
    "Even though she’s never been here before it didn’t scare her."
    "However, as she waited in the cave she felt more and more lonely."
    "The chilly atmosphere once again reminded her of the warmth of Enoki mushrooms."
    "She forgot to bring some with her now she feels nothing but the cold."
  
    L "I really wish there was a giant Enoki mushroom."

    L "Maybe it’s warmth would make me feel less lonely..."

    "She wondered to herself."
   
    Q "What if I told you that does exist?"
    
    "Lila shivered at the sudden tingling sensation left from the words whispered in her ears."

    L "WHAT?!"
   
    "Lila shouted and turned to look at the person who whispered those words."

    L "Minglou?!"

    m "What was that reaction?"

    "Minglou said standing there unfazed. Lila stared at her shocked."
   
    L "Why did you sneak up on me?"
    
    m "There’s no need for that. Someone as slow minded as you scared yourself."

    L "Huh?"

    "What does that even mean...Wait more importantly."

    L "What did you say exists?"

    "Lila asked, just catching on to Minglou’s previous statement."

    m "What did you think I said existed?"

    "She really hates it when Minglou questions her."
    "But if she doesn't respond back, she’ll never get the answers she’s looking for."
    "Why does she always do this?"
    "What should she say back?"

menu:
    "The enoki mushrooms?":
        jump EMush
    
    "Can you please explain to me what you mean?":
        jump PleaseEx
return

label EMush:
    
    "Minglou’s eyes widened."
    "Surprisingly she gently smiled."
    "For once it didn’t feel like an edge of a knife."
    
    m "Would you look at that? After so long you did grow after all. You listened for once."
    
    L "Wait? But doesn’t enoki mushrooms already exist?"
    
    "All in that one moment, Mingllou is back to her grumpy self."
    
    m "Just as I was about to say I was proud… I wasn’t talking about those tiny enoki mushrooms."
    
    L "But you just said I was correct."
    
    m "I said you listened but I take that back."
    
    "Ignoring all of Minglou’s unpleasant words Lila grew an immense interest in what she was talking about."
    
    L "No Way!"
    
    "Lila shouted in excitement while Minglou starred on the side in shock."
    
    L "Did you find a new mushroom species?!"
    
    "Minglou grumbled but she wasn’t displeased."
    
    m "Though that would be intriguing."
    m "I found something even more interesting."
    
    "Lila's eyes instantly sparkled."
    
    L "What did you find?!"
    
    "Minglou smirked."
    
    m "Follow me and you’ll know."
    
    "The two went deeper into the cave until they reached an area covered in enoki mushrooms."
    
    L "Whoa!"
    L "I didn’t know there were so many of them here."
    L "To think I was cold just a minute ago."
    
    "Lila was about to go gather some but Minglou stopped her."
    
    L "Huh? Why did you stop me?"
    
    "Lila questioned but Minglou gave her a very mischievous smirk."
    "Though Lila felt uncomfortable whenever Minglou gave her this look, she’s gotten somewhat used to it."
    
    m "Don't be so Hasty."
    m "Take a closer look..."
    m " Noticed anything unusual?"
    
    "Lila looked around."
    "There were two things that stood out to her."
    "One of the things that stood out was a particular spot that had a lot more enoki mushrooms gathered in one place compared to the other spots."
    "The other thing was that it felt very warm and fuzzy in this part of the cave despite it being cold on the other end."
    "But the biggest question which has Lila worried was, which one of the two is the answer Minglou is looking for?"

menu:
    "The Cave feels warm":
        jump WarmCave
    
    "That one spot...has too much Enoki Mushrooms":
        jump ToMany
return
    
label PleaseEx:
   
    "Minglou sighed."
    
    m "And here I thought you grew as a person. How disappointing..."
    
    "Lila felt a sense of devastation after hearing Minglou’s reply."
    
    m "Don’t look at me like that."
    m "You’re the one forgetting something I've said literally within a couple of seconds."
    
    "Lila looks at Minglou full of confusion."
    
    L "Seconds?"
    
    m "Right...I forgot that your race doesn't even know how to tell the span of time."
    
    "Lila has no clue what Minglou is referring too and can only helplessly stand there listening to her rant."
    
    m "Forget it."
    m "I’ll do you a favor."
    m "You are my last hope after all…."
    
    "Minglou murmured but Lila didn’t catch any of what she said."
    
    m "Just follow me…."
    
    "Lila quietly followed Minglou."
    "Although she has no clue what is happening she felt a bit sad and depressed."
    "She wants to cry but she knows Minglou won’t comfort her."
    "Minglou just watched her quietly."
    "However, after walking for a bit, Minglou decided to break the silence."
    
    m "What. Feeling upset?"
    
    L "..."
    
    "Lila didn’t say anything as tears welled up in her eyes."
    
    m "Why don’t you look up."
    m "You might just cheer up, you cry baby."
    
    "Curious about what Minglou was talking about Minglou looked around."
    "Lila’s eyes glittered instantly."
    "All of the tears evaporated in that one instant."
    "They were surrounded by enoki mushrooms."
    "So many have gathered in one place."
    "This is so rare!"
    
    L "There’s so many!"
    
    "She said, turning to face Minglou."
    "Minglou gave her a very mischievous smirk."
    "Though Lila felt uncomfortable whenever Minglou gave her this look, she’s gotten somewhat used to it."
    
    m "Noticed anything unusual?"
    m "Don’t disappoint me this time."
    
    "Though worried, Lila took the time to look around."
    "She noticed two things."
    "One of the things that stood out was a particular spot that had a lot more enoki mushrooms gathered in one place compared to the other spots. "
    "The other thing was that it felt very warm and fuzzy in this part of the cave despite it being cold on the other end."
    "But the biggest question which has Lila worried was, which one of the two is the answer Minglou is looking for?"
    
menu: 
      "The Cave feels warm":
          jump WarmCave
    
      "That one spot...has too much Enoki Mushrooms":
          jump ToMany
return

label WarmCave:
    m "Is that so?"
    
    "Minglou’s face didn’t change. She is still as stoic as ever."
    
    m "What do you think makes this place warm?"
    
    L "I believe it's the enoki mushrooms?"
    
    "Lila answered but was uncertain."
    
    m "That isn’t wrong."
    m "But I want you to think even deeper."
    m "When enoki mushrooms gather are they usually this warm?"
    
    "When Minglou asked that question something felt unpleasant to Lila."
    "She thought for a moment."
    "Enokis don’t produce enough warmth unless they gather together."
    "But if too much gathered they will overheat and cause a fire."
    "Yet...Why isn’t the cave burning?"
    "Minglou’s expression darkened."
    
    m "Honey, you are so close to the answer. Think even deeper."
    
    "Lila didn’t even notice the way Minglou was looking at her."
    "Her eyes focused on one thing only."
    "The pile of mushrooms gather in that one corner."
    "What is it that causes all of them to gather?"
    "Iching closer Lila looked into the pile of mushrooms."
    "In the center was one piece of paper."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn’t look that special."
    "What made Lila drawn to it was that even though the paper was surrounded none of the mushroom parts touched the paper."
    "While her eyes were still glued to the paper Minglou picked it up and in a one moment the paper went into flames."
    
    L "Minglou!"
    
    "Lila panicked as she screamed for Minglou."
    "Minglou is a water spirit."
    "Fire might cause her harm."
    "Yet in a blink of an eye the flames went out."
    "Standing in front of her was Minglou smiling while handing over the paper to Lila."
    "he blank piece of paper now filled with symbols is in her face."
    "Trying to wrap her head around everything Lila became very confused."
    
menu: 
    "Ask Minglou for context":
        jump MContext
 
    "Ask Minglou if she's ok":
        jump MingOk
return

label ToMany:
    m "Oh?"
    m "Nice job noticing."
    m "Why don’t you go check it out?"
    
    "Minglou said with a smirk on her face."
    "Though Lila’s felt this odd feeling from when she first met up with Minglou she still listened to her words."
    "She got closer to observe the mushrooms."
    "In the pile of all the mushrooms, there was a piece of paper in the center."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn’t look that special."
    "What made Lila drawn to it was that even though the paper was surrounded none of the mushroom parts touched the paper."
    "While her eyes were still glued to the paper Minglou picked it up and in a one moment the paper went into flames."
    
    L "Minglou!"
    
    "Lila panicked as she screamed for Minglou."
    "Minglou is a water spirit."
    "Fire might cause her harm."
    "Yet in a blink of an eye the flames went out."
    "Standing in front of her was Minglou smiling while handing over the paper to Lila."
    "The blank piece of paper now filled with symbols is in her face."
    "Trying to wrap her head around everything Lila became very confused."
    
menu: 
    "Ask Minglou for context":
        jump MContext
 
    "Ask Minglou if she's ok":
        jump MingOk
return

label MContext:

     L "Wha-What just happened?!"

     m "Nothing much."
     m "Just a little special ability of mine."
     m "Anyways you should pay more attention to this magnificent artifact."

     "It looks like Minglou won’t explain what has happened."
     "Has she always had an ability like that?"
     "Lila never knew."
     "Lila knows that unlike most spirits, Minglou can travel from her world to the spirit realm without the need of Lila’s powers."
     "Minglou is a very powerful spirit but can a water spirit withstand the intensity of flames?"
     "Unharmed?"
     "Lila regrets not paying attention in class now."
     "Staring at the paper Minglou handed to her, Lila noticed that there was some language written on there that seems familiar."
     "Other than those few symbols most of the other ones she’s never seen before."

     L "What does this say?"
     L "What is this?"

     "Lila questioned while Minglou looked at her in disbelief."

     m "Child{cps=2}...{/cps}It’s written in your home language."
     m "How can you not understand?"
     m "I get that some of it is in ancient lingo but you should be able to read the other symbols right?"

     "Lila stared at Minglou blankly."

     m "Ugh."
     m "Forget it."
     m " What was that peepsqueaks name?"
     m "The boy you always hang around with."

     L "Peepsqueak? Are you talking about Liam?"

     "Lila has no clue what Minglou meant but she has a gut feeling she was refering to Liam."

     m "Ah yes."
     m "Him."
     m "At least you’re not that dimwitted to not know your own friend’s name."
     
     L "Why do I feel like you said something rude again…"
     
     "Lila always hated the way Minglou spoke."
     "Even someone as level headed as Liam got pissed at Minglou once."
     
     m "Forget what I said and just take the paper to that dweeb."
     
     L "Who’s Dweeb?"
     L "Also why can’t you just tell me what it says?"
     
     "Minglou sounds frustrated."
     
     m "Because I refuse to help decode human words."
     m "I despise it."
     
     "Lila knew that Minglou had always hated her kind and she didn't know why."
     "Everytime she asks why, Minglou not only refuses to answer, she gets super heated."
     "So this time she chose to stay quiet."
     
     m "We’ve been here long enough already."
     m "Get going."
     m "Give that to the Liam kid."
     
     "Oh."
     "She was talking about Liam."
     
     L "Oh ok..."
     L "Um..."
     L "Do you mind if I ask one last question Minglou?"
     
     m "I’ll take as many questions as you have after you’ve talked with Liam."
     
     L "But it’s important."
     
     m "How important?"
     
     L "Uhhhh...."
        
     L "As important as I don’t know how to get back…"     
     
     m "Was that the question?"
     
     L "Kind of?"
     
     m "...."
     
     L " Yeah…"
     
     "Lila said smiling."
     "Minglou sighed."
     
     m "Just follow me."
     
     "As Lila followed Minglou out of the cave from a distance she spotted two figures."
     "From the looks of it, it was Liam and Emma."
     
menu: 
    "Look Minglou, it’s Liam and Emma! Let’s go say Hi!":
        jump MinglouHi
    
    "Call out to them":
        jump CallOut
return

label MingOk:
    
    m "Hm?"
    m "I’m perfectly fine."
    
    "Minglou sounded almost a bit annoyed but she wasn’t as harsh as the other times Lila pissed her off."
    
    L "B-But you're a water spirit…"
    
    "Minglou's eyes darkened."
    
    m "So what if I am?"
    
    L "Doesn’t water hurt you?"
    L "Did I remember wrong?"
    
    m "“I think you did."
    m "You tend to forget I’m not like those other weaklings."
    
    "Minglou was monotone but Lila felt a chill."
    
    m "I even went so far to show you this priceless artifact."
    m "Why don’t you appreciate this moment you have?"
    m "It’s a bit useless to worry about unnecessary things."
    
    "Minglou handed Lila the paper that was in flames."
    "She took the paper and looked at it."
    "Not even a single sign showed that it was in flames."
    "Didn’t paper burn into ashes when it comes into contact with fire?"
    "Why didn’t this one burn?"
    "However, besides that question."
    "The question that bothers her the most is what is the symbols that appeared on the paper."
    "How and why did it appear?"
    
    L "What does it say?"
    
    "Lila questioned as Minglou stood there in disbelief."
    
    m "You mean to tell me you don’t know how to read your own language?"
    
    "Lila looks embrassed." 
    
    m "Not even the basics?"
    
    L "No...But Liam Knows!"
    
    "Lila said in an upbeat tone while Minglou shivered at that name."
    
    m "Don’t mention that brat’s name."
    m "I hate the looks he gives me."
    m "It’s like he can read right through me."
    
    "Lila looked at her in confusion."
    
    m "Ugh."
    m "Forget it"
    m "Just take the paper and go ask him."
    
    "Minglou grumbled wanting to leave."
    "It seems she’s also  mentally exhausted."
    
    L "Ah wai-"
    
    "Sensing in her instinct that Minglou was about to leave she tried to stop her by calling out to her."
    
    L "And she's gone…"
    
    "Looks like she didn't call out in time."
    "Minglou's essence was no longer in the cave."
    "What should she do?"
    "She doesn't know the way out of the cave..."
    "While she was lamenting she hears familiar voices calling out her name." 
    "Following the voices she finds her way out of the cave."
    "Meeting up with her is Liam and Emma. "
 
menu:
    "I missed you guys!":
        jump MissedY

    "Liam! I was about to look for you!":
        jump LiamLook
        
return

label MissedY:
    
    L "Ah!"
    L "Liam!"
    L "Emma!"
    L "I missed you guys!"
    
    "Lila cheerfully called out to them."
    "The three of them gathered together as the two took their time to catch their breaths."
    
    L "Oh I also have to thank Ming-"
    
    "Lila wanted to thank Minglou for taking her out of the cave but she was already nowhere to be seen."
    
    fb "Huh?"
    fb "Did you say something Lila?"
    
    "Liam asked while his breath settled."
    
    L "Uh?"
    L "No-"
    L "I-it’s nothing."
    
    fb "You went a bit too fam."
    fb "We barely managed to find you."
    
    fa "You sure like causing trouble you direction freak."
    
    "Uh oh… Looks like she’s been scolded."
    "Wait... wasn’t there something she wanted to show them?"
    "Oh right!"
    L "You guys appeared just in time. I have something to show you…"
    
    "Lila said getting excited as she showed them the paper Minglou found for her."
    "It seems that being with her friends made her forget that she was lost. "
    
    fa "I told you you worried over nothing."
     
    "Emma growled at Liam. Liam only smiled back."
     
    fb "We can never be too cautious."
     
    "He replied before the three of them took a closer look at the paper."

    fb "That is so interesting…" 
     
    "Liam said as he held out a similar paper."
     
    L "Huh?"
    L "Where did you find that?"

    fb "By the Den…."
     
    L "What does yours say?"
    L "Can you read mine?"
    L "Minglou didn’t tell me anything."
     
    "The two of her friends flinched at the mention of Minglou’s name."
     
    fa "I’ve always hated that spirit of yours."
    fa "There’s something about her I don’t like."
     
    "Emma said but Lila has no clue what she’s referring too."
     
    L "Really?"
    L "I never thought anything of her that came off as bad."
     
    fa "That’s because you’re too mushy to notice."
     
    L "Mushy?"
     
    fa "Like I said-"
     
    fb "Nevermind that."
    fb "I just read these pages."
    fb "They talk about something terrifying."
     
    L "What do you mean?"
     
    "Emma was equally as confused."
     
    fb "It talks about the existence of something called The Sun…"
     
    "Emma's expression darkened."
     
    fa "That can’t be."
    fa "You must have read wrong."
     
    L "What are you guys talking about?"
    L "What is The Sun?"
     
    fb "Emma’s right."
    fb "I only know what’s written on here to some extent."
    fb "We should confirm it at the library where I can do more research."
     
    L "Wait, explain to me first."
     
    fa "Ughhhhhh!"
    fa "This is why you get on my nerves."
    fa "I say it once ok."
    fa "But you can’t tell no one...yet."
     
    L "Ok! I promise."
     
    fa "Remember the stuff you talked about before we played the game?"
     
    L "Uh...I don’t remember much really."
     
    fa "What?"
    fa "How can you forget?!"
    fa "It wasn’t too long ago!"
    fa "Urhhhh."
    fa "Nevermind."
    fa "Come closer and listen carefully."

    "Lila inched closer to Emma and in return Emma whispered back."
     
    fa "It’s what brings light into this world."
    fa "A light brighter than any mushrooms on this planet."
     
    "Lila’s eyes widened."
    "She didn’t even question how Emma knew that."
    "She’s even more curious about the existence of this thing called The Sun."
    
    L "Tell me more!"
     
    "Lila Shouted."
     
    fa "Shhhh! I just told you to be quiet about it."
     
    "Although Lila was confused why they were being so secretive about it."
    "She wanted to ask but Liam stopped her."
     
    fb "That’s only a legend spreaded by rumors."
    fb "We should get out of here first." 
    fb "There’s a reason why those rumors died out."
     
    "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
    "All three of them nodded and then started to head back towards the village."
    "It seems Liam wants to meet up again at the library."
    "Determined to find out more about The Sun, they continued down the path towards the library."
    
    "End."
    "Page 1 discovered."
    "Lila’s Route."  
return
     
label LiamLook:
     fb "Lila!"
     fb "Why did you go out so far!"
     fb "We barely managed to find you."
     
     fa "You sure like causing trouble you direction freak...Also why are you looking for Liam only?"
     
     "The two of them got closer to Lila as they grasped for breath."
     "Though Emma seems to be more upset than happy to see her."
     
     L "Oh."
     L "That’s because I have something to show him…"
     
     fa "I told you you worried over nothing."
     
     "Emma growled at Liam. Liam only smiled back."
     
     fb "We can never be too cautious."
     
     "He replied before the three of them took a closer look at the paper."

     fb "That is so interesting…" 
     
     "Liam said as he held out a similar paper."
     
     L "Huh?"
     L "Where did you find that?"

     fb "By the Den…."
     
     L "What does yours say?"
     L "Can you read mine?"
     L "Minglou didn’t tell me anything."
     
     "The two of her friends flinched at the mention of Minglou’s name."
     
     fa "I’ve always hated that spirit of yours."
     fa "There’s something about her I don’t like."
     
     "Emma said but Lila has no clue what she’s referring too."
     
     L "Really?"
     L "I never thought anything of her that came off as bad."
     
     fa "That’s because you’re too mushy to notice."
     
     L "Mushy?"
     
     fa "Like I said-"
     
     fb "Nevermind that."
     fb "I just read these pages."
     fb "They talk about something terrifying."
     
     L "What do you mean?"
     
     "Emma was equally as confused."
     
     fb "It talks about the existence of something called The Sun…"
     
     "Emma's expression darkened."
     
     fa "That can’t be."
     fa "You must have read wrong."
     
     L "What are you guys talking about?"
     L "What is The Sun?"
     
     fb "Emma’s right."
     fb "I only know what’s written on here to some extent."
     fb "We should confirm it at the library where I can do more research."
     
     L "Wait, explain to me first."
     
     fa "Ughhhhhh!"
     fa "This is why you get on my nerves."
     fa "I say it once ok."
     fa "But you can’t tell no one...yet."
      
     L "Ok! I promise."
     
     fa "Remember the stuff you talked about before we played the game?"
     
     L "Uh...I don’t remember much really."
     
     fa "What?"
     fa "How can you forget?!"
     fa "It wasn’t too long ago!"
     fa "Urhhhh."
     fa "Nevermind."
     fa "Come closer and listen carefully."

     "Lila inched closer to Emma and in return Emma whispered back."
     
     fa "It’s what brings light into this world."
     fa "A light brighter than any mushrooms on this planet."
     
     "Lila’s eyes widened."
     "She didn’t even question how Emma knew that."
     "She’s even more curious about the existence of this thing called The Sun."
    
     L "Tell me more!"
     
     "Lila Shouted."
     
     fa "Shhhh! I just told you to be quiet about it."
     
     "Although Lila was confused why they were being so secretive about it."
     "She wanted to ask but Liam stopped her."
     
     fb "That’s only a legend spreaded by rumors."
     fb "We should get out of here first." 
     fb "There’s a reason why those rumors died out."
     
     "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
     "All three of them nodded and then started to head back towards the village."
     "It seems Liam wants to meet up again at the library."
     "Determined to find out more about The Sun, they continued down the path towards the library."
    
     "End."
     "Page 1 discovered."
     "Lila’s Route."  
return

label MinglouHi:
     "Lila shouted, turning to face Minglou but by the time she turned Minglou was nowhere to be seen."
     "Still questioning where she went, her attention shifted as soon she heard someone called her name."
     
     fb "“Lila!"
     fb "Why did you go out so far!"
     fb "We barely managed to find you."
     
     L "Huh?"
     
     fa "You sure like causing trouble you direction freak."
     
     "The two of them got closer to Lila as they grasped for breath."
     
     L "You guys appeared just in time."
     L "I have something to show you…"
     
     "Lila said getting excited as she showed them the paper Minglou found for her."
     "It seems that being with her friends made her forget that she was lost."
     
     fa "I told you you worried over nothing."
     
     "Emma growled at Liam. Liam only smiled back."
     
     fb "We can never be too cautious."
     
     "He replied before the three of them took a closer look at the paper."

     fb "That is so interesting…" 
     
     "Liam said as he held out a similar paper."
     
     L "Huh?"
     L "Where did you find that?"

     fb "By the Den…."
     
     L "What does yours say?"
     L "Can you read mine?"
     L "Minglou didn’t tell me anything."
     
     "The two of her friends flinched at the mention of Minglou’s name."
     
     fa "I’ve always hated that spirit of yours."
     fa "There’s something about her I don’t like."
     
     "Emma said but Lila has no clue what she’s referring too."
     
     L "Really?"
     L "I never thought anything of her that came off as bad."
     
     fa "That’s because you’re too mushy to notice."
     
     L "Mushy?"
     
     fa "Like I said-"
     
     fb "Nevermind that."
     fb "I just read these pages."
     fb "They talk about something terrifying."
     
     L "What do you mean?"
     
     "Emma was equally as confused."
     
     fb "It talks about the existence of something called The Sun…"
     
     "Emma's expression darkened."
     
     fa "That can’t be."
     fa "You must have read wrong."
     
     L "What are you guys talking about?"
     L "What is The Sun?"
     
     fb "Emma’s right."
     fb "I only know what’s written on here to some extent."
     fb "We should confirm it at the library where I can do more research."
     
     L "Wait, explain to me first."
     
     fa "Ughhhhhh!"
     fa "This is why you get on my nerves."
     fa "I say it once ok."
     fa "But you can’t tell no one...yet."
     
     L "Ok! I promise."
     
     fa "Remember the stuff you talked about before we played the game?"
     
     L "Uh...I don’t remember much really."
     
     fa "What?"
     fa "How can you forget?!"
     fa "It wasn’t too long ago!"
     fa "Urhhhh."
     fa "Nevermind."
     fa "Come closer and listen carefully."

     "Lila inched closer to Emma and in return Emma whispered back."
     
     fa "It’s what brings light into this world."
     fa "A light brighter than any mushrooms on this planet."
     
     "Lila’s eyes widened."
     "She didn’t even question how Emma knew that."
     "She’s even more curious about the existence of this thing called The Sun."
     
     L "Tell me more!"
     
     "Lila Shouted."
     
     fa "Shhhh! I just told you to be quiet about it."
     
     "Although Lila was confused why they were being so secretive about it."
     "She wanted to ask but Liam stopped her."
     
     fb "That’s only a legend spreaded by rumors."
     fb "We should get out of here first." 
     fb "There’s a reason why those rumors died out."
     
     "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
     "All three of them nodded and then started to head back towards the village."
     "It seems Liam wants to meet up again at the library."
     "As they were walking Lila suddenly remembered a question she wanted Liam to answer."
     
     L "Say guys. What is a Dweeb?"
     
     "The two of them looked shocked."
     
     fb "Lila...?"
     fb "Where did you hear that word from?"
     
     "Sensing something off putting Lila wonders if she should tell the truth."
     
menu:
    "Minglou called you that.":
        jump MinglouCalled
        
    "Uh...Nevermind. I must have heard wrong.":
        jump UhNevermind
return

label CallOut:
    L "Ah!"
    L "Liam!"
    L "Emma!"
    L "I missed you guys!"
    
    "Lila cheerfully called out to them."
    "The three of them gathered together as the two took their time to catch their breaths."
    
    L "Oh I also have to thank Ming-"
    
    "Lila wanted to thank Minglou for taking her out of the cave but she was already nowhere to be seen."
    
    fb "Huh?"
    fb "Did you say something Lila?"
    
    "Liam asked while his breath settled."
    
    L "Uh?"
    L "No-"
    L "I-it’s nothing."
    
    fb "You went a bit too fam."
    fb "We barely managed to find you."
    
    fa "You sure like causing trouble you direction freak."
    
    "Uh oh… Looks like she’s been scolded."
    "Wait... wasn’t there something she wanted to show them?"
    "Oh right!"
    L "You guys appeared just in time. I have something to show you…"
    
    "Lila said getting excited as she showed them the paper Minglou found for her."
    "It seems that being with her friends made her forget that she was lost. "
    
    fa "I told you you worried over nothing."
     
    "Emma growled at Liam. Liam only smiled back."
     
    fb "We can never be too cautious."
     
    "He replied before the three of them took a closer look at the paper."

    fb "That is so interesting…" 
     
    "Liam said as he held out a similar paper."
     
    L "Huh?"
    L "Where did you find that?"

    fb "By the Den…."
     
    L "What does yours say?"
    L "Can you read mine?"
    L "Minglou didn’t tell me anything."
     
    "The two of her friends flinched at the mention of Minglou’s name."
     
    fa "I’ve always hated that spirit of yours."
    fa "There’s something about her I don’t like."
     
    "Emma said but Lila has no clue what she’s referring too."
     
    L "Really?"
    L "I never thought anything of her that came off as bad."
     
    fa "That’s because you’re too mushy to notice."
     
    L "Mushy?"
     
    fa "Like I said-"
     
    fb "Nevermind that."
    fb "I just read these pages."
    fb "They talk about something terrifying."
     
    L "What do you mean?"
     
    "Emma was equally as confused."
     
    fb "It talks about the existence of something called The Sun…"
     
    "Emma's expression darkened."
     
    fa "That can’t be."
    fa "You must have read wrong."
     
    L "What are you guys talking about?"
    L "What is The Sun?"
     
    fb "Emma’s right."
    fb "I only know what’s written on here to some extent."
    fb "We should confirm it at the library where I can do more research."
     
    L "Wait, explain to me first."
     
    fa "Ughhhhhh!"
    fa "This is why you get on my nerves."
    fa "I say it once ok."
    fa "But you can’t tell no one...yet."
     
    L "Ok! I promise."
     
    fa "Remember the stuff you talked about before we played the game?"
     
    L "Uh...I don’t remember much really."
     
    fa "What?"
    fa "How can you forget?!"
    fa "It wasn’t too long ago!"
    fa "Urhhhh."
    fa "Nevermind."
    fa "Come closer and listen carefully."

    "Lila inched closer to Emma and in return Emma whispered back."
     
    fa "It’s what brings light into this world."
    fa "A light brighter than any mushrooms on this planet."
     
    "Lila’s eyes widened."
    "She didn’t even question how Emma knew that."
    "She’s even more curious about the existence of this thing called The Sun."
    
    L "Tell me more!"
     
    "Lila Shouted."
     
    fa "Shhhh! I just told you to be quiet about it."
     
    "Although Lila was confused why they were being so secretive about it."
    "She wanted to ask but Liam stopped her."
     
    fb "That’s only a legend spreaded by rumors."
    fb "We should get out of here first." 
    fb "There’s a reason why those rumors died out."
     
    "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
    "All three of them nodded and then started to head back towards the village."
    "It seems Liam wants to meet up again at the library."
    "As they were walking Lila suddenly remembered a question she wanted Liam to answer."
     
    L "Say guys. What is a Dweeb?"
     
    "The two of them looked shocked."
     
    fb "Lila...?"
    fb "Where did you hear that word from?"
    
    "Sensing something off putting Lila wonders if she should tell the truth."
     
menu:
    "Minglou called you that.":
        jump MinglouCalled
        
    "Uh...Nevermind. I must have heard wrong.":
        jump UhNevermind
return

label MinglouCalled:
    "Liam's expression darkened."
    
    fb "I see…."
    fb "The next time you see her..."
    fb "Please let  her know I greatly appreciate her kind hostility."
    
    "Liam said with a smile but didn’t seem like it was gentle at all."
    
    L "Ok?"
    
    "Lila said in uncertainty."
    
    fb "Also"
    fb "Don’t use that word anymore Lila."
    fb "It makes some people uncomfortable."
    
    L "Oh sorry."
    L "I didn’t know that."
    L "Did it make you uncomfortable Liam?"
    
    fb "Not from you Lila."
    
    "Liam said with a smile."
    "Emma, on the other hand, looks very angry. "
    "Nevertheless, the three of them went on their way to find out more about The Sun that doesn’t exist in their world."
    
    "End."
    "Page 1 discovered."
    "Lila’s Route."  
return

label UhNevermind:
    fb "Well."
    fb "Whoever called you that is despicable."
    fb "Don’t listen to them."
    
    fa "That’s right!"
    fa "Only I get to call you that."
    
    "Ignoring Emma's words, Liam continued."
    
    fb "Ah!"
    fb "Don’t repeat that to anyone else, got it?"
    
    "Liam said strictly."
    "Although Lila nodded, she wonders if she should tell him that it was actually Minglou who called him that."
    "But she didn't want her friends fighting amongst themselves so she kept quiet on their whole journey to the library."
    
    "End."
    "Page 1 discovered."
    "Lila’s Route."  
return

label Den:
     L "I don’t like the idea of going to the cave…. "
     
     "Lila thought and was about to go down the path to the den but a sudden voice stopped her."
     
     Q "Don’t go that way…"
     
     "Shocked, Lila turned to face the direction of the voice."
     
     L "Minglou?! What are you doing here?"
     
     "It's not a surprise that a power spirit like Minglou can travel back and forth from her world to Lila's..."
     "What was shocking was that Minglou popped up for no reason."
     "Usually when she summons her she refuses to come out unless the reason is ugent."
     "Minglou just stood there staring at Lila."
     "Though her expression was stoic but her voice was soft and low."
     
     m "That’s not the right way…."
     
     L "Huh?" 
     L "What do you mean?"
     
     "How would Minglou know that this is the wrong way?"
     
     m "Just don’t go there."
     m "That’s not where your destiny lies."
     
     "The atmosphere suddenly felt heavy."
     
     L "But I don’t like the cave…"
     
     m "..."
     
     "Minglou was quiet for a moment until she spoke again."
     
     m "Would you feel better if I go with you?"
     
     "This is the first time Minglou’s been this desperate with her."
     "She’s usually very haughty but level headed."
     "Lila wonders why her personality suddenly changed so much."
     
     L "Why are you suddenly like this?"
     
     m "Just answer me. Are you still going to the den?"
     
menu: 
    "No. If you’re with me I’m ok.":
        jump NoYouWithMe

    "Yes. This is very uncomfortable":
        jump VeryUncomfy
return

label NoYouWithMe:
    
    "Minglou seems relieved."
    
    m "Good."
    m "Follow me."
    m "I’ll find a good hiding spot for you."
    
    "Although something felt off putting Lila still followed."
    "They continued into the forest for a while before Lila started to have second doubts."
    
    L "I’m sorry Minglou...But there’s this burning feeling telling I need to be at the Den."
    
    m "What?"
    m "What burning feeling?"
    
    "Minglou looked conflicted."
    
    L "I don’t know."
    L "It’s just this weird feeling."
    L "Also"
    L "I don’t like how strange you’re acting."
    L "I just don’t like this."
    
    m "Would I ever harm you?"
    
    "Lila gave Minglou a weird look."
    
    m "Well..."
    m "Allow me to rephrase that."
    m "Have I ever harmed you physically?"
    
    "Lila thought for a moment."
    "Has Minglou ever done anything too unforgiving?"
    "Nothing really came to mind."
    "Though this water spirit can be a bit sharp tongued she’s never hurt her to the point of no return."
    
    m "Really?"
    m "You’re going to spend that long thinking about it?"
    m "You don’t trust me?"
    m "I’ve watched over since you were in diapers."
    
    "Lila looked at Minglou."
    "Her eyes hide no lies yet there was a sense of motive."
    "However that statement is true."
    "They’ve been together since Lila was born."
    "That's what she remembers from her memory."
    
menu: 
    "Ok. I trust you.":
        jump ITrust
    
    "Sorry. I can’t seem to trust you…":
        jump SorryI
return

label ITrust:
       
    "Lila decided to go onwards with full determination."
    "I believe in Minglou."
    "Minglou sighed in relief."
    "They kept their pace until they reached the entrance to the cave."
    "As they walked into the cave Lila felt a chill." 
    "The dark cave felt cold and lonely."
    "She looked at Minglou and stared at her elegant features."
    "She couldn’t help but smile."
    
    m "What are you smiling about?"
    m "Stop looking at me like that."
    m "It’s creepy."
    
    "Lila was at a loss for words."
    
    L "I just thought it’s nice that I’m not alone…."
    
    "Lila sulked."
    
    "Minglou didn’t say anything at first."
    "All she did was glance over at Lila."
    "Nevertheless, she sighed and broke the unformforable silence."
    
    m "You’re usually very talkative."
    m "What’s got your tongue twisted?"
    
    "Lila didn’t say anything and just silently walked."
    "Minglou smirked cheekly."
    
    m "Don’t tell me the atmosphere got to you?"
    m "What was it I heard?"
    m "Ah! Yes."
    m "Don’t worry."
    m "I’ve heard that idiots don’t catch colds."
    
    "Hearing those words made Lila feel awful."
    "She was about to rebuttal but she paused when she looked around her surroundings."
    "The cave which was pitch black before is now filled with the gentle glows from the warm enoki mushrooms."
    "Not only was she no longer cold she also felt a fluffy feeling well up in her."
    
    m "Regardless, I wouldn’t let you catch it anyways…."
    
    "Minglou mumbled as Lila turned to look at her."
    
    L "Huh?"
    
    "Lila looked at Minglou in confusion."
    
    m "Nevermind."
    m "Just look at our surroundings."
    m "Do you see something unusual?"
    
    "Minglou suddenly brought up a point."
    "This made Lila curious as she looked around."
    "There were two things that stood out to her."
    "One of the things that stood out was a particular spot that had a lot more enoki mushrooms gathered in one place."
    "The other thing was that it felt very warm and fuzzy in this part of the cave despite it being cold on the other end."
    "Which one of the two things was the answer Minglou was looking for?"
    
menu:
    "That group of mushrooms are unusual":
        jump GroupMush
    
    "This place feels warm":
        jump WarmPlace
return

label GroupMush:
    m "Oh?"
    m "Nice job noticing."
    m "Why don’t you go check it out?"
    
    "Minglou said with a smirk on her face."
    "Though Lila’s had this odd feeling from when she first met up with Minglou she still listened to her words."
    "She got closer to observe the mushrooms."
    "In the pile of all the mushrooms, there was a piece of paper in the center."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn’t look that special."
    "What made Lila drawn to it was that even though the paper was surrounded, none of the mushroom parts touched the paper."
    "While her eyes were still glued to the paper, Minglou picked it up and all in a one moment the paper went into flames."
    
    L "Minglou!"
    
    "Lila panicked as she screamed for Minglou."
    "Minglou is a water spirit."
    "Fire might cause her harm."
    "Yet in a blink of an eye the flames went out."
    "Standing in front of her was Minglou smiling while handing over the paper to Lila."
    "The blank piece of paper now filled with symbols is in her face."
    "Trying to wrap her head around everything Lila became very confused."
    
menu:
    "Ask Minglou what just happened":
        jump MinglouH
 
    "Is Minglou ok?!":
        jump IsMingOk
return 

label WarmPlace:
    m "What do you think makes this place warm?"
    
    L "Is it the enoki mushrooms?"
    
    m "That isn’t wrong."
    m "But I want you to think even deeper."
    m "When enoki mushrooms gather are they usually this warm?"
    
    "When Minglou asked that question something felt unpleasant to Lila."
    "She thought for a moment. Enokis don’t produce enough warmth unless they gather together."
    "However, if too much gathered they will overheat and cause a fire."
    "Yet...Why isn’t the cave burning?"
    
    m "Think even deeper."
    
    "Lila didn’t even notice the way Minglou was looking at her."
    "Her eyes focused on one thing."
    "The pile of mushrooms gather in that one corner."
    "What is it that causes all of them to gather?"
    "Iching closer Lila looked into the pile of mushrooms."
    "In the center was one piece of paper."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn’t look that special."
    "What made Lila drawn to it was that the mushrooms only surrounded the paper yet none of it’s parts touched the paper."
    "While her eyes were still glued to the paper Minglou picked it up and in a one moment the paper went into flames."
    
    L "Minglou!"
    
    "Lila panicked as she screamed for Minglou."
    "Minglou is a water spirit."
    "Fire might cause her harm."
    "Yet in a blink of an eye the flames went out."
    "Standing in front of her was Minglou smiling while handing over the paper to Lila."
    "A paper now filled with symbols she’s never recognized was in her face."
    "Trying to wrap her head around everything Lila became very confused."
    "What just happened?"
    
menu:
    "Ask Minglou what just happened":
        jump MinglouH
 
    "Is Minglou ok?!":
        jump IsMingOk
return 

label MinglouH: 
     L "Wha-What just happened?!"

     m "Nothing much."
     m "Just a little special ability of mine."
     m "Anyways you should pay more attention to this magnificent artifact."

     "It looks like Minglou won’t explain what has happened."
     "Has she always had an ability like that?"
     "Lila never knew."
     "Lila knows that unlike most spirits, Minglou can travel from her world to the spirit realm without the need of Lila’s powers."
     "Minglou is a very powerful spirit but can a water spirit withstand the intensity of flames?"
     "Unharmed?"
     "Lila regrets not paying attention in class now."
     "Staring at the paper Minglou handed to her, Lila noticed that there was some language written on there that seems familiar."
     "Other than those few symbols most of the other ones she’s never seen before."

     L "What does this say?"
     L "What is this?"

     "Lila questioned while Minglou looked at her in disbelief."

     m "Child{cps=2}...{/cps}It’s written in your home language."
     m "How can you not understand?"
     m "I get that some of it is in ancient lingo but you should be able to read the other symbols right?"

     "Lila stared at Minglou blankly."

     m "Ugh."
     m "Forget it."
     m " What was that peepsqueaks name?"
     m "The boy you always hang around with."
     
     L "Peepsqueak?"
     L "Are you talking about Liam?"
     L "Why do I feel like you said something rude again…"
     
     m "Ah yes."
     m "Him."
     m "Why don’t you go ask him about this page?"
     
     L "He’s not with me right now."
     L "Actually, I don’t know where he is at."
     
     m "That’s no problem."
     m "I’ll lead you to him."
     
     L "You know where he is?!"
     
     m "I know everything."
     
     "Minglou said with a cheeky smirk."
     
     L "Why can’t you just tell me what it says?"
     
     m "Because...I refuse to help decode human words."
     m "I despise it."
     
     "Lila knew that Minglou had always hated her kind and she didn't know why."
     "Everytime she asks why, Minglou not only refuses to answer, she gets super heated."
     "Even though this time Minglou was not making a big deal out of it Lila still chose to stay quiet. "
     
     m "We’ve been here long enough already."
     m "Let’s get going."
     
     L "Ok!"
     
     "Just as the two were about to leave."
     "Minglou handed her a mushroom."
     
     L "Huh?"
     
     "Lila was confused but still took the mushroom."
     
     m "Take it."
     m "It’s going to get cold on the way out."
     
     "Minglou said with her normal expressionless face yet the tone of her voice was soft and gentle."
     
     L "Thank you!"
     
     "She said with a smile."
     "Nothing followed but the echoes of their footsteps."
     "Just as they were about to reach the exit of the cave she couldn’t help but ask the one question that has been bothering her this whole time. "

     L "What was in the den?"
     
     "She nervously questioned expecting another angry response."
     "Yet to her surprise there was a soft reply."
     
     m "You’ll see…"
     
     "Lila glanced at Minglou and saw that the usual frown on Minglou has turned into a smile."
     "It was such a rare sight."
     "She’d really wish she could record this moment."
     "If only she knew what’s to come in the near future she probably would have."
     
     Q "Lila!"
     
     "Breaking away from her thought process someone called her name."
     "She turned to face the direction of the noise and to her surprise she saw her two friends running towards her."
     "Excited she called out to them. "
     
menu:  
    "Hi! You guys!":
        jump HiGuys
 
    "I was looking for you Liam!":
        jump LookYouL
return

label HiGuys:
    
    L "Ah!"
    L "Liam!"
    L "Emma!"
    L "I missed you guys!"
    
    "Lila cheerfully called out to them."
    "The three of them gathered together as the two took their time to catch their breaths."
    
    L "Oh I also have to thank Ming-"
    
    "Lila wanted to thank Minglou for taking her out of the cave but she was already nowhere to be seen."
    
    fb "Huh?"
    fb "Did you say something Lila?"
    
    "Liam asked while his breath settled."
    
    L "Uh?"
    L "No-"
    L "I-it’s nothing."
    
    fb "You went a bit too fam."
    fb "We barely managed to find you."
    
    fa "You sure like causing trouble you direction freak."
    
    "Uh oh… Looks like she’s been scolded."
    "Wait... wasn’t there something she wanted to show them?"
    "Oh right!"
    L "You guys appeared just in time. I have something to show you…"
    
    "Lila said getting excited as she showed them the paper Minglou found for her."
    "It seems that being with her friends made her forget that she was lost. "
    
    fa "I told you you worried over nothing."
     
    "Emma growled at Liam. Liam only smiled back."
     
    fb "We can never be too cautious."
     
    "He replied before the three of them took a closer look at the paper."

    fb "That is so interesting…" 
     
    "Liam said as he held out a similar paper."
     
    L "Huh?"
    L "Where did you find that?"

    fb "By the Den…." 
    
    "Lila thought back on Minglou’s words..."
    
    L "What does yours say? Can you read mine? Minglou didn’t tell me much."
    
    "The two of her friends flinched at the mention of Minglou’s name."
    
    fa "I’ve always hated that spirit of yours."
    fa "There’s something about her I don’t like."
    
    "Emma said but Lila has no clue what she’s referring too."
    
    L "Really?"
    L "I never thought anything of her that came off as bad."
    L "I guess she is a bit secretive."
    
    fa "Huh?"
    fa "What do you mean?"
    
    L "I don’t know."
    L "Something about her just makes me want to question-"
    
    fb "Nevermind that."
    fb "I just read these pages."
    fb "They talk about something terrifying."
    
    "Liam said breaking their talk about Lila’s unusual spirit."
    "It seems that what’s written on the page is more important at the moment."
    
    L "Something terrifying?"
    
    "Lila questioned with Emma equally as confused."

    fb "It talks about the existence of something called The Sun…"
    
    "Emma's expression darkened."
    
    fa "That can’t be."
    fa "You must have read wrong."
     
    L "What are you guys talking about?"
    L "What is The Sun?"
     
    fb "Emma’s right."
    fb "I only know what’s written on here to some extent."
    fb "We should confirm it at the library where I can do more research."
     
    L "Wait, explain to me first."
     
    fa "Ughhhhhh!"
    fa "This is why you get on my nerves."
    fa "I say it once ok."
    fa "But you can’t tell no one...yet."
     
    L "Ok! I promise."
     
    fa "Remember the stuff you talked about before we played the game?"
     
    L "Uh...I don’t remember much really."
     
    fa "What?"
    fa "How can you forget?!"
    fa "It wasn’t too long ago!"
    fa "Urhhhh."
    fa "Nevermind."
    fa "Come closer and listen carefully."

    "Lila inched closer to Emma and in return Emma whispered back."
     
    fa "It’s what brings light into this world."
    fa "A light brighter than any mushrooms on this planet."
     
    "Lila’s eyes widened."
    "She didn’t even question how Emma knew that."
    "She’s even more curious about the existence of this thing called The Sun."
    
    L "Tell me more!"
     
    "Lila Shouted."
     
    fa "Shhhh! I just told you to be quiet about it."
     
    "Although Lila was confused why they were being so secretive about it."
    "She wanted to ask but Liam stopped her."
     
    fb "That’s only a legend spreaded by rumors."
    fb "We should get out of here first." 
    fb "There’s a reason why those rumors died out."
     
    "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
    "All three of them nodded and then started to head back towards the village."
    "It seems Liam wants to meet up again at the library."
    "Determined to find out more about The Sun, they continued down the path towards the library."
    
    "End."
    "Page 1 discovered."
    "Lila’s Route."  
return
    
label LookYouL:
     fb "Lila!"
     fb "Why did you go out so far!"
     fb "We barely managed to find you."
     
     fa "You sure like causing trouble you direction freak...Also why are you looking for Liam only?"
     
     "The two of them got closer to Lila as they grasped for breath."
     "Though Emma seems to be more upset than happy to see her."
     
     L "Oh."
     L "That’s because I have something to show him…"
     L "You see, me and Ming-"
     
     "Lila said getting excited as she showed them the paper Minglou found for her."
     "However, when she turned around to refer to Minglou she noticed that the spirit's already gone."
     "She didn’t even say Thank you to Minglou yet..."
     
     fa "I told you you worried over nothing."
     
     "Emma growled at Liam. Liam only smiled back."
     
     fb "We can never be too cautious."
     
     "He replied before the three of them took a closer look at the paper."

     fb "That is so interesting…" 
     
     "Liam said as he held out a similar paper."
     
     L "Huh?"
     L "Where did you find that?"

     fb "By the Den…."
     
     "The den? The one that Minglou told her not to go too?"
     
     L "What does it say? Minglou didn’t tell me much."
     
     "The two of her friends flinched at the mention of Minglou’s name."
    
     fa "I’ve always hated that spirit of yours."
     fa "There’s something about her I don’t like."
    
     "Emma said but Lila has no clue what she’s referring too."
    
     L "Really?"
     L "I never thought anything of her that came off as bad."
     L "I guess she is a bit secretive."
    
     fa "Huh?"
     fa "What do you mean?"
    
     L "I don’t know."
     L "Something about her just makes me want to question-"
     
     fb "Nevermind that."
     fb "I just read these pages."
     fb "They talk about something terrifying."
    
     "Liam said breaking their talk about Lila’s unusual spirit."
     "It seems that what’s written on the page is more important at the moment."
    
     L "Something terrifying?"
    
     "Lila questioned with Emma equally as confused."

     fb "It talks about the existence of something called The Sun…"
     
     "Emma's expression darkened."
    
     fa "That can’t be."
     fa "You must have read wrong."
      
     L "What are you guys talking about?"
     L "What is The Sun?"
     
     fb "Emma’s right."
     fb "I only know what’s written on here to some extent."
     fb "We should confirm it at the library where I can do more research."
     
     L "Wait, explain to me first."
     
     fa "Ughhhhhh!"
     fa "This is why you get on my nerves."
     fa "I say it once ok."
     fa "But you can’t tell no one...yet."
     
     L "Ok! I promise."
      
     fa "Remember the stuff you talked about before we played the game?"
     
     L "Uh...I don’t remember much really."
     
     fa "What?"
     fa "How can you forget?!"
     fa "It wasn’t too long ago!"
     fa "Urhhhh."
     fa "Nevermind."
     fa "Come closer and listen carefully."

     "Lila inched closer to Emma and in return Emma whispered back."
     
     fa "It’s what brings light into this world."
     fa "A light brighter than any mushrooms on this planet."
     
     "Lila’s eyes widened."
     "She didn’t even question how Emma knew that."
     "She’s even more curious about the existence of this thing called The Sun."
    
     L "Tell me more!"
     
     "Lila Shouted."
     
     fa "Shhhh! I just told you to be quiet about it."
     
     "Although Lila was confused why they were being so secretive about it."
     "She wanted to ask but Liam stopped her."
     
     fb "That’s only a legend spreaded by rumors."
     fb "We should get out of here first." 
     fb "There’s a reason why those rumors died out."
     
     "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
     "All three of them nodded and then started to head back towards the village."
     "It seems Liam wants to meet up again at the library."
     "Determined to find out more about The Sun, they continued down the path towards the library."
    
     "End."
     "Page 1 discovered."
     "Lila’s Route."  
return
     
label IsMingOk:
    L "Are you ok?!"
    
    m "Me? I’m perfectly fine."
    
    "Minglou said with a hint of annoyance but her tone was gentle."
    
    L "B-But you're a water spirit…"
    L "Doesn’t water hurt you?"
    L "Did I remember wrong?"
    
    m "“I think you did."
    m "You tend to forget I’m not like those other weaklings."
    
    "Minglou was monotone but Lila felt a chill."
    
    m "I even went so far to show you this priceless artifact."
    m "Why don’t you appreciate this moment you have?"
    m "It’s a bit useless to worry about unnecessary things."
    
    "Minglou handed Lila the paper that was in flames."
    "She took the paper and looked at it."
    "Not even a single sign showed that it was in flames."
    "Didn’t paper burn into ashes when it comes into contact with fire?"
    "Why didn’t this one burn?"
    "However, besides that question."
    "The question that bothers her the most is what is the symbols that appeared on the paper."
    "How and why did it appear?"
    
    L "What does it say?"
    
    "Lila questioned as Minglou stood there in disbelief."
    
    m "You mean to tell me you don’t know how to read your own language?"
    
    "Lila looks embrassed." 
    
    m "Not even the basics?"
    
    L "No...But Liam Knows!"
    
    "Lila said in an upbeat tone while Minglou shivered at that name."
    
    m "Don’t mention that brat’s name."
    m "I hate the looks he gives me."
    m "It’s like he can read right through me."
    
    "Lila looked at her in confusion."
    
    m "Ugh."
    m "Forget it"
    m "Just take the paper and go ask him."
    
    "Minglou grumbled wanting to leave."
    "It seems she’s also  mentally exhausted."
    
    L "Ah wai-"
    
    "Sensing in her instinct that Minglou was about to leave she tried to stop her by calling out to her."
    
    Minglou "What?"
    
menu: 
    "I don’t know how to get out of the cave":
        jump IDontCave

    "Nevermind. Goodbye.":
        jump NvmGood
return

label IDontCave:
    "Although Minglou gave her a weird look she ended the unpleasant look with a sigh."
    
    m "Come with me…"
    
    "She said and Lila gladly followed."
    "As the two were walking out of the cave Lila noticed that the warmth was slowly seeping away from her body."
    "Noticing her shivering Minglou held out an enoki mushroom."
    
    m "Take it."
    m "I have no use for it."
    
    "Minglou said, shoving the mushroom to Lila."
    "As Lila took the mushroom she thought to herself."
    "Even though the water spirit has just held the mushroom it still feels warm."
    "For a long time now, she knew that Minglou showed a lot of warning signs."
    "But she still smiled and held the mushroom close."
    "Even though every time she questioned her it results in a harsh scolding, she still hoped that one day, Minglou would be honest with her. "
    
    "Thank You."
    
    "She said with a smile."
    "Nothing followed but the echoes of their footsteps."
    "Just as they were about to reach the exit of the cave she couldn’t help but ask the one question that has been bothering her this whole time. "
    
    L "What was in the den?"
     
    "She nervously questioned expecting another angry response."
    "Yet to her surprise there was a soft reply."
     
    m "You’ll see…"
     
    "Lila glanced at Minglou and saw that the usual frown on Minglou has turned into a smile."
    "It was such a rare sight."
    "She’d really wish she could record this moment."
    "If only she knew what’s to come in the near future she probably would have."
     
    Q "Lila!"
     
    "Breaking away from her thought process someone called her name."
    "She turned to face the direction of the noise and to her surprise she saw her two friends running towards her."
    "Excited she called out to them. "
     
menu:  
    "Hi! You guys!":
        jump HiGuys
 
    "I was looking for you Liam!":
        jump LookYouL
return

label NvmGood:
    "She’s already troubled Lila enough today already."
    "It’s probably best if she just found a way out of the cave herself."
    "Minglou looked at Lila as she innocently smiled with the page gently gripped in her hand." 
       
    m "I’m just asking because I have a feeling..."
    m "But do you know the way out of the cave."
       
    "Lila looked shocked that Minglou figured out her troubles."
    "Minglou sighed in disbelief. "
       
    m "You’re so easy to read…."
       
    "Minglou said as she plucked a few enoki mushrooms."
    "Then she gave them to Lila."
       
    m "Take these and follow me."
       
    "Minglou said as she pulled Lila along with her."
    "Still in a daze held the mushrooms and Lila stared at Minglou."
       
    L "Why did you give me these?"
       
    m "No reason really."
    m "Now less talking and more moving."
       
    "Minglou said and the two continued down their path."
    "As they got closer and closer to the exit of the cave it got colder as well."
    "Yet because of the mushrooms bundled in Lila’s arms she felt warm."
       
    "Thank You."
    
    "She said with a smile."
    "Nothing followed but the echoes of their footsteps."
    "Just as they were about to reach the exit of the cave she couldn’t help but ask the one question that has been bothering her this whole time. "
    
    L "What was in the den?"
     
    "She nervously questioned expecting another angry response."
    "Yet to her surprise there was a soft reply."
     
    m "You’ll see…"
     
    "Lila glanced at Minglou and saw that the usual frown on Minglou has turned into a smile."
    "It was such a rare sight."
    "She’d really wish she could record this moment."
    "If only she knew what’s to come in the near future she probably would have."
     
    Q "Lila!"
    
    "Breaking away from her thought process someone called her name."
    "She turned to face the direction of the noise and to her surprise she saw her two friends running towards her."
    "Excited she called out to them. "
     
menu:  
    "Hi! You guys!":
        jump HiGuys
 
    "I was looking for you Liam!":
        jump LookYouL
return
            
label SorryI:
    "Lila slowly backed away from Minglou."
    "Before Minglou could say anything she ran to the den."
    "What was it that Minglou was hiding?"
    "Not only was she feeling uncomfortable, she was also very curious."
    "When she arrived at the den she noticed Emma who was supposed to hide standing outside of the den."
    
    L "Emma! Why are you here?"
    
    "Lila shouted while Emma looked at her with a grumpy expression."
    
    fa "So that’s where you went."
    fa "Why do you always cause so much trouble."
    fa "We've been looking for you for a long time now."
    
    "Lila looked a bit confused."
    
    L "Huh?"
    L "But I wasn’t even gone for that long...I think?"
    
    fa "Either way, Liam got worried so we went looking for you."
    fa "Not that was needed."
    
    "Emma grumbled as Lila stopped to catch her breath."
    
    L "Liam’s here too?! Where is he?"
    
    "Lila questions while Emma continues to look at her with a frown."
    
    fa "Inside….He went in there thinking you crawled inlike the animal you are."
    
    "Lila felt a thobe in her heart. Why did Emma’s words feel hurtful?"
    
menu: 
    "Why are you outside?":
        jump YouOut
   
    "Go in to check for Liam":
        jump CheckLiam
return   

label YouOut: 
    fa "For this reason of course."
    
    "Emma said with a smirk as she flicked Lila on the forehead."
    
    L "Ouch!"
    
    "Lila shouted in pain."
    "All of a sudden there were a bunch of rustling sounds coming from the den."
    
    fa "Ahhhhhh... I hate this."
    fa "Of course he responded."
    
    "Emma grumbled."
    "Just as Lila was going to ask why Emma behaved like this Liam rushed out of the den."
    
    fb "Emma!"
    fb "I just heard Lila’s voice!"
    fb "She must be hurt-"
    
    "Liam said in a rush but stopped when he saw the weird look Lila was giving him."
    "Emma glared and scowled. "
    
    fa "She’s fine, you blockhead."
    fa "She’s standing right here."
    fa "I told nothing happened."
    fa "You never listen."
    
    fb "Lila! When did you arrive?"
    "Liam didn't listen to a single word Emma said. Emma just pouted in response."
    
    L "A moment ago."
    
    "Lila replied. Liam composed himself and started questioning Emma."
    
    fb "Why didn’t you tell me she was already here?"
    
    fa "I did."
    
    fb "When?"
    
    fa "Does it matter?"
    fa "Look she's fine."
    fa "You're the one being over protective."
    
    fb "Right."
    fb "Excuse me."
    fb "I might have worried a little too much..."
    
    "Liam said with a smile but the tone of his voice was a bit scary."
    "Emma didn’t look too happy either."
    "It seems the two were at it again."
    
menu: 
    "Liam what did you find?":
        jump LiamWhaFind
   
    "Emma were you looking for me?":
        jump EmmaLook
return

label LiamWhaFind:
    fa "I thought you were worried a moment ago."
    
    L "He looks fine though."
    
    "Both Liam and Emma were surprised at how fast Lila moved on from the topic."
    "Noticing that the two older kids were bickering over something so small they felt embarrassed."
    
    fa "Uh right."
    fa "Sorry about that."
    
    "Emma said feeling ashamed."
    
    fb "No. I started it. I’m sorry too."
    
    "Liam was equally as embarrassed."
    
    fa "Forget about it."
    fa "What did you want to show us."
    
    fb "Right."
    
    "Liam's voice suddenly got serious."
    
    fb "Everything we saw and heard today must remain with the three of us understand?"
    
    "The two nodded in agreement."
    
    fb "Ok...So I picked this up in the den..."
    
    "Liam said as he held out a piece of paper."
    "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."
    
menu:
    "Huh? Why are you being secretive over this?":
        jump WhySecretive
   
    "What written on it?":
        jump WhatWritten
return 

label EmmaLook: 
    fa "Isn’t that obvious?"
    
    "Emma asked but it doesn’t look like she’s questioning."
    
    L "Oh…"
    L "Does that mean you were worried for me?"
    
    "For a short moment Emma was speechless."
    "Her face was filled with pure shock."
    
    fa "Wh-What-"
    fa "Wh-what nonsense is this?"
    fa "Of course not!"
    fa "I know you’re old enough to take care of yourself."
    fa "Who’s worried?!"
    
    "Emma said as she blushed."
    "Her eagerness to reject the idea made Liam laugh."
    
    fa "S-stop laughing!"
    fa "There’s nothing funny!"
    
    L "I see…"
    L "Thank you for caring!"
    
    "Lila said, feeling fluffy inside as Liam laughed harder."
    
    fa "Stop it!"
    fa "You’re making it worse!"
    
    fb "Bu-but you guys are so cute!"
    
    "Liam said, pulling himself together."
    
    fa "Enough!"
    fa "What on earth did you find!"
    fa "Took you long enough."
    fa "Show it to us already."
    
    "Emma said in a desperate attempt to diverge the attention."
    
    fb "Right…"
    
    "It seems her attempt worked as Liam slowly composed himself and started getting serious."
    
    fb "Everything we saw and heard today must remain with the three of us understand?"
    
    "Lila eagerly nodded in agreement."
    "Her excitement can be seen in her eyes."
    "Meanwhile, Emma slowly cooled down as well and nodded just as eager to find out why Liam was being so secretive. "
    
    fb "Ok...So I picked this up in the den..."
    
    "Liam said as he held out a piece of paper."
    "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."
    
menu:
    "Huh? Why are you being secretive over this?":
        jump WhySecretive
   
    "What written on it?":
        jump WhatWritten
return  

label WhySecretive:
    "Lila doesn't understand why a piece of paper is so important."
    "Emma gave her a very weird look."
    
    fa "Did you not read the symbols?"
    
    "As Emma said."
    "But before Lila could reply the two flinched when they heard Liam laugh."
    
    fa "What’s so funny?"
    
    "Emma questioned and Lila looked at Liam equally as confused."
    
    fb "It’s nothing."
    fb "Don't worry about it."
    fb "I’ll explain what’s on this paper."
    fb "This is probably too hard for Lila to understand."
    
    "Liam said, holding in his laughter."
    "Slowly he was able to pull himself back together."
    
    fa "Huh?"
    fa "What are you on about?"
    fa "Some of this is in the basics of our language."
    
    fb "Don’t worry about it."
    fb "It’s probably best if I explained it anyways."
    
    "Liam gave Emma a wink which made her loss all of her reasons."
    
    fa "If you say so…"
    
    "Emma replied and she quieted down."
    
    fb "Well as Emma pointed it out, what’s important is what’s written on the paper."
    
    "Liam said as the two listened in."
    
    fb "It talks about the existence of a magically being."
    fb "A being so powerful that can control a power known as The Sun."
    
    "Liam said as the tone of his voice lowered."
    "Lila’s eyes glimmered."
    
    L "The Sun?"
    
    "Lila questioned."
    "In response to her question, Liam smiled and pointed towards the endless dark night sky."
    
    fb "Yes."
    fb " It's essence was so strong it had the ability to light up the whole world."
    
    "Lila's mind was blown."
    "Although she had many and many questions running through her mind, she couldn’t help take a moment to digust everything Liam has just said. "
    
    L "Where is it now? The Sun!"
    L "Who’s controlling it?"
    L "Why haven’t we-"
    
    fa "Shhhhh!"
    fa "You dummy!"
    fa "Don’t say anymore... This is just a rumor."
    
    "Emma said hushing Lila."
    
    fb "Unfortunately, that is all of the information we have now."
    
    "Liam said. His voice almost sounded disappointed."
    
    fb "Who knows if this is only a joke someone wrote about or if this is a dream of some lunatic."
    
    "Emma said but Lila rebuttal."
    
    L "What if there were more of these pages!"
    L "What if we collected them all?"
    L "What do you think will happen?"
    
    "Lila’s response did ingrue the two but they can only laugh it off."
    
    fb "A lot of Maybes..."
    fb "Who knows really."
    
    "Liam said but that was all he said as he led the two out of the forest."
    
    fb "But Let’s rest up first before we dig deeper."
    
    fa "Right. I’m exhausted."
    
    "As her friends slowly left the den behind dragging her with them Lila turned to look at the den."
    "She couldn’t help wondering if the two took her seriously?"
    "Or did they just rub it off as a joke."
    "Either way, she’s determined to find out more about the page and the information written on it."
    "That is after she’s rested. "
        
    "End."
    "Page 1 discovered."
    "Lila’s Route."  
return

label WhatWritten:
    
    fa "Huh?"
    fa "Don’t tell me..."
    fa "You can’t read this?"
    
    "Emma questioned Lila as Liam nervously laughed at the side."
    
    L "Nope!"
    
    "Lila said with a wide grin across her face."
    
    fa "Did you not pay attention to class?!"
    fa "It’s the basics.... how can you not know?!"
    
    "Emma was shocked."
    "All this time she knows her friend is a bit airheaded but not to this point."
    
    fa "How did you pass all of your classes then?"
    fa "You even got As."
    
    fb "Now. Now."
    fb "Let’s just focus on what’s at hand."
    fb "So back to what I was saying…"
    
    "Suddenly Emma had a feeling she knows where Lila’s As came from."
    "Even though she felt a boil in her heart she maintained her anger. "
    
    fa "Unbelievable…"
    
    "She murmured underneath her breath."
    
    fb "Well as Emma pointed it out, what’s important is what’s written on the paper."
    
    "Liam said as the two listened in."
    
    fb "It talks about the existence of a magically being."
    fb "A being so powerful that can control a power known as The Sun."
    
    "Liam said as the tone of his voice lowered."
    "Lila’s eyes glimmered."
    
    L "The Sun?"
    
    "Lila questioned."
    "In response to her question, Liam smiled and pointed towards the endless dark night sky."
    
    fb "Yes."
    fb " It's essence was so strong it had the ability to light up the whole world."
    
    "Lila's mind was blown."
    "Although she had many and many questions running through her mind, she couldn’t help take a moment to digust everything Liam has just said. "
    
    L "Where is it now? The Sun!"
    L "Who’s controlling it?"
    L "Why haven’t we-"
    
    fa "Shhhhh!"
    fa "You dummy!"
    fa "Don’t say anymore... This is just a rumor."
    
    "Emma said hushing Lila."
    
    fb "Unfortunately, that is all of the information we have now."
    
    "Liam said. His voice almost sounded disappointed."
    
    fb "Who knows if this is only a joke someone wrote about or if this is a dream of some lunatic."
    
    "Emma said but Lila rebuttal."
    
    L "What if there were more of these pages!"
    L "What if we collected them all?"
    L "What do you think will happen?"
    
    "Lila’s response did ingrue the two but they can only laugh it off."
    
    fb "A lot of Maybes..."
    fb "Who knows really."
    
    "Liam said but that was all he said as he led the two out of the forest."
    
    fb "But Let’s rest up first before we dig deeper."
    
    fa "Right. I’m exhausted."
    
    "As her friends slowly left the den behind dragging her with them Lila turned to look at the den."
    "She couldn’t help wondering if the two took her seriously?"
    "Or did they just rub it off as a joke."
    "Either way, she’s determined to find out more about the page and the information written on it."
    "That is after she’s rested. "
        
    "End."
    "Page 1 discovered."
    "Lila’s Route."  
return

label CheckLiam: 
    "Lila was about to step into the Den to check on Liam but Emma’s sharp words stopped her."
    
    fa "Where do you think you’re going?"
    
    L "I wanted to see if Liam’s ok…"
    
    "Lila said, backing away from the den."
    
    fa "You never learn do you."
    fa "Just stay put." 
    fa "Liam is stronger than both of us."
    fa "If something does happen what can you do?"
    
    "Emma's words felt hurtful but they weren’t wrong."
    "It is true that both Liam and Emma are physically stronger than Lila."
    "Yet she couldn’t help but feel worried for Liam. "
    
    L "But I'm still worried."
    
    "Lila said as she looked at Emma pitfully."
    "Emma’s face softens when she sees Lila acting like a lost puppy."
    
    fa "You’ll still go in even if you might get hurt?"
    
    "Lila nodded her head."
    
    fa "Even if I refused to go with you?"
    
    "Lila nodded again."
    
    fa "What if you got hurt doing that?"
    
    "Lila thought for a moment and then replied with a smile."
    
    L "At least then only I would be the one hurt."
    L "Emma and Liam will be fine because you guys are strong."
    
    "Emma's eyes widened and was speechless for a few seconds."
    "Then she signed and smiled back."
    
    fa "I wouldn’t let you get hurt, idiot."
    fa "Wait out there."
    fa "I’ll go check on him."
    fa "Though I have feeling this is pointless worry."
    
    "Emma said, preparing to enter the cave."
    "Lila wanted to stop her so they two could go into together but just as she was about to say something Liam popped up."
    
    fb "Glad to hear you two doing well."
    
    "Lila was speechless while Emma clicked her tongue. "
    
menu: 
    "HUH? Are you ok?":
        jump HUHYOU

    "You had us worried!":
        jump UsWorried
return

label HUHYOU:
     fb "Hm? Me. I’m perfectly fine."
     
     "Liam said with a bright smile."
     
     fa "That was so much unnecessary worry."
     
     "Emma grunted but she looked relieved to see he was doing just fine."
     
     L "What happened in that cave?"
     
     "Lila asked and Liam’s face darkened."
     
     fb "I’m not sure how I can explain this..."
     fb "A Lot has happened."
     fb "I guess I should start with this."
     
     "Liam said as he held out a piece of paper."
     "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."
     "Emma’s face also darkened."
     
     L "Huh?"
     L "What is it…"
     
     fb "It’s best if you don’t know."
     
     "Liam said but Emma argued."

     fa "Why are you hiding this from her?"
     fa "She should know."
     
     "Although Emma also looked like she was in the state of shock her words were still headstrong."
     
     fb "She wouldn’t be able to handle this…."
     
     "Liam protested but Emma insisted that they should inform Lila about their situation."
     
     fa "You can’t baby her forever."
     fa "She’ll be the one hurt if you keep shielding her from reality."
     
     fb "I just don’t want her to break because she’s too pure."
     fb "You shouldn’t keep pushing her either."
     fb "We’re her friends."
     
     "Liam argued but he wasn’t angry."
     "If anything he just sounds a bit more disappointed."
     "His words made Emma more heated."
     "Although Lila has no clue why they are arguing all the time, she feels like she’s responsible for it."
     "How should she calm down the situation?"
     
menu: 
    "I think I should know…I can handle it!":
        jump ICanHandle
    
    "It’s ok if I don’t know.":
        jump OkIDont
return 

label UsWorried:
    fb "My apologies."
    
    "Liam said with a smile."
    
    fa "Anyways what happened in there?"
    
    "Emma asked and Liam’s face instantly darkened."
    
    fb "I’m not sure how I can explain this..."
    fb "A Lot has happened."
    fb "I guess I should start with this."
     
    "Liam said as he held out a piece of paper."
    "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."
    "Emma’s face also darkened."
     
    L "Huh?"
    L "What is it…"
     
    fb "It’s best if you don’t know."
     
    "Liam said but Emma argued."

    fa "Why are you hiding this from her?"
    fa "She should know."
     
    "Although Emma also looked like she was in the state of shock her words were still headstrong."
     
    fb "She wouldn’t be able to handle this…."
     
    "Liam protested but Emma insisted that they should inform Lila about their situation."
     
    fa "You can’t baby her forever."
    fa "She’ll be the one hurt if you keep shielding her from reality."
     
    fb "I just don’t want her to break because she’s too pure."
    fb "You shouldn’t keep pushing her either."
    fb "We’re her friends."
     
    "Liam argued but he wasn’t angry."
    "If anything he just sounds a bit more disappointed."
    "His words made Emma more heated."
    "Although Lila has no clue why they are arguing all the time, she feels like she’s responsible for it."
    "How should she calm down the situation?"
 
menu: 
    "I think I should know…I can handle it!":
        jump ICanHandle
    
    "It’s ok if I don’t know.":
        jump OkIDont
return 

label  ICanHandle:

     "Lila responded with enthusiasm. Her excitement broke through the tension that was built between the two."
     
     fa "That’s the spirit!"
     fa "The baby has finally grown!"
     
     "Emma shouted with a bright grin on her face."
     
     L "Baby?!"
     L "Did you always see me as a child?"
     
     "Lila pouted as Emma laughed."
     
     fa "What you just found out now?"
     fa "It’s ok this big sister will take care of you."
     
     "Emma said teasing Lila."
     
     L "I’m old enough to take care of myself!"
     L "So tell me what you guys found."
     L "I want to know too."
     
     "Lila rebelled but her tone wasn’t harsh."
     "Although Liam didn't look pleased he sighed and gave into the energy the two were emitting."
     
     fb "Ok. Ok."
     fb "It seems I’m the one being overprotective."
     fb "However, what we found today must remain with the three of us."
     fb "Understood?"
     
     "The two of them nodded."
     "Liam gently smiled at their engarness but soon his gentle demeanor was replaced with a serious tone."
     
     fb "Ok...So I picked this up in the den..."
    
     "Liam said as he held out a piece of paper."
     "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."
    
menu:
    "Huh? Why are you being secretive over this?":
        jump WhySecretive
   
    "What written on it?":
        jump WhatWritten
return  

label OkIDont:
    "After Lila spoke, the two went quiet."
    
    fb "Right...Then let’s just go back to the village."
    
    "Liam said with a sigh of relief but Emma won’t live this one down."
    
    fa "Weren’t you interested in the big light Lila?"
    fa "A light so big it covers the entity of Rhea."
    
    fb "Emma-!"
    "Liam almost lost his temper but Lila’s words stopped him."
    
    L "I said that?"
    L "When?"
    
    "Lila’s eyes were filled with wonder."
    "Her interest peaked and her eyes sparkled."
    
    fa "It doesn’t matter when you said it."
    fa "What matters is that light you talked about exists" 
    fa "It’s written on this page."
    
    L "It is?"
    
    "Emma snatched the paper from Liam and shoved it to Lila."
    
    fa "Read it for yourself."
    
    "She said but Lila gave her a confused look."
    
    L "What does it say?"
    
    "Emma’s eyes widen."
    
    fa "Huh? Don’t tell me..."
    fa "You can’t read this?"
    
    "Liam, who was silently watching finally stepped up."
    
    fb "Enough!"
    fb "Leave it be Emma."
    fb "This is just a fairy tale-"
    
    fa "But I want to know more Liam!"
    
    "Lila said, interrupting Liam."
    "In response Liam paused and looked at her."
    
    L "Please tell me more!"
    
    "Lila said desperately."
    "Looking into her pleading eyes Liam could say no."
    "He finally gave in."
    
    fb "Ok."
    fb "Fine."
    fb "But promise me this stays between the three of us."
    
    "When the two agreed Liam started his explanation."
    
    fb "It talks about the existence of a magically being."
    fb "A being so powerful that can control a power known as The Sun."
    
    "Liam said as the tone of his voice lowered."
    "Lila’s eyes glimmered."
    
    L "The Sun?"
    
    "Lila questioned."
    "In response to her question, Liam hesitantly pointed towards the endless dark night sky."
    
    fb "Yes."
    fb " It's essence was so strong it had the ability to light up the whole world."
    
    "Lila's mind was blown."
    "Although she had many and many questions running through her mind, she couldn’t help take a moment to digust everything Liam has just said. "
    
    L "Where is it now? The Sun!"
    L "Who’s controlling it?"
    L "Why haven’t we-"
    
    fa "Relax for a bit."
    fa "It’s just a rumor… "
    fa "But do you believe in it?"
    
    "Emma interrupted but Lila nodded."
    
    fb "Unfortunately, that is all of the information we have now."
    
    "Liam said. His voice did sound a bit disappointed. "
    
    L "What if there were more of these pages!"
    L "What if we collected them all?"
    L "What do you think will happen?"
    
    "Lila’s response did ingrue the two but they can’t be certain. "
    "Holding onto the page he took a deep breath and started to lead the two out of the forest."
    
    fb "Let’s rest up first before we dig deeper."
    
    fa "Right. I’m exhausted."
    
    "As her friends slowly left the den behind dragging her with them Lila turned to look at the den."
    "She couldn’t help wondering if the two took her seriously?"
    "Either way, they looked serious and she’s just as determined to find out more information about the page."
    "That is after she’s rested. "
        
    "End."
    "Page 1 discovered."
    "Lila’s Route."  
return

label VeryUncomfy:
    "Lila slowly backed away from Minglou."
    "Before Minglou could say anything she ran to the den."
    "What was it that Minglou was hiding?"
    "Not only was she feeling uncomfortable, she was also very curious."
    "When she arrived at the den she noticed that there really was nothing special about the den."
    "Feeling a sense of disappointment, she inch closer hopping whatever is inside might be what she's looking for." 
    "But she was stopped by another voice."
    
    Q "Lila! We finally found you!"
    
    "Lila turned around and found Liam."
    "Behind him was Emma who closed followed him."
    
    L "Huh?"
    L "Did you finish counting already?"
    
    fa "We finished counting a while ago you airhead."
    
    "Emma was grasping and  breathing for air."
    
    fa "He already found me."
    fa "I even had to wait awhile for him to go find you."
    fa "Yet you never showed up."
    
    L "Oh really?"
    L "I didn’t know I had walked that far…"
    
    fb "I don’t blame you."
    fb "Who knows how long it’s been since we last separated."
    fb "This planet is seemingless."
    
    "Lila has no idea what Liam means."
    "But more than anything else she’s more interested in what the Den has to offer."
    
    fa "“I’m feeling hungry."
    fa "Come let’s just go back to the village."
    fa "All of this searching has tired me out."
    
    fb "I agree with Emma."
    fb "Who knows how long it’s been since we left the village."
    
menu: 
    "Go into the den":
        jump IntoDen
    
    "Go with Liam and Emma":
        jump GoHome
return 

label GoHome:
    
    L "Now that you mentioned it. I’m feeling hungry too."
    
    fb "Then it’s settled! Let’s go home."
    
    fa "We could have played a bit more if a certain someone didn’t go missing."
    
    L "Hm? But I wasn’t gone for long…"
    
    fa "Then explain to me why is my energy drained?"
    fa "Who’s fault is that?"
    
    L "Huh?"
    L "Your energy is drained?"
    
    "Lila was completely clueless."
    "Just as Emma was about to shout back Liam spoke."
    
    fb "Well we can always play again after we eat."
    
    "Settling the situation the three of them continued to walk towards the village."
    "Unaware that they were being watched from a distance."
    "Minglou bitterly stared at the three kids laughing innocently"
    
    m "Ignorance is a blessing isn’t it?"
    m "What would you seedlings have done if you discovered you’ve been living in the darkness…"
    
    "Of course she didn’t just mean that in a literal sense."
    "Who knows because they’ll never know at this rate."
    "The children just smiled and laughed not knowing what the future holds…."
    
    "End"
    "No Pages found."
    "Lila's Route."
    
return
    
label IntoDen:
    "Lila couldn’t hold in her curiosity so she insisted on going into the den."
    
    fb "Wait Lila."
    fb "I’ll go in to check first."
    fb "You shouldn’t go."
    fb "It could be dangerous."
    
    "Liam said, stopping Lila in her tracks."
    
    fa "Just don’t go into the den."
    fa "Why do you always have to cause so much trouble?"
    
    "Emma said, clicking her tongue."
    
    L "I don’t mean too."
    L "It’s just that I feel like there’s something in this den that is calling out to me."
    
    fa "You’re in your daydream world again."
    fa "You make no sense."
    fa "Let’s just go home."
    
    "Emma complained but Liam calmly replied."
    
    fb "It’s ok."
    fb "I’ll be back quick."
    fb "Emma if you’re tired, why don’t you take Lila and go home first"
    
    fa "I’m not going home without you and I’m not tired."
    
    "Emma contradicted her own statement from before."
    
    L "Are you sure you don’t want me to go with you?"
    
    fb "It’s fine."
    fb "Who knows what’s in there?"
    fb "As the oldest one,  I should take a look first."
    fb "Wait for me out here."
    
    L "Ok…"

    "Lila said quietly while Emma stayed quiet."
    "Liam smiled and disappeared into the cave."
    "As the two quietly waited outside the tension between them seemed to increase."
    "Emma’s gaze was just suffocating to Lila."
    "She wanted to say something but everytime she wanted to talk she felt the pressure from Emma forcing her to stay quiet."
    "The two stayed like this until they heard movement inside the den."
    "Flinching the two turn towards the entrance of the den."  
    
menu: 
    "Let’s check on Liam...I think something happened.":
        jump LetsCheckL
    
    "I’m going to check on Liam.":
        jump ICheckL
        
return 

label LetsCheckL:
    fa "You stay here."
    fa "I’ll go."
    
    "Emma said in a demeaning tone."
    
    L "But wouldn’t it be dangerous to go by yourself?"
    
    fa "Who said I was by myself?"
    fa "Liam is in there."
    fa "Besides between the two of us I’m stronger."
    fa "So if anything happens you run back to the village and call for help."
    
    "Although Emma may sound bossy she did speak logic."
    "It was true that between her and Emma, Emma is physically stronger."
    "Not to mention she replied a lot on Minglou’s powers when she’s in trouble."
    "But Minglou isn’t here at the moment so it would make sense for Emma to go in instead of her."
    
    L "Please be careful…"
    
    "Lila whispered."
    
    fa "Stop saying it like you’re sending me off to a funeral."
    fa "You’re such a cry baby."
    fa "Can’t help it."
    fa "If both me and Liam were to leave you alone one day who knows if you’ll survive on your own."
    
    L "I’d be fine!"
    L "I still have grandma!"
    
    "Lila puffed while Emma smirked."
    
    fa "Relax."
    fa "I’m saying we won’t leave you on your own."
    fa "Behave for once and stay put."
    fa "Wait for us to come back."
    
    "Emma said and entered the Den."
    "Her words were sharp but somehow it made Lila feel better."
    
    L "Come back soon!"
    
    "Lila shouted as Emma disappeared into the shadows."
    "For while Lila didn’t see or hear any other movement."
    "After anxiously waiting till she was tired and hungry she finally heard some rustling within the den."
    "From the darkness Lila saw two shadows come out of the entrance."
    
menu:
    "Welcome back guys!":
        jump WelcomeGuys
    
    "What did you find? Was it dangerous?":
        jump DangerFind
        
return 

label ICheckL:
    fa "You stay put."
    fa "I'm going in."
    
    "Emma growled stopping Lila in her tracks."
    
    L "But I’m worried"
    
    fa "So?"
    fa "What can you do?"
    fa "Are you able to call your spirit right now?"
    
    "Lila thought about Emma's words."
    "She remembered how she left Minglou by herself."
    "Knowing her, Minglou probably will refuse to have contact with her for a few days."
    
    L "No..."
    
    fa "And you think you can just charge into danger unarmed."
    
    L "Sorry..."
    
    "Lila whispered."
    "Seeing Lila being so depressed, Emma sighed."
    
    fa "Listen."
    fa "I didn’t mean to make you upset but between the three of us, Liam is the strongest."
    fa "I am second."
    fa "So if something did happen to him I should go."
    fa "Who’ll call back up if I don’t return?"
    
    "Emma questioned as Lila looked at her with confusion."
    
    fa "I’m talking about you dummy."
    fa "Just be ready."
    fa "If I don’t come back for a while, run to the village, ok?"
    
    "Emma said in a soft tone as she entered the cave."
    
    L "Come back soon!"
    
    "Lila shouted as Emma disappeared into the shadows."
    "For while Lila didn’t see or hear any other movement."
    "After anxiously waiting till she was tired and hungry she finally heard some rustling within the den."
    "From the darkness Lila saw two shadows come out of the entrance."
    
menu:
    "Welcome back guys!":
        jump WelcomeGuys
    
    "What did you find? Was it dangerous?":
        jump DangerFind
        
return 

label WelcomeGuys:
    "Lila greeted them warmly yet the expressions on their faces turned the happy mood instantly sour."
    
    L "Wh-What happened in the den?"
    L "You guys don’t look too good."
    
    "Liam looks the worst but because of Lila’s worried expression he calmed down."
    
    fb "Don’t worry… "
    fb "We just found something shocking."
    fb "That’s all."
    fb "It just takes a moment to take in new information."
    
    "Liam spoke but his voice was filled with uncertainty."
    
    fa "Why are you hiding this from her?"
    fa "She should know."
    
    "Although Emma also looked like she was in the state of shock her words were still headstrong."
    
    "Although Emma also looked like she was in the state of shock her words were still headstrong."
     
    fb "She wouldn’t be able to handle this…."
     
    "Liam protested but Emma insisted that they should inform Lila about their situation."
     
    fa "You can’t baby her forever."
    fa "She’ll be the one hurt if you keep shielding her from reality."
     
    fb "I just don’t want her to break because she’s too pure."
    fb "You shouldn’t keep pushing her either."
    fb "We’re her friends."
     
    "Liam argued but he wasn’t angry."
    "If anything he just sounds a bit more disappointed."
    "His words made Emma more heated."
    "Although Lila has no clue why they are arguing all the time, she feels like she’s responsible for it."
    "How should she calm down the situation?"
     
menu: 
    "I think I should know…I can handle it!":
        jump ICanHandle
    
    "It’s ok if I don’t know.":
        jump OkIDont
return 
       
label DangerFind:
    fa "What happened to you being worried for us?"
    
    L "But you guys look fine."
    
    fa "Why am I not surprised hearing you say that."
    fa "This is why I said he baby y-"
    
    "Noticing Emma’s unconsciously hurting Lila again Liam cut her off."
    
    fb "We’re fine."
    fb "The dan wasn’t that dangerous."
    fb "What we found though can be dangerous so let’s just forget about it."
    
    "Although Emma was cut the first time she’s not letting him have his way this time."
    
    fa "Why are you hiding this from her?"
    fa "She should know."
    
    "Although Emma also looked like she was in the state of shock her words were still headstrong."
     
    fb "She wouldn’t be able to handle this…."
     
    "Liam protested but Emma insisted that they should inform Lila about their situation."
     
    fa "You can’t baby her forever."
    fa "She’ll be the one hurt if you keep shielding her from reality."
     
    fb "I just don’t want her to break because she’s too pure."
    fb "You shouldn’t keep pushing her either."
    fb "We’re her friends."
     
    "Liam argued but he wasn’t angry."
    "If anything he just sounds a bit more disappointed."
    "His words made Emma more heated."
    "Although Lila has no clue why they are arguing all the time, she feels like she’s responsible for it."
    "How should she calm down the situation?"
     
menu: 
    "I think I should know…I can handle it!":
        jump ICanHandle
    
    "It’s ok if I don’t know.":
        jump OkIDont
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
