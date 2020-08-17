#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D, 
    InfraredSensor, RemoteControl, INPUT_4,
    Leds, Sound
)

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TAIL_MOTOR = LargeMotor(address=OUTPUT_B)
CHEST_MOTOR = LargeMotor(address=OUTPUT_D)

IR_SENSOR = InfraredSensor(address=INPUT_4)
beacon = RemoteControl(sensor=IR_SENSOR,
                       channel=1)

LIGHTS = Leds()
SPEAKER = Sound()


def drive_once_by_ir_beacon(channel: int = 1, speed: float = 1000):
    if beacon.red_up and beacon.blue_up:
        TAIL_MOTOR.run_forever(speed_sp=speed)

    elif beacon.red_down and beacon.blue_down:
        TAIL_MOTOR.run_forever(speed_sp=-speed)

    elif beacon.red_up:
        MEDIUM_MOTOR.run_forever(speed_sp=-500)

        TAIL_MOTOR.run_forever(speed_sp=speed)

    elif beacon.blue_up:
        MEDIUM_MOTOR.run_forever(speed_sp=500)

        TAIL_MOTOR.run_forever(speed_sp=speed)

    elif beacon.red_down:
        MEDIUM_MOTOR.on(speed=-500)

        TAIL_MOTOR.on(speed=-speed)

    elif beacon.blue_down:
        MEDIUM_MOTOR.on(speed=500)

        TAIL_MOTOR.run_forever(speed_sp=-speed)

    else:
        MEDIUM_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)

        TAIL_MOTOR.stop(stop_action=Motor.STOP_ACTION_COAST)


def bite_by_ir_beacon(channel: int = 1, speed: float = 1000):
    if beacon.beacon:
        SPEAKER.play(wav_file='/home/robot/sound/Snake hiss.wav')

        CHEST_MOTOR.run_timed(
            speed_sp=speed,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        CHEST_MOTOR.wait_while(Motor.STATE_RUNNING)

        CHEST_MOTOR.run_timed(
            speed_sp=-300,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        CHEST_MOTOR.wait_while(Motor.STATE_RUNNING)

        while beacon.beacon:
            pass


CHEST_MOTOR.run_timed(
    speed_sp=-300,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
CHEST_MOTOR.wait_while(Motor.STATE_RUNNING)

while True:
    drive_once_by_ir_beacon(
        channel=1,
        speed=1000)

    bite_by_ir_beacon(
        channel=1,
        speed=1000)
