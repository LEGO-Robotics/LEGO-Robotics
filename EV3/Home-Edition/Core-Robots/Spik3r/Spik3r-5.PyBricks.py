#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop
from pybricks.tools import wait


BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A, 
                     positive_direction=Direction.CLOCKWISE)
GO_MOTOR = Motor(port=Port.B,
                 positive_direction=Direction.CLOCKWISE)
STING_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)

IR_SENSOR = InfraredSensor(port=Port.S4)


MEDIUM_MOTOR.run_time(
    speed=500,
    time=1000,
    then=Stop.HOLD,
    wait=True)

MEDIUM_MOTOR.run_time(
    speed=-500,
    time=0.3 * 1000,
    then=Stop.HOLD,
    wait=True)

STING_MOTOR.run_time(
    speed=400,
    time=1000,
    then=Stop.HOLD,
    wait=True)

GO_MOTOR.run(speed=-500)

BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

ir_beacon_distance = ir_beacon_angle = None

while (ir_beacon_distance is None) or (ir_beacon_angle is None) or (ir_beacon_distance >= 30):
    ir_beacon_distance, ir_beacon_angle = IR_SENSOR.beacon(channel=1)

while ir_beacon_angle <= 5:
    ir_beacon_distance, ir_beacon_angle = IR_SENSOR.beacon(channel=1)

GO_MOTOR.run(speed=-200)

while ir_beacon_angle >= 3:
    ir_beacon_distance, ir_beacon_angle = IR_SENSOR.beacon(channel=1)

GO_MOTOR.stop()

BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

for i in range(3):
    GO_MOTOR.run_angle(
        speed=-1000,
        rotation_angle=10,
        then=Stop.HOLD,
        wait=True)

    STING_MOTOR.run_angle(
        speed=-750,
        rotation_angle=220,
        then=Stop.HOLD,
        wait=True)

    wait(time=0.1 * 1000)

    STING_MOTOR.run_time(
        speed=-1000,
        time=1000,
        then=Stop.HOLD,
        wait=True)

    STING_MOTOR.run_time(
        speed=400,
        time=1000,
        then=Stop.HOLD,
        wait=True)

    # to avoid jerking
    wait(time=1000)

GO_MOTOR.run(speed=1000)

BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

for i in range(5):
    MEDIUM_MOTOR.run_time(
        speed=750,
        time=0.2 * 1000,
        then=Stop.HOLD,
        wait=True)

    MEDIUM_MOTOR.run_time(
        speed=-750,
        time=0.2 * 1000,
        then=Stop.HOLD,
        wait=True)

BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

GO_MOTOR.run_angle(
    speed=-1000,
    rotation_angle=2 * 360,
    then=Stop.HOLD,
    wait=True)

GO_MOTOR.run_angle(
    speed=1000,
    rotation_angle=2 * 360,
    then=Stop.HOLD,
    wait=True)
