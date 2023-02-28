label area_two_Classroom_3G:
    scene bg black
    with dissolve

    narrator "You enter the room labeled as 3G."

    scene bg areatwo classroom3g
    with dissolve

    if not vb_a2_cls_g3_visited:
        $ vb_a2_cls_g3_visited = True

        #pierwsze wejscie

    menu:
        "Leave through the eastern door.":
            jump area_two_Classroom_3G_LeavingE
        "Leave through the western door.":
            jump area_two_Classroom_3G_LeavingW

label area_two_Classroom_ClkM_LeavingE:
    scene bg black
    with dissolve

    narrator "You use the eastern door."

    jump area_two_Corridor_3G

label area_two_Classroom_ClkM_LeavingW:
    scene bg black
    with dissolve

    narrator "You use the western door."

    jump area_two_Corridor_3GGym