# [DONE]

label area_two_Classroom_Gym:
    scene bg black
    with dissolve

    narrator "You enter the gym."

    scene bg areatwo gym
    with dissolve

    if not vb_a2_cls_gym_visited:
        
        $ vb_a2_cls_gym_visited = True

        narrator """You slowly and carefully enter the gym. Terrified, you look out for some furry monster.
        
        However, you exit to a separate part of the gym intended for the backstage of the performance.
        
        The blood-red light you saw through the door was from the theater lights that someone hadn't turned off.
        
        All the props are neatly arranged, but on the ground there are a few scraps of furry outfits you saw on stage."""

        player_thinking """Oh my... I really hope that's only the suit, not the actor...
        
        Well, there is no blood so..."""

        narrator """As you contemplate over the remnants of the outfit you hear some growling and scratching...
        
        In the gym, sound travels very well, and its source is somewhere on the other side.
        
        You peek through the curtain and notice a furry figure, the same you saw when you lit the corridor."""

        player_thinking """ Shiet... What the hell is that..."""

        narrator """The figure is busy at the door, as if eating something. Or someone...
        
        You look around the gym and notice that there is a body on one of the dozens of chairs lined up for the show.

        You watch him from a distance and recognize the outfit - the janitor's favorite shirt, his blue work trousers."""

        player_thinking """Oh no... Poor Mr. Flynn... He was supposed to retire next year...
        
        Hey, wait! He should have the keys to this shithole!
        
        I need to get close..."""


        menu:
            "Approach the janitor's body.":
                jump area_two_Classroom_Gym_Janitor
            "Leave through the backstage doors.":
                jump area_two_Classroom_Gym_BSDoors


label area_two_Classroom_Gym_BSDoors:

    if not vb_item_janitorKey:

        narrator "You cowardly leave the gym."
        jump area_two_Corridor_3GGym

    else:

        narrator "You escape the creature just in time. Now is the time to escape the school."
        jump area_two_Corridor_3GGym

label area_two_Classroom_Gym_Janitor:

    narrator """You slowly slide between the chairs so that you can hide behind them if necessary.
    
    You slowly approach the janitor's body, and the sounds of the furry monster became more human...
    
    The position of the janitor's body suggests that he may just be sleeping.
    
    However, his skinless face, torn jaw and bulging eyes effectively convince that he is dead.
    
    It seems as if the furry figure, who is now only a few meters away from you, is muttering something under his breath.
    
    After listening, you managed to understand only a few words, something about eating his friend, begging for mercy and crying."""


    menu:
        "Take the keys.":
            jump area_two_Classroom_Gym_Janitor_Keys
        "Approach the monster":
            jump area_two_Classroom_Gym_Monster

label area_two_Classroom_Gym_Monster:

    narrator "You slowly stand up and try to reach the monster."

    player "Hello? Do you need help?"

    narrator """You barely had time to ask a question when the furry monster turned to you.
    
    His fangs were dripping with blood, his claws have leftovers on them from the wretch that was the monster's meal.
    
    You didn't even have time to think, try to run away or defend yourself.
    
    The monster lunged at you, grafted its huge paws into your mouth, and with all its might ripped your jaw off, now barely holding on to the remnants of your cheeks.
    
    He grabbed your head with one hand, digging his thumb with a long and sharp claw into your eye.
    
    With the last of your strength, you were able to see, and certainly feel, his other hand sink into your chest, rip your heart out of you and obscenely drink your warm, freshly oxygenated blood."""


    tutorial """For the record...
    
    {i}This is the death screen{i} {w} You can go back to the last decision, or start over."""

    $ vb_a2_cls_gym_visited = False
    $ vb_item_janitorKey = False

    menu:
        "Revert my decision.":
            jump area_two_Classroom_Gym
        "Start over.":
            jump game_start

label area_two_Classroom_Gym_Janitor_Keys:

    $ vb_item_janitorKey = True

    narrator """You grab the janitor's keys, slowly unfasten them from his belt - not so as not to make a noise, but because your hands are shaking with stress like never before.
        
    The keychain is quite large and the keys are not marked - it will take a while to find the right one.
        
    However you know that it will be safer to check them at the door itself, away from this creature.
        
    You remember that the gym has three exits.
        
    One is guarded by a monster, the other - the one you entered with - is on the other side, and the third one very close to you is blocked by a chair."""

    menu:
        "Escape through backstage door.":
            jump area_two_Classroom_Gym_Escape_Backstage
        "Escape through blocked door":
            jump area_two_Classroom_Gym_Escape_BlockedDoor


label area_two_Classroom_Gym_Escape_Backstage:

    narrator """Having taken the keys from the janitor, you begin to slowly backtrack to the door behind the backstage.
    
    The road to them is longer, but something tells you that it is much safer.
    
    After all, you don't have to walk past the monster.
    
    When you are a few steps away from the backsatee, you want to speed up, but your clumsiness takes its toll.
    
    You trip over one of the chairs and land on the ground with a huge clatter.
    
    The monster that has been eating something on the other side turns to you.
    
    He noticed you instantly and lunged at you with a shrill roar, baring his fangs.
    
    You made a run for it, ran across the stage, dodging between the sets you dashed for the door, almost feeling the beast's breath on your neck.
    
    At the last moment you managed to close the door behind you and turn the key.
    
    The beast pressed its whole body against the door, trying to force it open, but somehow it held strong."""
    
    player "Fuck, that was close... I need to get out of this place"

    jump area_two_Corridor_3GGym

label area_two_Classroom_Gym_Escape_BlockedDoor:

    if not vb_state_injured:

        narrator """You start sneaking towards the locked door.
        
        Everything goes smoothly as the monster seems to be busy eating his meal.
        
        You finally reach the door, trying not to make any noise, you push aside the chair blocking it and open it.
        
        You manage to silently walk out into the hallway, close the door behind you, and feel immensely relieved."""

        jump area_two_Corridor_4GGym

    else:

        narrator """You start sneaking towards the locked door.
        
        Everything goes smoothly, but suddenly the monster jumps up and you freeze in horror.
        
        You see how the furry figure start to sniff around as if it smelled something tasty.
        
        At that moment, you remember your cut on your cheek and blood dripping from it.
        
        The monster sensed your presence and turned to you, ready to attack.
        
        You run to the door hearing the monster bump into chairs behind you.
        
        You reach the door, kick the chair over and reach for the handle.
        
        Suddenly you feel a strange feeling in your stomach.
        
        You look down and see the monster's hand holding a piece of your spine go right through.
        
        The last thing you feel is the monster's fangs sinking into your neck."""

        tutorial """For the record...
    
        {i}This is the death screen{i} {w} You can go back to the last decision, or start over."""

        $ vb_a2_cls_gym_visited = False
        $ vb_item_janitorKey = False

        menu:
            "Revert my decision.":
                jump area_two_Classroom_Gym
            "Start over.":
                jump game_start

