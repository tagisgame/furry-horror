label area_two_Classroom_Gym:
    scene bg black
    with dissolve

    narrator "You enter the gym."

    scene bg areatwo gym
    with dissolve

    if not vb_a2_cls_gym_visited:
        $ vb_a2_cls_gym_visited = True

        #pierwsze wejscie

    menu:
        "Leave through the north-eastern door.":
            jump area_two_Classroom_Gym_LeavingNE
        "Leave through the south-eastern door.":
            jump area_two_Classroom_Gym_LeavingSE
        "Leave through the south-western door.":
            jump area_two_Classroom_Gym_LeavingSW

label area_two_Classroom_Gym_LeavingNE:
    scene bg black
    with dissolve

    narrator "You leave the gym through the north-eastern door."

    jump area_two_Corridor_4GGym

label area_two_Classroom_Gym_LeavingSE:
    scene bg black
    with dissolve

    narrator "You leave the gym through the south-eastern door."

    jump area_two_Corridor_ClkFGym

label area_two_Classroom_Gym_LeavingSW:
    scene bg black
    with dissolve

    narrator "You leave the gym through the south-western door."

    jump area_two_Corridor_3GGym