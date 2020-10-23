#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor, ColorSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop

from time import sleep

from dinor3x_util import cyclic_position_offset


class Dinor3x(EV3Brick):
    FAST_WALK_SPEED = 800
    NORMAL_WALK_SPEED = 400
    SLOW_WALK_SPEED = 200

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            jaw_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.jaw_motor = Motor(port=jaw_motor_port,
                               positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.roaring = False
        self.walk_speed = self.NORMAL_WALK_SPEED

    def roar_by_ir_beacon(self):
        """
        Dinor3x roars when the Beacon button is pressed
        """
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.roaring = True
            self.open_mouth()
            self.roar()

        elif self.roaring:
            self.roaring = False
            self.close_mouth()

    def keep_roaring_by_ir_beacon(self):
        while True:
            self.roar_by_ir_beacon()

    def change_speed_by_color(self):
        """
        Dinor3x changes its speed when detecting some colors
        - Red: walk fast
        - Green: walk normally
        - White: walk slowly
        """
        if self.color_sensor.color() == Color.RED:
            self.speaker.say(text='RUN!')
            self.walk_speed = self.FAST_WALK_SPEED
            self.walk(speed=self.walk_speed)

        elif self.color_sensor.color() == Color.GREEN:
            self.speaker.say(text='Normal')
            self.walk_speed = self.NORMAL_WALK_SPEED
            self.walk(speed=self.walk_speed)

        elif self.color_sensor.color() == Color.WHITE:
            self.speaker.say(text='slow......')
            self.walk_speed = self.SLOW_WALK_SPEED
            self.walk(speed=self.walk_speed)

    def keep_changing_speed_by_color(self):
        while True:
            self.change_speed_by_color()

    def walk_by_ir_beacon(self):
        """
        Dinor3x walks or turns according to instructions from the IR Beacon
        - 2 top/up buttons together: walk forward
        - 2 bottom/down buttons together: walk backward
        - Top Left / Red Up: turn left on the spot
        - Top Right / Blue Up: turn right on the spot
        - Bottom Left / Red Down: stop
        - Bottom Right / Blue Down: calibrate to make the legs straight
        """
        ir_beacon_buttons_pressed = \
            set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.walk(speed=self.walk_speed)

        # backward
        elif ir_beacon_buttons_pressed == \
                {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.walk(speed=-self.walk_speed)

        # turn left on the spot
        elif ir_beacon_buttons_pressed == {Button.LEFT_UP}:
            self.turn(speed=self.walk_speed)

        # turn right on the spot
        elif ir_beacon_buttons_pressed == {Button.RIGHT_UP}:
            self.turn(speed=-self.walk_speed)

        # stop
        elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN}:
            self.left_motor.hold()
            self.right_motor.hold()

        # turn right backward
        elif ir_beacon_buttons_pressed == {Button.RIGHT_DOWN}:
            self.calibrate_legs()

    def keep_walking_by_ir_beacon(self):
        while True:
            self.walk_by_ir_beacon()

    def jump(self):
        """
        Dinor3x Mission 02 Challenge: make it jump
        """
        ...

    # TRANSLATED FROM EV3-G MY BLOCKS
    # -------------------------------

    def calibrate_legs(self):
        self.left_motor.run(speed=100)
        self.right_motor.run(speed=200)

        while self.touch_sensor.pressed():
            pass

        self.left_motor.hold()
        self.right_motor.hold()

        self.left_motor.run(speed=400)

        while not self.touch_sensor.pressed():
            pass

        self.left_motor.hold()

        self.left_motor.run_angle(
            rotation_angle=-0.2 * 360,
            speed=500,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run(speed=400)

        while not self.touch_sensor.pressed():
            pass

        self.right_motor.hold()

        self.right_motor.run_angle(
            rotation_angle=-0.2 * 360,
            speed=500,
            then=Stop.HOLD,
            wait=True)

        self.left_motor.reset_angle(angle=0)
        self.right_motor.reset_angle(angle=0)

    def leg_to_pos(
            self,
            speed: float = 1000,
            left_position: float = 0,
            right_position: float = 0):
        self.left_motor.hold()
        self.right_motor.hold()

        self.left_motor.run_angle(
            speed=speed,
            rotation_angle=left_position -
                           cyclic_position_offset(
                                rotation_sensor=self.left_motor.angle(),
                                cyclic_degrees=360),
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run_angle(
            speed=speed,
            rotation_angle=right_position -
                           cyclic_position_offset(
                                rotation_sensor=self.right_motor.angle(),
                                cyclic_degrees=360),
            then=Stop.HOLD,
            wait=True)

    def position_legs(
            self,
            speed: float = 1000,
            left_position: float = 0,
            right_position: float = 0):
        self.left_motor.hold()
        self.right_motor.hold()

        self.left_motor.run_angle(
            speed=speed,
            rotation_angle=left_position - self.left_motor.angle() % 360,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run_angle(
            speed=speed,
            rotation_angle=right_position - self.right_motor.angle() % 360,
            then=Stop.HOLD,
            wait=True)

    def leg_adjust(
            self,
            cyclic_degrees: float = 360,
            speed: float = 1000,
            leg_offset_percent: float = 0,
            mirrored_adjust: bool = False,
            brake: bool = True):
        self.left_motor.hold()
        self.right_motor.hold()

        diff = cyclic_position_offset(
                rotation_sensor=self.left_motor.angle(),
                cyclic_degrees=cyclic_degrees) \
            - cyclic_position_offset(
                rotation_sensor=self.right_motor.angle(),
                cyclic_degrees=cyclic_degrees)

        if diff > (cyclic_degrees / 2):
            diff -= cyclic_degrees

        if diff < -180:
            diff += cyclic_degrees

        if speed >= 0:
            if diff >= 0:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

        else:
            if diff >= 0:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            self.screen.clear()
            self.screen.draw_text(
                x=2, y=5,
                text='{}, {}'.format(speed, diff),
                text_color=Color.BLACK,
                background_color=None)

    def adjust_legs(self, speed: float = 1000, brake: bool = True):
        self.left_motor.hold()
        self.right_motor.hold()

        diff = (self.left_motor.angle() % 360) \
            - (self.right_motor.angle() % 360)

        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360

        if speed >= 0:
            if diff >= 0:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

        else:
            if diff >= 0:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

    def walk(self, speed: float = 1000):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        self.left_motor.run(speed=-speed)
        self.right_motor.run(speed=-speed)

    def walk_n_steps(self, speed: float = 1000, n_steps: int = 1):
        ...

    def turn(self, speed: float = 1000):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        if speed >= 0:
            self.left_motor.run_angle(
                rotation_angle=180,
                speed=speed,
                then=Stop.HOLD,
                wait=True)

        else:
            self.right_motor.run_angle(
                rotation_angle=180,
                speed=-speed,
                then=Stop.HOLD,
                wait=True)

        self.left_motor.run(speed=speed)
        self.right_motor.run(speed=-speed)

    def turn_n_steps(self, speed: float = 1000, n_steps: int = 1):
        ...

    def close_mouth(self):
        self.jaw_motor.run_time(
            speed=-200,
            time=1000,
            then=Stop.COAST,
            wait=False)

    def open_mouth(self):
        self.jaw_motor.run_time(
            speed=200,
            time=1000,
            then=Stop.COAST,
            wait=False)

    def _open_mouth(self):
        self.jaw_motor.run(speed=200)
        sleep(1)
        self.jaw_motor.stop()

    def walk_until_blocked(self):
        self.left_motor.run(speed=-400)
        self.right_motor.run(speed=-400)

        while self.ir_sensor.distance() >= 25:
            pass

        self.left_motor.hold()
        self.right_motor.hold()

    def back_away(self):
        self.left_motor.run_angle(
            speed=750,
            rotation_angle=3 * 360,
            then=Stop.HOLD,
            wait=False)
        self.right_motor.run_angle(
            speed=750,
            rotation_angle=3 * 360,
            then=Stop.HOLD,
            wait=True)

    def roar(self):
        self.speaker.play_file(file=SoundFile.T_REX_ROAR)

        self.jaw_motor.run_angle(
            speed=400,
            rotation_angle=-60,
            then=Stop.HOLD,
            wait=True)

        for i in range(12):
            self.jaw_motor.run_time(
                speed=-400,
                time=0.05 * 1000,
                then=Stop.HOLD,
                wait=True)

            self.jaw_motor.run_time(
                speed=400,
                time=0.05 * 1000,
                then=Stop.HOLD,
                wait=True)

        self.jaw_motor.run_time(
            speed=200,
            time=0.5 * 1000,
            then=Stop.COAST,
            wait=True)

    # MAIN
    # ----

    def main(self):
        self.close_mouth()

        while True:
            self.roar_by_ir_beacon()
            self.change_speed_by_color()
            self.walk_by_ir_beacon()


if __name__ == '__main__':
    DINOR3X = Dinor3x()

    DINOR3X.main()
