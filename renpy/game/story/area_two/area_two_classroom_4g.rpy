# [DONE]

label area_two_Classroom_4G:
    scene bg black
    with dissolve

    narrator "You enter the room labeled 4G."

    scene bg areatwo classroom4g
    with dissolve

    if not vb_a2_cls_4g_visited:
        $ vb_a2_cls_4g_visited = True

        narrator "At first glance, you see many excersise mats laying across the floor and being stacked before the wall."
        
        player_thinking """This room is used for fitness classess.
        
        They take place once every week and most of my classmates hates them.
        
        I wonder if they actually care about their physique...
        
        Fitness is very good for our health, I'm glad I enjoy these classes."""

        narrator """You walk towards the center of the room avoiding the mats on the floor, and you find a clear spot in the middle.

        You can see every corner of the room now, what are you going to do?"""

        menu:
            "Inspect the room thoroughly.":
                jump area_two_Classroom_4G_Inspect
            "Leave through the eastern door.":
                jump area_two_Classroom_4G_LeavingN
            "Leave through the southern door.":
                jump area_two_Classroom_4G_LeavingS
    
    elif not vb_a2_cls_4g_inspected:
        narrator """This room is used for fitness classes.

        You walk towards the center of the room avoiding the mats on the floor, and you find a clear spot in the middle.

        You can see every corner of the room now, what are you going to do?"""

        menu:
            "Inspect the room thoroughly.":
                jump area_two_Classroom_4G_Inspect
            "Leave through the eastern door.":
                jump area_two_Classroom_4G_LeavingN
            "Leave through the southern door.":
                jump area_two_Classroom_4G_LeavingS

    else:
        narrator """This room is used for fitness classes.

        You stand in the middle and stare at the empty walls."""

        player_thinking "There's nothing to look for here."

        menu:
            "Leave through the eastern door.":
                jump area_two_Classroom_4G_LeavingN
            "Leave through the southern door.":
                jump area_two_Classroom_4G_LeavingS



label area_two_Classroom_4G_Inspect:
    $ vb_a2_cls_4g_inspected = True

    player_thinking """Okay...

    Let's take a look."""

    narrator """You look around the room with ease as besides the mats there is nothing obscuring your view.

    There is nothing interesting in the room."""

    player_thinking "I won't find anything here, let's head out."

    menu:
        "Leave through the eastern door.":
            jump area_two_Classroom_4G_LeavingN
        "Leave through the southern door.":
            jump area_two_Classroom_4G_LeavingS

label area_two_Classroom_4G_LeavingN:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor via northern door."

    jump area_two_Corridor_4GGym

label area_two_Classroom_4G_LeavingS:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor via southern door."

    jump area_two_Corridor_2GClkM4G