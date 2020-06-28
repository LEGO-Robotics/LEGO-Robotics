#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor
from ev3dev2.sound import Sound

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
IR_BEACON_DRIVER = \
    IRBeaconRemoteControlledTank(
        left_motor_port=OUTPUT_B,
        right_motor_port=OUTPUT_C,
        motor_class=LargeMotor,
        ir_sensor_port=INPUT_4,
        ir_beacon_channel=1)

TOUCH_SENSOR = TouchSensor(address=INPUT_1)
IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


def drive_by_ir_beacon(channel: int = 1, speed: float = 100):
    if IR_SENSOR.top_left(channel) and IR_SENSOR.top_right(channel):
        # go forward
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=speed)
    
    elif IR_SENSOR.bottom_left(channel) and IR_SENSOR.bottom_right(channel):
        # go backward
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=-speed)

    elif IR_SENSOR.top_left(channel) and IR_SENSOR.bottom_right(channel):
        # turn around left
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=speed)

    elif IR_SENSOR.top_right(channel) and IR_SENSOR.bottom_left(channel):
        # turn around right
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=-speed)

    elif IR_SENSOR.top_left(channel):
        # turn left
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=speed)

    elif IR_SENSOR.top_right(channel):
        # turn right
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=0)

    elif IR_SENSOR.bottom_left(channel):
        # left backward
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=-speed)

    elif IR_SENSOR.bottom_right(channel):
        # right backward
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=0)

    else:
        TANK_DRIVER.off(brake=False)


while True:
    IR_BEACON_DRIVER.drive(speed=100)
    # drive_by_ir_beacon(
    #     channel=1,
    #     speed=100)

    if IR_SENSOR.beacon(channel=1):
        if TOUCH_SENSOR.is_pressed:
            MEDIUM_MOTOR.on_for_seconds(
                speed=50,
                seconds=1,
                brake=True,
                block=True)

        else:
            MEDIUM_MOTOR.on(
                speed=-50,
                brake=False,
                block=False)

            TOUCH_SENSOR.wait_for_pressed()

            MEDIUM_MOTOR.off(brake=True)

        # *** NotImplementedError
        # IR_SENSOR.wait_for_released(
        #     buttons=['beacon'])
        while IR_SENSOR.beacon(channel=1):
            pass
