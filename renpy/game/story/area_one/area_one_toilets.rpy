label game_start:
    call area_one_story_vars from _call_area_one_story_vars
    call area_two_story_vars from _call_area_two_story_vars

    jump area_one_ToiletStall_Start

label area_one_ToiletStall_Start:
    scene bg areaone toiletstall
    with fade

    if not vb_a1_toilets_player_start_over:
        player_thinking """Urghhhh...

        I must have passed out."""

    narrator """You wake up in a cold toilet stall engrossed in darkness. You can't remember what has happened.

    You have a terrible headache trying to recall anything that led to this particular moment."""

    if not vb_a1_toilets_player_start_over:
        player_thinking """Ah crap... Well, it seems I'm still at school.

        Why did nobody come to help me? Didn't they notice someone has fainted in a toilet stall?

        So I guess my hiding spot indeed works. That was the point of it after all."""

    player "Wait..."

    narrator "You say that loudly, as if you couldn't control it."

    player_thinking """Is it dark in here? Was I knocked out for the whole day?

    I didn't know it is possible to be out that long.

    I gotta get a grip, gotta get my stuff together.

    What will my next move would be?

    Should I stay here?

    Or should I- go?"""

    menu:
        "Stay inside.":
            jump area_one_ToiletStall_PlayerStayed
        "Leave.":
            jump area_one_Toilets

label area_one_ToiletStall_PlayerStayed:
    narrator "You decide to stay inside the stall and contemplate for a little longer."

    if vi_a1_toilets_player_stayed_in_toilet == 1:
        player_thinking """What if it's only a joke. They just switched off the lights and that's all.

        It's impossible to faint and wake up after eight hours or so, right?

        Wait a second! What time is it now?"""

        narrator "You reach out to your pockets and realize that they are empty."

        player_thinking """Where's my phone?! Where's my wallet?! Where are my belongings?!

        Now it's getting darker..."""

        $ vb_a1_toilets_player_checked_pockets = True

    elif vi_a1_toilets_player_stayed_in_toilet == 2:
        player_thinking """At some point one of the teachers must come here...

        Oh wait, they have their own restroom..."""
    
    elif vi_a1_toilets_player_stayed_in_toilet == 3:
        player_thinking "I should leave this place. It's cold and stinky."

        if vb_a1_toilets_player_start_over:
            player_thinking """I have a terrible feeling about staying here.

            I really need to go out."""

            jump area_one_Toilets
    
    if vi_a1_toilets_player_stayed_in_toilet != 6:
        $ vi_a1_toilets_player_stayed_in_toilet += 1

        narrator """You contemplate for a while and don't come up with anything useful right now.

        What are you going to do now?"""

        menu:
            "Stay.":
                jump area_one_ToiletStall_PlayerStayed
            "Leave.":
                jump area_one_Toilets

    else:
        jump area_one_Toilets_StayedDeath
    
label area_one_Toilets_StayedDeath:
    narrator "You hear strange noise coming from the entrance of the toilets."

    player_thinking "What was that? Is it a teacher? Help? Finally..."

    narrator "You hear closing footsteps. You decide to open your stall to seek for help."

    scene bg areaone toilets
    with fade

    narrator "As you open the door, the dark humanoid shape emerges from the darkness."

    player "Hello! I must have passed out in the stall-"

    scene bg black

    narrator "Before you managed to say anything else..."

    scene cgi toilet death
    with flash

    narrator """Your eyes fill up with blood. You feel sharp pain on your face.

    You try to scream, but the blood clogs your throat.
    
    There is no face of yours any more.

    You lay lifeless on the floor in a puddle of blood.

    That's all. This is how your story ends."""

    scene bg black

    tutorial """Seriously? You thought it was a good idea?

    What were you expecting exactly?

    An additional content, right?

    Well, you got it. Are you happy now?

    This is your additional content, there you go. You died. That's the scene you were looking for?

    Bravo... 'I will stay in that toilet stall 6 times in a row'.

    Now you surely want a button to come back before you chose to die.

    Do you think that death works like that?

    Okay... Okay... I will give you the option to reverse your death.

    Here you go:"""

    $ vb_a1_toilets_player_start_over = True
    $ vi_a1_toilets_player_stayed_in_toilet = 1
    $ vb_a1_toilets_player_checked_pockets = False

    menu:
        "Start over.":
            jump area_one_ToiletStall_Start

    jump area_one_ToiletStall_Start

label area_one_Toilets:
    scene bg areaone toilets
    with fade

    if not vb_a1_toilets_visited:
        $vb_a1_toilets_visited = True

        narrator """As you step out of the stall you find yourself in the same filty restroom you entered before losing consciousness.

        You can feel some sort of unnatural aura. Unpleasant feeling that puts your instincts wary."""

        # Nie slychac nawet bg noise
        player_thinking """Why is it so quiet here?

        I should turn on the lights."""

        narrator """The moment you tried to turn on the lights you witnessed a strange scenery. The entire restroom seemed to be covered in blood and a strange black goo.

        This vison lasted only a second, after a short while it all disappeared.
        
        The light didn't turn on."""

        player "WHAT THE HELL..."

        player_thinking """Am I going nuts? What the fuck was that?!

        I didn't sign up for all that. My therapist said that it shouldn't happen again!"""
    
    else:
        narrator "It's just a regular restroom. Nothing interesting in here."

        # [WORK IN PROGRESS] more description needed?

    narrator "What are you going to do now?"

    menu:
        "Leave the toilets.":
            jump area_one_Corridor_Toilets2B

    jump area_one_Corridor_Toilets2B