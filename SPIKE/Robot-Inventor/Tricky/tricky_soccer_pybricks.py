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
from pybricks.tools import wait


class TrickyPlayingSoccer:
    WHEEL_DIAMETER = 44
    AXLE_TRACK = 88

    def __init__(
            self,
            left_wheel_motor_port: Port = Port.B,
            right_wheel_motor_port: Port = Port.A,
            kicker_motor_port: Port = Port.C,
            distance_sensor_port: Port = Port.D,
            color_sensor_port: Port = Port.E):
        self.hub = InventorHub()

        left_motor = Motor(port=left_wheel_motor_port,
                           positive_direction=Direction.COUNTERCLOCKWISE)
        right_motor = Motor(port=right_wheel_motor_port,
                            positive_direction=Direction.CLOCKWISE)
        self.drive_base = DriveBase(left_motor=left_motor,
                                    right_motor=right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)

        self.kicker_motor = Motor(port=kicker_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.distance_sensor = UltrasonicSensor(port=distance_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

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
        """
        This controls the kick. It takes one rotation to kick the ball.
        """
        self.kicker_motor.run_angle(
            speed=1000,
            rotation_angle=360,
            then=Stop.HOLD,
            wait=True)

    def run_to_and_kick_ball(self):
        self.drive_base.drive(
            speed=1000,
            turn_rate=0)

        # wait until Tricky sees the ball
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
        """
        This runs Tricky's celebration
        """
        self.hub.display.image(
            image=[[00, 11, 33, 11, 00],
                   [11, 33, 66, 33, 11],
                   [33, 66, 99, 66, 33],
                   [11, 33, 66, 33, 11],
                   [00, 11, 33, 11, 00]])

        self.hub.speaker.beep(
            frequency=1000,
            duration=1000)

        self.hub.light.animate(
            colors=[Color.CYAN, Color.GREEN, Color.MAGENTA],
            interval=100)

        # FIXME: below blocks cause Inventor Hub to loop forever
        # self.drive_base.drive(
        #     speed=0,
        #     turn_rate=360)

        # self.kicker_motor.run_angle(
        #     speed=1000,
        #     rotation_angle=5 * 360,
        #     then=Stop.COAST,
        #     wait=True)

        wait(1000)

        self.hub.display.off()

        self.hub.light.on(color=Color.BLACK)

        self.drive_base.stop()


if __name__ == '__main__':
    TRICKY = TrickyPlayingSoccer()

    TRICKY.reset_kicker_motor()

    # FIXME: the following causes Inventor Hub to hang
    # TRICKY.distance_sensor.lights.on(100)

    # keep practicing penalty kicks
    while True:
        # When the Distance Sensor is triggered, Tricky's goal run starts
        while TRICKY.distance_sensor.distance() >= 100:
            pass

        TRICKY.run_to_and_kick_ball()

        TRICKY.celebrate()
