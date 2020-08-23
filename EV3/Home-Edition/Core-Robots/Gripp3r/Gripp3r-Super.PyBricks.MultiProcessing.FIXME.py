#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase

from multiprocessing import Process


class Gripp3r(EV3Brick):
    WHEEL_DIAMETER = 26
    AXLE_TRACK = 115

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            grip_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.drive_base = DriveBase(left_motor=Motor(port=left_motor_port,
                                                     positive_direction=Direction.CLOCKWISE),
                                    right_motor=Motor(port=right_motor_port,
                                                      positive_direction=Direction.CLOCKWISE),
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)
            
        self.drive_base.settings(
            straight_speed=750,   # milimeters per second
            straight_acceleration=750,
            turn_rate=90,   # degrees per second
            turn_acceleration=90)
                
        self.grip_motor = Motor(port=grip_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def keep_driving_by_ir_beacon(
            self, channel: int = 1,
            speed: float = 1000   # milimeters per second
        ):
        while True:
            ir_beacon_buttons_pressed = set(self.ir_sensor.buttons(channel=channel))

            # forward
            if ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
                self.drive_base.drive(
                    speed=speed,
                    turn_rate=0   # degrees per second
                )

            # backward
            elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
                self.drive_base.drive(
                    speed=-speed,
                    turn_rate=0   # degrees per second
                )

            # turn left on the spot
            elif ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
                self.drive_base.drive(
                    speed=0,
                    turn_rate=-90   # degrees per second
                )

            # turn right on the spot
            elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_UP}:
                self.drive_base.drive(
                    speed=0,
                    turn_rate=90   # degrees per second
                )

            # turn left forward
            elif ir_beacon_buttons_pressed == {Button.LEFT_UP}:
                self.drive_base.drive(
                    speed=speed,
                    turn_rate=-90   # degrees per second
                )

            # turn right forward
            elif ir_beacon_buttons_pressed == {Button.RIGHT_UP}:
                self.drive_base.drive(
                    speed=speed,
                    turn_rate=90   # degrees per second
                )

            # turn left backward
            elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN}:
                self.drive_base.drive(
                    speed=-speed,
                    turn_rate=90   # degrees per second
                )

            # turn right backward
            elif ir_beacon_buttons_pressed == {Button.RIGHT_DOWN}:
                self.drive_base.drive(
                    speed=-speed,
                    turn_rate=-90   # degrees per second
                )

            # otherwise stop
            else:
                self.drive_base.stop()


    def grip_or_release_by_ir_beacon(self, speed: float = 500):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                if self.touch_sensor.pressed():
                    self.speaker.play_file(file=SoundFile.AIR_RELEASE)

                    self.grip_motor.run_time(
                        speed=speed,
                        time=1000,
                        then=Stop.BRAKE,
                        wait=True)

                else:
                    self.speaker.play_file(file=SoundFile.AIRBRAKE)

                    self.grip_motor.run(speed=-speed)

                    while not self.touch_sensor.pressed():
                        pass

                    self.grip_motor.stop()

                while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                    pass


    def main(self, speed: float = 1000):
        self.grip_motor.run_time(
            speed=-500,
            time=1000,
            then=Stop.BRAKE,
            wait=True)

        Process(target=self.grip_or_release_by_ir_beacon).start()
            
        self.keep_driving_by_ir_beacon(speed=speed)

        # FIXME: OSError: [Errno 5] EIO: 
        # Unexpected hardware input/output error with a motor or sensor:
        # --> Try unplugging the sensor or motor and plug it back in again.
        # --> To see which sensor or motor is causing the problem,
        #     check the line in your script that matches
        #     the line number given in the 'Traceback' above.
        # --> Try rebooting the hub/brick if the problem persists. 


if __name__ == '__main__':
    GRIPP3R = Gripp3r()

    GRIPP3R.main()
