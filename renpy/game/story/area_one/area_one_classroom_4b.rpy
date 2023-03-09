label area_one_Classroom_4B:
    scene bg black
    with dissolve

    narrator "You enter classroom 4B."

    scene bg areaone classroom
    with dissolve

    narrator "You're inside a regular classroom."

    player_thinking "I'm not sure what I'm even looking for here."

    narrator """You take a quick look around the room, but there is in fact nothing to be found.

    What are you about to do now?"""

    menu:
        "Leave.":
            jump area_one_Classroom_4B_Leaving
        "Go to room 3B.":
            jump area_one_Classroom_4B_GoTo3B

label area_one_Classroom_4B_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the classroom to the corridor."

    jump  area_one_Corridor_AreatwoAreathree4B

label area_one_Classroom_4B_GoTo3B:
    scene bg black
    with dissolve

    narrator "You go through the door leading to another room."

    jump  area_one_Classroom_3B