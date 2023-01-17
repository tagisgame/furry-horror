define character1 = Character("character1")
define character2 = Character("character2")


label start:
    character1 "Siemano!"
    jump first

label first:
    character2 "Nieprawda!"
    menu:
        "Nazwa":
            jump test1
        "Nazwa2":
            jump test2

label test1:
    "nie powinno"

label test2:
    "powinno"

