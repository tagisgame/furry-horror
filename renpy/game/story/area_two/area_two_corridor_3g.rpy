label area_two_Corridor_3G:
    scene bg areatwo corridor

    if not vb_a2_cor_3g_visited:
        $ vb_a2_cor_3g_visited = True

        #1


    menu:
        "Go west.":
            jump area_two_Corridor_3GGym
        "Go east.":
            jump area_two_Corridor_ClkFGym
        "Enter room 3G.":
            jump area_two_Classroom_3G