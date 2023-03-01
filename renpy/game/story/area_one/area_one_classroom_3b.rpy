# [DONE]

label area_one_Classroom_3B:
    scene bg black
    with dissolve

    narrator "You're going into classroom 3B."

    scene bg areaone classroom
    with dissolve

    if not vb_a1_cls_3b_visited:
        $ vb_a1_cls_3b_visited = True

        player "FUCK"

        narrator """Your heart starts pounding as you notice a skeleton right in front of you.

        It took you a second to realise that it is the human skeleton model for the biology class."""

        player_thinking """I swear to God I hate it here...

        If I recall correctly some studends called this skelly \"Bob\"

        A weird habbit to name dead objects... Especcialy if it's a HUMAN SKELETON!

        Well, at least it's not a furry costume..."""

        narrator "In this room there is additional door to room 4B."

        menu:
            "Examine the skeleton.":
                jump area_one_Classroom_3B_ExamineSkeleton
            "Leave to the corridor.":
                jump area_one_Classroom_3B_Leaving
            "Go to room 4B.":
                jump area_one_Classroom_3B_GoTo4B

    elif not vb_a1_cls_3b_skeleton_examined:
        narrator """You once again encounter the room with little happy skeleton named Bob.

        There still might be something useful here"""

        menu:
            "Examine the skeleton.":
                jump area_one_Classroom_3B_ExamineSkeleton
            "Leave to the corridor.":
                jump area_one_Classroom_3B_Leaving
            "Go to room 4B.":
                jump area_one_Classroom_3B_GoTo4B

    else:
        player_thinking "This Creepy Bob is still here..."

        menu:
            "Leave to the corridor.":
                jump area_one_Classroom_3B_Leaving
            "Go to room 4B.":
                jump area_one_Classroom_3B_GoTo4B

label area_one_Classroom_3B_ExamineSkeleton:
    $ vb_a1_cls_3b_skeleton_examined = True
    narrator """You approach the skeleton hoping to find something useful.

    At first it seems that there is nothing.

    Giving up with the search you once again glance at Bob.

    You notice that he has a note stuck between his ribs.

    Carefuly reaching for it, as you are still scared of the skeleton, you manage to take it out."""

    player "What is that note?"

    narrator """The note says:

    \"My sweetest... 

    I cannot wait any longer. 

    I hid the key in room A2, in your favorite flower on the windowsill. You'll use it to open my locker, and there'll be a spare key to the gym...

    Meet me there...\""""

    player_thinking """OH MY GOD THIS IS AWFUL!

    THEY DO WHAT THERE?!"""

    narrator "You shudder just thinking about the naughty things that were mentioned in the letter."

    player_thinking "Well, at least now I can find a key to a cabinet..."

    menu:
            "Leave to the corridor.":
                jump area_one_Classroom_3B_Leaving
            "Go to room 4B.":
                jump area_one_Classroom_3B_GoTo4B

label area_one_Classroom_3B_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the classroom to the corridor."

    jump  area_one_Corridor_3A3B

label area_one_Classroom_3B_GoTo4B:
    scene bg black
    with dissolve

    narrator "You go through the door leading to another room."

    jump  area_one_Classroom_4B