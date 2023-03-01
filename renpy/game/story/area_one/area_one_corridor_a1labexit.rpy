# [DONE]

label area_one_Corridor_A1LabExit:
    scene bg areaone corridor
    with dissolve

    if not vb_a1_cor_a1labexit_visited:
        $ vb_a1_cor_a1labexit_visited = True

        narrator """You rush to the exit as the feeling of exitement fills you up.

        You want to leave this place. Rushing to the doors and try to burst through them.

        As soon as you hit them you relize that they are closed. You bounce of them and land on the ground"""

        player_thinking "What..? The doors are closed?!"

        narrator """As soon as you get up you feel the cold breeze comming from the corridor.

        Looking back at the corridor you notice a shadow. A human like entity that seems to look at you.

        You rub your eyes and the shadow dissapears."""

        player_thinking """What the hell was that?? Am I halucinating...?

        I need to get out of here! But where I'll find the keys to this doors?"""

    else:
        player_thinking "There's the exit, but I can't open the doors."

    narrator "Apart from the exit, there are the entrances to the lab and a classroom."

    player_thinking "What to do now?"

    menu:
        "Go north.":
            jump area_one_Corridor_2A1BLab
        "Enter classroom 1A.":
            jump area_one_Classroom_1A
        "Enter the lab."
            jump area_one_Classroom_Lab