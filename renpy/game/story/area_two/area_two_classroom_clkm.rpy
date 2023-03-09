#trzeci z lewej

label area_two_Classroom_ClkM:
    scene bg black
    with dissolve

    narrator "You enter the male cloakroom."

    scene bg areatwo cloakroom
    with dissolve

    if not vb_a2_cls_clkm_visited:
        $ vb_a2_cls_clkm_visited = True

        narrator """The mere sight of the men's cloakroom gives you chills.
        
        You always hated the smell of sweat that lingers in this place.

        On one of the hangers you notice a thick, down jacket.
        
        It is so strange that at this time of year it is quite warm and no one in their right mind would wear such a jacket.
        
        You search it, hoping to find something that can help you.
        
        Maybe someone left a phone in it?
        
        Unfortunately for you, the jacket is empty and seems to smell like it belongs to some homeless person."""
        
            menu:
        "Leave.":
            jump area_two_Classroom_ClkM_Leaving

    else:
        
        narrator "You walk into a hated cloakroom with nothing of note."

        menu:
            "Leave.":
                jump area_two_Classroom_ClkM_Leaving

label area_two_Classroom_ClkM_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor."

    jump area_two_Corridor_2GClkM4G