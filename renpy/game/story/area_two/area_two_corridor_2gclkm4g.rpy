label area_two_Corridor_2GClkM4G:
    scene bg areatwo corridor

    if not vb_a2_cor_2gclkm4g_visited:
        $ vb_a2_cor_2gclkm4g_visited = True

        #1 wejscie

    menu:
        "Go north.":
            jump area_two_Corridor_4gGym
        "Go west.":
            jump area_two_Corridor_1GAreaOne
        "Go east.":
            jump area_two_Corridor_ClkFGym
        "Enter room 2G.":
            jump area_two_Classroom_2G
        "Enter the male cloakroom.":
            jump area_two_Classroom_ClkM
        "Enter room 4G.":
            jump area_two_Classroom_4G