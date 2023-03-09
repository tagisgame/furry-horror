# [DONE]

label area_one_Corridor_A1LabExit:
    scene bg areaone corridor
    with dissolve

    if not vb_a1_cor_a1labexit_visited:
        $ vb_a1_cor_a1labexit_visited = True

        narrator """You rush to the exit as the feeling of exitement fills you up.

        You want to leave this place. Rushing to the doors and try to burst through them.

        As soon as you hit them you relize that they are closed. You bounce of them and land on the ground"""

    elif not vb_item_janitorKey:

            player_thinking "What..? The doors are closed?!"

            narrator """As soon as you get up you feel the cold breeze comming from the corridor.

            Looking back at the corridor you notice a shadow. A human like entity that seems to look at you.

            You rub your eyes and the shadow dissapears."""

            player_thinking """What the hell was that?? Am I halucinating...?

            I need to get out of here! But where I'll find the keys to this doors?"""

    elif vb_item_janitorKey:
        jump area_one_corridor_a1labexit_escape 
        

    elif not vb_item_janitorKey:

        player_thinking "There's the exit, but I can't open the doors."

    narrator "Apart from the exit, there are the entrances to the lab and a classroom."

    player_thinking "What to do now?"

    menu:
        "Go north.":
            jump area_one_Corridor_2A1BLab
        "Enter classroom 1A.":
            jump area_one_Classroom_1A
        "Enter the lab.":
            jump area_one_Classroom_Lab


label area_one_corridor_a1labexit_escape:

    narrator """You hurriedly check every key taken from the dead janitor.
            
    Every key seems to be the wrong one, your hands start to tangle."""

    player_thinking """Come on... Come on... I need to get out of here!"""

    narrator """You've already checked half of the keys when suddenly you heard a huge crack coming from the depths of the school.
            
    Apparently, the monster has already managed to break through the door and is now heading your way. 
            
    He wants blood...

    Instinctively, you turn towards the corridor and see how a huge, hairy beast crashes into it, banging against the wall.
            
    This thing is running towards you and you have a few keys left to check"""

    player """I've come this far I can't give up...
            
    C'mon OPEN THE FUCKING DOOR"""

    narrator """As if by some magic spell, the key you put in the lock turned and the door opened.
            
    Without thinking, you ran out of school and started running towards your home.
            
    The beast that was chasing you stopped in the doorway, howled shrilly and came back inside.
            
    You are safe now..."""

    tutorial """Congratulations!
            
    You've escaped the horrors of your school, now all you have to do is convince your parents to change it..."""