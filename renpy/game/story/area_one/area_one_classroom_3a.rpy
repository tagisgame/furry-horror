# [DONE]

label area_one_Classroom_3A:
    scene bg black
    with dissolve

    narrator "You enter the classroom of everyone's favourite teacher - Mrs. Garlick."

    scene bg areaone classroom
    with dissolve

    if not vb_a1_cls_3a_visited:
        $ vb_a1_cls_3a_visited = True

        narrator """She's a rather weird persona that prides herself on her survival skills.

        No one would ever suspect her of such abilities because she looks like a frail woman.
        
        It's an ordinary class like many in this school. 

        Empty desks seem to wait patiently for students, the board is ready to be written on regarding the next lesson...

        Only the teacher's desk catches your attention - on it you find a handbag that seems to belong to Mrs. Garlick."""

        menu:
            "Take a closer look.":
                jump area_one_Classroom_3A_InspectBag
            "Leave.":
                jump area_one_Classroom_3A_Leaving

    elif not vb_item_flashlight:
        narrator "You enter Mrs. Garlick class that you had only glanced at before."

        player_thinking "That handbag on the desk is bugging me..."

        menu:
            "Take a closer look.":
                jump area_one_Classroom_3A_InspectBag
            "Leave.":
                jump area_one_Classroom_3A_Leaving

    else:
        narrator "You enter Mrs. Garlick class where you found the strongest flashligh on earth. At least you think it is."

        menu:
            "Leave.":
                jump area_one_Classroom_3A_Leaving

label area_one_Classroom_3A_InspectBag:
    $ vb_item_flashlight = True

    narrator """You search the bag, hoping to find something useful. It's a woman's handbag, after all...

    Among various lipsticks, handkerchiefs, an empty wallet, and a comb, you find a small flashlight.

    You turn it on by directing the beam of light directly into your eyes, and it turns out to be stronger than you expected."""

    player "Ouch!"

    player_thinking """Wasn't expecting it to be THAT STRONG.

    It literally illuminates the whole class!"""

    menu:
        "Leave.":
            jump area_one_Classroom_3A_Leaving

label area_one_Classroom_3A_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room through the only door."

    jump area_one_Corridor_3A3B