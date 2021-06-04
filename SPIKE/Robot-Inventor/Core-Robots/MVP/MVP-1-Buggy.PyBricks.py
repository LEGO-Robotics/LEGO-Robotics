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


if __name__ == '__main__':
    MVP_BUGGY = MVP()

    MVP_BUGGY.calibrate()

    MVP_BUGGY.steer_motor.run_angle(
        speed=350,
        rotation_angle=50,
        then=Stop.HOLD,
        wait=True)

    MVP_BUGGY.drive_motor.run_angle(
        speed=800,
        rotation_angle=-16 * 360,
        then=Stop.HOLD,
        wait=True)
