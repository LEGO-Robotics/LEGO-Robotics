#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TAIL_MOTOR = LargeMotor(address=OUTPUT_B)
CHEST_MOTOR = LargeMotor(address=OUTPUT_D)

IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


def drive_once_by_ir_beacon(channel: int = 1, speed: float = 100):
    if IR_SENSOR.top_left(channel=channel) and IR_SENSOR.top_right(channel=channel):
        TAIL_MOTOR.on(
            speed=speed,
            brake=False,
            block=False)

    elif IR_SENSOR.bottom_left(channel=channel) and IR_SENSOR.bottom_right(channel=channel):
        TAIL_MOTOR.on(
            speed=-speed,
            brake=False,
            block=False)

    elif IR_SENSOR.top_left(channel=channel):
        MEDIUM_MOTOR.on(
            speed=-50,
            brake=False,
            block=False)

        TAIL_MOTOR.on(
            speed=speed,
            brake=False,
            block=False)

    elif IR_SENSOR.top_right(channel=channel):
        MEDIUM_MOTOR.on(
            speed=50,
            brake=False,
            block=False)

        TAIL_MOTOR.on(
            speed=speed,
            brake=False,
            block=False)

    elif IR_SENSOR.bottom_left(channel=channel):
        MEDIUM_MOTOR.on(
            speed=-50,
            brake=False,
            block=False)

        TAIL_MOTOR.on(
            speed=-speed,
            brake=False,
            block=False)

    elif IR_SENSOR.bottom_right(channel=channel):
        MEDIUM_MOTOR.on(
            speed=50,
            brake=False,
            block=False)

        TAIL_MOTOR.on(
            speed=-speed,
            brake=False,
            block=False)

    else:
        MEDIUM_MOTOR.off(brake=True)
        TAIL_MOTOR.off(brake=False)


def bite_by_ir_beacon(channel: int = 1, speed: float = 100):
    if IR_SENSOR.beacon(channel=channel):
        CHEST_MOTOR.on_for_seconds(
            speed=speed,
            seconds=1,
            brake=True,
            block=False)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Snake hiss.wav',
            volume=100,
            play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

        CHEST_MOTOR.on_for_seconds(
            speed=-30,
            seconds=1,
            brake=True,
            block=True)

        while IR_SENSOR.beacon(channel=1):
            pass


CHEST_MOTOR.on_for_seconds(
    speed=-30,
    seconds=1,
    brake=True,
    block=True)

while True:
    drive_once_by_ir_beacon(
        channel=1,
        speed=100)

    bite_by_ir_beacon(
        channel=1,
        speed=100)
