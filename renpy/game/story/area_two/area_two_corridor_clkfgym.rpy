# [DONE]

label area_two_Corridor_ClkFGym:
    scene bg areatwo corridor

    if not vb_a2_cor_clkfgym_visited:
        $ vb_a2_cor_clkfgym_visited = True

        narrator """Making your way further into the corridor you stumble upon the first door to the gym.
        
        This is the door mysterious figure used to escape."""

        player_thinking """I'm not sure if I want to enter the gym...
        
        Especially through THAT door."""

    else:
        
        narrator "You enter the part of the corridor with the doors used by the creature."

    menu:
        "Go west.":
            jump area_two_Corridor_3G
        "Go east.":
            jump area_two_Corridor_2GClkM4G
        "Enter the female cloakroom.":
            jump area_two_Classroom_ClkF
        "Enter the gym." if not vb_item_janitorKey:
            jump area_two_Classroom_Gym_Entering_clkfgym

label area_two_Classroom_Gym_Entering_clkfgym:
    scene bg areatwo corridor

    narrator """You lightly press the handle and open the door.
    
    You see your gym covered in carpets and hundreds of chairs...
    
    ...apparently no one has cleaned up after the show.
    
    You hesitantly take the first step to go inside.
    
    Suddenly a huge, hairy figure appears in front of you.
    
    You can't see its face, or rather the muzzle, but the figure's fangs gleam snow-white.

    You try to scream but your mouth makes no sound.

    It takes you a moment to realize that the mysterious figure has dug its claws deep into your throat.

    You begin to choke on your own blood, all strength leaves your body, which falls limply to the ground.

    Your flashlight rolls on the ground, pointing its beam at you, blinding you one last time"""

    tutorial """For the record...
    
    {i}This is the death screen{i} {w} You can go back to the last decision, or start over."""

    $ vb_a2_cor_clkfgym_visited = False

    menu:
        "Revert my decision.":
            jump area_two_Corridor_ClkFGym
        "Start over.":
            jump game_start