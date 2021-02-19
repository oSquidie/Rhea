define L = Character('Lila', color="#ced0ff", image = "Lila")
define m = Character('Mingluo', color="#87ddfb", image = "Mingluo")
define fa = Character('Emma', color="#73fff0", image = "Emma")
define fb = Character('Liam', color="#a673ff", image = "Liam")
define Q = Character ("?")

#define persistent.Route1 = True
#define persistent.Route2 = True

#define persistent.value = 0

define audio.RheaSoundtrack ="audio/RheaSoundtrack.wav"
define audio.RheaMain = "audio/RheaMainMenuMusic.wav"

play music RheaMain


label start:
    stop music fadeout 1.0
    play music "audio/RheaSoundtrack.wav" fadein 5.0 volume 0.3

    #$persistent.Route1 = True
    #$persistent.Route2 = True

    default preferences.text_cps = 50
    scene Map
    "Within a planet shrouded in darkness..."
    "In a forest far away from the nearest village."
    show Map:
        ease 3.0 zoom 2.0

    "A group of friends gathers to play hide and seek."
    "Whispers can be heard as glimmers of radiance reveals three kids."
    #show Lila happy at flip for flipping the sprite

    scene image "Forest_Default.png" with dissolve
    show Lila default at left
    show Liam default at right
    show Emma default at middle
    L "Hey...Have you guys ever wondered what it's like living in a world filled with light?"
    show Emma default at flip with dissolve
    show Emma concern at flip with dissolve
    "The three of them were deciding who to go first when Lila popped the question."
    show Liam sigh at right with dissolve
    fb "We're already living in a world that's like that. Aren't we?"

    "Liam seems to be a bit confused on the kind of world Lila envisoned."
    show Lila pout at left with dissolve
    L "No. I don't mean a world like this one."
    L "Not just tiny specks of glow here and there."
    L "A world where the entire land, no, the entirety of Rhea is filled by a very, very bright light."
    show Emma angry at flip with dissolve
    fa "What are you suddenly talking about?"
    show Lila happy at left with dissolve
    L "You know! Something even more blinding than the glows from an Enoki mushroom!"
    show Emma sigh at flip with dissolve
    fa "You've lost your head again. Can we just focus the game?"
    show Liam wink at right with dissolve
    fb "Patience Emma. We have plenty of time."

    fa "I'm just saying I'm not interested in her make believe fantasy."

    fb "It may be fantasy but it might not be make-believe."
    show Emma concern at yflip with dissolve
    fa "Huh? What are you on about? If you keep leading her on these crazy daydreams..."
    fa "She'll become even more stu-"
    show Liam happy at right with dissolve
    fb "I also think we should start playing the game."
    fb "It's been a while since we've gathered. Let's enjoy this rare moment!"

    "Liam raised his voice but his uplifting tone didn't change."
    show Lila pout at left with dissolve
    L "Oh... I guess you guys are getting bored."
    show Emma sigh at flip with dissolve
    "Lila sounded disappointed at their reactions."
    "But she wasn't disappointed for long."
    show Lila smile at left with dissolve
    "She did miss her friends after all."

    fa "How are you so thick headed for you to realize that just now?"
    show Emma angry at flip with dissolve
    show Lila surprised at left with dissolve
    L "Huh? Thick headed?"
    show Lila pout at left with dissolve
    "She hates it when Emma uses words she don't understand. It always left an awful feeling in her."

    fb "Ah! Ignore her. Ignore her. Let's play! What do you want to be Lila? The seeker or hidder?"
    show Liam wink at right with dissolve
    menu:
        "Seeker?": #if persistent.Route1 == True:
            jump Seeker
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
    show Lila eyes closed at lilaflip with dissolve
    "Surrounded by tall trees Lila stood there counting in the dark."
    "The warm glows from the fireflies engulfs her mind as she slowly loses herself in her thoughts."

    L "55"
    L "54"
    L "53"
    show Lila sad at lilaflip with dissolve
    "Each time the numbers go down she feels a bit more lonely than before."
    "Is it because of the darkness?"
    "That can't be it...She grew up in such an environment."
    show Lila eyes closed at lilaflip with dissolve
    L "52"
    L "51..."

    Q "OUCH!" with vpunch
    show Lila shocked at yflip with dissolve
    "Startled, she lost her thought process."
    "She faced the direction where the loud noise came from. "
    "She waited for a few more moments for any kinds of other movement but all she heard was silence."
    "Thinking she may have misheard she went back to counting."
    show Lila eyes closed at lilaflip with dissolve
    L "50"
    L "4-!"

    Q "Ouch! What was that for?" with vpunch
    show Lila pout at lilaflip with dissolve
    "Once again grabbing her attention she observes from a distance."
    "She was a bit conflicted as to whether or not she should go check up on her friend."
    "After all, She is still in the middle of a game."
    "After thinking for a while, her concerns overpowered her determination to win."
    "She went to investigate the noise."
    show Lila surprised at yflip with dissolve
    L "Emma?"
    L "Are you ok?"
    show Emma angry at emmaflip with dissolve
    fa "I'm fine!"
    show Liam sigh at right with dissolve
    "Soon after Emma popped up her other friend Liam popped up as well"
    menu:
        "Are you sure? You sounded like you were in pain.":
            jump YouSure
        "Oh... Are you ok Liam?":
            jump LiamOk
return

label YouSure:
    show Emma pout at emmaflip with dissolve
    fa "I already said I'm fine."
    show Lila smile at yflip with dissolve
    L "I have some medication on me if you nee-"
    show Emma angry at emmaflip with dissolve
    show Lila pout at yflip with dissolve
    fa "Enough! I'm not that weak. Why are you so annoy-!"
    show Liam happy at right with dissolve
    fb "Ahaha! You found us! Looks like Emma is the seeker next."
    show Emma pout at emmaflip with dissolve
    "Liam cut Emma off mid-sentence."
    show Lila smile at yflip with dissolve
    L "I guess I did."
    L "But Emma you should still put some ointment on just in case..."

    fa "UGH! I don't need anything."
    show Emma angry at emmaflip with dissolve
    fa "Just listen to me."
    fa "This round isn't fair for Liam."
    fa " You should recount!"
    show Lila stunned at yflip with dissolve
    show Liam surprised at right with dissolve
    "Although the two should already be used to Emma's behavior they couldn't help but be a little bewildered."
    show Liam smile at right with dissolve
    fb "No. no."
    fb "It's fine."
    fb "I can be the seeker."
    fb "No need for Lila to re-"

    fa "This isn't fair. She needs to recount."
    show Liam sigh at right with dissolve
    "Liam sighed."

menu:
    "But I already found you guys":
        jump SeekerL

    "Oh ok! I can be seeker again!":
        jump SeekerLila

return

label SeekerL:
    show Lila pout at yflip with dissolve
    show Liam smile at right with dissolve
    fb "Lila's right."
    fb "She's already found us."
    fb "It would be more fair if one of us plays as the seeker next."
    show Emma pout at emmaflip with dissolve
    fa "..."
    show Lila nervous at yflip with dissolve
    "Lila anxiously wondered what she had done this time to bother Emma {cps=2}...{/cps} again. "
    show Emma angry at emmaflip with dissolve
    fa "Fine."
    fa "But I'm not being 'it'"
    hide Emma angry at emmaflip with dissolve
    show Liam wink at right with dissolve
    fb "That's ok. I'll be 'it'. You guys should hide. "
    show Lila sad at yflip with dissolve
    L "I'm sorry Liam..."

    "Lila suddenly felt a sense of guilt yet she doesn't know why."
    show Liam surprised at right with dissolve
    fb "Hm?"
    fb "Why do you feel sorry?"
    show Liam happy at right with dissolve
    fb "Don't worry."
    fb "There's nothing to be sorry about."
    fb "You should instead focus on hiding."
    show Lila surprised at yflip with dissolve
    "Lila felt conflicted on how to explain this feeling."
    "Before she can even formulate words Liam started to count."
    fb "Are you ready! I'm starting to count!"
    show Liam wink at right with dissolve
    "After leaving her with a wink he left her standing there"
    show Liam happy at right with dissolve
    fb "100!"
    fb "99!"
    fb "98!"
    hide Lila surprised at yflip with dissolve
    hide Liam happy at right with dissolve
    "Panicking she went to find a hiding spot."
    show Lila nervous at left with dissolve
    "Even after she has left the two of them she couldn't help but feel a bit awful."
    "Distracted by this feeling, she realized that she may have gone a bit too far."
    "Before she realized she was in an unfamiliar place."
    scene image "Twopaths.png" with fade
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
    show Lila happy at yflip with dissolve
    show Emma happy at emmaflip with dissolve
    fa "See! She wants to be the seeker!"
    show Liam surprised at right with dissolve
    "Liam looks shocked. While Emma Smirks"
    show Emma smug at emmaflip with dissolve
    fb "Are you sure? You don't have to force yourself."
    show Lila smile at yflip with dissolve
    #"Lila smiled."
    show Liam smile at right with dissolve
    L "I'm not forcing myself."
    L "I just love playing with you guys."
    L "As long as I can play with you guys...I don't mind what I am."
    show Liam sad at right with dissolve
    show Emma shocked at emmaflip with dissolve
    "Liam's smile dropped."
    "He thought deeply for a moment while Emma's face showed panic."

    fa "Hey Liam."
    fa "She already-"
    show Liam wink at right with dissolve
    fb "What if I wanted to be the seeker and I really want to be 'it'"
    show Emma pout at emmaflip with dissolve
    #"Emma frowned."
    "She knew Liam was going to play with Lila's heart strings."
    "Even so, she doesn't want to push him any further."
    "Even she knows she's being childish."
    "She can only pray Lila will reject that idea."
    show Lila surprised at yflip with dissolve
    L "Oh {cps=2}...{/cps}Do you really want to be 'it'?"

    #"Liam smiled."
    show Liam happy at right with dissolve
    fa "I definitely do!"

    #"Lila innocently smiled back."
    show Lila happy at yflip with dissolve
    L "Whatever makes you happy!"
    show Emma pout at emmaflip with dissolve
    #"Emma frowned."

    fa "Your favoritism is so obvious and I hate it..."

    "Emma grumbled but it was so quiet the other two didn't hear her."

    fb "Ok! I'll start counting now! Go hide!"

    L "Ok!"
    hide Emma pout at emmaflip with dissolve
    hide Lila happy at yflip with dissolve
    hide Liam happy at right with dissolve
    "With that the three scattered."
    "Emma and Lila went in opposite directions."
    "Lila continued to explore until she ended up in a place she's unfamiliar with."
    scene image "Twopaths.png" with fade
    show Lila surprised at left with dissolve
    L "I don't think I've been here before."

    "Catching her breath, she took a moment to frantically look around."
    "From what she could see, to her left was a cave covered in transparent crystals and tiny little glowing fungi."
    "The cave seems endless and very spacious."
    "Besides the cave, to her right was some kind of animal den."
    "Though pitched black inside, the outside is swarmed with fireflies and different kinds of glowing mushrooms."
    "She can't tell what kind of animal made this den but she knows she's big enough to fit through."

    "Despite the danger these do look like good hiding places."

    L "Which way should I go?"

menu:
    "The endless cave":
        jump Cave

    "The animal Den":
        jump Den

return

label LiamOk:
    show Liam wink at right with dissolve
    fb "Hm? How kind Lila."
    fb "Don't worry."
    fb "I'm perfectly fine."
    show Emma pout at emmaflip with dissolve
    fa "Of course he's fine!"
    fa "I was the one hurt..."

    #"Emma responded with a frown as she grinded her teeth."
    show Lila surprised at yflip with dissolve
    L "But I thought you said you are fine Emma?"

    "Lila said with no hostility."
    "She was actually just confused and puzzled."
    "However, for some reason Emma looks even more menacing."
    show Emma angry at emmaflip with dissolve
    fa "That's it!"
    fa "You're recounting Lila!"
    fa "This round isn't fair!"
    show Lila stunned at yflip with dissolve
    L "Huh?"
    show Liam nervous at right with dissolve
    fb "Now, now."
    fb "There's no need for that."
    fb "I can do the counting."
    fb "Let's take turns being the seeker."
    show Emma concern at emmaflip with dissolve
    fa "But that's not fair!"
    fa "You got found because of me."
    fa "So she should just recount and start over."
    show Liam smile at right with dissolve
    fb "Emma, don't be unreasonable."
    fb " I really don't mind being the seeker."
    fb "Let's not fight over something so small."
    show Lila pout at yflip with dissolve
    "Liam explained but he didn't even sound a bit annoyed."
    "Instead, he handled it with patience and sternness."
    "Still Emma refuses to back down."
    "What should Lila do?"
    menu:
        "I'm ok with being seeker again.":
            jump OkSeeker

        "I also want Liam to be the seeker this time!":
            jump LiamSeeker

