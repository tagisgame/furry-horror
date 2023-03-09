#czwarty z lewej

label area_two_Classroom_ClkF:
    scene bg black
    with dissolve

    narrator "You enter the female cloakroom."

    scene bg areatwo cloakroom
    with dissolve

    if not vb_a2_cls_clkf_visited:
        $ vb_a2_cls_clkf_visited = True

        narrator """When you enter the women's cloackroom, you realize that it actually smells much better than the one men use.
        
        After all, it is the girls who open the windows every day to ventilate the place and use their strong, sweet perfume.

        Hundred of scents mix and almost stupefy you.

        These pleasant smells make you want to stay in this place, but you know you have to find a way out of this school."""

        menu:
            "Leave.":
                jump area_two_Classroom_ClkF_Leaving

    else:
        narrator "You enter a wonderfully scented women's cloakroom."

        menu:
            "Leave.":
                jump area_two_Classroom_ClkF_Leaving

label area_two_Classroom_ClkF_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor."

    jump area_two_Corridor_ClkFGym