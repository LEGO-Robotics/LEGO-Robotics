#!/usr/bin/env micropython


__all__ = 'IRBeaconRemoteControlledTank',


from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor


class IRBeaconRemoteControlledTank:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C, motor_class=LargeMotor,
            ir_sensor_port: str = INPUT_4,   # ref: sites.google.com/site/ev3devpython/learn_ev3_python/using-sensors
            ir_beacon_channel: int = 1):
        self.tank_driver = \
            MoveTank(
                left_motor_port=left_motor_port,
                right_motor_port=right_motor_port,
                motor_class=motor_class)
        self.steer_driver = \
            MoveSteering(
                left_motor_port=left_motor_port,
                right_motor_port=right_motor_port,
                motor_class=motor_class)
        
        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.tank_drive_ir_beacon_channel = ir_beacon_channel

    def drive_once_by_ir_beacon(self, speed: float = 100):
        # forward
        if self.ir_sensor.top_left(channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.top_right(channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=speed)
    
        # backward
        elif self.ir_sensor.bottom_left(channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.bottom_right(channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=-speed)
    
        # turn left on the spot
        elif self.ir_sensor.top_left(channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.bottom_right(channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=-100,
                speed=speed)
    
        # turn right on the spot
        elif self.ir_sensor.top_right(channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.bottom_left(channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=100,
                speed=speed)
    
        # turn left forward
        elif self.ir_sensor.top_left(channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=-50,
                speed=speed)
    
        # turn right forward
        elif self.ir_sensor.top_right(channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=50,
                speed=speed)
    
        # turn left backward
        elif self.ir_sensor.bottom_left(channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=0,
                right_speed=-speed)
    
        # turn right backward
        elif self.ir_sensor.bottom_right(channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=0)
    
        # DISABLING BELOW TO AVOID CONFLICTS
        # otherwise stop
        # else:
        #     self.tank_driver.off(brake=False)

    # this method must be used in a parallel process/thread in order not to block other operations
    def keep_driving_by_ir_beacon(self, speed: float = 100):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    IR_BEACON_REMOTE_CONTROLLED_TANK = IRBeaconRemoteControlledTank()

    IR_BEACON_REMOTE_CONTROLLED_TANK.keep_driving_by_ir_beacon()
