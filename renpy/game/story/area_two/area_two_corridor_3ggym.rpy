# [DONE]

label area_two_Corridor_3GGym:
    scene bg areatwo corridor


    if not vb_a2_cor_3ggym_visited:
        $ vb_a2_cor_3ggym_visited = True

        narrator """You come to the end of the hall, where are another doors to the gym.
        
        A faint, blood-red light emanates from beneath them.

        No sound seems to come from inside, but nothing is heard throughout the school either."""

        player_thinking "That looks sinister... Maybe I can find something useful outside the gym..."
        
    else:
        
        
        narrator "You come to the end of the hall with a faint, blood-red light emanating from beneath the gym doors."

    menu:
        "Go west.":
            jump area_two_Corridor_3G
        "Enter room 3G.":
            jump area_two_Classroom_3G
        "Enter the gym.":
            jump area_two_Classroom_Gym_Entering_3ggym

label area_two_Classroom_Gym_Entering_3ggym:
    scene bg areatwo corridor

    if not vb_item_gymkey:

        narrator """You try to open the door, calmly pressing the handle. 
    
        The door does not move despite your attempt to open it"""

        player_thinking "Damn, they are closed... I must find the key if I want to enter."

        jump area_two_Corridor_3GGym

    else

        narrator """You open the door with the key you found previously.

        You open them slowly and slide into the gym."""

        jump area_two_Classroom_Gym