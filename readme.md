# Interaction through Python

### Learning goals
After this week, it is expected that you:

* can write python controls that get called as response to blender sensors
* can access the object and the sensor that called the python control
* can build the logic bricks of a blender game programatically in python
* can use the different sensors and their settings for efficiency

## The main example
There is a major example - the little red box car we have been working with over the last few weeks. This week it is represented in the files `lost_red_car_backup.blend` and two python scripts: `BuildGame.py` that installs the missing parts to the blender file, and `CarGame.py` that has the run-time behaviour for the game (scoring).

## Explanation of the example
Will be given in class, and expanded here before thursday.

The blender file `lost_red_car.blend` has the final game ready to be started, the file `lost_red_car_backup.blend` has the game as it was before camera and score was added.  The file `BuildGame.py` sets up camera, overlay, and makes the gemstones. Finally the file `CarGame.py` has the scoring system.

### Building the logic bricks from python
Once you find the right library it is reasonable to build them. In the file `BuildGame.py` the function `add_hud_overlay` is a good example. It shows how to add sensor, controller and actuator, and sets a few parameters on each. There is a little trick there, as the last added sensor, control and actuator can be found using indec -1. For example `sensor = camera.game.sensors[-1]`. 

### The python control
There are two `modes` of Python controllers, `Module` and `Script`. The script mode runs the entire file, in module mode only one function within the file is executed. Moreover, the file is only loaded once, so it is a supposedly (I have not timed it) faster than script. Also, it allow us to keep global variable state between each call, giving us a faster means to store scores, health, and whatever needs to be done in your game.

The function is called in responce to triggering a specific sensor. If it is just an `always` sensor, it seems that the *normal* way is to attach such scripts to an `empty` object.

### Acess to the sensor
Each of the sensors has some extra aspects which can be set and read from python. But first and foremost, you can find:

* The specific controller that started the python module of your code.
* Thorugh the controller, you can find
	* The object on which the controller is located
	* The sensors (and actuators) of the controler

In the file `CarGame.py`, the function `car_collision()` is called as a response to the car hitting something. It gives examples of several of these aspects.





