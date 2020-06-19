#!/usr/bin/env pybricks-micropython


from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import (Port, Button, Color, ImageFile,
                                 SoundFile)
from pybricks.tools import wait

# The Color Squares are red, green, blue, or yellow.
POSSIBLE_COLORS = (Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW)

# Configure the belt motor with default settings.  This motor drives
# the conveyor belt.
belt_motor = Motor(Port.D)

# Configure the feed motor with default settings.  This motor ejects
# the Color Squares.
feed_motor = Motor(Port.A)

# Set up the Touch Sensor.  It is used to detect when the belt motor
# has moved the sorter module all the way to the left.
touch_sensor = TouchSensor(Port.S1)

# Set up the Color Sensor.  It is used to detect the color of the Color
# Squares.
color_sensor = ColorSensor(Port.S3)

# This is the main part of the program.  It is a loop that repeats
# endlessly.
#
# First, it moves the 2 motors to their correct starting positions.
# Second, it waits for you to scan and insert up to 8 Color Squares.
# Finally, it sorts them by color and ejects them in their correct
# positions.
#
# Then the process starts over, so you can scan and insert the next set
# of Color Squares.
while True:
    # Initialize the feed motor.  This is done by running the motor
    # forward until it stalls.  This means that it cannot move any
    # further.  From this end point, the motor rotates backward by 180
    # degrees.  This is the starting position.
    feed_motor.run_until_stalled(120)
    feed_motor.run_angle(450, -180)

    # Initialize the conveyor belt motor.  This is done by first
    # running the belt motor backward until the Touch Sensor is
    # pressed.  Then the motor stops and the angle is reset to "0."
    # This means that when it rotates backward to "0" later on, it
    # returns to this starting position.
    belt_motor.run(-500)
    while not touch_sensor.pressed():
        pass
    belt_motor.stop()
    wait(1000)
    belt_motor.reset_angle(0)

    # Clear all the contents from the Display.
    brick.display.clear()

    # Scanning a Color Square stores the color in a list.  The list is
    # empty to start.  It will grow as colors are added to it.
    color_list = []

    # This loop scans the colors of the objects.  It repeats until 8
    # objects are scanned and placed in the chute.  This is done by
    # repeating the loop while the length of the list is less than 8.
    while len(color_list) < 8:
        # Display an arrow that points to the Color Sensor.
        brick.display.image(ImageFile.RIGHT)

        # Display how many Color Squares have been scanned so far.
        brick.display.text(len(color_list))

        # Wait until the Center Button is pressed or a Color Square is
        # scanned.
        while True:
            # Store "True" if the Center Button is pressed or "False"
            # if not.
            pressed = Button.CENTER in brick.buttons()
            # Store the color measured by the Color Sensor.
            color = color_sensor.color()
            # If the Center Button is pressed or one of the possible
            # colors is detected, break out of the loop.
            if pressed or color in POSSIBLE_COLORS:
                break

        if pressed:
            # If the button was pressed, end the loop early.  It will
            # no longer wait for any Color Squares to be scanned and
            # added to the chute.
            break
        else:
            # Otherwise, a color was scanned, so it is added (appended)
            # to the list.
            brick.sound.beep(1000, 100, 100)
            color_list.append(color)

            # It should not register the same color again if it is
            # still looking at the same Color Square.  So, before
            # continuing, wait until the sensor no longer sees the
            # Color Square.
            while color_sensor.color() in POSSIBLE_COLORS:
                pass
            brick.sound.beep(2000, 100, 100)

            # Display an arrow pointing down and wait 2 seconds to
            # allow some time to slide the Color Square into the
            # motorized chute.
            brick.display.image(ImageFile.BACKWARD)
            wait(2000)

    # Play a sound and display an image to indicate that scanning is
    # complete.
    brick.sound.file(SoundFile.READY)
    brick.display.image(ImageFile.EV3)

    # Now sort the bricks using the list of colors that have been
    # stored.  Do this by looping over each color in the list.
    for color in color_list:

        # Wait for 1 second between each sorting action.
        wait(1000)

        # Run the conveyor belt motor to the position that corresponds
        # to the stored color.
        if color == Color.BLUE:
            brick.sound.file(SoundFile.BLUE)
            belt_motor.run_target(500, 10)
        elif color == Color.GREEN:
            brick.sound.file(SoundFile.GREEN)
            belt_motor.run_target(500, 132)
        elif color == Color.YELLOW:
            brick.sound.file(SoundFile.YELLOW)
            belt_motor.run_target(500, 360)
        elif color == Color.RED:
            brick.sound.file(SoundFile.RED)
            belt_motor.run_target(500, 530)

        # Now that the conveyor belt is in the correct position, eject
        # the colored object.
        feed_motor.run_angle(1500, 90)
        feed_motor.run_angle(1500, -90)
