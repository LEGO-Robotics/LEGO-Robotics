#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B, right_motor_port=OUTPUT_C)
STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B, right_motor_port=OUTPUT_C)

IR_SENSOR = InfraredSensor(INPUT_4)

SPEAKER = Sound()


MEDIUM_MOTOR.on_for_seconds(
    speed=-50,
    seconds=1,
    brake=True,
    block=True)

while IR_SENSOR.proximity >= 25:
    TANK_DRIVER.on(
        left_speed=75,
        right_speed=75)

TANK_DRIVER.off(brake=True)
        
SPEAKER.play_file(
    wav_file='/home/robot/LEGO-Mindstorms/sounds/Airbrake.wav',
    volume=100,
    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

MEDIUM_MOTOR.on_for_seconds(
    speed=50,
    seconds=1,
    brake=True,
    block=True)

STEER_DRIVER.on_for_degrees(
    steering=100,
    speed=75,
    degrees=850,
    brake=True,
    block=True)

while IR_SENSOR.proximity >= 25:
    TANK_DRIVER.on(
        left_speed=75,
        right_speed=75)

TANK_DRIVER.off(brake=True)

MEDIUM_MOTOR.on(
    speed=-50,
    brake=False,
    block=False)

SPEAKER.play_file(
    wav_file='/home/robot/LEGO-Mindstorms/sounds/Air release.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
