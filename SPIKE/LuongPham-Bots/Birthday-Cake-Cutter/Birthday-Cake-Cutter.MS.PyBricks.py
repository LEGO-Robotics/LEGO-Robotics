from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import DriveBase
from pybricks.geometry import Axis
from pybricks.parameters import Button, Direction, Icon, Port, Stop

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
            self.drive_base.drive(
                speed=speed,
                turn_rate=0)

        # backward
        elif remote_button_pressed == (Button.LEFT_MINUS, Button.RIGHT_MINUS):
            self.drive_base.drive(
                speed=-speed,
                turn_rate=0)

        # turn left on the spot
        elif remote_button_pressed == (Button.RIGHT_MINUS, Button.LEFT_PLUS):
            self.drive_base.drive(
                speed=0,
                turn_rate=-turn_rate)

        # turn right on the spot
        elif remote_button_pressed == (Button.LEFT_MINUS, Button.RIGHT_PLUS):
            self.drive_base.drive(
                speed=0,
                turn_rate=turn_rate)

        # turn left forward
        elif remote_button_pressed == (Button.LEFT_PLUS,):
            self.drive_base.drive(
                speed=speed,
                turn_rate=-turn_rate)

        # turn right forward
        elif remote_button_pressed == (Button.RIGHT_PLUS,):
            self.drive_base.drive(
                speed=speed,
                turn_rate=turn_rate)

        # turn left backward
        elif remote_button_pressed == (Button.LEFT_MINUS,):
            self.drive_base.drive(
                speed=-speed,
                turn_rate=turn_rate)

        # turn right backward
        elif remote_button_pressed == (Button.RIGHT_MINUS,):
            self.drive_base.drive(
                speed=-speed,
                turn_rate=-turn_rate)

        # otherwise stop
        else:
            self.drive_base.stop()

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


class BirthdayCakeCutter(RemoteControlledDriveBase):
    WHEEL_DIAMETER = 44   # milimeters
    AXLE_TRACK = 75       # milimeters

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.A,
            first_cutter_motor_port: Port = Port.C,
            second_cutter_motor_port: Port = Port.D):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER,
            axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port,
            left_motor_pos_dir=Direction.COUNTERCLOCKWISE,
            right_motor_port=right_motor_port,
            right_motor_pos_dir=Direction.CLOCKWISE)

        self.hub = InventorHub(top_side=Axis.X,
                               front_side=Axis.Z)

        self.cake_cutting_mode = False

        self.first_cutter_motor = \
            Motor(port=first_cutter_motor_port,
                  positive_direction=Direction.CLOCKWISE)

        self.second_cutter_motor = \
            Motor(port=second_cutter_motor_port,
                  positive_direction=Direction.CLOCKWISE)

    def switch_mode_by_remote(self):
        remote_button_pressed = self.remote.buttons.pressed()

        if remote_button_pressed == (Button.LEFT,):
            if self.cake_cutting_mode:
                self.cake_cutting_mode = False
                print('Mode: Driving')

        elif remote_button_pressed == (Button.RIGHT,):
            if not self.cake_cutting_mode:
                self.cake_cutting_mode = True
                print('Mode: Cake-Cutting')

    def smile(self):
        self.hub.display.image(image=Icon.HAPPY)

    def sing_happy_birthday_by_remote_left_red_button(self):
        if self.remote.buttons.pressed() == (Button.LEFT,):
            self.hub.speaker.play_notes(
                notes=HAPPY_BIRTHDAY_SONG,
                tempo=120)

    def cut_piece_if_right_red_button_pressed(self):
        if self.remote.buttons.pressed() == (Button.RIGHT,):
            self.first_cutter_motor.run_until_stalled(
                speed=50,
                then=Stop.HOLD
            )
            self.second_cutter_motor.run_until_stalled(
                speed=50,
                then=Stop.HOLD
            )

    def main(self):
        self.smile()

        while True:
            self.switch_mode_by_remote()

            if self.cake_cutting_mode:
                ...

            else:
                self.drive_once_by_remote()
            #    self.cut_piece_if_right_red_button_pressed()
            #if self.cake_cutting_mode == False:
            #    
            #    self.sing_happy_birthday_by_remote_left_red_button()
            #el


if __name__ == '__main__':
    BIRTHDAY_CAKE_CUTTER = BirthdayCakeCutter()

    BIRTHDAY_CAKE_CUTTER.main()
