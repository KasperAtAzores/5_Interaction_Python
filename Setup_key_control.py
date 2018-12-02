import bpy
import Transfer

def add_key_listener_at(listner_name, handler):
    obj = bpy.data.objects[listner_name]

    bpy.ops.logic.sensor_add(type="KEYBOARD", name="keyboard", object=listner_name)
    bpy.ops.logic.controller_add(type='PYTHON', name="python keyboard", object=listner_name)
    
    sensor = obj.game.sensors[-1]
    sensor.use_all_keys = True
    sensor.show_expanded = False
    
    controller = obj.game.controllers[-1]
    controller.mode ="MODULE"
    controller.module = handler
    controller.show_expanded = False
    
    sensor.link( controller )


    
#add_key_listener_at('Empty', 'Game.keyboard_handler')    
add_key_listener_at('Empty', 'Game.add_to_counter')
set_counter(77)