label LiamSeeker:
    show Lila smile at yflip with dissolve
    "Just as the two were about to get heated Lila broke the tension."
    show Emma angry at emmaflip with dissolve
    fa "I just said that it was unfair for Liam. Are you de-"

    "Emma seems like she'll explode but Liam stopped her with a very calm voice."
    show Liam smile at right with dissolve
    fb "It's ok Emma. It would be more fair if I play as the seeker next."

    fa "..."
    show Lila nervous at yflip with dissolve
    "Lila anxiously wondered what she had done this time to bother Emma {cps=2}...{/cps}again."
    show Emma concern at emmaflip with dissolve
    fa "Fine."
    "Emma grumbled. Her voice sent a bit of fear down Lila's spin. "
    show Lila sad at yflip with dissolve
    L "I'm sorry Emma...I'm sorry Liam..."

    "Lila felt a sense of guilt yet she doesn't know why. "
    show Liam wink at right with dissolve
    fb "Hm?"
    fb "Why do you feel sorry?"
    fb "Don't worry."
    fb "There's nothing to be sorry about."
    fb "You should instead focus on hiding."
    show Emma angry at emmaflip with dissolve
    "Emma didn't say anything."
    #"She just stood there with a very scary face."
    "Lila felt conflicted on how to explain this feeling."
    show Lila pout at yflip with dissolve
    show Liam happy at right with dissolve
    show Lila nervous at yflip with dissolve
    fb "Are you ready! I'm starting to count!"
    "Before she can even explain anything Liam started to count."
    hide Emma angry at emmaflip with dissolve
    hide Lila nervous at yflip with dissolve
    "Panicking she went to find a hiding spot."

    fb "100!"
    fb "99!"
    fb "98!"
    hide Liam happy at right with dissolve
    scene image "Twopaths.png" with fade
    show Lila surprised at left with dissolve
    L "Oh no...I-I don't remember seeing these paths."
    show Lila surprised at left with dissolve
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
    show Emma smug at emmaflip with dissolve
    fa "See! She wants to be the seeker!"

    #"Liam looks shocked. While Emma Smirks"
    show Liam smile at right with dissolve
    fb "Are you sure? You don't have to force yourself."

    #"Lila smiled."
    show Lila smile at yflip with dissolve
    L "I'm not forcing myself."
    L "I just love playing with you guys."
    L "As long as I can play with you guys...I don't mind what I am."
    show Liam sad at right with dissolve
    show Emma shocked at emmaflip with dissolve
    "Liam's smile dropped."
    "He thought deeply for a moment while Emma's face showed panic."

    fa "Hey Liam."
    fa "She already-"
    show Liam wink at right with dissolve
    fb "What if I wanted to be the seeker and I really want to be 'it'"
    show Emma pout at emmaflip with dissolve
    #"Emma frowned."
    "She knew Liam was going to play with Lila's heart strings."
    "Even so, she doesn't want to push him any further."
    "Even she knows she's being childish."
    "She can only pray Lila will reject that idea."
    show Lila surprised at yflip with dissolve
    L "Oh {cps=2}...{/cps}Do you really want to be 'it'?"
    show Liam happy at right with dissolve
    #"Liam smiled."

    fa "I definitely do!"
    show Lila happy at yflip with dissolve
    "Lila innocently smiled back."

    L "Whatever makes you happy!"
    show Emma pout at emmaflip with dissolve
    #"Emma frowned."

    fa "Your favoritism is so obvious and I hate it..."

    "Emma grumbled but it was so quiet the other two didn't hear her."

    fb "Ok! I'll start counting now! Go hide!"

    L "Ok!"
    hide Emma pout at emmaflip with dissolve
    hide Lila happy at yflip with dissolve
    hide Liam happy at right with dissolve

    "With that the three scattered."
    "Emma and Lila went in opposite directions."
    "Lila continued to explore until she ended up in a place she's unfamiliar with."
    scene image "Twopaths.png" with fade
    show Lila surprised at left with dissolve
    L "I don't think I've been here before."

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
    scene Cave
    with dissolve
    show Lila default at lilaflip with dissolve
    L "At least it has more room to breath then the den."
    "Making up her mind Lila chose to hide inside the cave."
    "Even though she's never been here before it didn't scare her."
    show Lila sad at lilaflip with dissolve
    "However, as she waited in the cave she felt more and more lonely."
    "The chilly atmosphere once again reminded her of the warmth of Enoki mushrooms."
    "She forgot to bring some with her now she feels nothing but the cold."
    show Lila pout at lilaflip with dissolve
    L "I really wish there was a giant Enoki mushroom."

    L "Maybe it's warmth would make me feel less lonely..."

    "She wondered to herself."
    show Mingluo no eyes at right with dissolve
    Q "What if I told you that does exist?"
    show Lila shocked at lilaflip with dissolve
    "Lila shivered at the sudden tingling sensation left from the words whispered in her ears."

    L "WHAT?!"
    show Lila shocked at yflip with dissolve
    "Lila shouted and turned to look at the person who whispered those words."

    L "Minglou?!"

    m "What was that reaction?"
    show Mingluo skeptical at right with dissolve
    "Minglou said standing there unfazed. Lila stared at her shocked."
    show Lila nervous at yflip with dissolve
    L "Why did you sneak up on me?"

    m "There's no need for that. Someone as slow minded as you scared yourself."
    show Lila surprised at yflip with dissolve
    L "Huh?"

    "What does that even mean...Wait more importantly."
    show Lila stunned at yflip with dissolve
    L "What did you say exists?"

    "Lila asked, just catching on to Minglou's previous statement."
    show Mingluo annoyed at right with dissolve
    m "What did you think I said existed?"
    show Lila pout at yflip with dissolve
    "She really hates it when Minglou questions her."
    "But if she doesn't respond back, she'll never get the answers she's looking for."
    "Why does she always do this?"
    "What should she say back?"

menu:
    "The enoki mushrooms?":
        jump EMush

    "Can you please explain to me what you mean?":
        jump PleaseEx
return

label EMush:
    show Mingluo smile at right with dissolve
    #"Minglou's eyes widened."
    "Surprisingly she gently smiled."
    "For once it didn't feel like an edge of a knife."

    m "Would you look at that? After so long you did grow after all. You listened for once."
    show Lila surprised at yflip with dissolve
    L "Wait? But don't enoki mushrooms already exist?"
    show Mingluo angry at right with dissolve
    "All in that one moment, Minglou is back to her grumpy self."
    show Mingluo disgust at right with dissolve
    m "Just as I was about to say I was proud... I wasn't talking about those tiny enoki mushrooms."
    show Lila default at yflip with dissolve
    L "But you just said I was correct."

    m "I said you listened but I take that back."

    "Ignoring all of Minglou's unpleasant words Lila grew an immense interest in what she was talking about."
    show Lila happy at yflip with dissolve
    L "No Way!"

    "Lila shouted in excitement while Minglou starred on the side in shock."

    L "Did you find a new mushroom species?!"
    show Mingluo annoyed at right with dissolve
    "Minglou grumbled but she wasn't displeased."
    show Mingluo default at right with dissolve
    m "Though that would be intriguing."
    m "I found something even more interesting."
    show Lila surprised at yflip with dissolve
    "Lila's eyes instantly sparkled."
    show Lila happy at yflip with dissolve
    L "What did you find?!"
    show Mingluo smile at right with dissolve
    #"Minglou smirked."

    m "Follow me and you'll know."
    hide Lila happy at yflip with dissolve
    hide Mingluo smile at right with dissolve
    "The two went deeper into the cave until they reached an area covered in enoki mushrooms."
    show Lila happy at left with dissolve
    L "Whoa!"
    L "I didn't know there were so many of them here."
    L "To think I was cold just a minute ago."
    show Mingluo skeptical at right with dissolve
    "Lila was about to go gather some but Minglou stopped her."
    show Lila stunned at left with dissolve
    L "Huh? Why did you stop me?"
    show Mingluo smile at right with dissolve
    "Lila questioned but Minglou gave her a very mischievous smirk."
    "Though Lila felt uncomfortable whenever Minglou gave her this look, she's gotten somewhat used to it."

    m "Don't be so Hasty."
    m "Take a closer look..."
    m " Noticed anything unusual?"
    show Lila surprised at left with dissolve
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

    #"Minglou sighed."
    show Mingluo disgust at right with dissolve
    show Lila pout at left with dissolve
    m "And here I thought you grew as a person. How disappointing..."

    "Lila felt a sense of devastation after hearing Minglou's reply."

    m "Don't look at me like that."
    m "You're the one forgetting something I've said literally within a couple of seconds."
    show Lila stunned at left with dissolve
    #"Lila looks at Minglou full of confusion."

    L "Seconds?"
    show Mingluo annoyed at right with dissolve
    m "Right...I forgot that your race doesn't even know how to tell the span of time."

    "Lila has no clue what Minglou is referring too and can only helplessly stand there listening to her rant."
    show Mingluo default at right with dissolve
    m "Forget it."
    m "I'll do you a favor."
    m "You are my last hope after all...."

    "Minglou murmured but Lila didn't catch any of what she said."

    m "Just follow me...."

    "Lila quietly followed Minglou."
    hide Mingluo default at right with dissolve
    hide Lila stunned at left with dissolve
    "Although she has no clue what is happening she felt a bit sad and depressed."
    "She wants to cry but she knows Minglou won't comfort her."
    "Minglou just watched her quietly."
    "However, after walking for a bit, Minglou decided to break the silence."
    show Mingluo skeptical at right with dissolve
    m "What. Feeling upset?"
    show Lila sad at left with dissolve
    L "..."
    show Lila tears at left with dissolve
    "Lila didn't say anything as tears welled up in her eyes."
    show Mingluo disgust at right with dissolve
    m "Why don't you look up."
    m "You might just cheer up, you cry baby."
    show Lila surprised at left with dissolve
    "Curious about what Minglou was talking about Minglou looked around."
    "Lila's eyes glittered instantly."
    "All of the tears evaporated in that one instant."
    "They were surrounded by enoki mushrooms."
    "So many have gathered in one place."
    "This is so rare!"

    L "There's so many!"

    "She said, turning to face Minglou."
    show Mingluo smile at right with dissolve
    #"Minglou gave her a very mischievous smirk."
    "Though Lila felt uncomfortable whenever Minglou gave her this look, she's gotten somewhat used to it."

    m "Noticed anything unusual?"
    m "Don't disappoint me this time."

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
    show Mingluo skeptical at right with dissolve
    m "Is that so?"

    #"Minglou's face didn't change. She is still as stoic as ever."

    m "What do you think makes this place warm?"
    show Lila surprised at left with dissolve
    L "I believe it's the enoki mushrooms?"

    "Lila answered but was uncertain."
    show Mingluo annoyed at right with dissolve
    m "That isn't wrong."
    m "But I want you to think even deeper."
    m "When enoki mushrooms gather are they usually this warm?"

    "When Minglou asked that question something felt unpleasant to Lila."
    "She thought for a moment."
    "Enokis don't produce enough warmth unless they gather together."
    "But if too much gathered they will overheat and cause a fire."
    "Yet...Why isn't the cave burning?"
    #"Minglou's expression darkened."
    show Mingluo smile at right with dissolve
    m "Honey, you are so close to the answer. Think even deeper."

    "Lila didn't even notice the way Minglou was looking at her."
    "Her eyes focused on one thing only."
    "The pile of mushrooms gather in that one corner."
    "What is it that causes all of them to gather?"
    "Iching closer Lila looked into the pile of mushrooms."
    hide Mingluo smile at right with dissolve
    hide Lila surprised at left with dissolve
    scene image "SecondPage.png" with fade
    "In the center was one piece of paper."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn't look that special."
    "What made Lila drawn to it was that even though the paper was surrounded none of the mushroom parts touched the paper."
    "While her eyes were still glued to the paper Minglou picked it up and in a one moment the paper went into flames."
    scene image "Cave.png" with fade
    L "Minglou!"
    show Mingluo page at right with dissolve
    show Lila shocked at left with dissolve
    "Lila panicked as she screamed for Minglou."
    "Minglou is a water spirit."
    "Fire might cause her harm."
    "Yet in a blink of an eye the flames went out."
    "Standing in front of her was Minglou smiling while handing over the paper to Lila."
    "The blank piece of paper now filled with symbols is in her face."
    show Lila stunned at left with dissolve
    show Mingluo smile at right with dissolve
    "Trying to wrap her head around everything Lila became very confused."

menu:
    "Ask Minglou for context":
        jump MContext

    "Ask Minglou if she's ok":
        jump MingOk
return

label ToMany:
    show Mingluo smile at right with dissolve
    m "Oh?"
    m "Nice job noticing."
    m "Why don't you go check it out?"

    #"Minglou said with a smirk on her face."
    "Though Lila's felt this odd feeling from when she first met up with Minglou she still listened to her words."
    "She got closer to observe the mushrooms."
    hide Mingluo smile at right with dissolve
    hide Lila surprised at left with dissolve
    scene image "SecondPage.png" with fade
    "In the pile of all the mushrooms, there was a piece of paper in the center."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn't look that special."
    "What made Lila drawn to it was that even though the paper was surrounded none of the mushroom parts touched the paper."
    "While her eyes were still glued to the paper Minglou picked it up and in a one moment the paper went into flames."
    scene image "Cave.png" with fade
    L "Minglou!"
    show Lila shocked at left with dissolve
    "Lila panicked as she screamed for Minglou."
    "Minglou is a water spirit."
    "Fire might cause her harm."
    "Yet in a blink of an eye the flames went out."
    "Standing in front of her was Minglou smiling while handing over the paper to Lila."
    "The blank piece of paper now filled with symbols is in her face."
    show Mingluo smile at right with dissolve
    "Trying to wrap her head around everything Lila became very confused."

menu:
    "Ask Minglou for context":
        jump MContext

    "Ask Minglou if she's ok":
        jump MingOk
return

label MContext:
     show Lila stunned at left with dissolve
     L "Wha-What just happened?!"
     show Mingluo skeptical at right with dissolve
     m "Nothing much."
     m "Just a little special ability of mine."
     show Mingluo smile at right with dissolve
     m "Anyways you should pay more attention to this magnificent artifact."

     "It looks like Minglou won't explain what has happened."
     show Lila default at left with dissolve
     "Has she always had an ability like that?"
     "Lila never knew."
     "Lila knows that unlike most spirits, Minglou can travel from her world to the spirit realm without the need of Lila's powers."
     "Minglou is a very powerful spirit but can a water spirit withstand the intensity of flames?"
     "Unharmed?"
     "Lila regrets not paying attention in class now."
     "Staring at the paper Minglou handed to her, Lila noticed that there was some language written on there that seems familiar."
     "Other than those few symbols most of the other ones she's never seen before."
     show Lila surprised at left with dissolve
     L "What does this say?"
     L "What is this?"
     show Mingluo disgust at right with dissolve
     #"Lila questioned while Minglou looked at her in disbelief."

     m "Child{cps=2}...{/cps}It's written in your home language."
     m "How can you not understand?"
     m "I get that some of it is in ancient lingo but you should be able to read the other symbols right?"
     show Lila stunned at left with dissolve
     #"Lila stared at Minglou blankly."
     show Mingluo annoyed at right with dissolve
     m "Ugh."
     m "Forget it."
     m " What was that peepsqueaks name?"
     m "The boy you always hang around with."
     show Lila pout at left with dissolve
     L "Peepsqueak? Are you talking about Liam?"

     "Lila has no clue what Minglou meant but she has a gut feeling she was refering to Liam."
     show Mingluo smile at right with dissolve
     m "Ah yes."
     m "Him."
     m "At least you're not that dimwitted to not know your own friend's name."
     show Lila angry at left with dissolve
     L "Why do I feel like you said something rude again..."

     "Lila always hated the way Minglou spoke."
     "Even someone as level headed as Liam got pissed at Minglou once."

     m "Forget what I said and just take the paper to that dweeb."
     show Lila surprised at left with dissolve
     L "Who's Dweeb?"
     L "Also why can't you just tell me what it says?"
     show Mingluo angry at right with dissolve
     "Minglou sounds frustrated."

     m "Because I refuse to help decode human words."
     m "I despise it."
     show Lila pout at left with dissolve
     "Lila knew that Minglou had always hated her kind and she didn't know why."
     "Everytime she asks why, Minglou not only refuses to answer, she gets super heated."
     "So this time she chose to stay quiet."

     m "We've been here long enough already."
     m "Get going."
     m "Give that to the Liam kid."

     "Oh."
     "She was talking about Liam."
     show Lila default at left with dissolve
     L "Oh ok..."
     L "Um..."
     L "Do you mind if I ask one last question Minglou?"
     show Mingluo annoyed at right with dissolve
     m "I'll take as many questions as you have after you've talked with Liam."
     show Lila nervous at left with dissolve
     L "But it's important."

     m "How important?"

     L "Uhhhh...."

     L "As important as I don't know how to get back..."
     show Mingluo disgust at right with dissolve
     m "Was that the question?"

     L "Kind of?"

     m "...."
     show Lila smile at left with dissolve
     L " Yeah..."

     #"Lila said smiling."
     #"Minglou sighed."
     show Mingluo annoyed at right with dissolve
     m "Just follow me."
     scene image "Forest_Default.png" with fade
     "As Lila followed Minglou out of the cave from a distance she spotted two figures."
     "From the looks of it, it was Liam and Emma."

