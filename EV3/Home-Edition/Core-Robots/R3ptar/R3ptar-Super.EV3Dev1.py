#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D, 
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Sound
)


class R3ptar:
    def __init__(
            self,
            turn_motor_port: str = OUTPUT_A,
            move_motor_port: str = OUTPUT_B,
            scare_motor_port: str = OUTPUT_D,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.turn_motor = MediumMotor(address=turn_motor_port)
        self.move_motor = LargeMotor(address=move_motor_port)
        self.scare_motor = LargeMotor(address=scare_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=1)
        self.ir_beacon_channel = ir_beacon_channel

        self.noise = Sound()


    def drive_once_by_ir_beacon(self, speed: float = 1000):
        if self.beacon.red_up and self.beacon.blue_up:
            self.move_motor.run_forever(speed_sp=speed)

        elif self.beacon.red_down and self.beacon.blue_down:
            self.move_motor.run_forever(speed_sp=-speed)

        elif self.beacon.red_up:
            self.turn_motor.run_forever(speed_sp=-500)

            self.move_motor.run_forever(speed_sp=speed)

        elif self.beacon.blue_up:
            self.turn_motor.run_forever(speed_sp=500)

            self.move_motor.run_forever(speed_sp=speed)

        elif self.beacon.red_down:
            self.turn_motor.run_forever(speed_sp=-500)

            self.move_motor.run_forever(speed_sp=-speed)

        elif self.beacon.blue_down:
            self.turn_motor.run_forever(speed_sp=500)

            self.move_motor.run_forever(speed_sp=-speed)

        else:
            self.turn_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

            self.move_motor.stop(stop_action=Motor.STOP_ACTION_COAST)


    def bite_by_ir_beacon(self, speed: float = 1000):
        if self.beacon.beacon:
            self.noise.play(wav_file='/home/robot/sound/Snake hiss.wav')

            self.scare_motor.run_timed(
                speed_sp=speed,
                time_sp=1000,
                stop_action=Motor.STOP_ACTION_BRAKE)
            self.scare_motor.wait_while(Motor.STATE_RUNNING)

            self.scare_motor.run_timed(
                speed_sp=-300,
                time_sp=1000,
                stop_action=Motor.STOP_ACTION_BRAKE)
            self.scare_motor.wait_while(Motor.STATE_RUNNING)

            while self.beacon.beacon:
                pass


    def run_away_if_chased(self):
        if self.color_sensor.reflected_light_intensity > 30:
            self.move_motor.run_timed(
                speed_sp=500,
                time_sp=4000,
                stop_action=Motor.STOP_ACTION_BRAKE)
            self.move_motor.wait_while(Motor.STATE_RUNNING)

            for i in range(2):
                self.turn_motor.run_timed(
                    speed_sp=500,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_BRAKE)
                self.turn_motor.wait_while(Motor.STATE_RUNNING)

                self.turn_motor.run_timed(
                    speed_sp=-500,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_BRAKE)
                self.turn_motor.wait_while(Motor.STATE_RUNNING)


    def bite_if_touched(self):
        if self.touch_sensor.is_pressed:
            self.noise.play(wav_file='/home/robot/sound/Snake hiss.wav')

            self.scare_motor.run_timed(
                speed_sp=1000,
                time_sp=1000,
                stop_action=Motor.STOP_ACTION_COAST)
            self.scare_motor.wait_while(Motor.STATE_RUNNING)
        
            self.scare_motor.run_timed(
                speed_sp=-300,
                time_sp=1000,
                stop_action=Motor.STOP_ACTION_COAST)
            self.scare_motor.wait_while(Motor.STATE_RUNNING)


    def main(self, speed: float = 1000):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.bite_by_ir_beacon(speed=speed)

            self.bite_if_touched()
                
            self.run_away_if_chased()


if __name__ == '__main__':
    R3PTAR = R3ptar()
        
    R3PTAR.main(speed=1000)
