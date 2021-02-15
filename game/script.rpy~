define L = Character(_("Lila"), color="#ced0ff")
define m = Character(_("Mingluo"), color="#2e37ff")
define fa = Character(_("Emma"), color="#73fff0")
define fb = Character(_("Liam"), color="#a673ff")
define Q = Character ("?")

define persistent.Route1 = True
define persistent.Route2 = True

define persistent.value = 0

define audio.RheaSoundtrack ="audio/RheaSoundtrack.wav"

init:
    transform flip:
        xzoom -1

label start:
    stop music
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

    fb "I also think we should start playing."
    fb "It's been a while since we've gathered. Let's enjoy this rare moment!"

    "Laim did raise his voice but his uplifting tone didn’t change."

    L "Oh... I guess you guys are getting bored."

    "Lila sounded disappointed at their reactions. But she didn't still disappointed for long. She did miss her friends after all."

    fa "How are you so thick headed for you to realize that just now?"

    L "Huh? Thick headed?"

    "She hates it when Emma uses words she don't understand. It always leave an awful feeling in her."

    fb "Ah! Ignore her. Ignore her. Let's play! What do you want to be Lila? The seeker or hidder?"

    menu:
        "Seeker?" if persistent.Route1 == True:
            jump Seeker
        "Hidder?" if persistent.Route2 == True:
            jump Concealer
return

label Seeker:
    $persistent.Route1 = False
    $persistent.value += 1
    if persistent.value >= 2:
        $persistent.Route1 = True
        $persistent.Route2  = True
        $persistent.value = 0
    fa "Than start counting slowpoke."
    L "Oh, Ok!"
    fb "No worries! Take you're time!"
    "With that the two went to hide while Lila started to count."
    "She stood in the darkness with her back turned surrounded by tall trees along side the gentle glows from fireflies..."
    show Lila happy at left

    L "55"
    L "54"
    L "53"


    Q "OUCH!" with vpunch
    show Lila shocked at left with dissolve
    "Startled, she turned her head to face the direction where the loud noise came from."
    "From a distance, the bushes shook for a bit but became still soon after."
    "She waited for a few more moments for any kinds of other movement but all she heard was silence."
    "Thinking she may have misheard she went back to counting."
    show Lila eyes closed at left with dissolve
    L "52"
    L "51"
    L "50..."

    Q "Ouch! What was that for?" with vpunch
    show Lila pout at left with dissolve
    "Once again grabbing her attention she observes from a distance."
    "She was a bit conflicted as to rather or not she should go check up on her friend."
    "After all, She is still in the middle of a game."
    "After thinking for a while, her concerns overpowered her determination to win."
    "She stood up and walked over to the noise."
    show Lila surprised at left with dissolve
    L "Emma?"
    L "Are you ok?"

    "She questioned as she was about to peek over the bush but Emma popped up from her hiding spot."

    fa "I'm fine!"

    "Soon after Emma popped up her other friend Liam popped up after."
    menu:
        "Are you sure? You sounded like you were in pain.":
            jump YouSure
        "Liam, Did you hit Emma?":
            jump HitEmma
        "Oh... Are you ok Liam?":
            jump LiamOk
return

label YouSure:
    fa "I already said I'm fine."
    hide Lila surprised at left
    show Liladefault at left
    L "I have some medication on me if you nee-"

    fa "Enough! I'm not that weak. Why are you so annoy-!"

    fb "Ahahaha! Look at you Lila! You've found us! Looks like Emma's the seeker next."

    L "I guess I did."

    L "But Emma you should still put some ointment on just in case..."

    fa "I don't need anything. Listen to me. This round isn't fair for Liam. Recount!"

    "Although the two should already be used to Emma's behavior they couldn't help but be a little bewildered. Liam sighed."

    fb "No, no. I can be seeker next if you don't want to Emma. There's no need for Lila to re-"

    fa "This isn't fair. She needs to recount."

    "Not wanting Liam to finish his sentense Emma cut him off"

    fb "Emma you're being a bit immature."

    "Although Liam said that is deadly calm tone his face showed a hint of annoyance."

    fa "I said that for you sake."
    show Lila pout at left with dissolve
    "Emma scowled. It doesn't look like Emma wants to back down either..."

menu:
    "But I already found you guys":
        jump SeekerL

    "I want to be seeker again!":
        jump SeekerLila

return

