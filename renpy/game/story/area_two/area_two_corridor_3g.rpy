# [DONE]

label area_two_Corridor_3G:
    scene bg areatwo corridor

    if not vb_a2_cor_3g_visited:
        $ vb_a2_cor_3g_visited = True

        narrator "You go further into the corridor."

        player_thinking "Hmm... That's the place where those two other students talked about domestic violence..."

    else:
        
        narrator "You go further into the corridor."

    menu:
        "Go west.":
            jump area_two_Corridor_3GGym
        "Go east.":
            jump area_two_Corridor_ClkFGym
        "Enter room 3G.":
            jump area_two_Classroom_3G