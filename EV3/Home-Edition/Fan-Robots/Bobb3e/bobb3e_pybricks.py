#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port
from pybricks.robotics import DriveBase

from time import sleep


class Bobb3e(EV3Brick):
    """
    CHALLENGES:

    Here are some challenges you can try to do in order to make BOBB3E better:

    - Can you make BOBB3E say sounds when he is lifting/lowering his forks?

    - BOBB3E does by default drive rather slow - try to see if you can
    make him go faster!

    - You could utilise that the remote has 4 channels and use that as
    different gears. Say, for instance, that when using Channel 1 is the same
    as driving in 1st gear; very slow. Channel 2 could make him go a little
    faster and using channel 4 would make him go very fast!

    - The remote control can also be used as a Beacon, which BOBB3E is able to
    detect and drive towards. Can you make him automatically find the Beacon
    and lift it, when BOBB3E comes close enough to it?
    """

    WHEEL_DIAMETER = 24   # milimeters
    AXLE_TRACK = 100      # milimeters

    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            lift_motor_port: str = Port.A,
            ir_sensor_port: str = Port.S4, ir_beacon_channel: int = 1):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=Direction.COUNTERCLOCKWISE)
        self.drive_base = DriveBase(left_motor=self.left_motor,
                                    right_motor=self.right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)

        self.lift_motor = Motor(port=lift_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.reversing = False
        self.playing_sound = False

    """
    BOBB3E takes advantage of running multiple subprograms;
    one for receiving the commands from the remote control and
    one for handling the reversing alarm.
    """

    def drive_or_operate_forks_once_by_ir_beacon(
            self,
            speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
            ):
        """
        Read the commands from the remote control and convert them into actions
        such as go forward, lift and turn.
        """
        ir_beacon_button_pressed = \
            set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # lower the forks
        if ir_beacon_button_pressed == {Button.LEFT_UP, Button.LEFT_DOWN}:
            self.reversing = False

            self.drive_base.stop()

            self.lift_motor.run(speed=100)

        # raise the forks
        elif ir_beacon_button_pressed == {Button.RIGHT_UP, Button.RIGHT_DOWN}:
            self.reversing = False

            self.drive_base.stop()

            self.lift_motor.run(speed=-100)

        # forward
        elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.reversing = False

            self.drive_base.drive(
                speed=speed,
                turn_rate=0)

            self.lift_motor.hold()

        # backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.reversing = True

            self.drive_base.drive(
                speed=-speed,
                turn_rate=0)

            self.lift_motor.hold()

        # turn left on the spot
        elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
            self.reversing = False

            self.drive_base.drive(
                speed=0,
                turn_rate=-turn_rate)

            self.lift_motor.hold()

        # turn right on the spot
        elif ir_beacon_button_pressed == {Button.RIGHT_UP, Button.LEFT_DOWN}:
            self.reversing = False

            self.drive_base.drive(
                speed=0,
                turn_rate=turn_rate)

            self.lift_motor.hold()

        # turn left forward
        elif ir_beacon_button_pressed == {Button.LEFT_UP}:
            self.reversing = False

            self.drive_base.drive(
                speed=speed,
                turn_rate=-turn_rate)

            self.lift_motor.hold()

        # turn right forward
        elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
            self.reversing = False

            self.drive_base.drive(
                speed=speed,
                turn_rate=turn_rate)

            self.lift_motor.hold()

        # turn left backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
            self.reversing = True

            self.drive_base.drive(
                speed=-speed,
                turn_rate=turn_rate)

            self.lift_motor.hold()

        # turn right backward
        elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
            self.reversing = True

            self.drive_base.drive(
                speed=-speed,
                turn_rate=-turn_rate)

            self.lift_motor.hold()

        # otherwise stop
        else:
            self.reversing = False

            self.drive_base.stop()

            self.lift_motor.hold()

    def keep_driving_or_operating_forks_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        while True:
            self.drive_or_operate_forks_once_by_ir_beacon(speed=speed)

    def sound_alarm_if_reversing(self):
        """
        Whenever the Reversing variable is changed to True
        the alarm starts to play.
        When the value of the Reversing variable is set to False
        the alarm stops.
        """
        if self.reversing:
            if not self.playing_sound:
                self.playing_sound = True

                self.speaker.play_file(file=SoundFile.BACKING_ALERT)

        elif self.playing_sound:
            self.playing_sound = False

        sleep(0.01)

    def sound_alarm_whenever_reversing(self):
        while True:
            self.sound_alarm_if_reversing()
