import bge

score = 0
    
sensor_name = 'collision'
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
    # 33 is guestimated to work - one should actually use
    # either a fixed font, or font metrics
    score_text = '{:>33}'.format("Score: " + str(g_counter))
    score_object['Text'] = score_text
    
def car_collision():
    controller = bge.logic.getCurrentController()
    bump = controller.sensors[sensor_name].hitObject
    if bump is None: 
        return
    if bump.name == 'Plane':
        return
    global score
    if bump.name[0:1] == 'e':
        score = score + 10
    if bump.name[0:1] == 'r':
        score = score + 5
    
    # Get the hud_scene from the game scenes
    hud_scene = [scene for scene in bge.logic.getSceneList() if scene.name == hud_name][0]
    # Get the score object from the hud scene
    score_object = hud_scene.objects[counter_name]
    # 33 is guestimated to work - one should actually use
    # either a fixed font, or font metrics
    score_text = '{:>33}'.format("Score: " + str(score))
    score_object['Text'] = score_text
    bump.endObject()
    