menu:
    "Look Minglou, it's Liam and Emma! Let's go say Hi!":
        jump MinglouHi

    "Call out to them":
        jump CallOut
return

label MingOk:

    m "Hm?"
    m "I'm perfectly fine."
    show Mingluo annoyed at right with dissolve
    "Minglou sounded almost a bit annoyed but she wasn't as harsh as the other times Lila pissed her off."

    L "B-But you're a water spirit..."

    #"Minglou's eyes darkened."
    show Mingluo skeptical at right with dissolve
    m "So what if I am?"
    show Lila surprised at left with dissolve
    L "Doesn't water hurt you?"
    L "Did I remember wrong?"

    m "I think you did."
    m "You tend to forget I'm not like those other weaklings."

    "Minglou was monotone but Lila felt a chill."

    m "I even went so far to show you this priceless artifact."
    m "Why don't you appreciate this moment you have?"
    m "It's a bit useless to worry about unnecessary things."
    show Mingluo page at right with dissolve
    "Minglou handed Lila the paper that was in flames."
    "She took the paper and looked at it."
    "Not even a single sign showed that it was in flames."
    "Didn't paper burn into ashes when it comes into contact with fire?"
    "Why didn't this one burn?"
    "However, besides that question."
    "The question that bothers her the most is what is the symbols that appeared on the paper."
    "How and why did it appear?"

    L "What does it say?"
    show Mingluo disgust at right with dissolve
    #"Lila questioned as Minglou stood there in disbelief."

    m "You mean to tell me you don't know how to read your own language?"
    show Lila nervous at left with dissolve
    "Lila looks embrassed."

    m "Not even the basics?"

    L "No...But Liam Knows!"

    "Lila said in an upbeat tone while Minglou shivered at that name."
    show Mingluo annoyed at right with dissolve
    m "Don't mention that brat's name."
    m "I hate the looks he gives me."
    m "It's like he can read right through me."

    "Lila looked at her in confusion."

    m "Ugh."
    m "Forget it"
    m "Just take the paper and go ask him."

    "Minglou grumbled wanting to leave."
    "It seems she's also  mentally exhausted."

    L "Ah wai-"

    "Sensing in her instinct that Minglou was about to leave she tried to stop her by calling out to her."
    hide Mingluo annoyed at right with dissolve
    L "And she's gone..."
    show Lila pout at left with dissolve
    "Looks like she didn't call out in time."
    "Minglou's essence was no longer in the cave."
    "What should she do?"
    "She doesn't know the way out of the cave..."
    "While she was lamenting she hears familiar voices calling out her name."
    hide Lila pout at left with dissolve
    "Following the voices she finds her way out of the cave."
    "Meeting up with her is Liam and Emma."
    scene image "Forest_Default.png" with fade
menu:
    "I missed you guys!":
        jump MissedY

    "Liam! I was about to look for you!":
        jump LiamLook

return

label MissedY:
    show Lila happy at left with dissolve
    L "Ah!"
    L "Liam!"
    L "Emma!"
    L "I missed you guys!"

    "Lila cheerfully called out to them."
    show Emma pout at emmaflip with dissolve
    show Liam happy at right with dissolve
    "The three of them gathered together as the two took their time to catch their breaths."

    L "Oh I also have to thank Ming-"

    "Lila wanted to thank Minglou for taking her out of the cave but she was already nowhere to be seen."
    show Liam surprised at right with dissolve
    fb "Huh?"
    fb "Did you say something Lila?"

    "Liam asked while his breath settled."
    show Lila smile at left with dissolve
    L "Uh?"
    L "No-"
    L "I-it's nothing."
    show Liam nervous at right with dissolve
    fb "You went a bit too far."
    fb "We barely managed to find you."
    show Emma sigh at emmaflip with dissolve
    fa "You sure like causing trouble you direction freak."

    "Uh oh... Looks like she's been scolded."
    "Wait... wasn't there something she wanted to show them?"
    "Oh right!"
    show Lila happy at left with dissolve
    L "You guys appeared just in time. I have something to show you..."
    show Liam surprised at right with dissolve
    show Emma concern at emmaflip with dissolve
    "Lila said getting excited as she showed them the paper Minglou found for her."
    "It seems that being with her friends made her forget that she was lost. "

    fa "I told you, you worried over nothing."
    show Liam smile at right with dissolve
    show Emma angry at flip with dissolve
    "Emma growled at Liam. Liam only smiled back."

    fb "We can never be too cautious."

    "He replied before the three of them took a closer look at the paper."
    show Liam surprised at right with dissolve
    fb "That is so interesting..."
    show Emma pout at emmaflip with dissolve
    show Liam page at right with dissolve
    "Liam said as he held out a similar paper."
    show Lila surprised at left with dissolve
    L "Huh?"
    L "Where did you find that?"
    show Liam surprised at right with dissolve
    fb "By the Den...."

    L "What does yours say?"
    L "Can you read mine?"
    L "Minglou didn't tell me anything."
    show Emma shocked at emmaflip with dissolve
    show Liam shocked at right with dissolve
    "The two of her friends flinched at the mention of Minglou's name."
    show Emma angry at emmaflip with dissolve
    show Liam sigh at right with dissolve
    fa "I've always hated that spirit of yours."
    fa "There's something about her I don't like."
    show Emma angry at emmaflip with dissolve
    show Liam sigh at right with dissolve
    "Emma said but Lila has no clue what she's referring too."
    show Lila stunned at left with dissolve
    L "Really?"
    L "I never thought anything of her that came off as bad."
    show Emma concern at emmaflip with dissolve
    fa "That's because you're too mushy to notice."

    L "Mushy?"

    fa "Like I said-"
    show Liam angry at right with dissolve
    fb "Nevermind that."
    fb "I just read these pages."
    fb "They talk about something terrifying."
    show Emma concern at flip with dissolve
    show Lila surprised at left with dissolve
    L "What do you mean?"

    "Emma was equally as confused."

    fb "It talks about the existence of something called The Sun..."
    show Emma shocked at emmaflip with dissolve
    #"Emma's expression darkened."

    fa "That can't be."
    fa "You must have read wrong."
    show Lila stunned at left with dissolve
    L "What are you guys talking about?"
    L "What is The Sun?"
    show Liam sigh at right with dissolve
    fb "Emma's right."
    fb "I only know what's written on here to some extent."
    fb "We should confirm it at the library where I can do more research."
    show Emma concern at emmaflip with dissolve
    L "Wait, explain to me first."
    show Emma angry at flip with dissolve
    show Liam nervous at right with dissolve
    fa "Ughhhhhh!"
    fa "This is why you get on my nerves."
    fa "I say it once ok."
    fa "But you can't tell no one...yet."

    L "Ok! I promise."

    fa "Remember the stuff you talked about before we played the game?"
    show Lila surprised at left with dissolve
    L "Uh...I don't remember much really."

    fa "What?"
    fa "How can you forget?!"
    fa "It wasn't too long ago!"
    fa "Urhhhh."
    fa "Nevermind."
    fa "Listen carefully."

    #"Lila inched closer to Emma and in return Emma whispered back."

    fa "It's what brings light into this world."
    fa "A light brighter than any mushrooms on this planet."
    show Lila shocked at left with dissolve
    "Lila's eyes widened."
    "She didn't even question how Emma knew that."
    "She's even more curious about the existence of this thing called The Sun."
    show Lila happy at left with dissolve
    L "Tell me more!"

    "Lila Shouted."
    show Emma sigh at flip with dissolve
    fa "Shhhh! Be quiet!"

    "Although Lila was confused why they were being so secretive about it."
    "She wanted to ask but Liam stopped her."
    show Liam sigh at right with dissolve
    fb "That's only a legend spreaded by rumors."
    fb "We should get out of here first."
    fb "There's a reason why those rumors died out."

    "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
    "All three of them nodded and then started to head back towards the village."
    "It seems Liam wants to meet up again at the library."
    "Determined to find out more about The Sun, they continued down the path towards the library."
    hide Lila happy at left with dissolve
    hide Emma sigh at flip with dissolve
    hide Liam sigh at right with dissolve
    scene image "BGStart.png" with fade
    "End."
    "Page 1 discovered."
    "Lila's Route."
return

label LiamLook:
     show Lila happy at left with dissolve
     show Liam sigh at right with dissolve
     fb "Lila!"
     fb "Why did you go out so far!"
     fb "We barely managed to find you."
     show Emma angry at flip with dissolve
     fa "You sure like causing trouble you direction freak...Also why are you looking for Liam only?"
     show Lila pout at left with dissolve
     "The two of them got closer to Lila as they grasped for breath."
     "Though Emma seems to be more upset than happy to see her."

     L "Oh."
     L "That's because I have something to show him..."

     fa "I told you you worried over nothing."
     show Liam smile at right with dissolve
     show Emma angry at flip with dissolve
     "Emma growled at Liam. Liam only smiled back."

     fb "We can never be too cautious."

     "He replied before the three of them took a closer look at the paper."
     show Liam surprised at right with dissolve
     fb "That is so interesting..."
     show Emma pout at emmaflip with dissolve
     show Liam page at right with dissolve
     "Liam said as he held out a similar paper."
     show Lila surprised at left with dissolve
     L "Huh?"
     L "Where did you find that?"
     show Liam surprised at right with dissolve
     fb "By the Den...."

     L "What does yours say?"
     L "Can you read mine?"
     L "Minglou didn't tell me anything."
     show Emma shocked at emmaflip with dissolve
     show Liam shocked at right with dissolve
     "The two of her friends flinched at the mention of Minglou's name."
     show Emma angry at emmaflip with dissolve
     show Liam sigh at right with dissolve
     fa "I've always hated that spirit of yours."
     fa "There's something about her I don't like."
     show Lila stunned at left with dissolve
     "Emma said but Lila has no clue what she's referring too."
     show Lila stunned at left with dissolve
     L "Really?"
     L "I never thought anything of her that came off as bad."
     show Emma concern at emmaflip with dissolve
     fa "That's because you're too mushy to notice."

     L "Mushy?"

     fa "Like I said-"
     show Liam angry at right with dissolve
     fb "Nevermind that."
     fb "I just read these pages."
     fb "They talk about something terrifying."
     show Emma concern at flip with dissolve
     show Lila surprised at left with dissolve
     L "What do you mean?"

     "Emma was equally as confused."

     fb "It talks about the existence of something called The Sun..."
     show Emma shocked at emmaflip with dissolve
     #"Emma's expression darkened."

     fa "That can't be."
     fa "You must have read wrong."
     show Lila stunned at left with dissolve
     L "What are you guys talking about?"
     L "What is The Sun?"
     show Liam sigh at right with dissolve
     fb "Emma's right."
     fb "I only know what's written on here to some extent."
     fb "We should confirm it at the library where I can do more research."
     show Emma concern at emmaflip with dissolve
     L "Wait, explain to me first."
     show Emma angry at flip with dissolve
     show Liam nervous at right with dissolve
     fa "Ughhhhhh!"
     fa "This is why you get on my nerves."
     fa "I say it once ok."
     fa "But you can't tell no one...yet."

     L "Ok! I promise."

     fa "Remember the stuff you talked about before we played the game?"
     show Lila surprised at left with dissolve
     L "Uh...I don't remember much really."

     fa "What?"
     fa "How can you forget?!"
     fa "It wasn't too long ago!"
     fa "Urhhhh."
     fa "Nevermind."
     fa "Listen carefully."

     #"Lila inched closer to Emma and in return Emma whispered back."

     fa "It's what brings light into this world."
     fa "A light brighter than any mushrooms on this planet."
     show Lila shocked at left with dissolve
     "Lila's eyes widened."
     "She didn't even question how Emma knew that."
     "She's even more curious about the existence of this thing called The Sun."
     show Lila happy at left with dissolve
     L "Tell me more!"

     "Lila Shouted."
     show Emma sigh at flip with dissolve
     fa "Shhhh! Be Quiet!"

     "Although Lila was confused why they were being so secretive about it."
     "She wanted to ask but Liam stopped her."
     show Liam sigh at right with dissolve
     fb "That's only a legend spreaded by rumors."
     fb "We should get out of here first."
     fb "There's a reason why those rumors died out."

     "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
     "All three of them nodded and then started to head back towards the village."
     "It seems Liam wants to meet up again at the library."
     "Determined to find out more about The Sun, they continued down the path towards the library."
     hide Lila happy at left with dissolve
     hide Emma sigh at flip with dissolve
     hide Liam sigh at right with dissolve
     scene image "BGStart.png" with fade
     "End."
     "Page 1 discovered."
     "Lila's Route."
return

