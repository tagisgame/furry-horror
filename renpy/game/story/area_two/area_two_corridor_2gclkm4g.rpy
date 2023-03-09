# [DONE]

label area_two_Corridor_2GClkM4G:
    scene bg areatwo corridor

    if not vb_a2_cor_2gclkm4g_visited:
        $ vb_a2_cor_2gclkm4g_visited = True

        narrator """You go deeper into the corridor and the air becomes colder.
        
        The darkness seems to be unnaturally greater and your flashlight is no longer able to illuminate the entire corridor."""

        player_thinking """How is that even possible?

        I took only a few steps and the flashlight does not illuminate anything... 
        
        As if there was only the floor in front of me and nothing else."""
    
    else:

        narrator "You come to a place where the flashlight unnaturally loses its power."

    menu:
        "Go north.":
            jump area_two_Corridor_4GGym
        "Go east.":
            jump area_two_Corridor_1GAreaOne
        "Go west.":
            jump area_two_Corridor_ClkFGym
        "Enter room 2G.":
            jump area_two_Classroom_2G
        "Enter the male cloakroom.":
            jump area_two_Classroom_ClkM
        "Enter room 4G.":
            jump area_two_Classroom_4G