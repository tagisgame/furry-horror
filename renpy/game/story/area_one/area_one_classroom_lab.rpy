# [DONE]

label area_one_Classroom_Lab:
    scene bg black
    with dissolve

    narrator "You enter the school's science lab."

    scene bg areaone lab
    with dissolve

    if not vb_a1_cls_lab_visited:
        $ vb_a1_cls_lab_visited = True

        narrator """As you enter the class you are hit with strong smell of chemicals.

        The smell makes you nauseous, however, you overcome your reflexes and keep a sharp mind.

        After a quck glance you notice that the class has two set of doors and the windows are blocked with metal bars.

        Only soft moonlight illuminates the room"""

        player_thinking "Why does it looks so creepy..."

        narrator """The laboratory reminds you of the interior of lunatic asylums you saw in countless horrors. 

        You never noticed that similarity until you had a chance to visit this class in almost pure darkness.

        Looking around you notice some flasks on the teacher's desk.

        It seems like several of them contain some kind of liquids.

        Maybe the teacher was about to conduct an experiment, but the lesson finished?"""

        menu:
            "Examine the flasks.":
                jump area_one_Classroom_Lab_Chem
            "Contine looking around.":
                pass
        
        narrator """Overall the class is tidy. Every student left his desk in a perfect condition.

        Yet, on the back of the class you notice one desk that stands out.

        It appears that one student left all his belongings. 

        His desk look like he never left the class - it is prepared for the upcoming lesson."""

        menu:
            "Inspect the desk.":
                jump area_one_Classroom_Lab_Desk
            "Contine looking around.":
                pass

        narrator """As you look around the class one last time you notice a big poster on the wall. 

        There is not enough light to see its content from a distance.

        It might be something interesting.

        Or completly irrelevant."""

        menu:
            "Examine the flasks.":
                jump area_one_Classroom_Lab_Chem
            "Inspect the desk.":
                jump area_one_Classroom_Lab_Desk
            "Inspect the poster.":
                jump area_one_Classroom_Lab_Ptable
            "Leave.":
                pass

        menu:
            "Leave through the northern door.":
                jump area_one_Corridor_2A1BLab
            "Leave through the southern door.":
                jump area_one_Corridor_A1LabExit

    elif not vb_a1_cls_lab_experiment:
        narrator """You are yet again treated with a strong chemical smell.

        The experiment is yet to conduct."""

        menu:
            "Examine the flasks.":
                jump area_one_Classroom_Lab_Chem
            "Inspect the desk.":
                jump area_one_Classroom_Lab_Desk
            "Inspect the poster.":
                jump area_one_Classroom_Lab_Ptable
            "Leave.":
                pass

        menu:
            "Leave through the northern door.":
                jump area_one_Corridor_2A1BLab
            "Leave through the southern door.":
                jump area_one_Corridor_A1LabExit
    else:
        narrator """You are yet again treated with a strong chemical smell.

        There is nothing interesting left."""
        
        menu:
            "Leave through the northern door.":
                jump area_one_Corridor_2A1BLab
            "Leave through the southern door.":
                jump area_one_Corridor_A1LabExit

label area_one_Classroom_Lab_Desk:
    if not vb_a1_cls_lab_desk_inspected:
        narrator """After going through one student's notes you find some statements about the experiment.

        One being the result. Or at least it looks like one, hovewer the student's chicken scratch handwriting makes it impossible to read.

        The second note is no better, but you are able to read several words:

        \"Properly\", \"conduct\", \"pour ingredients\", \"order\".
        """
    else:
        narrator "Only legible words you can spot are: \"Properly\", \"conduct\", \"pour ingredients\", \"order\"."

    player_thinking "Order... Hmm..."

    menu:
            "Examine the flasks.":
                jump area_one_Classroom_Lab_Chem
            "Inspect the poster.":
                jump area_one_Classroom_Lab_Ptable
            "Leave.":
                pass

    menu:
        "Leave through the northern door.":
            jump area_one_Corridor_2A1BLab
        "Leave through the southern door.":
            jump area_one_Corridor_A1LabExit

label area_one_Classroom_Lab_Ptable:
    if not vb_a1_cls_lab_ptable_inspected:
        $ vb_a1_cls_lab_ptable_inspected = True

        narrator """On one of the walls you notice a large poster.

        A quick qlance told you that it is the periodic table of the emelents.

        It reminds you of countess hours spent trying to memorise some of them, as required by the teacher."""

    player "Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon, Sodium..."

    player_thinking """Why am I inspecting periodic table?

    There must be something more exiting here..."""


    menu:
        "Examine the flasks.":
            jump area_one_Classroom_Lab_Chem
        "Inspect the desk.":
            jump area_one_Classroom_Lab_Desk
        "Leave.":
            pass

    menu:
        "Leave through the northern door.":
            jump area_one_Corridor_2A1BLab
        "Leave through the southern door.":
            jump area_one_Corridor_A1LabExit


