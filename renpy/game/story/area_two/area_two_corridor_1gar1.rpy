# [DONE]

label area_two_Corridor_1GAreaOne:
    scene bg areatwo corridor

    if not vb_a2_cor_1gar1_visited:
        $ vb_a2_cor_1gar1_visited = True
        
        narrator """You enter the hallway that leads to the gym. 
        
        The silence in this place seems less natural than in the first part of the school.
        
        During the day, this corridor is filled with the sounds of balls bouncing in the gym.
        
        The silence and darkness, dispersed by the found flashlight, make you shiver."""

        player_thinking """Ohh, I've never liked this corridor...
        
        It reminds me of pointless PE classes and boring meetings led by the principal.
        
        And now there was a show with those furries..."""

        narrator """As soon as you illuminated the further part of the corridor, you noticed how the hairy figure escaped through the door leading to the gymnasium.
        
        The thing seemed huge, but it made no sound."""

        player_thinking """Oh God, something is here!
        
        I really hope I don't have to enter the gym..."""

    else:
        narrator """You enter the hallway that leads to the gym.

        Here you noticed a strange figure in the distance."""

    menu:
        "Go west.":
            jump area_two_Corridor_2GClkM4G
        "Enter room 1G":
            jump area_two_Classroom_1G
        "Enter the main building.":
            jump area_one_Corridor_AreaTwo
