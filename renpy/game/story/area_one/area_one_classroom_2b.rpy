# [DONE]

label area_one_Classroom_2B:
    scene bg black
    with dissolve

    scene bg areaone classroom

    if not vb_a1_cls_2b_visited:
        $ vb_a1_cls_2b_visited = True

        narrator """You enter one of many classrooms in this school.

        Weirdly enough the windows are bricked up, yet you remember that once or twice you sneaked from the school through them. 

        The teacher's chairs seems to be broken. There are some parts laying on the ground."""

        menu:
            "Check the chair.":
                jump area_one_Classroom_2B_CheckChair
            "Keep looking around.":
                pass
        
        narrator  """At the back of the class you see several cabinets. They seem to contain inessential for you items.

        On the walls you can see posters with mathematic equations. You shudder as they made you remember about math.

        All you can remember is that if you don't remember what to do \"you are discriminant\".

        Apart from that the class seems to be properly cleaned, everything but teacher's chair is in it's place"""

        menu:
            "Check the chair.":
                jump area_one_Classroom_2B_CheckChair
            "Leave.":
                jump area_one_Corridor_Toilets2B

    elif not vb_a1_cls_2b_chair_checked:
        narrator """An ordinary classroom that reminds you of countless hours spent pretending to be a diligent student.

        That broken chair is still there."""

        menu:
            "Check the chair.":
                jump area_one_Classroom_2B_CheckChair
            "Leave.":
                jump area_one_Corridor_Toilets2B
    
    elif not vb_item_screwdriver:
        narrator """An ordinary classroom that reminds you of countless hours spent pretending to be a diligent student.

        Under the teacher's chair still lies the screwdriver."""

        menu:
            "Pick up the screwdriver.":
                jump area_one_Classroom_2B_PickUpScrewdriver
            "Leave.":
                jump area_one_Classroom_2B_Leaving

    else:
        narrator "An ordinary classroom that reminds you of countless hours spent pretending to be a diligent student."

    menu:
        "Leave.":
            jump area_one_Classroom_2B_Leaving

label area_one_Classroom_2B_CheckChair:
    $ vb_a1_cls_2b_chair_checked = True

    narrator """You approach the teacher's chair and you notice that it has a few loose screws.

    It looks like someone tried to pull a prank on the math teacher. 

    The plan must have failed since the chair is holding up so-so and the screwdriver is still there."""

    player_thinking """What a lame prank... 

    If I were here to help them it would be something much better!"""

    menu:
        "Pick up the screwdriver.":
            jump area_one_Classroom_2B_PickUpScrewdriver
        "Leave.":
            jump area_one_Classroom_2B_Leaving

label area_one_Classroom_2B_PickUpScrewdriver:
    $ vb_item_screwdriver = True
    narrator "You obtained the {b}screwdriver{/b}."

    player_thinking "Okay, now that I've got it, what is my next move?"

    menu:
        "Leave.":
            jump area_one_Classroom_2B_Leaving

label area_one_Classroom_2B_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the classroom to a corridor."
    
    jump area_one_Corridor_Toilets2B