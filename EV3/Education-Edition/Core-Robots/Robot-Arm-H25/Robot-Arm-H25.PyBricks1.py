#!/usr/bin/env pybricks-micropython


from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import (Port, Stop, Direction, Button,
                                 ImageFile, SoundFile)
from pybricks.tools import wait

# Configure the gripper motor with default settings.
gripper_motor = Motor(Port.A)

# Configure the elbow motor.  It has an 8-tooth and a 40-tooth gear
# connected to it.  Set the motor direction to counterclockwise, so
# that positive speed values make the arm move upward.
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

# Configure the motor that rotates the base.  It has a 12-tooth and a
# 36-tooth gear connected to it.  Set the motor direction to
# counterclockwise, so that positive speed values make the arm move
# away from the Touch Sensor.
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

# Limit the elbow and base accelerations.  This results in very smooth
# motion, like that of an industrial robot.
elbow_motor.set_run_settings(60, 120)
base_motor.set_run_settings(60, 120)

# Set up the Touch Sensor.  It is used to detect when the base has
# moved to its starting position.
touch_sensor = TouchSensor(Port.S1)

# Set up the Color Sensor.  It is used in Reflected Light Intensity
# Mode to detect the white beam when the elbow is in its starting
# position.
color_sensor = ColorSensor(Port.S3)

# Initialize the elbow.  This is done by first moving down for 1 second
# and then slowly moving up until the Color Sensor detects the white
# beam.  Then the motor stops, holds its position, and resets the angle
# to "0."  This means that when it rotates backward to "0" later on, it
# returns to this starting position.
elbow_motor.run_time(-30, 1000)
elbow_motor.run(15)
while color_sensor.reflection() < 30:
    wait(10)
elbow_motor.stop(Stop.HOLD)
elbow_motor.reset_angle(0)

# Initialize the base.  This is done by first running the base motor
# counterclockwise until the Touch Sensor is pressed.  Then the motor
# stops, holds its position, and resets the angle to "0."  This means
# that when it rotates backward to "0" later on, it returns to this
# starting position.
base_motor.run(-60)
while not touch_sensor.pressed():
    wait(10)
base_motor.stop(Stop.HOLD)
base_motor.reset_angle(0)

# Initialize the gripper.  This is done by running the motor forward
# until it stalls.  This means that it cannot move any further.  From
# this closed gripper position, the motor rotates backward by 90
# degrees, so the gripper opens up.  This is the starting position.
gripper_motor.run_until_stalled(200, Stop.COAST, 50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)

def robot_pick(position):
    # This function rotates the base to the pick up position.  There,
    # it lowers the arm, closes the gripper, and raises the arm to pick
    # up the wheel stack.
    base_motor.run_target(60, position, Stop.HOLD)
    elbow_motor.run_target(60, -45)
    gripper_motor.run_until_stalled(200, Stop.HOLD, 50)
    elbow_motor.run_target(60, 0, Stop.HOLD)

def robot_release(position):
    # This function rotates the base to the drop-off position.  There,
    # it lowers the arm, opens the gripper to release the wheel stack,
    # and raises the arm again.
    base_motor.run_target(60, position, Stop.HOLD)
    elbow_motor.run_target(60, -45)
    gripper_motor.run_target(200, -90)
    elbow_motor.run_target(60, 0, Stop.HOLD)

# Define the 3 destinations for picking up and dropping off the wheel
# stacks.
LEFT = 200
CENTER = 100
RIGHT = 0

# Rotate the base to the center.
base_motor.run_target(60, CENTER, Stop.HOLD)

# This is the main part of the program.  It is a loop that repeats
# endlessly.
#
# First, the robot waits until the Up or Down Button is pressed.
# Second, the robot waits until the Center Button is pressed.
# Finally, the robot picks up the wheel stack and drops it off in the
# center.
#
# Then the process starts over, so the robot can pick up another wheel
# stack.
while True:

    # Display a question mark to indicate that the robot should await
    # instructions.
    brick.display.image(ImageFile.QUESTION_MARK)

    # Wait until the Up or Down Button is pressed.
    while True:
        # First, wait until any button is pressed.
        while not any(brick.buttons()):
            wait(10)
        # Then store which button was pressed.
        button = brick.buttons()[0]
        # If the Up or Down Button was pressed, break out of the loop.
        if button in (Button.UP, Button.DOWN):
            break

    # Play a sound and display an arrow to show where the arm will move.
    brick.sound.file(SoundFile.AIR_RELEASE)
    if button == Button.UP:
        brick.display.image(ImageFile.FORWARD)
    elif button == Button.DOWN:
        brick.display.image(ImageFile.BACKWARD)

    # Wait until the Center Button is pressed, then display a check
    # mark to indicate that the instruction has been accepted.
    while not Button.CENTER in brick.buttons():
        wait(10)
    brick.display.image(ImageFile.ACCEPT)

    # Pick up the wheel stack. Depending on which button was pressed,
    # move left or right.
    if button == Button.UP:
        robot_pick(RIGHT)
    elif button == Button.DOWN:
        robot_pick(LEFT)

    # Drop off the wheel stack in the center.
    robot_release(CENTER)
