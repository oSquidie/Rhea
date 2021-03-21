###Note for Candy (:##
# This is how you call this script in the main game script

#show screen positive_affection <<-- For positive icon
#$ affbarposi = True

#show screen negative_affection <<-- For negative icon
#$ affbarnegative = True
##Note to make one false when you're showing one of them getting a point or taking a point away##

init:
    $ emma_points = 0 # this is a variable for emma's affection points throughout your game
    $ liam_points = 0 # this is a variable for liam's affection points throughout your game
    $ emma_max = 10 # this variable should be set to emma's maximum affection points
    $ liam_max = 10 # this variable should be set to liam's maximum affection points
    $ affbarposi = False # when false, the  positive icon affection screen button doesn't appear on the screen
    $ affbarnegative = False # when false, negative icon screen doesnt appear.
#########Positive Affection Screen##########
screen positive_affection: #The screen to show when calling it in the script
    if affbarposi:
        vbox xalign -4 yalign -9:
            textbutton "Show affection points" action ui.callsinnewcontext("aff_screen_label1") #Show affection text button
            # you can also use an image button:
            imagebutton: #Image icon
                idle  "heartposiicon.png"
                hover "heartposiiconhover.png"
                action ui.callsinnewcontext("aff_screen_label1")

screen aff_screen1:  #What shows on the affection screen

    vbox yalign -9: #adjusting the position of the menu
        text "Emma: [emma_points] points"
        text "Liam: [liam_points] points"
        textbutton "Return" action Return()

label aff_screen_label1:
    call screen aff_screen1
    return




#########Negative Affection Screen##########
screen negative_affection: #The screen to show when calling it in the script
    if affbarnegative:
        vbox xalign -4 yalign -9:
            textbutton "Show affection points" action ui.callsinnewcontext("aff_screen_label2") #Show affection text button
            # you can also use an image button:
            imagebutton: #Image icon
                idle  "heartnegativeicon.png"
                hover "heartnegativeiconhover.png"
                action ui.callsinnewcontext("aff_screen_label2")

screen aff_screen2:  #What shows on the affection screen

    vbox yalign -9: #adjusting the position of the menu
        text "Emma: [emma_points] points"
        text "Liam: [liam_points] points"
        textbutton "Return" action Return()

label aff_screen_label2:
    call screen aff_screen2
    return
