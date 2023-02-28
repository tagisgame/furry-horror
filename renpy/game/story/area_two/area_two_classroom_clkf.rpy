label area_two_Classroom_ClkF:
    scene bg black
    with dissolve

    narrator "You enter the female cloakroom."

    scene bg areatwo cloakroom
    with dissolve

    if not vb_a2_cls_clkf_visited:
        $ vb_a2_cls_clkf_visited = True

        #pierwsze wejscie

    menu:
        "Leave.":
            jump area_two_Classroom_ClkF_Leaving

label area_two_Classroom_ClkF_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor."

    jump area_two_Corridor_ClkFGym