label SeekerL:
   fb "Lila's right. She's already found us."
   fb "Let's all play fair. It would be unreasonable if she has to look for us again."

   fa "..."
   "Emma's arms crossed as she frowned. Her eyebrows creaded as she galred at Lila."
   "Lila only tilted her head at Emma's usual behavior. She could only wonder what she had done this time to bother Emma {cps=2}...{/cps} again."
   fa "Fine."
   fa "But I'm not being 'it'"

   "Liam smiled and petted Emma on her shoulders. Feeling the warmth from Liam's gentleness the atmosphere soften."

   fb "Don't worry. I'll be 'it'. You guys can go ahead and hide. "

   fa "I don't need you're pity."
   "Emma said as she softly swat away Liam's hand."
   "Liam only reacted with a patient smile as Emma pouted"
   show Lila sad at left with dissolve
   "Lila suddenly felt a sense of guilt."
   L "I'm sorry Liam..."
   show Liladefault at left with dissolve
   "She said lowing her head."
   fb "Hm? What are you sorry for silly? There's nothing to be sorry about."
   fb "Instead, you should be focused on hiding."
   "Lila opened her mouth feeling the words welled up in her throat but a small pitch on her noise made her speechless."
   fb "I'm starting to count."
   "Removing his hand from her nose and after a wink he left her standing there"
   "He started counting down with his body turned leaning towards a tree."

   fb "100!"
   fb "99!"
   fb "98!"
   hide Liladefault at left with dissolve
   "With that Lila immediately started to run."
   "She kept running further and futher into the darkness until she can no longer remember where she is."
   show Lila surprised at left with easeinleft
   L "Oh no...I-I don't remember seeing these paths."
   show Lila pout at left with dissolve
   "She huffed and puffed as she looked around her. It would seem like she's lost."
   "From what she could see, to her left was a cave covered in transparent crystals and tiny glowing fungi."
   "The cave seem endless and very spacious."
   "Besides the cave, to her right was some kind of animal den."
   "The inside of the den seemed a bit dark while the outside is swarmed with fireflies."
   "Though she can't tell what kind of animal made this"
   "She does know it's big enough for her to fit through."

   L "Which way should I hide?"

menu:
    "The endless cave":
        jump Cave
    "The animal Den":
        jump Den

return

label Cave:
    L "I think there be more room to breath compared to the den."
    show Lila happy at left with dissolve
    L "Maybe I'll even find a new mushroom species!"
    scene Cave
    with dissolve
    show Liladefault at left with dissolve
    "Making up her mind Lila chose to hide inside the cave."
    "Following the tiny dimly lit mushrooms Lila walks deeper and deeper into the cave."
    "After exploring the new territory, she settled on a spot she thought was comfortable."
    "Even though the atmosphere was cold and chilly, it didn't scare her."
    "What worried her was the amount of time she has waited in the cave since she's arrived."
    "She waited and waited till her bottom is numb and her body went limp."
    show Lila pout at left with dissolve
    "Feeling the boredom creep up her, she decided to summon her spirit."
    show Lila eyes closed at left with dissolve
    "She closed her eyes and focused her mind."

    L "Must be at a state of peace."

    "She repeated as the energy of nature engulfs her. Her breath slowly merges with the purity of the air."
    "She was in this state until she successfully called upon the water spirit named Minglou."
    show Mingluo default at right with easeinright
    m "Ah! That feels good."
    m "Been a while since I've been summoned."

    "Minglou stretched her arms as her energy levels settled with the current environment."
    show Liladefault at left with dissolve
    m "I'll give you props for doing it correctly for once."
    m "I've lost count of the amount of times you've managed to summon me midway."
    m "God that was an awful experience."
    show Lila happy at left with dissolve
    "Excited to be complimented for once by this pompous spirit Lila shouted in celebration."

    L "I've been practicing! I'm so glad it worked well this time. I was-"

    m "Don't get ahead of yourself."

    "In one moment all of the excitement she felt was gone."
    show Lila pout at left with dissolve
    m "In fact, I should smack you for the poor condition you are in."
    m "Did you not think how that will affect me physically if you summon me like that?"

    "Each time Minglou shows up she seemed fine so she's never thought about that."
    show Lila surprised at left with dissolve
    L "Does that mean you are hurt-"

    m "Also where the hell are we?"

    "Minglou gilded across the cave while asking in a booming voice."
    "Once again it seems like Minglou is fine. So Lila is only more confused then concerned."
    show Liladefault at left with dissolve
    L "Um... Minglou I can do a check up to see if you need healing-"

    "Minglou prioritized her questiosn over Lila's concerns."

    m "Why was I summoned?"

    "Lila gulped, already forgetting what she was concerned about."

    m "There better be a good reason for this."
    show Lila surprised at left with dissolve
    "She knew Minglou wasn't going to let her off the hook."
    "She seems a bit mad...What should Lila say?"

