from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Direction, Port


class RemoteControlledDriveBase:
    def __init__(
            self,
            wheel_diameter: float, axle_track: float,   # both in milimeters
            left_motor_port: Port = Port.A,
            left_motor_pos_dir: Direction = Direction.COUNTERCLOCKWISE,
            right_motor_port: Port = Port.B,
            right_motor_pos_dir: Direction = Direction.CLOCKWISE):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=left_motor_pos_dir)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=right_motor_pos_dir)

        self.drive_base = DriveBase(left_motor=self.left_motor,
                                    right_motor=self.right_motor,
                                    wheel_diameter=wheel_diameter,
                                    axle_track=axle_track)

        self.remote = Remote()
        print('Remote Connected!')

    def drive_by_remote(
            self,
            speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
            ):
        remote_button_pressed = self.remote.buttons.pressed()

        # forward
        if remote_button_pressed == (Button.LEFT_PLUS, Button.RIGHT_PLUS):
            self.left_motor.run(speed=speed)
            self.right_motor.run(speed=speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=speed,
            #     turn_rate=0)

        # backward
        elif remote_button_pressed == (Button.LEFT_MINUS, Button.RIGHT_MINUS):
            self.left_motor.run(speed=-speed)
            self.right_motor.run(speed=-speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=-speed,
            #     turn_rate=0)

        # turn left on the spot
        elif remote_button_pressed == (Button.RIGHT_MINUS, Button.LEFT_PLUS):
            self.left_motor.run(speed=-speed)
            self.right_motor.run(speed=speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=0,
            #     turn_rate=-turn_rate)

        # turn right on the spot
        elif remote_button_pressed == (Button.LEFT_MINUS, Button.RIGHT_PLUS):
            self.left_motor.run(speed=speed)
            self.right_motor.run(speed=-speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=0,
            #     turn_rate=turn_rate)

        # turn left forward
        elif remote_button_pressed == (Button.LEFT_PLUS,):
            self.right_motor.run(speed=speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=speed,
            #     turn_rate=-turn_rate)

        # turn right forward
        elif remote_button_pressed == (Button.RIGHT_PLUS,):
            self.left_motor.run(speed=speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=speed,
            #     turn_rate=turn_rate)

        # turn left backward
        elif remote_button_pressed == (Button.LEFT_MINUS,):
            self.right_motor.run(speed=-speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=-speed,
            #     turn_rate=turn_rate)

        # turn right backward
        elif remote_button_pressed == (Button.RIGHT_MINUS,):
            self.left_motor.run(speed=-speed)
            # *** BELOW NOT WORKING ***
            # self.drive_base.drive(
            #     speed=-speed,
            #     turn_rate=-turn_rate)

        # otherwise stop
        else:
            self.left_motor.hold()
            self.right_motor.hold()
            # *** BELOW NOT WORKING ***
            # self.drive_base.stop()

    def main(
            self,
            speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
            ):
        while True:
            self.drive_by_remote(
                speed=speed,
                turn_rate=turn_rate)


if __name__ == '__main__':
    DRIVE_BASE = \
        RemoteControlledDriveBase(
            wheel_diameter=44, axle_track=99,
            left_motor_port=Port.D,
            left_motor_pos_dir=Direction.COUNTERCLOCKWISE,
            right_motor_port=Port.C,
            right_motor_pos_dir=Direction.CLOCKWISE)

    DRIVE_BASE.main()
