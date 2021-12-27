#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_4,
    Sound
)


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
LEFT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_MOTOR = LargeMotor(address=OUTPUT_C)

TOUCH_SENSOR = TouchSensor(address=INPUT_1)
IR_SENSOR = InfraredSensor(address=INPUT_4)
BEACON_CONTROL = RemoteControl(sensor=IR_SENSOR,
                               channel=1)

SPEAKER = Sound() 


def drive_once_by_ir_beacon(speed: float = 1000):
    if BEACON_CONTROL.red_up and BEACON_CONTROL.blue_up:
        # go forward
        LEFT_MOTOR.run_forever(speed_sp=speed)
        RIGHT_MOTOR.run_forever(speed_sp=speed)
    
    elif BEACON_CONTROL.red_down and BEACON_CONTROL.blue_down:
        # go backward
        LEFT_MOTOR.run_forever(speed_sp=-speed)
        RIGHT_MOTOR.run_forever(speed_sp=-speed)

    elif BEACON_CONTROL.red_up and BEACON_CONTROL.blue_down:
        # turn around left
        LEFT_MOTOR.run_forever(speed_sp=-speed)
        RIGHT_MOTOR.run_forever(speed_sp=speed)

    elif BEACON_CONTROL.red_down and BEACON_CONTROL.blue_up:
        # turn around right
        LEFT_MOTOR.run_forever(speed_sp=speed)
        RIGHT_MOTOR.run_forever(speed_sp=-speed)

    elif BEACON_CONTROL.red_up:
        # turn left
        LEFT_MOTOR.run_forever(speed_sp=0)
        RIGHT_MOTOR.run_forever(speed_sp=speed)

    elif BEACON_CONTROL.blue_up:
        # turn right
        LEFT_MOTOR.run_forever(speed_sp=speed)
        RIGHT_MOTOR.run_forever(speed_sp=0)

    elif BEACON_CONTROL.red_down:
        # left backward
        LEFT_MOTOR.run_forever(speed_sp=0)
        RIGHT_MOTOR.run_forever(speed_sp=-speed)

    elif BEACON_CONTROL.blue_down:
        # right backward
        LEFT_MOTOR.run_forever(speed_sp=-speed)
        RIGHT_MOTOR.run_forever(speed_sp=0)

    else:
        LEFT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)
        RIGHT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)


while True:
    drive_once_by_ir_beacon(speed=1000)

    if BEACON_CONTROL.beacon:
        if TOUCH_SENSOR.is_pressed:
            MEDIUM_MOTOR.run_timed(
                speed_sp=500,
                time_sp=1000,
                stop_action=Motor.STOP_ACTION_BRAKE)
            MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

        else:
            MEDIUM_MOTOR.run_forever(speed_sp=-500)

            while not TOUCH_SENSOR.is_pressed:
                pass

            MEDIUM_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)

        while BEACON_CONTROL.beacon:
            pass