label MinglouHi:
     hide Mingluo annoyed at right with dissolve
     "Lila shouted, turning to face Minglou but by the time she turned Minglou was nowhere to be seen."
     "Still questioning where she went, her attention shifted as soon she heard someone called her name."
     show Liam nervous at right with dissolve
     show Emma sigh at emmaflip with dissolve
     fb "“Lila!"
     fb "Why did you go out so far!"
     fb "We barely managed to find you."
     show Lila surprised at left with dissolve

     L "Huh?"
     show Emma sigh at emmaflip with dissolve
     fa "You sure like causing trouble you direction freak."

     "The two of them got closer to Lila as they grasped for breath."
     show Lila happy at left with dissolve
     L "You guys appeared just in time."
     L "I have something to show you..."

     "Lila said getting excited as she showed them the paper Minglou found for her."
     "It seems that being with her friends made her forget that she was lost."

     fa "I told you you worried over nothing."
     show Liam smile at right with dissolve
     show Emma angry at flip with dissolve
     "Emma growled at Liam. Liam only smiled back."

     fb "We can never be too cautious."

     "He replied before the three of them took a closer look at the paper."
     show Liam surprised at right with dissolve
     fb "That is so interesting..."
     show Emma pout at emmaflip with dissolve
     show Liam page at right with dissolve
     "Liam said as he held out a similar paper."
     show Lila surprised at left with dissolve
     L "Huh?"
     L "Where did you find that?"
     show Liam surprised at right with dissolve
     fb "By the Den...."

     L "What does yours say?"
     L "Can you read mine?"
     L "Minglou didn't tell me anything."
     show Emma shocked at emmaflip with dissolve
     show Liam shocked at right with dissolve
     "The two of her friends flinched at the mention of Minglou's name."
     show Emma angry at emmaflip with dissolve
     show Liam sigh at right with dissolve
     fa "I've always hated that spirit of yours."
     fa "There's something about her I don't like."

     "Emma said but Lila has no clue what she's referring too."
     show Lila stunned at left with dissolve
     L "Really?"
     L "I never thought anything of her that came off as bad."
     show Emma concern at emmaflip with dissolve
     fa "That's because you're too mushy to notice."

     L "Mushy?"

     fa "Like I said-"
     show Liam angry at right with dissolve
     fb "Nevermind that."
     fb "I just read these pages."
     fb "They talk about something terrifying."
     show Emma concern at flip with dissolve
     show Lila surprised at left with dissolve
     L "What do you mean?"

     "Emma was equally as confused."

     fb "It talks about the existence of something called The Sun..."
     show Emma shocked at emmaflip with dissolve

     #"Emma's expression darkened."

     fa "That can't be."
     fa "You must have read wrong."
     show Lila stunned at left with dissolve
     L "What are you guys talking about?"
     L "What is The Sun?"
     show Liam sigh at right with dissolve
     fb "Emma's right."
     fb "I only know what's written on here to some extent."
     fb "We should confirm it at the library where I can do more research."
     show Emma concern at emmaflip with dissolve
     L "Wait, explain to me first."
     show Emma angry at flip with dissolve
     show Liam nervous at right with dissolve
     fa "Ughhhhhh!"
     fa "This is why you get on my nerves."
     fa "I say it once ok."
     fa "But you can't tell no one...yet."

     L "Ok! I promise."

     fa "Remember the stuff you talked about before we played the game?"
     show Lila surprised at left with dissolve
     L "Uh...I don't remember much really."

     fa "What?"
     fa "How can you forget?!"
     fa "It wasn't too long ago!"
     fa "Urhhhh."
     fa "Nevermind."
     fa "Come closer and listen carefully."

     "Lila inched closer to Emma and in return Emma whispered back."

     fa "It's what brings light into this world."
     fa "A light brighter than any mushrooms on this planet."
     show Lila shocked at left with dissolve
     "Lila's eyes widened."
     "She didn't even question how Emma knew that."
     "She's even more curious about the existence of this thing called The Sun."
     show Lila happy at left with dissolve
     L "Tell me more!"

     "Lila Shouted."
     show Emma sigh at flip with dissolve
     fa "Shhhh! Be quiet!"

     "Although Lila was confused why they were being so secretive about it."
     "She wanted to ask but Liam stopped her."
     show Liam sigh at right with dissolve
     fb "That's only a legend spreaded by rumors."
     fb "We should get out of here first."
     fb "There's a reason why those rumors died out."

     "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
     "All three of them nodded and then started to head back towards the village."
     "It seems Liam wants to meet up again at the library."
     "As they were walking Lila suddenly remembered a question she wanted Liam to answer."
     show Lila surprised at left with dissolve
     L "Say guys. What is a Dweeb?"

     "The two of them looked shocked."
     show Liam surprised at right with dissolve
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
    hide Mingluo annoyed at right with dissolve
    show Lila happy at left with dissolve
    L "Ah!"
    L "Liam!"
    L "Emma!"
    L "I missed you guys!"
    show Emma pout at emmaflip with dissolve
    show Liam happy at right with dissolve

    "Lila cheerfully called out to them."
    "The three of them gathered together as the two took their time to catch their breaths."
    L "Oh I also have to thank Ming-"

    "Lila wanted to thank Minglou for taking her out of the cave but she was already nowhere to be seen."

    fb "Huh?"
    fb "Did you say something Lila?"

    "Liam asked while his breath settled."
    show Lila smile at left with dissolve
    L "Uh?"
    L "No-"
    L "I-it's nothing."
    show Liam nervous at right with dissolve
    fb "You went a bit too far."
    fb "We barely managed to find you."
    show Emma sigh at emmaflip with dissolve
    fa "You sure like causing trouble you direction freak."

    "Uh oh... Looks like she's been scolded."
    "Wait... wasn't there something she wanted to show them?"
    "Oh right!"
    show Lila happy at left with dissolve
    L "You guys appeared just in time. I have something to show you..."

    "Lila said getting excited as she showed them the paper Minglou found for her."
    "It seems that being with her friends made her forget that she was lost. "

    fa "I told you you worried over nothing."
    show Liam smile at right with dissolve
    show Emma angry at flip with dissolve
    "Emma growled at Liam. Liam only smiled back."

    fb "We can never be too cautious."

    "He replied before the three of them took a closer look at the paper."
    show Liam surprised at right with dissolve
    fb "That is so interesting..."
    show Emma pout at emmaflip with dissolve
    show Liam page at right with dissolve
    "Liam said as he held out a similar paper."

    show Lila surprised at left with dissolve
    L "Huh?"
    L "Where did you find that?"
    show Liam surprised at right with dissolve
    fb "By the Den...."

    L "What does yours say?"
    L "Can you read mine?"
    L "Minglou didn't tell me anything."
    show Emma shocked at emmaflip with dissolve
    show Liam shocked at right with dissolve
    "The two of her friends flinched at the mention of Minglou's name."
    show Emma angry at emmaflip with dissolve
    show Liam sigh at right with dissolve
    fa "I've always hated that spirit of yours."
    fa "There's something about her I don't like."

    "Emma said but Lila has no clue what she's referring too."
    show Lila stunned at left with dissolve
    L "Really?"
    L "I never thought anything of her that came off as bad."

    fa "That's because you're too mushy to notice."

    L "Mushy?"

    fa "Like I said-"
    show Liam angry at right with dissolve
    fb "Nevermind that."
    fb "I just read these pages."
    fb "They talk about something terrifying."
    show Emma concern at flip with dissolve
    show Lila surprised at left with dissolve
    L "What do you mean?"

    "Emma was equally as confused."

    fb "It talks about the existence of something called The Sun..."
    show Emma shocked at emmaflip with dissolve
    #"Emma's expression darkened."

    fa "That can't be."
    fa "You must have read wrong."
    show Lila stunned at left with dissolve
    L "What are you guys talking about?"
    L "What is The Sun?"
    show Liam sigh at right with dissolve
    fb "Emma's right."
    fb "I only know what's written on here to some extent."
    fb "We should confirm it at the library where I can do more research."
    show Emma concern at emmaflip with dissolve
    L "Wait, explain to me first."
    show Emma angry at flip with dissolve
    show Liam nervous at right with dissolve
    fa "Ughhhhhh!"
    fa "This is why you get on my nerves."
    fa "I say it once ok."
    fa "But you can't tell no one...yet."

    L "Ok! I promise."

    fa "Remember the stuff you talked about before we played the game?"
    show Lila surprised at left with dissolve
    L "Uh...I don't remember much really."

    fa "What?"
    fa "How can you forget?!"
    fa "It wasn't too long ago!"
    fa "Urhhhh."
    fa "Nevermind."
    fa "Come closer and listen carefully."

    "Lila inched closer to Emma and in return Emma whispered back."

    fa "It's what brings light into this world."
    fa "A light brighter than any mushrooms on this planet."
    show Lila shocked at left with dissolve
    "Lila's eyes widened."
    "She didn't even question how Emma knew that."
    "She's even more curious about the existence of this thing called The Sun."
    show Lila happy at left with dissolve
    L "Tell me more!"

    "Lila Shouted."
    show Emma sigh at flip with dissolve
    fa "Shhhh! I just told you to be quiet about it."

    "Although Lila was confused why they were being so secretive about it."
    "She wanted to ask but Liam stopped her."
    show Liam sigh at right with dissolve
    fb "That's only a legend spreaded by rumors."
    fb "We should get out of here first."
    fb "There's a reason why those rumors died out."

    "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
    "All three of them nodded and then started to head back towards the village."
    "It seems Liam wants to meet up again at the library."
    "As they were walking Lila suddenly remembered a question she wanted Liam to answer."

    L "Say guys. What is a Dweeb?"
    show Liam surprised at right with dissolve
    show Emma shocked at flip with dissolve
    #"The two of them looked shocked."

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
    #"Liam's expression darkened."
    show Liam smile at right with dissolve
    fb "I see...."
    fb "The next time you see her..."
    fb "Please let  her know I greatly appreciate her kind hostility."

    "Liam said with a smile but didn't seem like it was gentle at all."
    show Lila surprised at left with dissolve
    L "Ok?"

    "Lila said in uncertainty."
    show Liam nervous at right with dissolve
    fb "Also"
    fb "Don't use that word anymore Lila."
    fb "It makes some people uncomfortable."
    show Lila pout at left with dissolve
    L "Oh sorry."
    L "I didn't know that."
    L "Did it make you uncomfortable Liam?"

    fb "Not from you Lila."
    show Emma angry at flip with dissolve
    "Liam said with a smile."
    "Emma, on the other hand, looks very angry. "
    "Nevertheless, the three of them went on their way to find out more about The Sun that doesn't exist in their world."
    hide Lila pout at left with dissolve
    hide Emma angry at flip with dissolve
    hide Liam nervous at right with dissolve
    scene image "BGStart.png" with fade
    "End."
    "Page 1 discovered."
    "Lila's Route."
return

label UhNevermind:
    show Liam nervous at right with dissolve
    fb "Well."
    fb "Whoever called you that is despicable."
    fb "Don't listen to them."
    show Emma angry at flip with dissolve
    fa "That's right!"
    fa "Only I get to call you that."
    show Lila happy at left with dissolve
    "Ignoring Emma's words, Liam continued."

    fb "Ah!"
    fb "Don't repeat that to anyone else, got it?"
    show Liam default at right with dissolve
    "Liam said strictly."
    "Although Lila nodded, she wonders if she should tell him that it was actually Minglou who called him that."
    "But she didn't want her friends fighting amongst themselves so she kept quiet on their whole journey to the library."
    hide Lila happy at left with dissolve
    hide Emma angry at flip with dissolve
    hide Liam default at right with dissolve
    scene image "BGStart.png" with fade
    "End."
    "Page 1 discovered."
    "Lila's Route."
return

label Den:
     show Lila default at lilaflip with dissolve
     L "I don't like the idea of going to the cave... "

     "Lila thought and was about to go down the path to the den but a sudden voice stopped her."
     show Mingluo no eyes at right with dissolve
     Q "Don't go that way..."

     "Shocked, Lila turned to face the direction of the voice."
     show Lila shocked at yflip with dissolve
     L "Minglou?! What are you doing here?"

     "It's not a surprise that a power spirit like Minglou can travel back and forth from her world to Lila's..."
     "What was shocking was that Minglou popped up for no reason."
     "Usually when she summons her she refuses to come out unless the reason is ugent."
     "Minglou just stood there staring at Lila."
     #"Though her expression was stoic but her voice was soft and low."
     show Mingluo default at right with dissolve
     m "That's not the right way..."
     show Lila surprised at yflip with dissolve
     L "Huh?"
     L "What do you mean?"

     "How would Minglou know that this is the wrong way?"

     m "Just don't go there."
     m "That's not where your destiny lies."

     "The atmosphere suddenly felt heavy."
     show Lila pout at yflip with dissolve
     L "But I don't like the cave..."

     m "..."

     "Minglou was quiet for a moment until she spoke again."

     m "Would you feel better if I go with you?"

     "This is the first time Minglou's been this desperate with her."
     "She's usually very haughty but level headed."
     "Lila wonders why her personality suddenly changed so much."
     show Mingluo annoyed at right with dissolve
     show Lila surprised at yflip with dissolve
     L "Why are you suddenly like this?"

     m "Just answer me. Are you still going to the den?"

menu:
    "No. If you're with me I'm ok.":
        jump NoYouWithMe

    "Yes. This is very uncomfortable":
        jump VeryUncomfy
return

label NoYouWithMe:
    show Mingluo happy at right with dissolve
    "Minglou seems relieved."

    m "Good."
    m "Follow me."
    m "I'll find a good hiding spot for you."
    show Lila pout at yflip with dissolve
    "Although something felt off putting Lila still followed."
    hide Lila pout at yflip with dissolve
    hide Mingluo happy at right with dissolve
    "They continued into the forest for a while before Lila started to have second doubts."
    show Lila pout at left with dissolve
    L "I'm sorry Minglou...But there's this burning feeling telling I need to be at the Den."
    show Mingluo annoyed at right with dissolve
    m "What?"
    m "What burning feeling?"

    #"Minglou looked conflicted."

    L "I don't know."
    L "It's just this weird feeling."
    L "Also"
    L "I don't like how strange you're acting."
    L "I just don't like this."
    show Mingluo disgust at right with dissolve
    m "Would I ever harm you?"

    #"Lila gave Minglou a weird look."

    m "Well..."
    m "Allow me to rephrase that."
    m "Have I ever harmed you physically?"
    show Lila stunned at left with dissolve
    "Lila thought for a moment."
    "Has Minglou ever done anything too unforgiving?"
    "Nothing really came to mind."
    "Though this water spirit can be a bit sharp tongued she's never hurt her to the point of no return."
    show Mingluo skeptical at right with dissolve
    m "Really?"
    m "You're going to spend that long thinking about it?"
    m "You don't trust me?"
    m "I've watched over since you were in diapers."
    show Lila stunned at left with dissolve
    #"Lila looked at Minglou."
    "Her eyes hide no lies yet there was a sense of motive."
    show Lila pout at left with dissolve
    "However that statement is true."
    "They've been together since Lila was born."
    "That's what she remembers from her memory."

menu:
    "Ok. I trust you.":
        jump ITrust

    "Sorry. I can't seem to trust you...":
        jump SorryI
return

