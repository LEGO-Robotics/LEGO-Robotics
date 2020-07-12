#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4
)

from multiprocessing import Process


class Kraz33Hors3:
    def __init__(
            self,
            back_foot_motor_port: str = OUTPUT_C, front_foot_motor_port: str = OUTPUT_B,
            gear_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.front_foot_motor = LargeMotor(address=front_foot_motor_port)
        self.back_foot_motor = LargeMotor(address=back_foot_motor_port)

        self.gear_motor = MediumMotor(address=gear_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)


    def drive_once_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        # forward
        if self.remote_control.red_up and self.remote_control.blue_up:
            self.front_foot_motor.run_timed(
                speed_sp=speed,
                time_sp=1000,   # ms
                stop_action=Motor.STOP_ACTION_COAST)
            self.back_foot_motor.run_timed(
                speed_sp=-speed,
                time_sp=1000,   # ms
                stop_action=Motor.STOP_ACTION_COAST)
            self.front_foot_motor.wait_while(Motor.STATE_RUNNING)
            self.back_foot_motor.wait_while(Motor.STATE_RUNNING)
            
        # backward
        elif self.remote_control.red_down and self.remote_control.blue_down:
            self.front_foot_motor.run_timed(
                speed_sp=-speed,
                time_sp=1000,   # ms
                stop_action=Motor.STOP_ACTION_COAST)
            self.back_foot_motor.run_timed(
                speed_sp=speed,
                time_sp=1000,   # ms
                stop_action=Motor.STOP_ACTION_COAST)
            self.front_foot_motor.wait_while(Motor.STATE_RUNNING)
            self.back_foot_motor.wait_while(Motor.STATE_RUNNING)
                       
        # move crazily
        elif self.remote_control.beacon:
            self.gear_motor.run_forever(speed_sp=speed)

            self.front_foot_motor.run_timed(
                speed_sp=speed / 3,
                time_sp=1000,   # ms
                stop_action=Motor.STOP_ACTION_COAST)
            self.back_foot_motor.run_timed(
                speed_sp=speed / 3,
                time_sp=1000,   # ms
                stop_action=Motor.STOP_ACTION_COAST)
            self.front_foot_motor.wait_while(Motor.STATE_RUNNING)
            self.back_foot_motor.wait_while(Motor.STATE_RUNNING)

        else:
            self.gear_motor.stop(stop_action=Motor.STOP_ACTION_COAST)
            
    def keep_driving_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        while True: 
            self.drive_once_by_ir_beacon(speed=speed)

        
    def back_whenever_touched(
            self,
            speed: float = 1000   # deg/s
        ):
        while True:
            if self.touch_sensor.is_pressed:
                self.front_foot_motor.run_timed(
                    speed_sp=-speed,
                    time_sp=1000,   # ms
                    stop_action=Motor.STOP_ACTION_COAST)
                self.back_foot_motor.run_timed(
                    speed_sp=speed,
                    time_sp=1000,   # ms
                    stop_action=Motor.STOP_ACTION_COAST) 
                self.front_foot_motor.wait_while(Motor.STATE_RUNNING)
                self.back_foot_motor.wait_while(Motor.STATE_RUNNING)
                    

    def main(self,
             speed: float = 1000   # deg/s
            ):
        Process(target=self.back_whenever_touched).start()
            
        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    KRAZ33_HORS3 = Kraz33Hors3()
    
    KRAZ33_HORS3.main()
