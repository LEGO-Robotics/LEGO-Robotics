#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Color, Direction, Port, Stop

from random import randint
from threading import Thread

import sys
sys.path.append(os.path.expanduser('/home/robot'))
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Ev3rstorm(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 26   # milimeters
    AXLE_TRACK = 102      # milimeters


    def __init__(
            self,
            left_leg_motor_port: Port = Port.B, right_leg_motor_port: Port = Port.C,
            bazooka_blast_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_leg_motor_port, right_motor_port=right_leg_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)
        
        self.bazooka_blast_motor = Motor(port=bazooka_blast_motor_port,
                                         positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

    
    def dance_whenever_ir_beacon_pressed(self):
        while True:
            while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.drive_base.turn(angle=randint(-360, 360))

    
    def keep_detecting_objects_by_ir_sensor(self):
        """
        Ev3rstorm reacts by turning his LEDs red and speaking when his IR Sensor detects an object in front
        (inspiration from LEGO Mindstorms EV3 Home Edition: Ev3rstorm: Tutorial #4)
        """
        while True:
            if self.ir_sensor.distance() < 25:
                self.light.on(color=Color.RED)
                self.speaker.play_file(file=SoundFile.OBJECT)
                self.speaker.play_file(file=SoundFile.DETECTED)
                self.speaker.play_file(file=SoundFile.ERROR_ALARM)
                
            else:
                self.light.off()


    def blast_bazooka_whenever_touched(self):
        """
        Ev3rstorm blasts his bazooka when his Touch Sensor is pressed
        (inspiration from LEGO Mindstorms EV3 Home Edition: Ev3rstorm: Tutorial #5)
        """
        MEDIUM_MOTOR_N_ROTATIONS_PER_BLAST = 3
        MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST = MEDIUM_MOTOR_N_ROTATIONS_PER_BLAST * 360

        while True:
            if self.touch_sensor.pressed():
                if self.color_sensor.ambient() < 5:   # 15 not dark enough
                    self.speaker.play_file(file=SoundFile.UP)

                    self.bazooka_blast_motor.run_angle(
                        speed=2 * MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,   # shoot quickly in half a second
                        rotation_angle=-MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,
                        then=Stop.HOLD,
                        wait=True)

                    self.speaker.play_file(file=SoundFile.LAUGHING_1)

                else:
                    self.speaker.play_file(file=SoundFile.DOWN)

                    self.bazooka_blast_motor.run_angle(
                        speed=2 * MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,   # shoot quickly in half a second
                        rotation_angle=MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,
                        then=Stop.HOLD,
                        wait=True)

                    self.speaker.play_file(file=SoundFile.LAUGHING_2)


    def main(self,
             driving_speed: float = 1000   # mm/s
            ):
        """
        Ev3rstorm's main program performing various capabilities
        """
        self.screen.load_image(ImageFile.TARGET)

        # FIXME: following thread seems to fail to run
        Thread(target=self.dance_whenever_ir_beacon_pressed).start()

        # DON'T use IR Sensor in 2 different modes in the same program / loop
        # - https://github.com/pybricks/support/issues/62
        # - https://github.com/ev3dev/ev3dev/issues/1401
        # Thread(target=self.keep_detecting_objects_by_ir_sensor).start()

        Thread(target=self.blast_bazooka_whenever_touched).start()

        self.keep_driving_by_ir_beacon(speed=driving_speed)


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()
    
    EV3RSTORM.main()
