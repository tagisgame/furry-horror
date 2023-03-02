label area_two_Corridor_4GGym:
    scene bg areatwo corridor

    if not vb_a2_cor_4ggym_visited:
        $ vb_a2_cor_4ggym_visited = True

        #1


    menu:
        "Go south.":
            jump area_two_Corridor_2GClkM4G
        "Enter room 4G.":
            jump area_two_Classroom_4G
        "Enter the gym.":
            jump area_two_Classroom_Gym
