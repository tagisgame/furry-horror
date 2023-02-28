label area_two_Corridor_1GAreaOne:
    scene bg areatwo corridor

    if not vb_a2_cor_1gar1_visited:
        $ vb_a2_cor_1gar1_visited = True

        # Pierwsze wejście
    
    else:
        #kolejne wejścia

    menu:
        "Go west.":
            jump area_two_Corridor_2GClkM4G
        "Enter room 1G":
            jump area_two_Classroom_1G
        "Enter the main building.":
            jump area_one_Corridor_AreaTwo
