# [DONE]

label area_one_Classroom_1B:
    scene bg areaone classroom
    with dissolve

    if not vb_a1_cls_1b_visited:
        $ vb_a1_cls_1b_visited = True

        narrator """This classroom was assigned to the sports class.

        Even though they left hours ago, you can still smell the mixture of 
        deodorant and sweat.

        You remember a small quarrel between the students and the principal concerning the windows in this class.

        The students wanted to keep them open after their physical education lessons, and the principal was againt it. Especially during the winter,

        After all the principal won and ordered to put in lockable windows that only teachers had keys to."""

        player_thinking "Should I take a better look at the room?"

        menu:
            "Take a look around.":
                jump area_one_Classroom_1B_LookAround
            "Leave.":
                jump area_one_Corridor_2A1BLab

    elif not vb_a1_cls_1b_investigated:
        narrator "You enter the sports class room. It might contain something interesting."

        menu:
            "Take a look around.":
                jump area_one_Classroom_1B_LookAround
            "Leave.":
                jump area_one_Corridor_2A1BLab
    
    elif not vb_item_gymkey:
        narrator "You enter the sports class room with the closed file cabinet. It might hide something interesting"

        jump area_one_Classroom_1B_OpenMenu

    else:
        narrator """You enter the sports class room. 

        You searched it previously and found a key to the gym."""

        menu:
            "Leave.":
                jump area_one_Corridor_2A1BLab
    
label area_one_Classroom_1B_LookAround:
    narrator """After examining the room you notice a few file cabinets that pick your attention.

    Searching them you find various documents concerning every single competition the sports class took part.

    Among these files you find school diary. A tempting opportunity to mess with the bullies from this class.

    However you are more interested in the last cabinet.

    As you try to open it you realise it is locked."""

    player_thinking """Hmm... There must be something interesting in here.

    But how do I open it?"""

    jump area_one_Classroom_1B_OpenMenu

label area_one_Classroom_1B_OpenMenu:
    if vb_item_screwdriver and vb_item_1bkey:
        menu:
            "Use a screwdriver to open the cabinet.":
                jump area_one_Classroom_1B_UseScrewdriver
            "Try the key on the cabinet.":
                jump area_one_Classroom_1B_UseKey
            "Force the cabinet open.":
                jump area_one_Classroom_1B_UseForce
            "Leave it.":
                jump area_one_Classroom_1B_UseNothing
    
    elif vb_item_screwdriver:
        menu:
            "Use a screwdriver to open the cabinet.":
                jump area_one_Classroom_1B_UseScrewdriver
            "Force the cabinet open.":
                jump area_one_Classroom_1B_UseForce
            "Leave it.":
                jump area_one_Classroom_1B_UseNothing

    elif vb_item_1bkey:
        menu:
            "Try the key on the cabinet.":
                jump area_one_Classroom_1B_UseKey
            "Force the cabinet open.":
                jump area_one_Classroom_1B_UseForce
            "Leave it.":
                jump area_one_Classroom_1B_UseNothing

    else:
        menu:
            "Force the cabinet open.":
                jump area_one_Classroom_1B_UseForce
            "Leave it.":
                jump area_one_Classroom_1B_UseNothing

label area_one_Classroom_1B_UseScrewdriver:
    $ vb_item_gymkey = True

    player_thinking """I can use this screwdriver to unscrew the doors. 

    It's not a perfectly secure cabinet if I can do this..."""

    narrator """Unscrewing the few screws allows you to repeal the cabinets doors.

    You put your hand inside, trying to find something useful.

    After a while you are able to feel a smal item inside.

    You instinctively grab it and you take your hand out of the file cabinet.

    Now you're holding a key with a rugby ball keychain in your hand"""

    player_thinking "Hey, that's the key the P.E. teacher uses to let us in into the gym!"

    narrator "You get the {b}key to the gym{/b}."

    menu:
        "Leave.":
            jump area_one_Corridor_2A1BLab

label area_one_Classroom_1B_UseKey:
    $ vb_item_gymkey = True

    narrator """Keeping in mind the found key, you check if it matches the lock.

    You turn the key and the cabinet opens.

    Weirdly enough it is almost empty, the only thing that was protected by the lock was another key.

    You reach out for him and notice that it has a rugby ball keychain"""

    player_thinking "Hey, that's the key the P.E. teacher uses to let us in into the gym!"

    narrator "You get the {b}key to the gym{/b}."

    menu:
        "Leave.":
            jump area_one_Corridor_2A1BLab

label area_one_Classroom_1B_UseForce:
    $ vb_item_gymkey = True
    $ vb_state_injured = True
    narrator """The cabinet seems flimsy enough that you would be able to force it open.

    You shove your hands in the gap between the door and the rest of the cabinet.

    You strain your frail muscles, tense your whole body until the door finally bursts open.

    The door swung unluckily and its sharp metal corner grazed your cheek, leaving a huge gash."""

    player "FUCK! Oh my God that hurts so bad!"

    narrator """As you scream in pain you cheek starts to bleed profusely. 

    Trying to stop the bleeding, you hold your wound with your hand, look at the contents of the cupboard and notice one item: keys with a rugby ball keychain.

    You grab the key and hear some sort of howling comming from the depths of the school."""

    narrator "You get the {b}key to the gym{/b}."

    player_thinking """What the hell is that?

    We\'ve got no animals in school... The howling must come from outside.

    I hope so..."""

    menu:
        "Leave.":
            jump area_one_Corridor_2A1BLab

label area_one_Classroom_1B_UseNothing:
    menu:
        "Leave.":
            jump area_one_Corridor_2A1BLab
        "Open the cabinet.":
            jump area_one_Classroom_1B_OpenMenu