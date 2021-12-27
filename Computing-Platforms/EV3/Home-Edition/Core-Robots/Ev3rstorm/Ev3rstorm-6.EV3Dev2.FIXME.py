#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound


class Ev3rstorm:
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            bazooka_blast_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.tank_driver = MoveTank(left_motor_port=left_foot_motor_port,
                                    right_motor_port=right_foot_motor_port,
                                    motor_class=LargeMotor)

        self.bazooka_blast_motor = MediumMotor(address=bazooka_blast_motor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.leds = Leds()
        self.speaker = Sound()


    def seek_wheeler(self):
        self.leds.animate_rainbow(
            group1=Leds.LEFT,
            group2=Leds.RIGHT,
            increment_by=0.1,
            sleeptime=0.5,
            duration=5,
            block=True)

        if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            heading_difference = self.ir_sensor.heading(channel=self.ir_beacon_channel) - (-3)

            proximity_difference = self.ir_sensor.distance(channel=self.ir_beacon_channel) - 70

            if (heading_difference == 0) and (proximity_difference == 0):
                self.tank_driver.off(brake=True)

                self.leds.animate_rainbow(
                    group1=Leds.LEFT,
                    group2=Leds.RIGHT,
                    increment_by=0.1,
                    sleeptime=0.5,
                    duration=5,
                    block=True)

                self.bazooka_blast_motor.on_for_rotations(
                    speed=100,
                    rotations=3,
                    brake=True,
                    block=True)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Laughing 2.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            else:
                # FIXME: make it work
                self.tank_driver.on(
                    left_speed=max(min((3 * proximity_difference + 4 * heading_difference) / 5, 100), -100),
                    right_speed=max(min((3 * proximity_difference - 4 * heading_difference) / 5, 100), -100))

        else:
            self.tank_driver.off(brake=True)


    def main(self):
        while True:
            self.seek_wheeler()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
