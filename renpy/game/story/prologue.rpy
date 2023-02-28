label prologue_start:
    python:
        vs_player_name = renpy.input("What is your name?", length=16)
        vs_player_name = vs_player_name.strip()
        if not vs_player_name:
            vs_player_name = "You"
    
    scene bg prologue gym

    player_thinking "I stared blankly at the colorful costiumes of the actors on the stage. I could not help but stare with dread at their 'cute' faces..."

    narrator """
    Fox represents trickery and deceit. His ability to shapeshift into anything or anyone he desires may deceive even the best observers.

    Bunny, who bit the Moon and changed its shape to a croissant then provided people with medicine out of moondust. {i}His benevolence knew no bounds.{/i}"""

    player_thinking "Yeah, for sure he won't hestitate to taste human flesh."

    narrator "Weasel, who is believed to trip people. Actually, there are two more of them: one of which wounds you and the other heals you."

    player_thinking "'Course, they had to choose the deadliest one... As if their bare existance wasn't enough."

    narrator "Wolf being the one of the protective spirits that deters malicious ghosts, but will turn on you the moment you make a mistake."

    player_thinking """I wonder how people find these costumes cute... or anything. Anything besides frightening.

    If I were to stand close to that terrifying abominations I would probably die of a heart attack...

    Just thinking about their fur gives me the shivers."""

    narrator "You try to look up to see what's happening in the stageplay. You respect the effort students put into making the play."

    narrator "It's just your unexplainable fear towards furry animals that makes you feel uncomfortable."

    player_thinking "I- I don't know why I am anxious about them... I just don't trust antropomorphic animals."

    narrator """Finally you are able to gaze at them.. 

    On the stage you may see the spirits sitting around a decoration that represents a small bonfire and having a chat."""

    show weaselactor

    weasel_actor "*jiggle* I love tripping up humans, It's so easy to catch them off guard and make them stumble!"

    show bunnyactor

    bunny_actor "Weasel, you should not take pleasure in hurting others. Humans are fragile creatures after all."

    wolf_actor "Humans are weak and vulnerable. They need protection, yet I would not hestitate to hurt them if they happened to slip *heckle*"

    fox_actor "My dear fellows, you all have your own unique ways of interacting with humans. I prefer to deceive them."

    fox_actor "I enjoy playing tricks on them, keep them humans on their toes. It makes it a way more interesting."

    weasel_actor "Oh Fox, you always know how to have fun..."

    weasel_actor "But we cannot forget, we must be careful not to harm them too much. We are spirits of the natuaral world and we are connected to them."

    bunny_actor "That's true, Weasel. *nodding* We should always strive to balance our actions and find a way to coexist with humans."

    show bg prologue gym
    with flash

    player "Whoah... What was that?!"

    narrator "People around turn to look at you as you are yelling these words."

    player_thinking "Did I just... Did I just yell? What the hell was that?! Have others seen it too?"

    narrator "You start sweating after you realised that you cought the attention of students around you."

    player_thinking "I gotta hide. I need to take a breather."

    narrator """You begin to shoulder your way through the crowd towards the exit of the gym.

    You reach the door leading to a hallway. You open them and walk through."""

    jump prologue_hallway

label prologue_hallway:
    scene bg prologue hallway
    with fade

    narrator """You are wandering the hallway that, despite the ongoing show, is crowded with people.

    Those people seem to be interested in your person and you can feel thier piercing eyes on you.

    However, everyone is occupied with their struggles, noone glances at you.

    Despite all that you try to pass the hallway without attracting any attention as you are terrified of their deadly stares.

    Passing by the two students, no more than a year older than you, you can overhear their conversation."""

    student1 "My beloved father presented us with another domestic violence show last night. Damn drunk..."

    student2 "Such behavior is inappropriate! He should consider his acctions and you should talk to him about that!"

    student1 """I do not intend to speak to him anymore. And he'll have enough time to think while he rots in jail!

    That's the third time he hit my mom, I called the police and they took him away. They say he won't come out anytime soon."""

    player_thinking "Hmm... So third time lucky..."

    narrator """This conversation somehow made you more anxious. Shivers run down your spine as you hasten your steps.

    Finally, after mentally exhausting journey to the toilet, you reach the place."""

    jump prologue_toilets

label prologue_toilets:

    # Black screen - the transition between the corridor and bathroom stall - omitting the Toilets scene

    scene bg black
    with dissolve

    narrator "Those toilets are always cold and too filthy to be used. They disgust you but it is the only safe place in this school."

    scene bg prologue toiletstall

    player_thinking """Those furry costumes... There is someting unsettling about them. I can't explain it tho...

    People say that they look cute, some even fantasize about them... Bleh...

    How people can say things like that?! Those are bloodthirsty monsters!"""

    player "Fuck..."

    player_thinking """I need to get out! I can't stand this shit I need to get home and relax.

    But what will people think? They certainly will talk behind my back. They will call me coward!

    Screw those people! What if the actors are on break and I'll bump into one of them wearing his suit?!

    I can't get out now... But I have to..."""

    narrator """Suddenly you feel nauseous. You can feel your guts trembling inside of you.

    You start to lose your breath as you feel unnatural pressure on your lungs. Your throat feels squeezed as you desperately try to take a breath."""

    player_thinking "Oh God... What do I do now..."

    narrator """Suddenly, you hear the door opening. Quiet footsteps can be heard outside the stall.

    You notice a shadow of a person under the door. Every part of your body starts to ache in fear."""

    mysterious_person "Hello? Is anybody in there?"

    narrator "Hearing this calm, yet unsettling voice, you feel your consciousness fading."

    jump game_start