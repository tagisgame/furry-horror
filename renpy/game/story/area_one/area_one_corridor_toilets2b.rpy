# [DONE]

label area_one_Corridor_Toilets2B:
    scene bg area one corridor
    with dissolve

    if not vb_a1_cor_toilets2b_visited:
        $vb_a1_cor_toilets2b_visited = True

        narrator """Your curiosity seems to be stronger than your fear. You hesitantly go out into the corridor.

        Everything seems fine, only the silence seems unnatural.

        You are able to sense a strange presence, even though the corridors are empty. As if someone, or something, is watching you."""
    
        narrator """In front of you there is a classroom labeled as 2B. To the south you see the exit you use everyday to get in and out.

        To the north are more classrooms, and at the end of the corridor it seems to split."""

    else:
        narrator """There is an entrance to the classroom labeled as 2B and door to the toilets. To the south you see the exit.

        To the north are more classrooms, and at the end of the corridor it seems to split."""
        
    player_thinking "Hmm... Where to now?"

    menu:
        "Enter classroom 2B.":
            jump area_one_Classroom_2B
        "Enter the toilets.":
            jump area_one_Toilets
        "Go north.":
            jump area_one_Corridor_3A3B
        "Go south.":
            jump area_one_Corridor_2A1BLab