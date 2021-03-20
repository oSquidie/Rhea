init:
    $ emma_points = 0 # this is a variable for emma's affection points throughout your game
    $ liam_points = 0 # this is a variable for liam's affection points throughout your game
    $ emma_max = 10 # this variable should be set to emma's maximum affection points
    $ liam_max = 10 # this variable should be set to liam's maximum affection points
    $ affbar = False # when false, the affection screen button doesn't appear on the screen

#########Affection Screen##########
screen button: #The screen to show when calling it in the script
    if affbar:
        vbox xalign 0.1 yalign 0.1:
            textbutton "Show affection points" action ui.callsinnewcontext("aff_screen_label") #Show affection text button
            # you can also use an image button:
            imagebutton: #Image icon
                idle  "button_idle.png"
                hover "button_hover.png"
                action ui.callsinnewcontext("aff_screen_label")

screen aff_screen:  #What shows on the affection screen

    vbox yalign -9: #adjusting the position of the menu
        text "Emma: [emma_points] points"
        text "Liam: [liam_points] points"
        textbutton "Return" action Return()

label aff_screen_label:
    call screen aff_screen
    return
