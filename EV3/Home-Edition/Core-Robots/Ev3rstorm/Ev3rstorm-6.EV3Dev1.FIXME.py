#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    InfraredSensor, RemoteControl, BeaconSeeker, INPUT_4,
    Leds, Sound
)


LEFT_FOOT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_FOOT_MOTOR = LargeMotor(address=OUTPUT_C)

BAZOOKA_BLAST_MOTOR = MediumMotor(address=OUTPUT_A)

IR_SENSOR = InfraredSensor(address=INPUT_4)
REMOTE_CONTROL = RemoteControl(sensor=IR_SENSOR,
                               channel=1)
BEACON_SEEKER = BeaconSeeker(sensor=IR_SENSOR,
                                channel=1)

LEDS = Leds()
SPEAKER = Sound()

        
while True:
    LEDS.set_color(
        group=Leds.LEFT,
        color=Leds.ORANGE,
        pct=1)
    LEDS.set_color(
        group=Leds.RIGHT,
        color=Leds.ORANGE,
        pct=1)

    if REMOTE_CONTROL.beacon:
        heading_difference = BEACON_SEEKER.heading - (-3)

        proximity_difference = BEACON_SEEKER.distance - 70

        if (heading_difference == 0) and (proximity_difference == 0):
            LEFT_FOOT_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)
            RIGHT_FOOT_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)

            LEDS.set_color(
                group=Leds.LEFT,
                color=Leds.RED,
                pct=1)
            LEDS.set_color(
                group=Leds.RIGHT,
                color=Leds.RED,
                pct=1)

            BAZOOKA_BLAST_MOTOR.run_to_rel_pos(
                speed_sp=1000,   # degrees per second
                position_sp=3 * 360,   # degrees
                stop_action=Motor.STOP_ACTION_HOLD)

            SPEAKER.play(wav_file='/home/robot/sound/Laughing 2.wav').wait()

        else:
            # TODO: fix to make it work
            ...

    else:
        LEFT_FOOT_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)
        RIGHT_FOOT_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)
