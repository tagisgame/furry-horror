label area_two_Classroom_2G:
    scene bg black
    with dissolve

    narrator "You enter the room labeled as 2G."

    scene bg areatwo clasroom2g
    with dissolve

    if not vb_a2_cls_2g_visited:
        $ vb_a2_cls_2g_visited = True

        #pierwsze wejscie

    menu:
        "Leave.":
            jump area_two_Classroom_2G_Leaving
        "Go to room 1G."
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