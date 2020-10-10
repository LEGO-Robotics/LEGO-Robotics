# Guide


## Map

The simulated map is 2362mm by 1143mm; the size of an FLL / WRO field mat. If providing a custom image, ensure that it is 2362 x 1143 pixels; each pixel represents 1mm. Images of different dimensions should load, but would probably not provide the result you're expecting.

Click on the map to make measurements. A second click locks the line in place, and a third click clears the measurement.

Robot Configuration
- OUTPUT B: Left motor
- OUTPUT C: Right motor
- INPUT 1: Ultrasonic Sensor
- INPUT 2: Left Color Sensor
- INPUT 3: Right Color Sensor
- INPUT 4: Gyro Sensor
All other outputs and inputs are unconnected.

Read the [python-ev3dev2 documents](https://python-ev3dev.readthedocs.io/en/latest/index.html) for the API documentations. Most common APIs are supported, and you can check the following table for details.


## [Supported python-ev3dev2 API](https://www.aposteriori.com.sg/Ev3devSim)
