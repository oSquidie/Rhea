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
            idle_child "MagnifyingGlass.png"
            hover_child "MagnifyingGlassHover.png"
            droppable False
            dragged glass_dragged
            xpos 700 ypos 650

        drag:
            drag_name "Crystal Door."
            draggable False
            idle_child "CrystalDoor.png"
            selected_idle_child "CrystalDoorHover.png"
            xpos 1515 ypos 50

        drag:
            drag_name "Opus Door."
            draggable False
            idle_child "OpusDoor.png"
            selected_idle_child "OpusDoorHover.png"
            xpos 700 ypos 135

        drag:
            drag_name "Treasure Door."
            draggable False
            idle_child "TreasureDoor.png"
            selected_idle_child "TreasureDoorHover.png"
            xpos 60  ypos 90

        drag:
            drag_name "vine?"
            draggable False
            idle_child "VineDoor.png"
            selected_idle_child "VineDoorHover.png"
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
            idle_child "MagnifyingGlass.png"
            hover_child "MagnifyingGlassHover.png"
            droppable False
            dragged glass_dragged
            xpos 700 ypos 650

        drag:
            drag_name "Crystal Door."
            draggable False
            idle_child "CrystalDoor.png"
            selected_idle_child "CrystalDoorHover.png"
            xpos 1515 ypos 50

        drag:
            drag_name "Opus Door."
            draggable False
            idle_child "OpusDoor.png"
            selected_idle_child "OpusDoorHover.png"
            xpos 700 ypos 135

        drag:
            drag_name "Treasure Door."
            draggable False
            idle_child "TreasureDoor.png"
            selected_idle_child "TreasureDoorHover.png"
            xpos 60  ypos 90

        drag:
            drag_name "vine?"
            draggable False
            idle_child "VineDoor.png"
            selected_idle_child "VineDoorHover.png"
            xpos 1500 ypos 650

return
