label area_one_Corridor_AreatwoAreathree4B:
    scene bg areaone corridor
    with dissolve

    if not vb_a1_cor_ar2ar34b_visited:
        $ vb_a1_cor_ar2ar34b_visited = True

        narrator """You make your way to the corridor diverge.

        The dark corridors emanate some kind of fretful energy.

        It is almost incomprehensible."""

        player_thinking "Why is it so dark and creepy in here? It's just a school of mine..."

    if not vb_item_flashlight:
        if not vb_a1_toilets_player_checked_pockets:
            player_thinking """Hey I can use my flashlight in my phone...

            OR BETTER!

            I can CALL FOR HELP!"""

            narrator """You frantically search your pockets, but the phone was nowhere to be found.

            As you realise that you have lost you phone you can't shake the feeling that you are being watched."""

            jump area_one_Corridor_AreatwoAreathree4B_Darkness
        
        else:
            player_thinking """So... I've got no phone and no flashlight...

            Maybe I should turn back and look for something useful..."""

            narrator "There's an entrance to the room 4B."

            menu:
                "Go south.":
                    jump area_one_Corridor_3A3B
                "Enter classroom 4B.":
                    jump area_one_Classroom_4B
                "Approach the darkness.":
                    jump area_one_Corridor_AreatwoAreathree4B_Darkness

    else:
        if vb_a1_cor_ar2ar34b_visited:
            narrator "You step deeper into the school, the corridors are too dark to see anything."

        narrator """Fortunately, you have a flashlight with which you can dispel the darkness.
        
        To the west there is a corridor leading to the gym.
        
        Opposite to this is the entrance to the room 4B."""

        menu:
            "Go south.":
                jump area_one_Corridor_3A3B
            "Go west.":
                jump area_one_Corridor_GymEntrance
            "Enter classroom 4B.":
                jump area_one_Classroom_4B

label area_one_Corridor_AreatwoAreathree4B_Darkness:
    narrator """You stare blankly into the corridor. The darkness seems to devour everything.
    
    Yet your eyes must be deceiving you, as you can see a shadowy figure standing there in the darkness.

    Seeing glowing eyes staring at you, your legs turn to jelly.

    Trying to step back you bounce into lockers whose metallic sound echoes down the corridor.

    When you get up from the floor, you notice that the corridor is empty - no one is chasing you."""

    player "Oh my..."

    player_thinking """My brain is surely playing tricks on me.

    What should i do now? I should leave this place as fast as I can..."""

    menu:
        "Go south.":
            jump area_one_Corridor_AreatwoAreathree4B_SouthDeath

        "Enter classroom 4B.":
            jump area_one_Corridor_AreatwoAreathree4B_ClassroomDeath
        
label area_one_Corridor_AreatwoAreathree4B_SouthDeath:
    scene bg areaone corridor
    with dissolve

    narrator """There are two sets of doors on the west and east wall each. They are labeled as classrooms.

    On the north you see the corridor split, to the south there's the exit."""

    mysterious_person "*GROWL*"

    player "What the-"

    narrator """In the splits of second instead of the corridor you see nothing.

    You feel harsh fur on your skin.

    You feel a strong headache.

    You realise you're eyes left your sockets.

    {i}{color=#6b0700}Blood is spilling on the floor{/i}{/color}"""

    player_thinking """So that is what my death looks like.

    Well, it doesn't look like anything at all...

    Complete darkness{w=1.0}, headache{w=1.0}, fur{w=0.2}.{w=0.2}.{w=0.2}."""

    tutorial """For the record...
    
    {i}This is the death screen{i} {w} You can go back to the last decision, or start over."""

    $ vb_a1_cor_ar2ar34b_visited = False
    $ vb_a1_toilets_player_checked_pockets = True

    menu:
        "Revert my decision.":
            jump area_one_Corridor_AreatwoAreathree4B
        "Start over.":
            jump game_start

label area_one_Corridor_AreatwoAreathree4B_ClassroomDeath:
    scene bg black
    with dissolve

    narrator "You enter classroom 4B."

    scene bg areaone classroom
    with dissolve

    narrator "You're inside a regular classroom."

    mysterious_person "*GROWL*"

    player "What the-"

    narrator """In the splits of second instead of the corridor you see nothing.

    You feel harsh fur on your skin.

    You feel a strong headache.

    You realise you're eyes left your sockets.

    {i}{color=#6b0700}Blood is spilling on the floor{/i}{/color}"""

    player_thinking """So that is what my death looks like.

    Well, it doesn't look like anything at all...

    Complete darkness{w=1.0}, headache{w=1.0}, fur{w=0.2}.{w=0.2}.{w=0.2}."""

    tutorial """For the record...
    
    {i}This is the death screen{i} {w} You can go back to the last decision, or start over."""

    $ vb_a1_cor_ar2ar34b_visited = False
    $ vb_a1_toilets_player_checked_pockets = True

    menu:
        "Revert my decision.":
            jump area_one_Corridor_AreatwoAreathree4B
        "Start over.":
            jump game_start