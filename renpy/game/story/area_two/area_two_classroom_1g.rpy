# [To check - done]
label area_two_Classroom_1G:
    scene bg black
    with dissolve

    narrator "You enter the room labeled as 1G."

    scene bg areatwo classroom1g
    with dissolve

    if not vb_a2_cls_1g_visited:
        $ vb_a2_cls_1g_visited = True

        narrator """You notice that in this room is flooded.
        
        Your sneakers got slightly soaked."""

        menu:
            "Leave.":
               jump area_two_Classroom_1G_Leaving
         "Go to room 1G.":
                jump area_two_Classroom_1G_GoTo2G
          "Inspect the room thoroughly.":
                jump area_two_Classroom_1g_Inspect


label area_two_Classroom_1g_Inspect
    scene bg areatwo classroom1g

    if not vb_a2_cls_1g_inspected:
    

        narrator """Your first instinct is to check for the liquid that covers the entire floor.
    
        Reluctantly, you bend down and reach out to touch it.
    
        Is it blood? Or maybe some other goo...?"""

        player_thinking "Wait... It's just plain water!"

        narrator """You look up and notice a stockpile of five-gallon water bottles in the corner of the room.
    
        They seem to be torn apart, as if someone or something has sunk its huge, sharp claws into each of them in anger.
    
        You're just wondering how that water didn't get out of this room..."""

        player_thinking """Is this even possible? This room is not lower than the others, it doesn't even have threshold to stop the water...
     
        And why they store the water here... Near a computer!
    
        I could use it..."""

                menu
            "Leave.":
                jump area_two_Classroom_1G_Leaving
            "Go to room 1G.":
                jump area_two_Classroom_1G_GoTo2G
            "Check the computer.":
                jump area_two_Classroom_1G_Computer

    else:

        narrator "There is nothing interesting left in this room."

                menu
            "Leave.":
                jump area_two_Classroom_1G_Leaving
            "Go to room 1G.":
                jump area_two_Classroom_1G_GoTo2G




label area_two_Classroom_1G_Computer
    $ vb_a2_cls_1g_inspected = True

    if not vb_item_gloves:

        player_thinking """Hmm... Quite an old computer, probably Windows 95...
        
        The power strip is off, I have to turn it on."""

        narrator """As soon as you press the switch, you notice that the cable running from the power strip is damaged.
        
        You don't have time to react and you see a huge spark jump into your hand and the strip itself starts to burn.
        
        The dose of electricity you took surprisingly turned out to be lethal, your electrocuted body trembles, and the room bursts into flames."""

    else:
        player_thinking """Hmm... Quite an old computer, probably Windows 95...
        
        The power strip is off, I have to turn it on.
        
        But it's soaked in water... I should put on those anti-surge gloves for safety."""

        narrator """As soon as you press the switch, you notice that the cable running from the power strip is damaged. 
        
        You notice how a huge spark jumps on the power strip and you hear a loud crack.
        
        Your gloves certainly saved your life, but the power strip is blown and the computer is out of power."""

        player_thinking "Shit... I should have foreseen it..."


    menu:
        "Leave.":
            jump area_two_Classroom_1G_Leaving
        "Go to room 1G.":
            jump area_two_Classroom_1G_GoTo2G

label area_two_Classroom_1G_Leaving:
    scene bg black
    with dissolve

    narrator "You leave the room to a corridor."

    jump area_two_Corridor_1GAreaOne

label area_two_Classroom_1G_GoTo2G:
    scene bg black
    with dissolve

    narrator "You leave the room via door leading to room 2G."

    jump area_two_Classroom_2G