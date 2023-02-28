label area_two_Corridor_3GGym:
    scene bg areatwo corridor

    if not vb_a2_cor_3ggym_visited:
        $ vb_a2_cor_3ggym_visited = True

        #1
    
    else:
        #kol

    menu:
        "Go west.":
            jump area_two_Corridor_3G
        "Enter room 3G.":
            jump area_two_Classroom_3G
        "Enter the gym.":
            jump area_two_Classroom_Gym