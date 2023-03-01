# [DONE]

label area_two_Corridor_4GGym:
    scene bg areatwo corridor

    

    if not vb_a2_cor_4ggym_visited:
        $ vb_a2_cor_4ggym_visited = True

        narrator """You make your way to the end of the corridor.

        The window that usually illuminates this place on warm spring days seems to be flooded with a brown, sticky substance.

        Trying to reach it, hoping to find a window beyond it, you feel the caustic vapors trying to break through your skin."""

        player "Oh that burns! I won't be able to reach that window..."

        narrator """You stare blankly at the sticky substance.

        It takes you a second to realise that this part of the corridor is used to move from the gym to the fitness class."""

    else:
        
        narrator """The sticky substance is still there, blocking the window.""""

    menu:
        "Go south.":
            jump area_two_Corridor_2GClkM4G
        "Enter room 4G.":
            jump area_two_Classroom_4G
        "Enter the gym.":
            jump area_two_Classroom_Gym_Entering_4ggym

label area_two_Classroom_Gym_Entering_4ggym:
    scene bg areatwo corridor

    narrator """You press the handle and it doesn't move.
    
    The door seems to be open, but blocked by something heavy on the other side."""

    player "They won't budge... Sighs... I need to find another way in."

    jump area_two_Corridor_4GGym