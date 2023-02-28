label area_two_Corridor_ClkFGym:
    scene bg areatwo corridor

    if not vb_a2_cor_clkfgym_visited:
        $ vb_a2_cor_clkfgym_visited = True

        #1

    else:
        #kolejne

    menu:
        "Go West.":
            jump area_two_Corridor_3G
        "Go East.":
            jump area_two_Corridor_2GClkM4G
        "Enter the female cloakroom.":
            jump area_two_Classroom_ClkF
        "Enter the gym.":
            jump area_two_Classroom_Gym