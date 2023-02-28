label area_two_Classroom_1G:
    scene bg black
    with dissolve

    narrator "You enter the room labeled as 1G."

    scene bg areatwo clasroom1g
    with dissolve

    if not vb_a2_cls_1g_visited:
        $ vb_a2_cls_1g_visited = True

        #pierwsze wejscie

    menu:
        "Leave.":
            jump area_two_Classroom_1G_Leaving
        "Go to room 1G."
            jump area_two_Classroom_1G_GoTo2G

label area_two_Classroom_1G_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor."

    jump area_two_Corridor_1GAreaOne

laberl area_two_Classroom_1G_GoTo2G:
    scene bg black
    with dissolve

    narrator "You leave the room via door leading to room 2G."

    jump area_two_Classroom_2G