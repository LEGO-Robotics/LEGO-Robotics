#!/usr/bin/env python3
# (Display not yet working in MicroPython as of June 2020)


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound


class Ev3rstorm:
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B,
            right_foot_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4,
            ir_beacon_channel: int = 1):
        self.tank_driver = MoveTank(left_motor_port=left_foot_motor_port,
                                    right_motor_port=right_foot_motor_port,
                                    motor_class=LargeMotor)

        self.shooting_motor = MediumMotor(address=shooting_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

        self.screen = Display()

        self.speaker = Sound()


    def drive_by_ir_beacon(self, speed: float = 100):
        # forward
        if self.ir_sensor.top_left(self.ir_beacon_channel) and self.ir_sensor.top_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=speed)

        # backward
        elif self.ir_sensor.bottom_left(self.ir_beacon_channel) and self.ir_sensor.bottom_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=-speed)

        # turn left on the spot
        elif self.ir_sensor.top_left(self.ir_beacon_channel) and self.ir_sensor.bottom_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=speed)

        # turn right on the spot
        elif self.ir_sensor.top_right(self.ir_beacon_channel) and self.ir_sensor.bottom_left(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=-speed)

        # turn left forward
        elif self.ir_sensor.top_left(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=0,
                right_speed=speed)

        # turn right forward
        elif self.ir_sensor.top_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=0)

        # turn left backward
        elif self.ir_sensor.bottom_left(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=0,
                right_speed=-speed)

        # turn right backward
        elif self.ir_sensor.bottom_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=0)

        # otherwise stop
        else:
            self.tank_driver.off(brake=False)


    def shoot_when_touched(self):
        if self.touch_sensor.is_pressed:
            if self.color_sensor.ambient_light_intensity <= 15:
                self.speaker.play_file(
                    wav_file='/home/robot/sound/Up.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.shooting_motor.on_for_rotations(
                    speed=100,
                    rotations=-3,
                    brake=True,
                    block=True)

            else:
                self.speaker.play_file(
                    wav_file='/home/robot/sound/Down.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.shooting_motor.on_for_rotations(
                    speed=100,
                    rotations=3,
                    brake=True,
                    block=True)
 
    
    def main(self):
        self.screen.image_filename(
            filename='/home/robot/image/Target.bmp',
            clear_screen=True)
    
        while True:
            self.drive_by_ir_beacon()
            
            self.shoot_when_touched()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()