label ITrust:
    show Lila default at left with dissolve
    "Lila decided to go onwards with full determination."
    "I believe in Minglou."
    #"Minglou sighed in relief."
    show Mingluo smile at right with dissolve
    hide Lila default at left with dissolve
    hide Mingluo smile at right with dissolve
    scene image "Cave.png" with fade
    "They kept their pace until they reached the entrance to the cave."
    "As they walked into the cave Lila felt a chill."
    "The dark cave felt cold and lonely."
    "She looked at Minglou and stared at her elegant features."
    "She couldn't help but smile."
    show Lila smile at left with dissolve
    show Mingluo skeptical at right with dissolve
    m "What are you smiling about?"
    m "Stop looking at me like that."
    m "It's creepy."
    show Lila shocked at left with dissolve
    "Lila was at a loss for words."
    show Lila pout at left with dissolve
    L "I just thought it's nice that I'm not alone...."

    "Lila sulked."

    "Minglou didn't say anything at first."
    #"All she did was glance over at Lila."
    "Nevertheless, she sighed and broke the unformforable silence."

    m "You're usually very talkative."
    m "What's got your tongue twisted?"
    show Mingluo annoyed at right with dissolve
    "Lila didn't say anything and just silently walked."
    #"Minglou smirked cheekly."

    m "Don't tell me the atmosphere got to you?"
    m "What was it I heard?"
    m "Ah! Yes."
    m "Don't worry."
    m "I've heard that idiots don't catch colds."
    show Lila angry at left with dissolve
    "Hearing those words made Lila feel awful."
    "She was about to rebuttal but she paused when she looked around her surroundings."
    "The cave which was pitch black before is now filled with the gentle glows from the warm enoki mushrooms."
    "Not only was she no longer cold she also felt a fluffy feeling well up in her."
    show Mingluo soft at right with dissolve
    m "Regardless, I wouldn't let you catch it anyways...."

    #"Minglou mumbled as Lila turned to look at her."
    show Lila surprised at left with dissolve
    L "Huh?"

    "Lila looked at Minglou in confusion."
    show Mingluo disgust at right with dissolve
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
    show Mingluo smile at right with dissolve
    m "Oh?"
    m "Nice job noticing."
    m "Why don't you go check it out?"

    "Minglou said with a smirk on her face."
    hide Mingluo smile at right with dissolve
    hide Lila surprised at left with dissolve
    scene image "SecondPage.png" with fade
    "Though Lila's had this odd feeling from when she first met up with Minglou she still listened to her words."
    "She got closer to observe the mushrooms."

    "In the pile of all the mushrooms, there was a piece of paper in the center."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn't look that special."
    "What made Lila drawn to it was that even though the paper was surrounded, none of the mushroom parts touched the paper."
    "While her eyes were still glued to the paper, Minglou picked it up and all in a one moment the paper went into flames."
    scene image "Cave.png" with fade
    L "Minglou!"
    show Lila shocked at left with dissolve
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
    show Mingluo skeptical at right with dissolve
    m "What do you think makes this place warm?"
    show Lila surprised at left with dissolve
    L "Is it the enoki mushrooms?"

    m "That isn't wrong."
    m "But I want you to think even deeper."
    m "When enoki mushrooms gather are they usually this warm?"

    "When Minglou asked that question something felt unpleasant to Lila."
    "She thought for a moment. Enokis don't produce enough warmth unless they gather together."
    "However, if too much gathered they will overheat and cause a fire."
    "Yet...Why isn't the cave burning?"

    m "Think even deeper."
    show Lila pout at left with dissolve
    "Lila didn't even notice the way Minglou was looking at her."
    "Her eyes focused on one thing."
    hide Mingluo skeptical at right with dissolve
    hide Lila pout at left with dissolve
    scene image "SecondPage.png" with fade
    "The pile of mushrooms gather in that one corner."
    "What is it that causes all of them to gather?"
    "Iching closer Lila looked into the pile of mushrooms."
    "In the center was one piece of paper."
    "A paper so beaten yet somehow it still manages to remain whole."
    "Nothing was written on the paper."
    "It didn't look that special."
    "What made Lila drawn to it was that the mushrooms only surrounded the paper yet none of it's parts touched the paper."
    "While her eyes were still glued to the paper Minglou picked it up and in a one moment the paper went into flames."
    scene image "Cave.png" with fade
    L "Minglou!"
    show Lila shocked at left with dissolve
    show Mingluo page at right with dissolve
    "Lila panicked as she screamed for Minglou."
    "Minglou is a water spirit."
    "Fire might cause her harm."
    "Yet in a blink of an eye the flames went out."
    "Standing in front of her was Minglou smiling while handing over the paper to Lila."
    "A paper now filled with symbols she's never recognized was in her face."
    "Trying to wrap her head around everything Lila became very confused."
    "What just happened?"

menu:
    "Ask Minglou what just happened":
        jump MinglouH

    "Is Minglou ok?!":
        jump IsMingOk
return

label MinglouH:
     show Lila shocked at left with dissolve
     L "Wha-What just happened?!"
     show Mingluo smile at right with dissolve
     m "Nothing much."
     m "Just a little special ability of mine."
     m "Anyways you should pay more attention to this magnificent artifact."

     "It looks like Minglou won't explain what has happened."
     "Has she always had an ability like that?"
     "Lila never knew."
     "Lila knows that unlike most spirits, Minglou can travel from her world to the spirit realm without the need of Lila's powers."
     "Minglou is a very powerful spirit but can a water spirit withstand the intensity of flames?"
     "Unharmed?"
     "Lila regrets not paying attention in class now."
     "Staring at the paper Minglou handed to her, Lila noticed that there was some language written on there that seems familiar."
     "Other than those few symbols most of the other ones she's never seen before."
     show Lila surprised at left with dissolve
     L "What does this say?"
     L "What is this?"
     show Mingluo annoyed at right with dissolve
     #"Lila questioned while Minglou looked at her in disbelief."

     m "Child{cps=2}...{/cps}It's written in your home language."
     m "How can you not understand?"
     m "I get that some of it is in ancient lingo but you should be able to read the other symbols right?"

     "Lila stared at Minglou blankly."

     m "Ugh."
     m "Forget it."
     m " What was that peepsqueaks name?"
     m "The boy you always hang around with."
     show Lila pout at left with dissolve
     L "Peepsqueak?"
     L "Are you talking about Liam?"
     L "Why do I feel like you said something rude again..."
     show Mingluo smile at right with dissolve
     m "Ah yes."
     m "Him."
     m "Why don't you go ask him about this page?"

     L "He's not with me right now."
     L "Actually, I don't know where he is at."

     m "That's no problem."
     m "I'll lead you to him."
     show Lila surprised at left with dissolve
     L "You know where he is?!"

     m "I know everything."

     #"Minglou said with a cheeky smirk."

     L "Why can't you just tell me what it says?"
     show Lila angry at left with dissolve
     m "Because...I refuse to help decode human words."
     m "I despise it."

     "Lila knew that Minglou had always hated her kind and she didn't know why."
     "Everytime she asks why, Minglou not only refuses to answer, she gets super heated."
     "Even though this time Minglou was not making a big deal out of it Lila still chose to stay quiet. "
     show Mingluo annoyed at right with dissolve
     show Lila pout at left with dissolve
     m "We've been here long enough already."
     m "Let's get going."
     show Lila happy at left with dissolve
     L "Ok!"

     "Just as the two were about to leave."
     show Mingluo mushroom at right with dissolve
     "Minglou handed her a mushroom."

     L "Huh?"
     show Lila surprised at left with dissolve
     "Lila was confused but still took the mushroom."

     m "Take it."
     m "It's going to get cold on the way out."
     show Mingluo soft at right with dissolve
     #"Minglou said with her normal expressionless face yet the tone of her voice was soft and gentle."

     L "Thank you!"
     show Lila happy at left with dissolve
     #"She said with a smile."
     "Nothing followed but the echoes of their footsteps."
     "Just as they were about to reach the exit of the cave she couldn't help but ask the one question that has been bothering her this whole time. "

     L "What was in the den?"
     show Lila pout at left with dissolve
     show Lila nervous at left with dissolve
     "She nervously questioned expecting another angry response."
     "Yet to her surprise there was a soft reply."
     show Mingluo soft at right with dissolve
     m "You'll see..."
     show Lila default at left with dissolve
     "Lila glanced at Minglou and saw that the usual frown on Minglou has turned into a smile."
     "It was such a rare sight."
     "She'd really wish she could record this moment."
     hide Mingluo soft at right with dissolve
     hide Lila default at left with dissolve
     "If only she knew what's to come in the near future she probably would have."
     scene image "Forest_Default.png" with fade
     Q "Lila!"

     "Breaking away from her thought process someone called her name."
     "She turned to face the direction of the noise and to her surprise she saw her two friends running towards her."
     "Excited she called out to them. "
     show Lila default at left with dissolve
     show Emma pout at emmaflip with dissolve
     show Liam happy at right with dissolve
menu:
    "Hi! You guys!":
        jump HiGuys

    "I was looking for you Liam!":
        jump LookYouL
return

label HiGuys:
    show Lila smile at left with dissolve
    L "Ah!"
    L "Liam!"
    L "Emma!"
    L "I missed you guys!"

    "Lila cheerfully called out to them."
    "The three of them gathered together as the two took their time to catch their breaths."
    show Emma default at emmaflip with dissolve
    show Liam smile at right with dissolve
    show Lila stunned at left with dissolve
    L "Oh I also have to thank Ming-"

    "Lila wanted to thank Minglou for taking her out of the cave but she was already nowhere to be seen."

    fb "Huh?"
    fb "Did you say something Lila?"
    show Lila pout at left with dissolve
    "Liam asked while his breath settled."

    L "Uh?"
    L "No-"
    L "I-it's nothing."

    fb "You went a bit too far."
    fb "We barely managed to find you."
    show Emma sigh at emmaflip with dissolve
    fa "You sure like causing trouble you direction freak."

    "Uh oh... Looks like she's been scolded."
    "Wait... wasn't there something she wanted to show them?"
    "Oh right!"
    L "You guys appeared just in time. I have something to show you..."
    show Lila smile at left with dissolve
    "Lila said getting excited as she showed them the paper Minglou found for her."
    "It seems that being with her friends made her forget that she was lost. "

    fa "I told you you worried over nothing."
    show Liam smile at right with dissolve
    show Emma angry at flip with dissolve
    "Emma growled at Liam. Liam only smiled back."

    fb "We can never be too cautious."

    "He replied before the three of them took a closer look at the paper."
    show Liam surprised at right with dissolve
    fb "That is so interesting..."
    show Emma pout at emmaflip with dissolve
    show Liam page at right with dissolve
    "Liam said as he held out a similar paper."
    L "Huh?"
    L "Where did you find that?"
    show Liam surprised at right with dissolve
    fb "By the Den...."

    "Lila thought back on Minglou's words..."

    L "What does yours say? Can you read mine? Minglou didn't tell me much."
    show Emma shocked at emmaflip with dissolve
    show Liam shocked at right with dissolve
    "The two of her friends flinched at the mention of Minglou's name."
    show Emma angry at emmaflip with dissolve
    show Liam sigh at right with dissolve
    fa "I've always hated that spirit of yours."
    fa "There's something about her I don't like."

    "Emma said but Lila has no clue what she's referring too."
    show Lila stunned at left with dissolve
    L "Really?"
    L "I never thought anything of her that came off as bad."
    L "I guess she is a bit secretive."
    show Emma concern at emmaflip with dissolve
    fa "Huh?"
    fa "What do you mean?"
    show Lila default at left with dissolve
    L "I don't know."
    L "Something about her just makes me want to question-"

    fb "Nevermind that."
    fb "I just read these pages."
    fb "They talk about something terrifying."

    "Liam said breaking their talk about Lila's unusual spirit."
    "It seems that what's written on the page is more important at the moment."

    L "Something terrifying?"

    "Lila questioned with Emma equally as confused."
    show Emma shocked at emmaflip with dissolve

    fb "It talks about the existence of something called The Sun..."

    #"Emma's expression darkened."

    fa "That can't be."
    fa "You must have read wrong."
    show Lila surprised at left with dissolve
    L "What are you guys talking about?"
    L "What is The Sun?"
    show Liam nervous at right with dissolve
    fb "Emma's right."
    fb "I only know what's written on here to some extent."
    fb "We should confirm it at the library where I can do more research."

    L "Wait, explain to me first."
    show Emma annoyed at emmaflip with dissolve
    fa "Ughhhhhh!"
    fa "This is why you get on my nerves."
    fa "I say it once ok."
    fa "But you can't tell no one...yet."
    show Lila default at left with dissolve
    L "Ok! I promise."

    fa "Remember the stuff you talked about before we played the game?"
    show Emma default at emmaflip with dissolve
    L "Uh...I don't remember much really."

    fa "What?"
    fa "How can you forget?!"
    fa "It wasn't too long ago!"
    fa "Urhhhh."
    fa "Nevermind."
    fa "Come closer and listen carefully."

    "Lila inched closer to Emma and in return Emma whispered back."

    fa "It's what brings light into this world."
    fa "A light brighter than any mushrooms on this planet."
    show Lila shocked at left with dissolve
    "Lila's eyes widened."
    "She didn't even question how Emma knew that."
    "She's even more curious about the existence of this thing called The Sun."
    show Lila happy at left with dissolve
    L "Tell me more!"

    #"Lila Shouted."
    show Emma sigh at flip with dissolve
    fa "Shhhh! I just told you to be quiet about it."

    "Although Lila was confused why they were being so secretive about it."
    "She wanted to ask but Liam stopped her."
    show Liam sigh at right with dissolve
    fb "That's only a legend spreaded by rumors."
    fb "We should get out of here first."
    fb "There's a reason why those rumors died out."

    "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
    "All three of them nodded and then started to head back towards the village."
    "It seems Liam wants to meet up again at the library."
    "Determined to find out more about The Sun, they continued down the path towards the library."
    hide Lila happy at left with dissolve
    hide Emma sigh at flip with dissolve
    hide Liam sigh at right with dissolve
    scene image "BGStart.png" with fade
    "End."
    "Page 1 discovered."
    "Lila's Route."
return

label LookYouL:

     fb "Lila!"
     fb "Why did you go out so far!"
     fb "We barely managed to find you."

     fa "You sure like causing trouble you direction freak...Also why are you looking for Liam only?"

     "The two of them got closer to Lila as they grasped for breath."
     "Though Emma seems to be more upset than happy to see her."

     L "Oh."
     L "That's because I have something to show him..."
     L "You see, me and Ming-"

     "Lila said getting excited as she showed them the paper Minglou found for her."
     "However, when she turned around to refer to Minglou she noticed that the spirit's already gone."
     "She didn't even say Thank you to Minglou yet..."

     fa "I told you you worried over nothing."
     show Liam smile at right with dissolve
     show Emma angry at flip with dissolve
     "Emma growled at Liam. Liam only smiled back."

     fb "We can never be too cautious."

     "He replied before the three of them took a closer look at the paper."
     show Liam surprised at right with dissolve
     fb "That is so interesting..."
     show Emma pout at emmaflip with dissolve
     show Liam page at right with dissolve
     "Liam said as he held out a similar paper."

     L "Huh?"
     L "Where did you find that?"
     show Liam surprised at right with dissolve
     fb "By the Den...."

     "The den? The one that Minglou told her not to go too?"

     L "What does it say? Minglou didn't tell me much."

     "The two of her friends flinched at the mention of Minglou's name."

     fa "I've always hated that spirit of yours."
     fa "There's something about her I don't like."
     show Emma angry at emmaflip with dissolve
     show Liam sigh at right with dissolve
     "Emma said but Lila has no clue what she's referring too."
     show Lila stunned at left with dissolve
     L "Really?"
     L "I never thought anything of her that came off as bad."
     L "I guess she is a bit secretive."

     fa "Huh?"
     fa "What do you mean?"

     L "I don't know."
     L "Something about her just makes me want to question-"

     fb "Nevermind that."
     fb "I just read these pages."
     fb "They talk about something terrifying."

     "Liam said breaking their talk about Lila's unusual spirit."
     "It seems that what's written on the page is more important at the moment."

     L "Something terrifying?"

     "Lila questioned with Emma equally as confused."

     fb "It talks about the existence of something called The Sun..."

     "Emma's expression darkened."

     fa "That can't be."
     fa "You must have read wrong."

     L "What are you guys talking about?"
     L "What is The Sun?"

     fb "Emma's right."
     fb "I only know what's written on here to some extent."
     fb "We should confirm it at the library where I can do more research."

     L "Wait, explain to me first."

     fa "Ughhhhhh!"
     fa "This is why you get on my nerves."
     fa "I say it once ok."
     fa "But you can't tell no one...yet."

     L "Ok! I promise."

     fa "Remember the stuff you talked about before we played the game?"

     L "Uh...I don't remember much really."

     fa "What?"
     fa "How can you forget?!"
     fa "It wasn't too long ago!"
     fa "Urhhhh."
     fa "Nevermind."
     fa "Come closer and listen carefully."

     "Lila inched closer to Emma and in return Emma whispered back."

     fa "It's what brings light into this world."
     fa "A light brighter than any mushrooms on this planet."
     show Lila shocked at left with dissolve
     "Lila's eyes widened."
     "She didn't even question how Emma knew that."
     "She's even more curious about the existence of this thing called The Sun."
     show Lila happy at left with dissolve
     L "Tell me more!"

     "Lila Shouted."
     show Emma sigh at flip with dissolve
     fa "Shhhh! I just told you to be quiet about it."

     "Although Lila was confused why they were being so secretive about it."
     "She wanted to ask but Liam stopped her."
     show Liam sigh at right with dissolve
     fb "That's only a legend spreaded by rumors."
     fb "We should get out of here first."
     fb "There's a reason why those rumors died out."

     "Though Lila wanted to know more about this she listened to Liam because he sounded more serious than usual."
     "All three of them nodded and then started to head back towards the village."
     "It seems Liam wants to meet up again at the library."
     "Determined to find out more about The Sun, they continued down the path towards the library."
     hide Lila happy at left with dissolve
     hide Emma sigh at flip with dissolve
     hide Liam sigh at right with dissolve
     scene image "BGStart.png" with fade
     "End."
     "Page 1 discovered."
     "Lila's Route."
