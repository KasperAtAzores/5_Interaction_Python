import bge
import bpy

g_counter = 0

sensor_name = 'i key'
hud_name = 'HUD'
counter_name = 'Score'
  
def add_to_counter():
    cont = bge.logic.getCurrentController()
    key_sensor = cont.sensors[sensor_name]
    status = key_sensor.events[0][1] # bge.logic.KX_INPUT_JUST_ACTIVATED
    if status != bge.logic.KX_INPUT_JUST_ACTIVATED:
        return  

    global g_counter
    g_counter = g_counter + 1
    # Get the hud_scene from the game scenes
    hud_scene = [scene for scene in bge.logic.getSceneList() if scene.name == hud_name][0]
    # Get the score object from the hud scene
    score_object = hud_scene.objects[counter_name]
    score_object['Text'] = "Score: " + str(g_counter)
    


