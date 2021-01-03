"""
This program is for Tricky's "Soccer: Penalty Kick" activity.

Follow the corresponding building instructions in the LEGO® MINDSTORMS®
Robot Inventor App.

For each penalty kick practice round, ready Tricky in front of
the red ball and the goal, then trigger the run-up and the kick
by placing something near the Distance Sensor behind Tricky.
"""

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase


class TrickyPlayingSoccer:
    WHEEL_DIAMETER = 44
    AXLE_TRACK = 88

    def __init__(self):
        self.hub = InventorHub()

        left_motor = Motor(port=Port.B,
                           positive_direction=Direction.COUNTERCLOCKWISE)
        right_motor = Motor(port=Port.A,
                            positive_direction=Direction.CLOCKWISE)
        self.drive_base = DriveBase(left_motor=left_motor,
                                    right_motor=right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)

        self.kicker_motor = Motor(port=Port.C,
                                  positive_direction=Direction.CLOCKWISE)

        self.distance_sensor = UltrasonicSensor(port=Port.D)

        self.color_sensor = ColorSensor(port=Port.E)

    def reset_kicker_motor(self):
        self.hub.light.on(color=Color.BLACK)

        self.kicker_motor.run_time(
            speed=-1000,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.kicker_motor.run_angle(
            speed=1000,
            rotation_angle=325,
            then=Stop.HOLD,
            wait=True)

    def kick(self):
        self.kicker_motor.run_angle(
            speed=1000,
            rotation_angle=360,
            then=Stop.HOLD,
            wait=True)

    def run_to_and_kick_ball(self):
        self.drive_base.drive(
            speed=1000,
            turn_rate=0)

        while self.color_sensor.color(surface=True) != Color.RED:
            pass

        self.hub.light.on(color=Color.RED)

        self.hub.speaker.beep(
            frequency=100,
            duration=100)

        self.kick()

        self.drive_base.stop()

        self.hub.light.on(color=Color.BLACK)

    def celebrate(self):
        self.hub.display.image(
            image=[[00, 11, 33, 11, 00],
                   [11, 33, 66, 33, 11],
                   [33, 66, 99, 66, 33],
                   [11, 33, 66, 33, 11],
                   [00, 11, 33, 11, 00]])

        self.hub.speaker.beep(
            frequency=1000,
            duration=1000)

        self.hub.display.off()


TRICKY = TrickyPlayingSoccer()

TRICKY.reset_kicker_motor()

# keep practicing penalty kicks
while True:
    # wait until the player puts an object near the Distance Sensor
    # to trigger Tricky to start running towards the ball and the goal
    while TRICKY.distance_sensor.distance() >= 100:
        pass

    TRICKY.run_to_and_kick_ball()

    TRICKY.celebrate()
