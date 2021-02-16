from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


class Blast:
    WHEEL_DIAMETER = 44
    AXLE_TRACK = 100

    def __init__(
            self,
            left_wheel_motor_port: Port = Port.C,
            right_wheel_motor_port: Port = Port.A,
            action_motor_port: Port = Port.B,
            arm_movement_motor_port: Port = Port.D,
            color_sensor_port: Port = Port.E,
            distance_sensor_port: Port = Port.F):
        self.hub = InventorHub()

        left_motor = Motor(port=left_wheel_motor_port,
                           positive_direction=Direction.COUNTERCLOCKWISE)
        right_motor = Motor(port=right_wheel_motor_port,
                            positive_direction=Direction.CLOCKWISE)
        self.drive_base = DriveBase(left_motor=left_motor,
                                    right_motor=right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)

        self.arm_movement_motor = Motor(port=arm_movement_motor_port,
                                        positive_direction=Direction.CLOCKWISE)

        self.action_motor = Motor(port=action_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.distance_sensor = UltrasonicSensor(port=distance_sensor_port)

    def calibrate(self):
        self.arm_movement_motor.run_target(
            speed=1000,
            target_angle=0,
            then=Stop.HOLD,
            wait=True)

    def setup(self):
        for _ in range(10):
            self.hub.display.image(
                image=[[00, 11, 33, 11, 00],
                       [11, 33, 66, 33, 11],
                       [33, 66, 99, 66, 33],
                       [11, 33, 66, 33, 11],
                       [00, 11, 33, 11, 00]])

            self.hub.light.on(color=Color.RED)

            wait(100)

            self.hub.display.off()
            self.hub.light.off()

            wait(100)


if __name__ == '__main__':
    BLAST = Blast()

    BLAST.setup()