menu:
    "Apologize":
        jump Apologize
    "Change the topic":
        jump ChangeTopic
    "Explain the situation":
        jump ExplainSit

return

label Apologize:
    show Lila sad at left with dissolve
    L "I'm soooooooooooo sorryyyyyyyyy!"
    "Lila bowed on her hands and knees while Minglou gave her a werid look."

    m "{cps=2}Right...{/cps}"
    m "What exactly are you apologizing for?"

    L "Um..."
    show Lila surprised at left with dissolve
    "Lila though for a while. Wait... WHAT IS SHE SORRY FOR? She don't know how to answer that."

    m "You apologized and you don't even know what you did wrong?"
    "It was like Minglou saw right through her."
    "Lila closed her eyes and smiled brightly while looking up at Minglou."
    show Lila happy at left with dissolve
    L "I don't know but I still wanted to apologize."

    "Minglou was speechless. She tilted her head down and placed a hand on her forehead."
    "Shaking her head she complained."

    m "You... you are just UNBELIEVABLE."

    L "Thank you!"

    "Standing up Lila replied with a hand on teh back of her head. Still smiling, she blushed."
    show Lila blush at left with dissolve

    m "That wasn't a compliment airhead."
    show Lila pout at left with dissolve
    L "A-air-Airhead?!"

    "Lila's eyes widened and faced puffed. She looked ay Minglou in disbelief."

    m "What? Now you're going to get mad at me?"

    L "Uh. "

    L "Actually, I don't know what that means. But I had a funny feeling when you called me that."

    m "Ugh! Enough with this foolery. Tell me exactly what is this place?!"

menu:
    "I don't know":
        jump IDK
    "A cave...I think?":
        jump IThink

return

label IDK:
    m  "Elaborate."
    show Liladefault at left with dissolve
    L "?"
    "Minglou sighed."
    m "Explain to me what do you mean you don't know?"

    L "Oh! Well...You see. I was playing hide and seek."
    show Lila happy at left with dissolve
    m "And?"

    L "Andddd I after looking for a while. Here I am!"
    m "So...You got lost?"

    L "Nope!"
    show Liladefault at left with dissolve
    L "Liam and Emma just haven't found me yet!"
    m "....."
    m "How long has it been since you've hide here?"
    show Lila surprised at left with dissolve
    L "Uhhhhh. I'm not usre. I lost count of time."
    show Liladefault at left with dissolve
    m "..."

    m "Well."

    m "That was a waste of time."

    "Minglou grunted and grabbed Lila by the collar. She started to drag her across the floor."
    show Lila angry at left with dissolve
    L "Wait-!"
    L "Ouch that hurts!"
    L "Where are you taking me?!"

    m "Nowhere really. Just be quite and follow me."
    show Lila surprised at left with dissolve
    L "What does that even mean?!"

    m "Since we're here anyways I'll show you something extraordinary."

    L "Something extraordinary? "
    "Lila stopped struggling. A wave of curiosity overtook her mind and body."
    "Minglou saw the spark in her eyes and smirked."
    show Liladefault at left with dissolve
    "Lila was about to question Minglou but they came to a sudden stop."
    show Lila surprised at left with dissolve
    L "Huh?"
    "Lila looked around. She notices they were still inside the cave."

    L "Uh... Minglou. Are you lost too?"

    m "Of course not."

    L "Then why does it feel like we are still in the cave?"

    m "Cause we are."

    L "I thought you said you'll take me out?"

    m "I will."

    m "After I show you something."
    show Lila surprised at left with dissolve
    L "?"

    "Curiosity overpowered her logic. Lila now is interested in what eactly Minglou has to show her."

    "Would have gave more choices here... For now to be contuined."
return

label HitEmma:
   "To be contuined"
return

label LiamOk:
   "To be contuined"
return

label SeekerLila:
    "To be contuined"
return

label Den:
    "To be contuined"
return

label ChangeTopic:
    "To be contuined"
return

label ExplainSit:
    "To be contuined"
return

label IThink:
    "To be contuined"
return



label Concealer:
    "To be contuined"
    $persistent.Route2 = False
    $persistent.value +=1
    if persistent.value >= 2:
        $persistent.Route1 = True
        $persistent.Route2 = True
        $persistent.value = 0
return

#init python:
    #def reset():
        #persistent.Route1 = True
        #persistent.Route2 = True
        #persistent.value = 0
return
