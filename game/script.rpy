# The script of the game goes in this file.
define config.automatic_images = '_'
define m = Character("[momname]", color="#7f22e8")
define mr = Character("[momrelate]")
define mf = Character("[momfamily]")
define p = Character("[yourname]", color="#ffd700")
define l = Character("Liane")
define lr = Character("[cuzrelate]")
define longfade = Fade(1.0, 0.0, 1.0)
define longerfade = Fade(2.0, 0.0, 2.0)
image black = "#000"
image white = "#fff"
image ph = "#000"
image extnight = "1Home_Ext_Night.png"

# The game starts here.

label start:
    $ momlove = 0
    $ momcorr = 0

    show black
    with dissolve

    pause 0.5

    python:
        yourname = renpy.input("Please enter your name. (or skip to use default)")
        yourname = yourname.strip().title()
        if not yourname:
            yourname = "Chris"

    show extnight
    with longfade
    "*Crunch Crunch*"
    "Asphalt crunches beneath my feet, as my home slowly comes into view."
    "There's a warm breeze coming in from the beach - just a short walk down the road."
    "It's been unusually pleasant this time of the year."
    "No screaming kids, no masses of people muscling their way to the koisks.."
    "Just the odd couple hanging out, enjoying whatever modium of privacy this place could afford them."
    "I'm half tempted to make my way down, and enjoy the sea breeze myself."
    "Not that I have anyone to enjoy it with."
    "Tonight's different though, It's been a couple days since I've been back."
    "But it's the first time in awhile since I've been home for dinner."

    scene 3ext
    with dissolve
    "It's a lot quieter then I remembered though."
    "I don't miss the shouting, of course. Much less the sound of crashing furniture."
    "But staying here properly for the first time in years..."
    "It's going to take a bit of getting used to."
    "The smell of food wafts towards me as I crack open the door."

    scene 4kitchen_doorway_night_mom1
    with fade
    $ momname = renpy.input("How would you address this character? Eg: Hi _ , I'm home")
    $ momname = momname.strip().title()
    if not momname:
        $ momname = "Diane"
    if momname == "Mom":
        $ momrelate = "mom"
        jump familylabel
    if momname == "mum":
        $ momrelate = "mum"
        jump familylabel
    $ momrelate = renpy.input("What's her relation to you? Eg: But you are my _ .")
    $ momrelate = momrelate.strip().lower()
    if not momrelate:
        $ momrelate = "Landlady"
    label familylabel:
        $ momfamily = renpy.input("How would you describe both of your relationships? Eg: We are _ " )
        $ momfamily = momfamily.strip().lower()
        if not momfamily:
            $ momfamily = "friends"
    p "I'm back. What's that I'm smelling?"
    "You give her your usual grin."

    scene 4kitchen_night_mom2_brownkeyes
    "She turns up at the sound of my voice."
    m "You'll see. Welcome home dear."
    "She gives a tired smile and gestures for me to step closer."

    scene 4kitchen_night_mom3_brownkeyes

    m "Come here."

    pause 1

    scene 4kitchen_night_mom_closeup3brownkeyes

    "As she leans in close for a hug, I smell the light fragrance of her sweat and shampoo as she draws near.."
    "Must have a been a busy day for her."

    pause 0.5

    scene 4kitchen_night_mom5_brownkeyes

    "I gave a quick hug, [momname] lightly pressing her wrists over my back. I think I glimpse a touch of ketchup on her hands."
    m "So. How was the meet up?"
    p "Just kids talking amongst ourselves."
    p "I'm glad I made it back in time though. Dinner smells great! I can't wait to get started."
    "She chuckles lightly, and releases me."

    scene 4kitchen_night_mom2_brownkeyes

    "We used to be much closer. Leaving for college really made us drift apart."
    "It wasn't even that long ago to be honest. We used to be able to laugh at anything together even as she indulges my childish games."
    "I smile a little at that thought."
    "It's really been awhile since we've had a chance to sit and catch-up a little."

    scene 4kitchen_night_mom_closeup1

    "She's always been a little over-protective. It can get a little stifling but I know she means well."
    "It's a been a pretty trying last couple of years, [momname]'s been working pretty hard to keep it all together."
    "Maybe things might change now that I'm back."
    "Although, despite all that, she still looks great for her age."
    m "So, what do young people talk about these days?"

    scene 4kitchen_night_mom2_brownkeyes

    "Crap. I hope she didn't catch me staring."
    p "Ah. Just.. boring school stuff."
    p "Yea, everyone can't believe that it's finally over."
    p "No more exams. No more homework. We're finally free."
    "She gives a laugh."
    m "Free indeed!"
    "She chuckles again."
    m "Here."
    "She places the plate of food in front of me."
    p "Some of the guys already went for interviews, I guess they've already figured what they want to do."

    scene 4kitchen_night_mom6
    "Now that is a nice plate of bangers and mash."
    m "Oh? How're you coming along then?"
    "Crap. Wrong topic."
    "I can feel her looking intently at me as I glance down at my food."
    p "I've...got a few plans in mind."

    scene 4kitchen_night_mom4_brownkeyes

    m "Mmhm. Any chance you'll like to share that?"
    "I fidget nervously in my seat as I start to twirl the food around."
    p "Aah.. I was thinking of doing something fitness related.."
    p "A trainer maybe? Something like that."

    scene 4kitchen_night_mom_closeup2

    "I shrug non committally."
    "Ever since dad left, [momname] used to hope I'll eventually become a big shot executive of some kind. The kind of jobs that gets your name on a building somewhere."
    "Heh."
    "The recent years have sobered her a bit to the reality of things though."
    "I've very little desire to put myself into that sort of high pressure environment."

    scene 4kitchen_night_mom8_brownkeyes

    "She gives a small sigh."
    m "Liane started her new job last week."
    "If that was meant to get me to start working, that was the last person to compare against."
    "Still, that was news to me."
    "She's never been the 'working' type.'"
    "I wonder what sort of work she's gotten herself into.."
    p "Liane? Working?"

    scene 4kitchen_night_mom9

    "She tries to hide a wry smile"

    scene 4kitchen_night_mom8_brownkeyes

    m "Don't you judge now. She's had a rough couple of years."
    m "it's great to see her getting things back on track."

    "I'll believe it when I see it."
    "Liane. She grew up tormenting me every chance she gets."
    "It's been a good 10 years since I've seen her though."
    "And not long enough if you ask me."
    "I really doubt much has change."
    m "She called earlier by the way, I gave her your number."
    "Good lord."
    p "...[momname], you know we aren't on the best of terms."
    m "She's still [momfamily] dear. Besides, that's when you two were still kids."
    "I wince inwardly."

    scene 4kitchen_night_mom10
    with fade

    m "Don't give me that face - it's been awhile since you've caught up with her hasn't it?"
    p "- yea but.."

    scene 4kitchen_night_mom11

    m "I know you hate these gatherings.."
    "Sigh."
    m "But promise me you'll go."

    scene 4kitchen_night_mom12

    p "You're not going?"
    m "You know I can't."
    "Does she not see the irony in this?"
    m "Don't ignore what I said earlier about job hunting alright?"
    m "It's for your own good."
    m "You'll thank me eventually."
    "I lowered by head and finish up the last of the dinner in silence."

    show black
    with fade

    "..."
    "Every conversations with her inevitably turns into a lecture."
    "I should be used to this by now."
    "But having spent the last 4 years in college. It gets under my skin a little."
    "And she wonders why we don't talk as much."

    scene 5_mc_bedroom_night1
    with dissolve

    "Ugh."
    "I get that she has my best interest in mind.. but.."
    "..."
    "Fine. Whatever."

    scene 5_mc_bedroom_night2
    with fade

    "*tap tap*"
    "...."
    "..yea, half of these job ads look like scams."
    "..."
    "..."
    "..."

    "None of these interests me, but it looks like a newish gym opened a month ago not too far from here."
    "Guess it wouldn't hurt to check it out.."
    "I send a quick email asking for a potential interview."
    "..."
    "..."
    "There."
    "Now that that's taken care of.."

    scene 5_mc_bedroom_night3
    with fade

    "Perhaps I'm finally allowed to get some bloody sleep.."

    show black
    with fade

    "..."
    "..."
    "But of course."
    "I can't sleep."
    "The previous conversation is still turning about in my head."
    "It's a bit of a sore topic for me, since I've been looking unsuccessfully for a bit."
    "I've been kindda avoiding it lately."
    "..."
    "Maybe I'll get a drink.."

    scene 6_bathroom_ext_night1
    with fade

    "..hm?"
    "Oh [momname] must be in the shower."
    "That door has always been a bit wonky."
    "Looks like she didn't close it properly this time."

    scene 6_bathroom_ext_night2
    "Fine, let me just shut it for her..."

    pause 0.5

    menu:
        "What will I do?"
        "Take a quick peek.":
            $ momcorr += 1
            scene 7_bathroom_int_night1
            with hpunch
            "Oh god she's naked inside!"
            "I stood very still, trying hard not to make a sound"
            "Turning away is probably the best thing to do now."
            "But for some reason instead I'm rooted to the spot."
            "!!!"
            "I knew she kept in shape but wow."
            "She must be used to being alone in the house."
            "I can see her sweat glisten thinly on her skin, accentuating the curve of her body."
            "As she brushes her teeth in rhythmic strokes, her breasts bounces lightly in response."
            "I stared, transfixed by them."
            "I really should close the door before she turns around."
            "It would be horrifically bad to be caught like this."
            "..."
            "..."
            pause 1.0
            scene 7bathroom_int_night2
            with longfade
            "Try as I might, I still can't tear myself away."
            "Just the slightest hint of her aerola can be seen from my position."
            "My chapped lips feel dry as I swallow my saliva."
            "..."
            "It's not like I've not seen a naked women before."
            "College awarded me plenty of opportunities."
            "But something about this situation makes it really erotic.."
            "Is it because it's [momname]?"
            "..."
            scene 7bathroom_int_night3
            "I freeze for a moment as she stops to rinse out her mouth."
            "Oh fuck."
            "She's turning around!"
            "With sudden fear exploding through my heart, I scramble off, all thoughts of morality forgotten."

        "Shut it quietly.":
            "Best not not embarrass her...I'l do this quietly"
            "*Clicks*"
            jump nopeek1

    scene 8bathroom_int_night1
    with longfade
    "I held my breath on my bed, waiting for her to burst into my room at any moment."
    "..."
    "Minutes passed."
    "Nothing."
    "I think she didn't noticed."
    "Jesus."
    "What the hell was I thinking? That was way too close."
    "..."
    "I don't know came over me."
    "And what's worse - the fact that I peeped on [momname]..."
    "..or that I wished I'd stayed when she turned around."
    "..."
    "..."
    "Why didn't I just shut the damn door.."
    "I need to sleep this off.."
    show black
    with longerfade
    "Zzzz.."
    #scene ph
    #with longfade
    #"A dark figure approaches me.."
    #scene ph
    #with fade
    #pause
    #scene ph
    #with fade
    #pause
    #scene ph
    #m "is this.."
    #scene ph
    #m "what you're looking for?"
    #"she breaths heavily into my ear."
    #pause
    #show black
    #with longfade
    #"I wake with a start."

    jump day2

    label nopeek1:
        scene black
        with longfade
        "I padded down to the kitchen for a drink before returning to my room."
        "By the time I got back the lights in the bathroom has gone out."
        scene 8bathroom_int_night1
        with fade
        "Lets see if I can't sleep now.."
        show black
        with longerfade
        pause
        jump day2

    # This ends the game.
    label endgame:
    return
