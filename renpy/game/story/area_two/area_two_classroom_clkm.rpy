label area_two_Classroom_ClkM:
    scene bg black
    with dissolve

    narrator "You enter the male cloakroom."

    scene bg areatwo cloakroom
    with dissolve

    if not vb_a2_cls_clkm_visited:
        $ vb_a2_cls_clkm_visited = True

        #pierwsze wejscie

    menu:
        "Leave.":
            jump area_two_Classroom_ClkM_Leaving

label area_two_Classroom_ClkM_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor."

    jump area_two_Corridor_2GClkM4G