return

label IsMingOk:
    show Lila shocked at left with dissolve
    show Mingluo skeptical at right with dissolve
    L "Are you ok?!"

    m "Me? I'm perfectly fine."

    "Minglou said with a hint of annoyance but her tone was gentle."
    show Lila pout at left with dissolve
    L "B-But you're a water spirit..."
    L "Doesn't water hurt you?"
    L "Did I remember wrong?"
    show Mingluo annoyed at right with dissolve
    m "“I think you did."
    m "You tend to forget I'm not like those other weaklings."

    "Minglou was monotone but Lila felt a chill."

    m "I even went so far to show you this priceless artifact."
    m "Why don't you appreciate this moment you have?"
    m "It's a bit useless to worry about unnecessary things."
    show Mingluo page at right with dissolve
    show Mingluo skeptical at right with dissolve
    "Minglou handed Lila the paper that was in flames."
    "She took the paper and looked at it."
    "Not even a single sign showed that it was in flames."
    "Didn't paper burn into ashes when it comes into contact with fire?"
    "Why didn't this one burn?"
    "However, besides that question."
    "The question that bothers her the most is what is the symbols that appeared on the paper."
    "How and why did it appear?"

    L "What does it say?"
    show Lila surprised at left with dissolve
    #"Lila questioned as Minglou stood there in disbelief."
    show Mingluo skeptical at right with dissolve
    m "You mean to tell me you don't know how to read your own language?"
    show Lila nervous at left with dissolve
    #"Lila looks embrassed."

    m "Not even the basics?"

    L "No...But Liam Knows!"

    "Lila said in an upbeat tone while Minglou shivered at that name."
    show Mingluo angry at right with dissolve
    m "Don't mention that brat's name."
    m "I hate the looks he gives me."
    m "It's like he can read right through me."
    show Lila stunned at left with dissolve
    #"Lila looked at her in confusion."

    m "Ugh."
    m "Forget it"
    m "Just take the paper and go ask him."
    show Mingluo default at right with dissolve
    "Minglou grumbled wanting to leave."
    "It seems she's also  mentally exhausted."

    L "Ah wai-"

    "Sensing in her instinct that Minglou was about to leave she tried to stop her by calling out to her."

    m "What?"

menu:
    "I don't know how to get out of the cave":
        jump IDontCave

    "Nevermind. Goodbye.":
        jump NvmGood
return

label IDontCave:
    show Mingluo disgust at right with dissolve
    "Although Minglou gave her a weird look she ended the unpleasant look with a sigh."

    m "Come with me..."

    "She said and Lila gladly followed."
    hide Mingluo disgust at right with dissolve
    hide Lila stunned at left with dissolve
    "As the two were walking out of the cave Lila noticed that the warmth was slowly seeping away from her body."
    show Mingluo mushroom at right with dissolve
    "Noticing her shivering Minglou held out an enoki mushroom."
    show Lila smile at left with dissolve
    m "Take it."
    m "I have no use for it."

    "Minglou said, shoving the mushroom to Lila."
    "As Lila took the mushroom she thought to herself."
    "Even though the water spirit has just held the mushroom it still feels warm."
    "For a long time now, she knew that Minglou showed a lot of warning signs."
    "But she still smiled and held the mushroom close."
    "Even though every time she questioned her it results in a harsh scolding, she still hoped that one day, Minglou would be honest with her. "
    show Lila happy at left with dissolve
    show Mingluo soft at right with dissolve
    L "Thank You."

    #"She said with a smile."
    "Nothing followed but the echoes of their footsteps."
    "Just as they were about to reach the exit of the cave she couldn't help but ask the one question that has been bothering her this whole time. "

    L "What was in the den?"

    "She nervously questioned expecting another angry response."
    "Yet to her surprise there was a soft reply."
    show Mingluo smile at right with dissolve
    m "You'll see..."

    "Lila glanced at Minglou and saw that the usual frown on Minglou has turned into a smile."
    "It was such a rare sight."
    "She'd really wish she could record this moment."
    hide Mingluo soft at right with dissolve
    hide Lila default at left with dissolve
    "If only she knew what's to come in the near future she probably would have."
    scene image "Forest_Default.png" with fade
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
    show Lila smile at left with dissolve
    show Mingluo skeptical at right with dissolve
    "She's already troubled Lila enough today already."
    "It's probably best if she just found a way out of the cave herself."
    "Minglou looked at Lila as she innocently smiled with the page gently gripped in her hand."


    m "I'm just asking because I have a feeling..."
    m "But do you know the way out of the cave."

    "Lila looked shocked that Minglou figured out her troubles."
    #"Minglou sighed in disbelief. "
    show Mingluo annoyed at right with dissolve
    m "You're so easy to read...."
    hide Mingluo annoyed at right with dissolve
    hide Lila smile at left with dissolve
    show Mingluo mushroom at right with dissolve
    "Minglou said as she plucked a few enoki mushrooms."
    "Then she gave them to Lila."

    m "Take these and follow me."

    "Minglou said as she pulled Lila along with her."
    #"Still in a daze held the mushrooms and Lila stared at Minglou."
    show Lila smile at left with dissolve
    L "Why did you give me these?"
    show Mingluo skeptical at right with dissolve
    m "No reason really."
    m "Now less talking and more moving."
    hide Mingluo skeptical at right with dissolve
    hide Lila smile at left with dissolve
    "Minglou said and the two continued down their path."
    "As they got closer and closer to the exit of the cave it got colder as well."
    "Yet because of the mushrooms bundled in Lila's arms she felt warm."
    show Lila smile at left with dissolve
    L "Thank You."
    show Mingluo soft at right with dissolve
    #"She said with a smile."
    hide Mingluo soft at right with dissolve
    hide Lila smile at left with dissolve
    "Nothing followed but the echoes of their footsteps."
    "Just as they were about to reach the exit of the cave she couldn't help but ask the one question that has been bothering her this whole time. "
    show Lila surprised at left with dissolve
    L "What was in the den?"

    "She nervously questioned expecting another angry response."
    "Yet to her surprise there was a soft reply."
    show Mingluo soft at right with dissolve
    m "You'll see..."

    "Lila glanced at Minglou and saw that the usual frown on Minglou has turned into a smile."
    "It was such a rare sight."
    "She'd really wish she could record this moment."
    hide Lila surprised at left with dissolve
    hide Mingluo soft at right with dissolve
    "If only she knew what's to come in the near future she probably would have."
    scene image "Forest_Default.png" with fade
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
    hide Mingluo skeptical at right with dissolve
    hide Lila pout at left with dissolve
    "Lila slowly backed away from Minglou."
    "Before Minglou could say anything she ran to the den."
    "What was it that Minglou was hiding?"
    "Not only was she feeling uncomfortable, she was also very curious."
    scene image "OutsideDen.png" with fade
    "When she arrived at the den she noticed Emma who was supposed to hide standing outside of the den."
    show Emma concern at emmaflip with dissolve
    show Lila surprised at left with dissolve
    L "Emma! Why are you here?"

    "Lila shouted while Emma looked at her with a grumpy expression."
    show Emma angry at emmaflip with dissolve
    fa "So that's where you went."
    fa "Why do you always cause so much trouble."
    fa "We've been looking for you for a long time now."

    #"Lila looked a bit confused."

    L "Huh?"
    L "But I wasn't even gone for that long...I think?"

    fa "Either way, Liam got worried so we went looking for you."
    fa "Not that was needed."

    "Emma grumbled as Lila stopped to catch her breath."

    L "Liam's here too?! Where is he?"

    #"Lila questions while Emma continues to look at her with a frown."
    show Emma pout at emmaflip with dissolve
    fa "Inside....He went in there thinking you crawled inlike the animal you are."
    show Lila angry at left with dissolve
    "Lila felt a throb in her heart. Why did Emma's words feel hurtful?"

menu:
    "Why are you outside?":
        jump YouOut

    "Go in to check for Liam":
        jump CheckLiam
return

label YouOut:
    show Emma smug at emmaflip with dissolve
    fa "For this reason of course."

    "Emma said with a smirk as she flicked Lila on the forehead."
    show Lila angry at left with dissolve
    L "Ouch!"

    "Lila shouted in pain."
    "All of a sudden there were a bunch of rustling sounds coming from the den."
    show Emma angry at emmaflip with dissolve
    fa "Ahhhhhh... I hate this."
    fa "Of course he responded."

    "Emma grumbled."
    "Just as Lila was going to ask why Emma behaved like this Liam rushed out of the den."
    show Liam nervous at right with dissolve
    fb "Emma!"
    fb "I just heard Lila's voice!"
    fb "She must be hurt-"

    "Liam said in a rush but stopped when he saw the weird look Lila was giving him."
    #"Emma glared and scowled. "
    show Lila stunned at left with dissolve
    show Emma sigh at emmaflip with dissolve
    fa "She's fine, you blockhead."
    fa "She's standing right here."
    fa "I told nothing happened."
    fa "You never listen."
    show Liam smile at right with dissolve
    fb "Lila! When did you arrive?"
    "Liam didn't listen to a single word Emma said. Emma just pouted in response."
    show Lila smile at left with dissolve
    L "A moment ago."

    "Lila replied. Liam composed himself and started questioning Emma."

    fb "Why didn't you tell me she was already here?"
    show Emma pout at emmaflip with dissolve
    fa "I did."

    fb "When?"

    fa "Does it matter?"
    fa "Look she's fine."
    fa "You're the one being over protective."
    show Liam nervous at right with dissolve
    fb "Right."
    fb "Excuse me."
    fb "I might have worried a little too much..."

    "Liam said with a smile but the tone of his voice was a bit scary."
    show Emma concern at emmaflip with dissolve
    show Lila default at left with dissolve
    "Emma didn't look too happy either."
    "It seems the two were at it again."

menu:
    "Liam what did you find?":
        jump LiamWhaFind

    "Emma were you looking for me?":
        jump EmmaLook
return

label LiamWhaFind:
    show Emma pout at emmaflip with dissolve
    fa "I thought you were worried a moment ago."
    show Lila smile at left with dissolve
    L "He looks fine though."
    show Emma shocked at emmaflip with dissolve
    show Liam surprised at right with dissolve
    "Both Liam and Emma were surprised at how fast Lila moved on from the topic."
    "Noticing that the two older kids were bickering over something so small they felt embarrassed."
    show Emma blush at emmaflip with dissolve

    fa "Uh right."
    fa "Sorry about that."

    "Emma said feeling ashamed."
    show Liam nervous at right with dissolve
    fb "No. I started it. I'm sorry too."

    "Liam was equally as embarrassed."
    show Emma sigh at emmaflip with dissolve
    fa "Forget about it."
    fa "What did you want to show us."

    fb "Right."
    show Liam default at right with dissolve
    "Liam's voice suddenly got serious."

    fb "Everything we saw and heard today must remain with the three of us understand?"

    "The two nodded in agreement."
    show Emma shocked at emmaflip with dissolve
    fb "Ok...So I picked this up in the den..."
    show Lila surprised at left with dissolve
    show Liam page at right with dissolve
    "Liam said as he held out a piece of paper."
    "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."

menu:
    "Huh? Why are you being secretive over this?":
        jump WhySecretive

    "What written on it?":
        jump WhatWritten
return

label EmmaLook:
    show Emma angry at emmaflip with dissolve
    show Lila default at left with dissolve
    fa "Isn't that obvious?"

    "Emma asked but it doesn't look like she's questioning."

    L "Oh..."
    show Lila smile at left with dissolve
    L "Does that mean you were worried for me?"
    show Emma shocked at emmaflip with dissolve
    "For a short moment Emma was speechless."
    "Her face was filled with pure shock."
    show Emma blush at emmaflip with dissolve
    fa "Wh-What-"
    fa "Wh-what nonsense is this?"
    fa "Of course not!"
    fa "I know you're old enough to take care of yourself."
    fa "Who's worried?!"

    #"Emma said as she blushed."
    show Liam happy at right with dissolve
    "Her eagerness to reject the idea made Liam laugh."

    fa "S-stop laughing!"
    fa "There's nothing funny!"
    show Lila happy at left with dissolve
    L "I see..."
    L "Thank you for caring!"

    "Lila said, feeling fluffy inside as Liam laughed harder."

    fa "Stop it!"
    fa "You're making it worse!"

    fb "Bu-but you guys are so cute!"

    "Liam said, pulling himself together."
    show Emma angry at emmaflip with dissolve
    fa "Enough!"
    fa "What on earth did you find!"
    fa "Took you long enough."
    fa "Show it to us already."

    "Emma said in a desperate attempt to diverge the attention."
    show Liam nervous at right with dissolve
    fb "Right..."

    "It seems her attempt worked as Liam slowly composed himself and started getting serious."

    fb "Everything we saw and heard today must remain with the three of us understand?"
    show Lila smile at left with dissolve
    "Lila eagerly nodded in agreement."
    "Her excitement can be seen in her eyes."
    show Emma default at emmaflip with dissolve
    "Meanwhile, Emma slowly cooled down as well and nodded just as eager to find out why Liam was being so secretive. "

    fb "Ok...So I picked this up in the den..."
    show Liam page at right with dissolve
    "Liam said as he held out a piece of paper."
    "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."

menu:
    "Huh? Why are you being secretive over this?":
        jump WhySecretive

    "What written on it?":
        jump WhatWritten
return

