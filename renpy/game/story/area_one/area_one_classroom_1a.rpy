label area_one_Classroom_1A:
    scene bg black
    with dissolve

    narrator "You entered the classroom."

    scene bg areaone classroom
    with dissolve

    if not vb_a1_cls_1a_visited:
        $ vb_a1_cls_1a_visited = True

        narrator """You enter the darkest room you have encountered so far.

        The moment you stepped through the door they slammed behind you.

        You try to reach for the doorknob, but your hand touched the wall. 

        You are unable to feel the door and the wall feels sticky as if something is running down its walls.

        Suddenly, a light came on at the other end of the room. 

        It was very dim, illuminating only the space around it.

        You realise that the classroom transformed into a dark theater.

        Watching in terror you notice the furry characters from the play came to life on stage.

        But instead of dancing and singing, they are growling and snarling, their eyes fixed on you.

        You try to escape, but the furry characters pinned you to the wall.

        They are vicious predators, and they had set their sights on you.

        Lunging at you, their claws tear into your flesh.

        As soon as you start screaming the vision unfolds and you are back in the normal classroom."""

        player """What...

        The fu...

        WHAT WAS THAT?!

        I DON'T WANT TO STAY HERE"""

        narrator """You feel your heart pounding.

        You tremble in fear as you nervously look for the door the escape the room.

        You notice that there are two of them."""

    else:
        narrator "You still remember the terrifying vision with furries in theatre"

        player_thinking "Oh hell nah, I'm not staying in that class."

    menu:
        "Leave.":
            jump area_one_Classroom_1A_Leaving
        "Go to classroom 2A.":
            jump area_one_Classroom_1A_GoTo2A

label area_one_Classroom_1A_Leaving:
    scene bg black
    with dissolve

    narrator "You decide to leave the room to a corridor."

    jump area_one_Corridor_A1LabExit

label area_one_Classroom_1A_GoTo2A: 
    scene bg black
    with dissolve

    narrator "You decide to go to the room 2A."

    jump area_one_Classroom_2A