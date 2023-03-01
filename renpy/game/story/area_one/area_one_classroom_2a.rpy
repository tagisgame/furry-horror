label area_one_Classroom_2A:
    scene bg black
    with dissolve

    narrator "You enter classroom 2A."

    scene bg areaone classroom
    with dissolve

    if not vb_a1_cls_2a_visited:
        $ vb_a1_cls_2a_visited = True

        narrator """You enter a classroom beautifully decorated with various flowers.

        One could mistake it for the biology class, yet you rembember that one of the teachers really loves flowers.

        This teacher is seriously obsessed with her flowers and the classroom is filled with all kinds of fertilizers, special types of soil, and huge water cans.

        Students often complain that because of her interests, they have to take a makeup class, because most of the classes are devoted to flowers and not teaching"""

        

    else:
        narrator "You enter a classroom beautifully decorated with various flowers."

    if not vb_item_cabinetkey:
        if not vb_a1_cls_3b_skeleton_examined:
            player_thinking """Hmm I don't want to get my hands dirty...

            There probably isn't even a thing worth my time"""

        else:
            $ vb_item_cabinetkey = True
            player_thinking """If I remember correctly, there is a key hidden in one of the flowers...

            Now, which one would it be?"""

            narrator """You searched every pot with flowers on the windowsill.

            Trying to find the key you didn't hasitete to dig in the soil and your hands got dirty.

            You did not consider action and started looking for the key in random pots.

            And it so happened that the last pot you checked, the one that's the closest to the teacher's desk had a key, waiting there on the soil."""
    else:
        narrator "It was here where you found a key to a cabinet in 1B."

    narrator "There is a entrance to classroom 1A."

    menu:
        "Leave.":
            jump area_one_Classroom_2A_Leaving
        "Go to classroom 1A.":
            jump area_one_Classroom_2A_GoTo1A

label area_one_Classroom_2A_Leaving:
    scene bg black
    with dissolve

    narrator "You decide to leave the room to a corridor."

    jump area_one_Corridor_2A1BLab

label area_one_Classroom_2A_GoTo1A: 
    scene bg black
    with dissolve

    narrator "You decide to visit the room 1A."

    jump area_one_Classroom_1A
