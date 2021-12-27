#!/usr/bin/env python3


from ev3dev.ev3 import(
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B
)


LARGE_MOTOR = LargeMotor(address=OUTPUT_B)
MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)


LARGE_MOTOR.run_forever(speed_sp=1000)

for i in range(3):
    MEDIUM_MOTOR.run_timed(
        speed_sp=100,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_COAST)
    MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

    MEDIUM_MOTOR.run_timed(
        speed_sp=-100,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_COAST)
    MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)