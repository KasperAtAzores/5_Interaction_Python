# Interaction through Python

### Learning goals
After this week, it is expected that you:

* can write python controls that get called as response to blender sensors
* can access the object and the sensor that called the python control
* understand when and how to have python access the logic actuators
* can build the logic bricks of a blender game programatically in python
* can use the different sensors and their settings for efficiency

### The python control


### Acess to the sensor

### Acess to an actuator
As an example, there is an actuator for updating display. It uses the underlying C++ code to change the text and handle the UI change propagation. In general it is more efficient to call down into the underlying blender libraries than to rewrite them in python.




