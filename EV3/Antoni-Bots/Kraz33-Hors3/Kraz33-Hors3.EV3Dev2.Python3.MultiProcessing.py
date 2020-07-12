#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor

from multiprocessing import Process


class Kraz33Hors3:
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

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def drive_once_by_ir_beacon(self, speed: float = 100):
        # forward
        if self.ir_sensor.top_left(channel=self.ir_beacon_channel) and self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            self.tank_driver.on_for_seconds(
                left_speed=speed,
                right_speed=-speed,
                seconds=1,
                brake=False,
                block=True)

        # backward
        elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel) and self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            self.tank_driver.on_for_seconds(
                left_speed=-speed,
                right_speed=speed,
                seconds=1,
                brake=False,
                block=True)

        # move crazily
        elif self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            self.gear_motor.on(
                speed=speed,
                brake=False,
                block=False)

            self.tank_driver.on_for_seconds(
                left_speed=-speed / 3,
                right_speed=-speed / 3,
                seconds=1,
                brake=False,
                block=True)

        else:
            self.gear_motor.off(brake=False)
            
    def keep_driving_by_ir_beacon(self, speed: float = 100):
        while True: 
            self.drive_once_by_ir_beacon(speed=speed)


    def back_whenever_touched(self, speed: float = 100):
        while True:
            if self.touch_sensor.is_pressed:
                self.tank_driver.on_for_seconds(
                    left_speed=-speed,
                    right_speed=speed,
                    seconds=1,
                    brake=False,
                    block=True)
                

    def main(self):
        Process(target=self.back_whenever_touched,
                daemon=True).start()

        self.keep_driving_by_ir_beacon()

 
if __name__ == '__main__':
    KRAZ33_HORS3 = Kraz33Hors3()
    
    KRAZ33_HORS3.main()
