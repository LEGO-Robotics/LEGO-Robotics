#!/usr/bin/env pybricks-micropython


from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, SoundFile
from pybricks.tools import wait
from random import randint

# Configure the belt motor, which drives the conveyor belt.  Set the
# motor direction to counterclockwise, so that positive speed values
# make the conveyor move upward.
belt_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# Configure the "catch" motor with default settings.  This motor moves
# the ball to either cup.
catch_motor = Motor(Port.D)

# Set up the Color Sensor.  It is used in Reflected Light Intensity
# Mode to detect when the ball is placed at the bottom of the conveyor
# belt.
color_sensor = ColorSensor(Port.S3)

# Set up the Touch Sensor.  It is used to detect when the ball reaches
# the catch at the end of the ramp.
touch_sensor = TouchSensor(Port.S4)

# Initialize the conveyor belt.  This is done by slowly running the
# motor backward until it stalls.  This means that it cannot move any
# further.  Then it resets the angle to "0."  This means that when it
# rotates backward to "0" later on, it returns to this starting
# position.
belt_motor.run_until_stalled(-300, Stop.BRAKE, 30)
belt_motor.reset_angle(0)

# This is the main part of the program.  It is a loop that repeats
# endlessly.
#
# First, it waits until the ball is placed on the conveyor belt.
# Second, the ball is moved upward until it reaches the ramp where it
# rolls down to the catch.
# Finally, the ball is moved to the left or the right cup, or an error
# sound is made, chosen at random.
#
# Then the process starts over.  The ball can be placed at the
# beginning of the conveyor belt again.
while True:

    # Wait until the ball is placed in front of the Color Sensor.
    while color_sensor.reflection() < 5:
        wait(10)
    wait(500)

    # Move the ball up on the conveyor belt.
    belt_motor.run_target(250, 450, Stop.COAST, False)

    # Wait until the ball hits the Touch Sensor at the catch at the end
    # of the ramp.
    while not touch_sensor.pressed():
        wait(10)

    # Generate a random integer between "-1" and "1" to determine what
    # to do with the ball.
    catch_command = randint(-1, 1)

    # If it generates a "1," change the light to green and move the
    # ball to the right cup.
    if catch_command == 1:
        brick.light(Color.GREEN)
        catch_motor.run_target(400, -20)
        wait(1000)
        catch_motor.run_target(400, 0, Stop.HOLD)
    # If it generates a "0," change the light to orange and move the
    # ball to the left cup.
    elif catch_command == 0:
        brick.light(Color.ORANGE)
        catch_motor.run_target(400, 20)
        wait(1000)
        catch_motor.run_target(400, 0, Stop.HOLD)
    # Otherwise, change the light to red and play an error sound.
    else:
        brick.light(Color.RED)
        brick.sound.file(SoundFile.RATCHET)
        wait(1000)

    # Return the conveyor belt to its starting position.
    belt_motor.run_target(250, 0)
