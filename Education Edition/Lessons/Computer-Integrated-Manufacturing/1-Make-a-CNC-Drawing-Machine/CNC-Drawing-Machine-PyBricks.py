#!/usr/bin/env pybricks-micropython


from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Color, ImageFile
from pybricks.tools import wait

# Configure the turntable motor, which rotates the arm.  It has a
# 20-tooth, a 12-tooth, and a 28-tooth gear connected to it.
turntable_motor = Motor(Port.B, Direction.CLOCKWISE, [20, 12, 28])

# Configure the seesaw motor with default settings.  This motor raises
# and lowers the Pen Holder.
seesaw_motor = Motor(Port.C)

# Set up the Gyro Sensor.  It is used to measure the angle of the arm.
# Keep the Gyro Sensor and EV3 steady when connecting the cable and
# during start-up of the EV3.
gyro_sensor = GyroSensor(Port.S2)

# Set up the Color Sensor.  It is used to detect whether there is white
# paper under the drawing machine.
color_sensor = ColorSensor(Port.S3)

# Set up the Touch Sensor.  It is used to detect when it is pressed,
# telling it to start drawing the pattern.
touch_sensor = TouchSensor(Port.S4)


def pen_holder_raise():
    # This function raises the Pen Holder.
    seesaw_motor.run_target(50, 25, Stop.HOLD)
    wait(1000)


def pen_holder_lower():
    # This function lowers the Pen Holder.
    seesaw_motor.run_target(50, 0, Stop.HOLD)
    wait(1000)


def pen_holder_turn_to(target_angle):
    # This function turns the arm to the specified target angle.

    # Run the turntable motor until the arm reaches the target angle.
    if target_angle > gyro_sensor.angle():
        # If the target angle is greater than the current Gyro Sensor
        # angle, run clockwise at a positive speed.
        turntable_motor.run(70)
        while gyro_sensor.angle() < target_angle:
            pass
    elif target_angle < gyro_sensor.angle():
        # If the target angle is less than the current Gyro Sensor
        # angle, run counterclockwise at a negative speed.
        turntable_motor.run(-70)
        while gyro_sensor.angle() > target_angle:
            pass
    # Stop the motor when the target angle is reached.
    turntable_motor.stop(Stop.BRAKE)


# Initialize the seesaw.  This raises the Pen Holder.
pen_holder_raise()

# This is the main part of the program.  It is a loop that repeats
# endlessly.
#
# First, it waits until the Color Sensor detects white paper or a blue
# mark on the paper.
# Second, it waits for the Touch Sensor to be pressed before starting
# to draw the pattern.
# Finally, it draws the pattern and returns to the starting position.
#
# Then the process starts over, so it can draw the pattern again.
while True:
    # Set the Brick Status Light to red, and display "thumbs down" to
    # indicate that the machine is not ready.
    brick.light(Color.RED)
    brick.display.image(ImageFile.THUMBS_DOWN)

    # Wait until the Color Sensor detects blue or white paper.  When it
    # does, set the Brick Status Light to green and display "thumbs up."
    while color_sensor.color() not in (Color.BLUE, Color.WHITE):
        wait(10)
    brick.light(Color.GREEN)
    brick.display.image(ImageFile.THUMBS_UP)

    # Wait until the Touch Sensor is pressed to reset the Gyro Sensor
    # angle and start drawing the pattern.
    while not touch_sensor.pressed():
        wait(10)

    # Draw the pattern.
    gyro_sensor.reset_angle(0)
    pen_holder_turn_to(15)
    pen_holder_lower()
    pen_holder_turn_to(30)
    pen_holder_raise()
    pen_holder_turn_to(45)
    pen_holder_lower()
    pen_holder_turn_to(60)

    # Raise the Pen Holder and return to the starting position.
    pen_holder_raise()
    pen_holder_turn_to(0)
