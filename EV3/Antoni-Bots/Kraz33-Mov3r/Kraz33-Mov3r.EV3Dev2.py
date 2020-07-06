#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.led import Leds
from ev3dev2.sound import Sound


class Kraz33Mov3r:
    def __init__(
            self,
            back_foot_motor_port: str = OUTPUT_B, front_foot_motor_port: str = OUTPUT_C,
            gear_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.tank_driver = MoveTank(left_motor_port=back_foot_motor_port,
                                    right_motor_port=front_foot_motor_port,
                                    motor_class=LargeMotor)
            
        self.gear_motor = MediumMotor(address=gear_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=INPUT_4)
        self.ir_beacon_channel = ir_beacon_channel

        self.leds = Leds()
        self.screen = Display()
        self.speaker = Sound()


    def drive_once_by_ir_beacon(self, speed: float = 100):
        # forward
        if self.ir_sensor.top_left(self.ir_beacon_channel) and self.ir_sensor.top_right(self.ir_beacon_channel):
            self.tank_driver.on_for_rotations(
                left_speed=speed,
                right_speed=-speed,
                rotations=3,
                brake=True,
                block=True)

        # backward
        elif self.ir_sensor.bottom_left(self.ir_beacon_channel) and self.ir_sensor.bottom_right(self.ir_beacon_channel):
            self.tank_driver.on_for_rotations(
                left_speed=-speed,
                right_speed=speed,
                rotations=3,
                brake=True,
                block=True)

        # move crazily
        elif self.ir_sensor.beacon(self.ir_beacon_channel):
            self.tank_driver.on_for_rotations(
                left_speed=-speed / 9,
                right_speed=-speed / 9,
                rotations=3,
                brake=True,
                block=True)

        else:
            self.tank_driver.off(brake=False)


    def main(self):
        while True:
            self.drive_once_by_ir_beacon()


if __name__ =='__main__':
    KRAZ33_MOV3R = Kraz33Mov3r()
    
    KRAZ33_MOV3R.main()