label WhySecretive:
    show Lila stunned at left with dissolve
    "Lila doesn't understand why a piece of paper is so important."
    #"Emma gave her a very weird look."
    show Emma pout at emmaflip with dissolve
    fa "Did you not read the symbols?"

    "As Emma said."
    show Liam happy at right with dissolve
    "But before Lila could reply the two flinched when they heard Liam laugh."

    fa "What's so funny?"
    show Emma concern at emmaflip with dissolve
    "Emma questioned and Lila looked at Liam equally as confused."

    fb "It's nothing."
    fb "Don't worry about it."
    fb "I'll explain what's on this paper."
    fb "This is probably too hard for Lila to understand."
    show Lila pout at left with dissolve
    "Liam said, holding in his laughter."
    "Slowly he was able to pull himself back together."

    fa "Huh?"
    fa "What are you on about?"
    fa "Some of this is in the basics of our language."

    fb "Don't worry about it."
    fb "It's probably best if I explained it anyways."
    show Liam wink at right with dissolve
    #"Liam gave Emma a wink which made her loss all of her reasons."

    fa "If you say so..."

    "Emma replied and she quieted down."
    show Liam default at right with dissolve
    fb "Well as Emma pointed it out, what's important is what's written on the paper."

    "Liam said as the two listened in."

    fb "It talks about the existence of a magically being."
    show Emma shocked at emmaflip with dissolve
    fb "A being so powerful that can control a power known as The Sun."
    show Lila surprised at left with dissolve
    "Liam said as the tone of his voice lowered."
    "Lila's eyes glimmered."

    L "The Sun?"

    #"Lila questioned."
    "In response to her question, Liam smiled and pointed towards the endless dark night sky."
    show Liam smile at right with dissolve
    fb "Yes."
    fb " It's essence was so strong it had the ability to light up the whole world."

    "Lila's mind was blown."
    "Although she had many and many questions running through her mind, she couldn't help take a moment to digust everything Liam has just said. "

    L "Where is it now? The Sun!"
    L "Who's controlling it?"
    L "Why haven't we-"
    show Emma angry at emmaflip with dissolve
    fa "Shhhhh!"
    fa "You dummy!"
    fa "Don't say anymore... This is just a rumor."

    "Emma said hushing Lila."
    show Liam sigh at right with dissolve
    fb "Unfortunately, that is all of the information we have now."

    #"Liam said. His voice almost sounded disappointed."

    fb "Who knows if this is only a joke someone wrote about or if this is a dream of some lunatic."

    #"Emma said but Lila rebuttal."
    show Lila happy at left with dissolve
    L "What if there were more of these pages!"
    show Emma pout at emmaflip with dissolve
    show Liam surprised at right with dissolve
    L "What if we collected them all?"
    L "What do you think will happen?"

    "Lila's response did intrigued the two but they can only laugh it off."
    show Liam sigh at right with dissolve
    fb "A lot of Maybes..."
    fb "Who knows really."

    "Liam said but that was all he said as he led the two out of the forest."

    fb "But Let's rest up first before we dig deeper."
    show Emma concern at emmaflip with dissolve
    fa "Right. I'm exhausted."
    hide Liam sigh at right with dissolve
    hide Emma concern at emmaflip with dissolve
    hide Lila happy at left with dissolve
    "As her friends slowly left the den behind dragging her with them Lila turned to look at the den."
    "She couldn't help wondering if the two took her seriously?"
    "Or did they just rub it off as a joke."
    "Either way, she's determined to find out more about the page and the information written on it."
    "That is after she's rested. "
    scene image "BGStart.png" with fade
    "End."
    "Page 1 discovered."
    "Lila's Route."
return

label WhatWritten:

    show Lila pout at left with dissolve
    show Emma concern at emmaflip with dissolve
    fa "Huh?"
    fa "Don't tell me..."
    fa "You can't read this?"
    show Liam happy at right with dissolve
    "Emma questioned Lila as Liam nervously laughed at the side."
    show Lila happy at left with dissolve
    L "Nope!"

    #"Lila said with a wide grin across her face."
    show Emma angry at emmaflip with dissolve
    fa "Did you not pay attention to class?!"
    fa "It's the basics.... how can you not know?!"

    "Emma was shocked."
    "All this time she knows her friend is a bit airheaded but not to this point."

    fa "How did you pass all of your classes then?"
    fa "You even got As."
    show Liam nervous at right with dissolve
    fb "Now. Now."
    fb "Let's just focus on what's at hand."
    fb "So back to what I was saying..."
    show Emma sigh at emmaflip with dissolve
    "Suddenly Emma had a feeling she knows where Lila's As came from."
    "Even though she felt a boil in her heart she maintained her anger. "

    fa "Unbelievable..."

    "She murmured underneath her breath."

    fb "Well as Emma pointed it out, what's important is what's written on the paper."

    "Liam said as the two listened in."
    show Liam smile at right with dissolve
    show Emma default at emmaflip with dissolve
    show Lila default at left with dissolve
    fb "It talks about the existence of a magically being."
    fb "A being so powerful that can control a power known as The Sun."

    "Liam said as the tone of his voice lowered."
    "Lila's eyes glimmered."
    show Lila surprised at left with dissolve
    L "The Sun?"

    #"Lila questioned."
    "In response to her question, Liam smiled and pointed towards the endless dark night sky."

    fb "Yes."
    fb " It's essence was so strong it had the ability to light up the whole world."

    "Lila's mind was blown."
    "Although she had many and many questions running through her mind, she couldn't help take a moment to digust everything Liam has just said. "

    L "Where is it now? The Sun!"
    L "Who's controlling it?"
    L "Why haven't we-"
    show Emma angry at emmaflip with dissolve
    fa "Shhhhh!"
    fa "You dummy!"
    fa "Don't say anymore... This is just a rumor."

    "Emma said hushing Lila."
    show Liam nervous at right with dissolve
    fb "Unfortunately, that is all of the information we have now."

    "Liam said. His voice almost sounded disappointed."

    fb "Who knows if this is only a joke someone wrote about or if this is a dream of some lunatic."
    show Emma concern at emmaflip with dissolve
    #"Emma said but Lila rebuttal."
    show Lila happy at left with dissolve
    L "What if there were more of these pages!"
    L "What if we collected them all?"
    L "What do you think will happen?"

    "Lila's response did ingrue the two but they can only laugh it off."
    show Liam sigh at right with dissolve
    fb "A lot of Maybes..."
    fb "Who knows really."

    "Liam said but that was all he said as he led the two out of the forest."

    fb "But Let's rest up first before we dig deeper."

    fa "Right. I'm exhausted."
    hide Liam sigh at right with dissolve
    hide Lila happy at left with dissolve
    hide Emma concern at emmaflip with dissolve
    "As her friends slowly left the den behind dragging her with them Lila turned to look at the den."
    "She couldn't help wondering if the two took her seriously?"
    "Or did they just rub it off as a joke."
    "Either way, she's determined to find out more about the page and the information written on it."
    "That is after she's rested. "
    scene image "BGStart.png" with fade
    "End."
    "Page 1 discovered."
    "Lila's Route."
return

label CheckLiam:
    show Lila default at left with dissolve
    show Emma concern at emmaflip with dissolve
    "Lila was about to step into the Den to check on Liam but Emma's sharp words stopped her."

    fa "Where do you think you're going?"
    show Lila pout at left with dissolve
    L "I wanted to see if Liam's ok..."

    #"Lila said, backing away from the den."
    show Emma angry at emmaflip with dissolve
    fa "You never learn do you."
    fa "Just stay put."
    fa "Liam is stronger than both of us."
    fa "If something does happen what can you do?"
    show Lila sad at left with dissolve
    "Emma's words felt hurtful but they weren't wrong."
    "It is true that both Liam and Emma are physically stronger than Lila."
    "Yet she couldn't help but feel worried for Liam. "
    show Lila pout at left with dissolve
    L "But I'm still worried."

    #"Lila said as she looked at Emma pitfully."
    #"Emma's face softens when she sees Lila acting like a lost puppy."
    show Emma sigh at emmaflip with dissolve
    fa "You'll still go in even if you might get hurt?"

    "Lila nodded her head."

    fa "Even if I refused to go with you?"

    "Lila nodded again."

    fa "What if you got hurt doing that?"
    show Lila smile at left with dissolve
    "Lila thought for a moment and then replied with a smile."

    L "At least then only I would be the one hurt."
    L "Emma and Liam will be fine because you guys are strong."
    show Emma shocked at emmaflip with dissolve
    #"Emma's eyes widened and was speechless for a few seconds."
    #"Then she signed and smiled back."
    show Emma sigh at emmaflip with dissolve
    show Emma smile at emmaflip with dissolve
    fa "I wouldn't let you get hurt, idiot."
    fa "Wait out there."
    fa "I'll go check on him."
    fa "Though I have feeling this is pointless worry."
    show Emma pout at emmaflip with dissolve
    "Emma said, preparing to enter the cave."
    "Lila wanted to stop her so they two could go into together but just as she was about to say something Liam popped up."
    show Liam smile at right with dissolve
    fb "Glad to hear you two doing well."

    "Lila was speechless while Emma clicked her tongue. "

menu:
    "HUH? Are you ok?":
        jump HUHYOU

    "You had us worried!":
        jump UsWorried
return

label HUHYOU:
     show Lila surprised at left with dissolve
     show Liam happy at right with dissolve
     fb "Hm? Me. I'm perfectly fine."

     #"Liam said with a bright smile."
     show Emma pout at emmaflip with dissolve
     fa "That was so much unnecessary worry."

     "Emma grunted but she looked relieved to see he was doing just fine."

     L "What happened in that cave?"

     #"Lila asked and Liam's face darkened."
     show Liam sigh at right with dissolve
     fb "I'm not sure how I can explain this..."
     fb "A Lot has happened."
     fb "I guess I should start with this."
     show Liam page at right with dissolve
     "Liam said as he held out a piece of paper."
     "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."
     #"Emma's face also darkened."
     show Lila stunned at left with dissolve
     L "Huh?"
     L "What is it..."

     fb "It's best if you don't know."
     show Emma angry at emmaflip with dissolve
     #"Liam said but Emma argued."

     fa "Why are you hiding this from her?"
     fa "She should know."

     #"Although Emma also looked like she was in the state of shock her words were still headstrong."

     fb "She wouldn't be able to handle this...."

     "Liam protested but Emma insisted that they should inform Lila about their situation."

     fa "You can't baby her forever."
     fa "She'll be the one hurt if you keep shielding her from reality."

     fb "I just don't want her to break because she's too pure."
     fb "You shouldn't keep pushing her either."
     fb "We're her friends."

     "Liam argued but he wasn't angry."
     "If anything he just sounds a bit more disappointed."
     "His words made Emma more heated."
     "Although Lila has no clue why they are arguing all the time, she feels like she's responsible for it."
     "How should she calm down the situation?"

menu:
    "I think I should know...I can handle it!":
        jump ICanHandle

    "It's ok if I don't know.":
        jump OkIDont
return

label UsWorried:
    show Lila stunned at left with dissolve
    show Liam wink at right with dissolve
    fb "My apologies."
    show Liam default at right with dissolve
    #"Liam said with a smile."
    show Lila smile at left with dissolve
    fa "Anyways what happened in there?"
    show Emma angry at emmaflip with dissolve
    #"Emma asked and Liam's face instantly darkened."
    show Liam sigh at right with dissolve
    fb "I'm not sure how I can explain this..."
    fb "A Lot has happened."
    fb "I guess I should start with this."
    show Liam page at right with dissolve
    "Liam said as he held out a piece of paper."
    "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."
    #"Emma's face also darkened."
    show Emma shocked at emmaflip with dissolve
    L "Huh?"
    L "What is it..."
    show Lila surprised at left with dissolve
    fb "It's best if you don't know."

    #"Liam said but Emma argued."
    show Emma angry at emmaflip with dissolve
    fa "Why are you hiding this from her?"
    fa "She should know."

    "Although Emma also looked like she was in the state of shock her words were still headstrong."

    fb "She wouldn't be able to handle this...."
    show Liam angry at right with dissolve
    "Liam protested but Emma insisted that they should inform Lila about their situation."

    fa "You can't baby her forever."
    fa "She'll be the one hurt if you keep shielding her from reality."

    fb "I just don't want her to break because she's too pure."
    fb "You shouldn't keep pushing her either."
    fb "We're her friends."

    "Liam argued but he wasn't angry."
    "If anything he just sounds a bit more disappointed."
    "His words made Emma more heated."
    "Although Lila has no clue why they are arguing all the time, she feels like she's responsible for it."
    "How should she calm down the situation?"

menu:
    "I think I should know...I can handle it!":
        jump ICanHandle

    "It's ok if I don't know.":
        jump OkIDont
return

label  ICanHandle:
     show Lila default at left with dissolve
     show Emma smug at emmaflip with dissolve
     "Lila responded with enthusiasm. Her excitement broke through the tension that was built between the two."
     show Liam surprised at right with dissolve
     fa "That's the spirit!"
     fa "The baby has finally grown!"

     "Emma shouted with a bright grin on her face."
     show Lila surprised at left with dissolve
     L "Baby?!"
     L "Did you always see me as a child?"
     show Emma happy at emmaflip with dissolve
     #"Lila pouted as Emma laughed."

     fa "What you just found out now?"
     fa "It's ok this big sister will take care of you."
     show Lila pout at left with dissolve
     "Emma said teasing Lila."
     show Liam smile at right with dissolve
     L "I'm old enough to take care of myself!"
     L "So tell me what you guys found."
     L "I want to know too."

     "Lila rebelled but her tone wasn't harsh."
     "Although Liam didn't look pleased he sighed and gave into the energy the two were emitting."
     show Liam default at right with dissolve
     show Emma happy at emmaflip with dissolve
     show Lila default at left with dissolve
     fb "Ok. Ok."
     fb "It seems I'm the one being overprotective."
     fb "However, what we found today must remain with the three of us."
     fb "Understood?"
     show Liam smile at right with dissolve
     "The two of them nodded."
     "Liam gently smiled at their engarness but soon his gentle demeanor was replaced with a serious tone."

     fb "Ok...So I picked this up in the den..."
     show Liam page at right with dissolve
     "Liam said as he held out a piece of paper."
     "The paper was in terrible condition yet the symbols written on the paper seemed to be freshly made."

menu:
    "Huh? Why are you being secretive over this?":
        jump WhySecretive

    "What written on it?":
        jump WhatWritten
return

