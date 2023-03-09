#piąty z lewej

label area_two_Classroom_3G:
    scene bg black
    with dissolve

    narrator "You enter the room labeled as 3G."

    scene bg areatwo classroom3g
    with dissolve

    if not vb_a2_cls_g3_visited:
        $ vb_a2_cls_g3_visited = True

        narrator """You enter the class for the drama club.
        
        This class is not adapted to lessons, and a large part of it is occupied by boxes with props.
        
        Some of them had to be moved to the gym, and the other is scattered around as if they were looking for something specific."""


    menu:
        "Inspect the room.":
            jump area_two_Classroom_3G_Inspecting
        "Leave through the eastern door.":
            jump area_two_Classroom_3G_LeavingE
        "Leave through the western door.":
            jump area_two_Classroom_3G_LeavingW

    else:

        narrator "You enter the class for the drama club."

    menu:
        "Inspect the room." if not vb_a2_cls_3g_inspected:
            jump area_two_Classroom_3G_Inspecting
        "Leave through the eastern door.":
            jump area_two_Classroom_3G_LeavingE
        "Leave through the western door.":
            jump area_two_Classroom_3G_LeavingW

area_two_Classroom_3G_Inspecting
    $ vb_a2_cls_3g_inspected = True

    narrator """You search through the other boxes, but these have nothing useful in them.
    
    You find several costumes of pirates, vikings or angels for nativity plays.
    
    When you open the last box you notice the head of a furry monster, whose fangs seem ready to sink into your neck."""

    player "Oh fuck!"

    narrator """You fall onto your back and recoil in horror, waiting for the monster to leap at you.
    
    This one, however, remains in the box.
    
    You decide to get up, you look in the box again.
    
    You realize it's just a mask, not a monster ready to throw itself down your throat."""

    player """Uhh... I guess I should have been braver...
    
    It's just a costume after all, it won't hurt me...
    
    Still, I don't want to be here."""

    menu:
        "Leave through the eastern door.":
            jump area_two_Classroom_3G_LeavingE
        "Leave through the western door.":
            jump area_two_Classroom_3G_LeavingW


label area_two_Classroom_ClkM_LeavingE:
    scene bg black
    with dissolve

    narrator "You use the eastern door."

    jump area_two_Corridor_3G

label area_two_Classroom_ClkM_LeavingW:
    scene bg black
    with dissolve

    narrator "You use the western door."

    jump area_two_Corridor_3GGym