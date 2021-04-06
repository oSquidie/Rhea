window hide
init python:

    def glass_dragged(drags, drop):

        if not drop:
            return

        store.glass = drags[0].drag_name
        store.object = drop.drag_name

        return True
window hide
screen slide_glass_screen:
    add "CaveExploreMainEmpty.png"
    draggroup:
        drag:
            drag_name "You"
            child "MagnifyingGlass.png"
            droppable False
            dragged glass_dragged
            xpos 700 ypos 650

        drag:
            drag_name "Crystal Door."
            draggable False
            child "CrystalDoor.png"
            xpos 1515 ypos 50

        drag:
            drag_name "Opus Door."
            draggable False
            child "OpusDoor.png"
            xpos 700 ypos 135

        drag:
            drag_name "Treasure Door."
            draggable False
            child "TreasureDoor.png"
            xpos 60  ypos 90

        drag:
            drag_name "a vine?"
            draggable False
            child "VineDoor.png"
            xpos 1500 ypos 650

        drag:
            drag_name "Rock."
            draggable False
            child "HiddenRock.png"
            xpos 1255  ypos 500

return
window hide

init python:

    def glass_dragged(drags, drop):

        if not drop:
            return

        store.glass = drags[0].drag_name
        store.object = drop.drag_name

        return True
window hide

screen slide_glass_screen2:
    add "CaveExploreMainEmpty.png"
    draggroup:
        drag:
            drag_name "You"
            child "MagnifyingGlass.png"
            droppable False
            dragged glass_dragged
            xpos 700 ypos 650

        drag:
            drag_name "Crystal Door."
            draggable False
            child "CrystalDoor.png"
            xpos 1515 ypos 50

        drag:
            drag_name "Opus Door."
            draggable False
            child "OpusDoor.png"
            xpos 700 ypos 135

        drag:
            drag_name "Treasure Door."
            draggable False
            child "TreasureDoor.png"
            xpos 60  ypos 90

        drag:
            drag_name "vine?"
            draggable False
            child "VineDoor.png"
            xpos 1500 ypos 650

return
