from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import DriveBase
from pybricks.geometry import Axis
from pybricks.parameters import Button, Direction, Icon, Port

# from pybricks.experimental import run_parallel


HAPPY_BIRTHDAY_SONG = [
    'G3/8', 'G3/8', 'A3/4', 'G3/4', 'C4/4', 'B3/2',
    'G3/8', 'G3/8', 'A3/4', 'G3/4', 'D4/4', 'C4/2',
    'G3/8', 'G3/8', 'G4/4', 'E4/4',
    'C4/8', 'C4/8', 'B3/4', 'A3/4',
    'F4/8', 'F4/8', 'E4/4', 'C4/4', 'D4/4', 'C4/2'
]


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

    def drive_once_by_remote(
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

    # this method must be used in a parallel process/thread
    # in order not to block other operations
    def keep_driving_by_remote(
            self,
            speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
            ):
        while True:
            self.drive_once_by_remote(
                speed=speed,
                turn_rate=turn_rate)


class BirthdayCandleBlower(RemoteControlledDriveBase):
    WHEEL_DIAMETER = 44   # milimeters
    AXLE_TRACK = 99       # milimeters

    def __init__(
            self,
            left_motor_port: Port = Port.D, right_motor_port: Port = Port.C,
            fan_motor_port: Port = Port.A):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER,
            axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port,
            left_motor_pos_dir=Direction.COUNTERCLOCKWISE,
            right_motor_port=right_motor_port,
            right_motor_pos_dir=Direction.CLOCKWISE)

        self.hub = InventorHub(top_side=Axis.X,
                               front_side=Axis.Z)

        self.fan_motor = Motor(port=fan_motor_port,
                               positive_direction=Direction.CLOCKWISE)

    def smile(self):
        self.hub.display.image(image=Icon.HAPPY)

    def sing_happy_birthday_by_remote_left_red_button(self):
        if self.remote.buttons.pressed() == (Button.LEFT,):
            self.hub.speaker.play_notes(
                notes=HAPPY_BIRTHDAY_SONG,
                tempo=120)

    def spin_fan_by_remote_right_red_button(self):
        if self.remote.buttons.pressed() == (Button.RIGHT,):
            self.fan_motor.run(speed=1000)

        else:
            self.fan_motor.stop()

    def main(self):
        self.smile()

        while True:
            self.drive_once_by_remote()
            self.sing_happy_birthday_by_remote_left_red_button()
            self.spin_fan_by_remote_right_red_button()


if __name__ == '__main__':
    BIRTHDAY_CANDLE_BLOWER = BirthdayCandleBlower()

    BIRTHDAY_CANDLE_BLOWER.main()
