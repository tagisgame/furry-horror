# [DONE]

label area_one_Corridor_2A1BLab:
    scene bg areaone corridor
    with dissolve

    if not vb_a1_cor_2a1blab_visited:
        $ vb_a1_cor_2a1blab_visited = True

        narrator "You are getting closer to the exit. A sweet feeling of relief starts to displace your fear"

    narrator """There are three classrooms that you can go in from here.

    One of them is a science lab."""

    if not vb_a1_cor_2a1blab_visited:
        player_thinking """This week there was no class in science lab yet.

        I wonder how the lab looks like when it's unused"""

    player_thinking "What now?"

    menu:
        "Go north.":
            jump area_one_Corridor_Toilets2B
        "Go south.":
            jump area_one_Corridor_A1LabExit
        "Enter classroom 2A.":
            jump area_one_Classroom_2A
        "Enter classroom 1B.":
            jump area_one_Classroom_1B
        "Enter the lab.":
            jump area_one_Classroom_Lab