#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A,
    InfraredSensor, RemoteControl, INPUT_4,
    Sound
)


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

IR_SENSOR = InfraredSensor(address=INPUT_4)
BEACON_CONTROL = RemoteControl(sensor=IR_SENSOR,
                               channel=1)

SPEAKER = Sound()

is_gripping = False


while True:
    if BEACON_CONTROL.beacon:
        if is_gripping:
            MEDIUM_MOTOR.run_timed(
                speed_sp=1000,
                time_sp=2000,
                stop_action=Motor.STOP_ACTION_BRAKE)
            MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

            SPEAKER.play(wav_file='/home/robot/sound/Air release.wav').wait()

            is_gripping = False

        else:
            MEDIUM_MOTOR.run_timed(
                speed_sp=-1000,
                time_sp=2000,
                stop_action=Motor.STOP_ACTION_BRAKE)
            MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

            SPEAKER.play(wav_file='/home/robot/sound/Airbrake.wav').wait()

            is_gripping = True

        while BEACON_CONTROL.beacon:
            pass
