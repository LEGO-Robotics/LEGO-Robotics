from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase


class Tricky:
    WHEEL_DIAMETER = 44
    AXLE_TRACK = 88

    def __init__(
            self,
            left_wheel_motor_port: Port = Port.A,
            right_wheel_motor_port: Port = Port.B,
            sport_motor_port: Port = Port.C,
            distance_sensor_port: Port = Port.D,
            color_sensor_port: Port = Port.E):
        self.hub = InventorHub()

        left_motor = Motor(port=left_wheel_motor_port,
                           positive_direction=Direction.COUNTERCLOCKWISE)
        right_motor = Motor(port=right_wheel_motor_port,
                            positive_direction=Direction.CLOCKWISE)
        self.driving_base = DriveBase(left_motor=left_motor,
                                      right_motor=right_motor,
                                      wheel_diameter=self.WHEEL_DIAMETER,
                                      axle_track=self.AXLE_TRACK)

        self.sport_motor = Motor(port=sport_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.distance_sensor = UltrasonicSensor(port=distance_sensor_port)
