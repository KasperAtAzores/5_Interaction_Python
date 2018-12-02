import bpy

# This function will make a new scene which can be used as an overlay. 
# Here, it is a simple score keeping overlay
def add_hud_scene():
    bpy.ops.scene.new(type='NEW')
    hud_scene = bpy.context.scene
    hud_scene.name = "HUD"

    bpy.ops.object.camera_add(location=(0, 0, 7))
    bpy.context.object.data.type = 'ORTHO'
    #bpy.ops.view3d.viewnumpad(type='CAMERA')


    bpy.ops.object.text_add()
    textObject = bpy.context.object
    textObject.name = "Score"
    textObject.data.body = "{:>33}".format("Score: 0")
    bpy.ops.transform.resize(value=(0.5, 0.5, 1))
    bpy.ops.transform.translate(value=(-3, 1.2,0))
    
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            override = bpy.context.copy()
            override['area'] = area
            bpy.ops.view3d.viewnumpad(override, type = 'CAMERA')
            break
        
    # get back to main scene
    bpy.context.screen.scene=bpy.data.scenes["Scene"]

def add_hud_overlay(camera_name='Camera'):
    camera = bpy.data.objects[camera_name]
    bpy.ops.logic.sensor_add(type="ALWAYS", name="always", object=camera_name)
    bpy.ops.logic.controller_add(name="always_scene", object=camera_name)
    bpy.ops.logic.actuator_add(type="SCENE",name="hud overlay", object=camera_name)
    sensor = camera.game.sensors[-1]
    controller = camera.game.controllers[-1]
    actuator = camera.game.actuators[-1]
    actuator.mode ="ADDFRONT" # Set parameters on actuator
    actuator.scene = bpy.data.scenes["HUD"]
    sensor.link( controller ) # Link 
    actuator.link( controller )    

add_hud_scene()    
add_hud_overlay()


