# [DONE]

label area_one_Corridor_3A3B:
    scene bg areaone corridor
    with dissolve

    if not vb_a1_cor_3a3b_visited:
        $ vb_a1_cor_3a3b_visited = True

        narrator """As you make your way through the corridor you feel shivers running down your spine.

        You are moving away from the exit, hoping that you will finnaly find some help.
        """

        player """The exit is not this way... 

        Should I investigate the school or head right to the exit?
        """

        player_thinking "Another decision to make..."

    narrator """There are two sets of doors on the west and east wall each. They are labeled as classrooms.

    On the north you see the corridor split, to the south there's the exit."""

    menu:
        "Go north.":
            jump area_one_Corridor_AreatwoAreathree4B
        "Go south.":
            jump area_one_Corridor_Toilets2B
        "Enter classroom 3A.":
            jump area_one_Classroom_3A
        "Enter classroom 3B.":
            jump area_one_Classroom_3B