label area_one_Classroom_Lab_Chem:
    if not vb_a1_cls_lab_experiment_started:
        python:
            vb_a1_cls_lab_experiment_started = True
            varr_experiment_mixture = ["","","",""]
            vi_experiment_current_flask = 0

        narrator """In front of you there are 5 flasks, and all but one are filled with colourful liquids.

        Empty flask appears to be larger than the others, you can clearly pour all chemicals into it."""

        player_thinking """Hmm I wonder what goes first,,,

        Every flask has it's own letter...

        H, C, F, and O.

        What does that mean?"""

    jump area_one_Classroom_Lab_Chem_Options

label area_one_Classroom_Lab_Chem_StepBack:
    narrator "You take a step back."

    menu:
        "Examine the flasks.":
            jump area_one_Classroom_Lab_Chem
        "Inspect the desk.":
            jump area_one_Classroom_Lab_Desk
        "Leave.":
            pass

    menu:
        "Leave through the northern door.":
            jump area_one_Corridor_2A1BLab
        "Leave through the southern door.":
            jump area_one_Corridor_A1LabExit

label area_one_Classroom_Lab_Chem_Options:
    if vi_experiment_current_flask >= 3:
        jump area_one_Classroom_Lab_Chem_Result

    menu:
        "Pour from flask H." if not "H" in varr_experiment_mixture:
            jump area_one_Classroom_Lab_Chem_PourH
        "Pour from flask C." if not "C" in varr_experiment_mixture:
            jump area_one_Classroom_Lab_Chem_PourC
        "Pour from flask F." if not "F" in varr_experiment_mixture:
            jump area_one_Classroom_Lab_Chem_PourF
        "Pour from flask O." if not "O" in varr_experiment_mixture:
            jump area_one_Classroom_Lab_Chem_PourO
        "Step back.":
            jump area_one_Classroom_Lab_Chem_StepBack

label area_one_Classroom_Lab_Chem_PourH:
    $ varr_experiment_mixture[vi_experiment_current_flask] = "H"
    $ vi_experiment_current_flask += 1

    narrator "You added contents of the flask with \"H\" into the big flask."

    jump area_one_Classroom_Lab_Chem_Options

label area_one_Classroom_Lab_Chem_PourC:
    $ varr_experiment_mixture[vi_experiment_current_flask] = "C"
    $ vi_experiment_current_flask += 1

    narrator "You added contents of the flask with \"C\" into the big flask."

    jump area_one_Classroom_Lab_Chem_Options

label area_one_Classroom_Lab_Chem_PourF:
    $ varr_experiment_mixture[vi_experiment_current_flask] = "F"
    $ vi_experiment_current_flask += 1

    narrator "You added contents of the flask with \"F\" into the big flask."

    jump area_one_Classroom_Lab_Chem_Options

label area_one_Classroom_Lab_Chem_PourO:
    $ varr_experiment_mixture[vi_experiment_current_flask] = "O"
    $ vi_experiment_current_flask += 1

    narrator "You added contents of the flask with \"O\" into the big flask."

    jump area_one_Classroom_Lab_Chem_Options

label area_one_Classroom_Lab_Chem_Result:
    $ vb_a1_cls_lab_experiment = True

    if varr_experiment_mixture[0] = "H" and varr_experiment_mixture[1] = "C" and varr_experiment_mixture[2] = "O":
        $ vb_item_gloves = True
        narrator """As you mix the solution you notice it changed its colour to dark red.

        You step back, as you fear that you did something wrong.

        Seconds later the mixture erupts like a volcano.

        You witness a beautiful show of fake and completly harmless, momemade, volcano."""

        player "HA, I MADE A VOLCANOOOOO!"

        narrator """Filled with joy you start to preforme your favourite dance - macarena.

        Your clumsiness awakes..

        Trying to end the dance with a bang you knock down the mixture and it pours out on the floor.

        As the solution spreads you notice a small box laying on the ground

        Inside this box you find a pair of anti-surge gloves"""
    
    else:
        narrator """As you mix the solution you start to notice it is somehow boiling.

        The clear and colorless mixture starts to rapidly change its colours.

        A beautiful color show is calming and you tilt your face to see it better.

        Before you get a chance to react the solution erupted straight into you face.

        Hot and corrosive substance covered you face, as you tremble in pain."""

    menu:
        "Leave through the northern door.":
            jump area_one_Corridor_2A1BLab
        "Leave through the southern door.":
            jump area_one_Corridor_A1LabExit