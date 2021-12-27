#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.sound import Sound

from threading import Thread


class R3ptar:
    def __init__(
            self,
            turn_motor_port: str = OUTPUT_A,
            move_motor_port: str = OUTPUT_B,
            scare_motor_port: str = OUTPUT_D,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.turn_motor = MediumMotor(address=turn_motor_port)
        self.move_motor = LargeMotor(address=move_motor_port)
        self.scare_motor = LargeMotor(address=scare_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.noise = Sound()


    def keep_driving_by_ir_beacon(self, speed: float = 100):
        while True:
            if self.ir_sensor.top_left(channel=self.ir_beacon_channel) and \
                    self.ir_sensor.top_right(channel=self.ir_beacon_channel):
                self.move_motor.on(
                    speed=speed,
                    brake=False,
                    block=False)

            elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel) and \
                    self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
                self.move_motor.on(
                    speed=-speed,
                    brake=False,
                    block=False)

            elif self.ir_sensor.top_left(channel=self.ir_beacon_channel):
                self.turn_motor.on(
                    speed=-50,
                    brake=False,
                    block=False)

                self.move_motor.on(
                    speed=speed,
                    brake=False,
                    block=False)

            elif self.ir_sensor.top_right(channel=self.ir_beacon_channel):
                self.turn_motor.on(
                    speed=50,
                    brake=False,
                    block=False)

                self.move_motor.on(
                    speed=speed,
                    brake=False,
                    block=False)

            elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel):
                self.turn_motor.on(
                    speed=-50,
                    brake=False,
                    block=False)

                self.move_motor.on(
                    speed=-speed,
                    brake=False,
                    block=False)

            elif self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
                self.turn_motor.on(
                    speed=50,
                    brake=False,
                    block=False)

                self.move_motor.on(
                    speed=-speed,
                    brake=False,
                    block=False)

            else:
                self.turn_motor.off(brake=True)

                self.move_motor.off(brake=False)


    def bite_by_ir_beacon(self, speed: float = 100):
        while True:
            if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                self.scare_motor.on_for_seconds(
                    speed=speed,
                    seconds=1,
                    brake=True,
                    block=False)

                self.noise.play_file(
                    wav_file='/home/robot/sound/Snake hiss.wav',
                    volume=100,
                    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                self.scare_motor.on_for_seconds(
                    speed=-speed,
                    seconds=1,
                    brake=True,
                    block=True)

                while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                    pass


    def run_away_if_chased(self):
        while True:
            if self.color_sensor.reflected_light_intensity > 30:
                self.move_motor.on_for_seconds(
                    speed=50,
                    seconds=4,
                    brake=True,
                    block=False)

                for i in range(2):
                    self.turn_motor.on_for_seconds(
                        speed=50,
                        seconds=1,
                        brake=False,
                        block=True)

                    self.turn_motor.on_for_seconds(
                        speed=-50,
                        seconds=1,
                        brake=False,
                        block=True)


    def bite_if_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                self.scare_motor.on_for_seconds(
                    speed=100,
                    seconds=1,
                    brake=True,
                    block=False)

                self.noise.play_file(
                    wav_file='/home/robot/sound/Snake hiss.wav',
                    volume=100,
                    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                self.scare_motor.on_for_seconds(
                    speed=-10,
                    seconds=10,
                    brake=True,
                    block=True)


    def main(self, speed: float = 100):
        Thread(target=self.bite_by_ir_beacon,
               daemon=True).start()

        Thread(target=self.bite_if_touched,
               daemon=True).start()

        Thread(target=self.run_away_if_chased,
               daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)

        # FIXME: ValueError: invalid syntax for integer with base 10: '' or '\x00'
        # when multiple Threads access the same InfraredSensor


if __name__ == '__main__':
    R3PTAR = R3ptar()
        
    R3PTAR.main(speed=100)
