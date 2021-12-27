from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop


class MVP:
    def __init__(
            self,
            drive_motor_port: Port = Port.B,
            steer_motor_port: Port = Port.A):
        self.hub = InventorHub()

        self.drive_motor = Motor(port=drive_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.steer_motor = Motor(port=steer_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

    def calibrate(self):
        self.steer_motor.run_target(
            speed=1000,
            target_angle=0,
            then=Stop.HOLD,
            wait=True)
