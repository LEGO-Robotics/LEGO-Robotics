from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase


class Tricky:
    WHEEL_DIAMETER = 44
    AXLE_TRACK = 88

    def __init__(
            self,
            left_wheel_motor_port: Port = Port.A,
            right_wheel_motor_port: Port = Port.B,
            distance_sensor_port: Port = Port.D):
        self.hub = InventorHub()

        left_motor = Motor(port=left_wheel_motor_port,
                           positive_direction=Direction.COUNTERCLOCKWISE)
        right_motor = Motor(port=right_wheel_motor_port,
                            positive_direction=Direction.CLOCKWISE)
        self.drive_base = DriveBase(left_motor=left_motor,
                                    right_motor=right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)

        self.distance_sensor = UltrasonicSensor(port=distance_sensor_port)


if __name__ == '__main__':
    TRICKY = Tricky()

    # FIXME: below causes Inventor Hub to hang
    # TRICKY.distance_sensor.lights.on(100)

    while True:
        # Tricky will begin when
        # the Distance Sensor detects something closer than 10 cm
        if TRICKY.distance_sensor.distance() < 100:
            TRICKY.drive_base.turn(angle=360)
            TRICKY.drive_base.turn(angle=-360)
