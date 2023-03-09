#drugi z lewej


label area_two_Classroom_2G:
    scene bg black
    with dissolve

    narrator "You enter the room labeled as 2G."

    scene bg areatwo clasroom2g
    with dissolve

    if not vb_a2_cls_2g_visited:
        $ vb_a2_cls_2g_visited = True

        narrator """You enter a room that was intended to store exercise equipment.
        
        The shelves are filled with various rackets, darts, balls and various other equipment that you are unable to name.
        
        After all, you were never a sports fan.
        
        You've been sent here a few times during class, and you know there's nothing of interest here."""

    else:

        narrator "You enter the storage for exercise equipment. There is nothing interesing."

    menu:
        "Leave.":
            jump area_two_Classroom_2G_Leaving
        "Go to room 1G.":
            jump area_two_Classroom_2G_GoTo1G

label area_two_Classroom_2G_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor."

    jump area_two_Corridor_2GClkM4G

laberl area_two_Classroom_2G_GoTo1G:
    scene bg black
    with dissolve

    narrator "You leave the room via door leading to room 1G."

    jump area_two_Classroom_1G