label OkIDont:
    show Lila smile at left with dissolve
    "After Lila spoke, the two went quiet."
    show Emma angry at emmaflip with dissolve
    fb "Right...Then let's just go back to the village."

    #"Liam said with a sigh of relief but Emma won't live this one down."
    show Liam sigh at right with dissolve
    fa "Weren't you interested in the big light Lila?"
    fa "A light so big it covers the entity of Rhea."
    show Emma happy at emmaflip with dissolve
    fb "Emma-!"
    "Liam almost lost his temper but Lila's words stopped him."
    show Lila surprised at left with dissolve
    L "I said that?"
    L "When?"
    show Liam surprised at right with dissolve
    "Lila's eyes were filled with wonder."
    "Her interest peaked and her eyes sparkled."

    fa "It doesn't matter when you said it."
    fa "What matters is that light you talked about exists"
    fa "It's written on this page."

    L "It is?"

    "Emma snatched the paper from Liam and shoved it to Lila."

    fa "Read it for yourself."

    "She said but Lila gave her a confused look."

    L "What does it say?"
    show Emma shocked at emmaflip with dissolve
    #"Emma's eyes widen."

    fa "Huh? Don't tell me..."
    fa "You can't read this?"

    "Liam, who was silently watching finally stepped up."
    show Liam angry at right with dissolve
    fb "Enough!"
    fb "Leave it be Emma."
    fb "This is just a fairy tale-"
    show Emma angry at emmaflip with dissolve
    fa "But I want to know more Liam!"

    "Lila said, interrupting Liam."
    "In response Liam paused and looked at her."

    L "Please tell me more!"
    show Lila smile at left with dissolve
    #"Lila said desperately."
    "Looking into her pleading eyes Liam could say no."
    "He finally gave in."

    fb "Ok."
    fb "Fine."
    fb "But promise me this stays between the three of us."
    show Emma default at emmaflip with dissolve
    "When the two agreed Liam started his explanation."
    show Liam sigh at right with dissolve
    fb "It talks about the existence of a magically being."
    fb "A being so powerful that can control a power known as The Sun."
    show Lila surprised at left with dissolve
    "Liam said as the tone of his voice lowered."
    "Lila's eyes glimmered."

    L "The Sun?"

    "Lila questioned."
    "In response to her question, Liam hesitantly pointed towards the endless dark night sky."
    show Liam default at right with dissolve
    fb "Yes."
    fb " It's essence was so strong it had the ability to light up the whole world."

    "Lila's mind was blown."
    "Although she had many and many questions running through her mind, she couldn't help take a moment to digust everything Liam has just said. "

    L "Where is it now? The Sun!"
    L "Who's controlling it?"
    L "Why haven't we-"
    show Emma pout at emmaflip with dissolve
    fa "Relax for a bit."
    fa "It's just a rumor... "
    fa "But do you believe in it?"

    "Emma interrupted but Lila nodded."

    fb "Unfortunately, that is all of the information we have now."

    "Liam said. His voice did sound a bit disappointed. "
    show Lila happy at left with dissolve
    L "What if there were more of these pages!"
    L "What if we collected them all?"
    L "What do you think will happen?"
    show Emma default at emmaflip with dissolve
    "Lila's response did intrigue the two but they can't be certain. "
    "Holding onto the page he took a deep breath and started to lead the two out of the forest."
    show Liam sigh at right with dissolve
    fb "Let's rest up first before we dig deeper."
    show Emma concern at emmaflip with dissolve
    fa "Right. I'm exhausted."
    hide Lila happy at left with dissolve
    hide Emma concern at emmaflip with dissolve
    hide Liam sigh at right with dissolve
    "As her friends slowly left the den behind dragging her with them Lila turned to look at the den."
    "She couldn't help wondering if the two took her seriously?"
    "Either way, they looked serious and she's just as determined to find out more information about the page."
    "That is after she's rested. "
    scene image "BGStart.png" with fade
    "End."
    "Page 1 discovered."
    "Lila's Route."
return

label VeryUncomfy:
    show Lila pout at left with dissolve
    "Lila slowly backed away from Minglou."
    hide Lila pout at left with dissolve
    hide Mingluo annoyed at right with dissolve
    "Before Minglou could say anything she ran to the den."
    "What was it that Minglou was hiding?"
    "Not only was she feeling uncomfortable, she was also very curious."
    scene image "OutsideDen.png" with fade
    window hide
    pause
    window show
    "When she arrived at the den she noticed that there really was nothing special about the den."
    "Feeling a sense of disappointment, she inch closer hopping whatever is inside might be what she's looking for."
    "But she was stopped by another voice."

    Q "Lila! We finally found you!"
    show Lila smile at left with dissolve
    show Emma default at emmaflip with dissolve
    show Liam default at right with dissolve
    "Lila turned around and found Liam."
    "Behind him was Emma who closed followed him."

    L "Huh?"
    L "Did you finish counting already?"
    show Emma concern at emmaflip with dissolve
    fa "We finished counting a while ago you airhead."

    #"Emma was grasping and  breathing for air."

    fa "He already found me."
    fa "I even had to wait awhile for him to go find you."
    fa "Yet you never showed up."
    show Lila surprised at left with dissolve
    L "Oh really?"
    L "I didn't know I had walked that far..."

    fb "I don't blame you."
    fb "Who knows how long it's been since we last separated."
    fb "This planet is seemingless."

    "Lila has no idea what Liam means."
    "But more than anything else she's more interested in what the Den has to offer."
    show Emma pout at emmaflip with dissolve
    fa "I'm feeling hungry."
    fa "Come let's just go back to the village."
    fa "All of this searching has tired me out."
    show Liam smile at right with dissolve
    fb "I agree with Emma."
    fb "Who knows how long it's been since we left the village."

menu:
    "Go into the den":
        jump IntoDen

    "Go with Liam and Emma":
        jump GoHome
return

label GoHome:
    show Lila happy at left with dissolve
    L "Now that you mentioned it. I'm feeling hungry too."
    show Liam happy at right with dissolve
    fb "Then it's settled! Let's go home."
    show Emma angry at emmaflip with dissolve
    fa "We could have played a bit more if a certain someone didn't go missing."
    show Lila surprised at left with dissolve
    L "Hm? But I wasn't gone for long..."

    fa "Then explain to me why is my energy drained?"
    fa "Who's fault is that?"

    L "Huh?"
    L "Your energy is drained?"

    "Lila was completely clueless."
    "Just as Emma was about to shout back Liam spoke."

    fb "Well we can always play again after we eat."
    hide Lila surprised at left with dissolve
    hide Liam happy at right with dissolve
    hide Emma angry at emmaflip with dissolve
    scene image "Forest_Default.png" with fade
    "Settling the situation the three of them continued to walk towards the village."
    "Unaware that they were being watched from a distance."
    "Minglou bitterly stared at the three kids laughing innocently"
    show Mingluo no eyes at right with dissolve
    m "Ignorance is a blessing isn't it?"
    m "What would you seedlings have done if you discovered you've been living in the darkness..."
    hide Mingluo no eyes at right with dissolve
    "Of course she didn't just mean that in a literal sense."
    "Who knows because they'll never know at this rate."
    "The children just smiled and laughed not knowing what the future holds...."
    scene image "BGStart.png" with fade
    "End"
    "No Pages found."
    "Lila's Route."

return

label IntoDen:
    show Lila pout at left with dissolve
    "Lila couldn't hold in her curiosity so she insisted on going into the den."
    show Liam sigh at right with dissolve
    fb "Wait Lila."
    fb "I'll go in to check first."
    fb "You shouldn't go."
    fb "It could be dangerous."

    "Liam said, stopping Lila in her tracks."
    show Emma angry at emmaflip with dissolve
    fa "Just don't go into the den."
    fa "Why do you always have to cause so much trouble?"

    "Emma said, clicking her tongue."

    L "I don't mean too."
    L "It's just that I feel like there's something in this den that is calling out to me."

    fa "You're in your daydream world again."
    fa "You make no sense."
    fa "Let's just go home."

    "Emma complained but Liam calmly replied."

    fb "It's ok."
    fb "I'll be back quick."
    fb "Emma if you're tired, why don't you take Lila and go home first"

    fa "I'm not going home without you and I'm not tired."

    "Emma contradicted her own statement from before."

    L "Are you sure you don't want me to go with you?"

    fb "It's fine."
    fb "Who knows what's in there?"
    fb "As the oldest one,  I should take a look first."
    fb "Wait for me out here."

    L "Ok..."

    "Lila said quietly while Emma stayed quiet."
    show Liam smile at right with dissolve
    hide Liam smile at right with dissolve
    #"Liam smiled and disappeared into the cave."
    "As the two quietly waited outside the tension between them seemed to increase."
    "Emma's gaze was just suffocating to Lila."
    "She wanted to say something but everytime she wanted to talk she felt the pressure from Emma forcing her to stay quiet."
    "The two stayed like this until they heard movement inside the den."
    "Flinching the two turn towards the entrance of the den."

menu:
    "Let's check on Liam...I think something happened.":
        jump LetsCheckL

    "I'm going to check on Liam.":
        jump ICheckL

return

label LetsCheckL:
    show Emma default at emmaflip with dissolve
    fa "You stay here."
    fa "I'll go."

    "Emma said in a demeaning tone."
    show Lila pout at left with dissolve
    L "But wouldn't it be dangerous to go by yourself?"

    fa "Who said I was by myself?"
    fa "Liam is in there."
    fa "Besides between the two of us I'm stronger."
    fa "So if anything happens you run back to the village and call for help."

    "Although Emma may sound bossy she did speak logic."
    "It was true that between her and Emma, Emma is physically stronger."
    "Not to mention she replied a lot on Minglou's powers when she's in trouble."
    "But Minglou isn't here at the moment so it would make sense for Emma to go in instead of her."

    L "Please be careful..."

    #"Lila whispered."
    show Emma concern at emmaflip with dissolve
    fa "Stop saying it like you're sending me off to a funeral."
    fa "You're such a cry baby."
    fa "Can't help it."
    fa "If both me and Liam were to leave you alone one day who knows if you'll survive on your own."
    show Lila angry at left with dissolve
    L "I'd be fine!"
    L "I still have grandma!"

    #"Lila puffed while Emma smirked."
    show Lila pout at left with dissolve
    fa "Relax."
    fa "I'm saying we won't leave you on your own."
    show Emma angry at emmaflip with dissolve
    fa "Behave for once and stay put."
    fa "Wait for us to come back."
    hide Emma angry at emmaflip with dissolve
    #"Emma said and entered the Den."
    "Her words were sharp but somehow it made Lila feel better."

    L "Come back soon!"

    "Lila shouted as Emma disappeared into the shadows."
    "For while Lila didn't see or hear any other movement."
    "After anxiously waiting till she was tired and hungry she finally heard some rustling within the den."
    "From the darkness Lila saw two shadows come out of the entrance."

menu:
    "Welcome back guys!":
        jump WelcomeGuys

    "What did you find? Was it dangerous?":
        jump DangerFind

return

label ICheckL:
    show Emma concern at emmaflip with dissolve
    fa "You stay put."
    fa "I'm going in."

    "Emma growled stopping Lila in her tracks."
    show Lila sad at left with dissolve
    L "But I'm worried"
    show Emma angry at emmaflip with dissolve
    fa "So?"
    fa "What can you do?"
    fa "Are you able to call your spirit right now?"

    "Lila thought about Emma's words."
    "She remembered how she left Minglou by herself."
    "Knowing her, Minglou probably will refuse to have contact with her for a few days."

    L "No..."
    show Emma sigh at emmaflip with dissolve
    fa "And you think you can just charge into danger unarmed."

    L "Sorry..."

    "Lila whispered."
    "Seeing Lila being so depressed, Emma sighed."
    show Emma concern at emmaflip with dissolve
    fa "Listen."
    fa "I didn't mean to make you upset but between the three of us, Liam is the strongest."
    fa "I am second."
    fa "So if something did happen to him I should go."
    fa "Who'll call back up if I don't return?"

    "Emma questioned as Lila looked at her with confusion."
    show Lila pout at left with dissolve
    fa "I'm talking about you dummy."
    fa "Just be ready."
    fa "If I don't come back for a while, run to the village, ok?"
    show Emma default at emmaflip with dissolve
    "Emma said in a soft tone as she entered the cave."
    hide Emma default at emmaflip with dissolve
    L "Come back soon!"

    "Lila shouted as Emma disappeared into the shadows."
    "For while Lila didn't see or hear any other movement."
    "After anxiously waiting till she was tired and hungry she finally heard some rustling within the den."
    "From the darkness Lila saw two shadows come out of the entrance."

menu:
    "Welcome back guys!":
        jump WelcomeGuys

    "What did you find? Was it dangerous?":
        jump DangerFind

return

label WelcomeGuys:
    show Lila happy at left with dissolve
    "Lila greeted them warmly yet the expressions on their faces turned the happy mood instantly sour."
    show Emma shocked at emmaflip with dissolve
    show Liam shocked at right with dissolve
    L "Wh-What happened in the den?"
    L "You guys don't look too good."

    "Liam looks the worst but because of Lila's worried expression he calmed down."
    show Liam nervous at right with dissolve
    fb "Don't worry... "
    fb "We just found something shocking."
    fb "That's all."
    fb "It just takes a moment to take in new information."

    "Liam spoke but his voice was filled with uncertainty."
    show Emma pout at emmaflip with dissolve
    fa "Why are you hiding this from her?"
    fa "She should know."
    show Lila surprised at left with dissolve
    "Although Emma also looked like she was in the state of shock her words were still headstrong."

    "Although Emma also looked like she was in the state of shock her words were still headstrong."

    fb "She wouldn't be able to handle this...."
    show Liam sigh at right with dissolve
    "Liam protested but Emma insisted that they should inform Lila about their situation."

    fa "You can't baby her forever."
    fa "She'll be the one hurt if you keep shielding her from reality."

    fb "I just don't want her to break because she's too pure."
    fb "You shouldn't keep pushing her either."
    fb "We're her friends."
    show Lila pout at left with dissolve
    "Liam argued but he wasn't angry."
    "If anything he just sounds a bit more disappointed."
    "His words made Emma more heated."
    "Although Lila has no clue why they are arguing all the time, she feels like she's responsible for it."
    "How should she calm down the situation?"

menu:
    "I think I should know...I can handle it!":
        jump ICanHandle

    "It's ok if I don't know.":
        jump OkIDont
return

label DangerFind:
    show Liam default at right with dissolve
    show Emma concern at emmaflip with dissolve
    show Lila surprised at left with dissolve
    fa "What happened to you being worried for us?"

    L "But you guys look fine."
    show Lila pout at left with dissolve
    fa "Why am I not surprised hearing you say that."
    fa "This is why I said he baby y-"
    show Liam sigh at right with dissolve
    "Noticing Emma's unconsciously hurting Lila again Liam cut her off."

    fb "We're fine."
    fb "The den wasn't that dangerous."
    fb "What we found though can be dangerous so let's just forget about it."

    "Although Emma was cut the first time she's not letting him have his way this time."
    show Emma pout at emmaflip with dissolve
    fa "Why are you hiding this from her?"
    fa "She should know."

    "Although Emma also looked like she was in the state of shock her words were still headstrong."

    fb "She wouldn't be able to handle this...."

    "Liam protested but Emma insisted that they should inform Lila about their situation."
    show Emma angry at emmaflip with dissolve
    fa "You can't baby her forever."
    fa "She'll be the one hurt if you keep shielding her from reality."

    fb "I just don't want her to break because she's too pure."
    fb "You shouldn't keep pushing her either."
    fb "We're her friends."
    show Lila sad at left with dissolve
    "Liam argued but he wasn't angry."
    "If anything he just sounds a bit more disappointed."
    "His words made Emma more heated."
    "Although Lila has no clue why they are arguing all the time, she feels like she's responsible for it."
    "How should she calm down the situation?"

menu:
    "I think I should know...I can handle it!":
        jump ICanHandle

    "It's ok if I don't know.":
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
