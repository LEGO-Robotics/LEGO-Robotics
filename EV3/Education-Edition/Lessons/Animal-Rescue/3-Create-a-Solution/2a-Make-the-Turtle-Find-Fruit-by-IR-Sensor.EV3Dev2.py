#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.sound import Sound


TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
IR_SENSOR = InfraredSensor(address=INPUT_4)
SPEAKER = Sound()


def zigzag():
    TANK_DRIVER.on_for_seconds(
        left_speed=-100,
        right_speed=0,
        seconds=1,
        brake=True,
        block=True)

    TANK_DRIVER.on_for_seconds(
        left_speed=0,
        right_speed=-100,
        seconds=1,
        brake=True,
        block=True)


while IR_SENSOR.proximity >= 16:
    zigzag()

SPEAKER.play_file(
    wav_file='/home/robot/sound/Fanfare.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
