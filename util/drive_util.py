__all__ = 'IRBeaconDriver',


from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor


class IRBeaconDriver:
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
        
        self.ir_sensor = InfraredSensor(ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
    

    def drive_once_by_ir_beacon(self, speed: float = 100):
        if self.ir_sensor.top_left(self.ir_beacon_channel) and \
                self.ir_sensor.top_right(self.ir_beacon_channel):
            # go forward
            self.tank_driver.on(
                left_speed=speed,
                right_speed=speed)
    
        elif self.ir_sensor.bottom_left(self.ir_beacon_channel) and \
                self.ir_sensor.bottom_right(self.ir_beacon_channel):
            # go backward
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=-speed)
    
        elif self.ir_sensor.top_left(self.ir_beacon_channel) and \
                self.ir_sensor.bottom_right(self.ir_beacon_channel):
            # turn around left
            self.steer_driver.on(
                steering=-100,
                speed=speed)
    
        elif self.ir_sensor.top_right(self.ir_beacon_channel) and \
                self.ir_sensor.bottom_left(self.ir_beacon_channel):
            # turn around right
            self.steer_driver.on(
                steering=100,
                speed=speed)
    
        elif self.ir_sensor.top_left(self.ir_beacon_channel):
            # turn left forward
            self.steer_driver.on(
                steering=-50,
                speed=speed)
    
        elif self.ir_sensor.top_right(self.ir_beacon_channel):
            # turn right forward
            self.steer_driver.on(
                steering=50,
                speed=speed)
    
        elif self.ir_sensor.bottom_left(self.ir_beacon_channel):
            # turn left backward
            self.tank_driver.on(
                left_speed=0,
                right_speed=-speed)
    
        elif self.ir_sensor.bottom_right(self.ir_beacon_channel):
            # turn right backward
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=0)
    
        else:
            # stop moving
            self.tank_driver.off(brake=False)

    # this method must be used in a parallel process in order not to block other operations
    def keep_driving_by_ir_beacon(self, speed: float = 100):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)
