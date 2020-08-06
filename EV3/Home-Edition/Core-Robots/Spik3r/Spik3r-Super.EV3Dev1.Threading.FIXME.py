#!/usr/bin/env python3


from ev3dev.ev3 import( 
    Motor, OUTPUT_A, OUTPUT_B, OUTPUT_D,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Screen, Sound
)

from PIL import Image
from threading import Thread


class Spik3r:
    def __init__(
            self,
            sting_motor_port: str = OUTPUT_D, go_motor_port: str = OUTPUT_B,
            claw_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.sting_motor = Motor(address=sting_motor_port)
        self.go_motor = Motor(address=go_motor_port)
        self.claw_motor = Motor(address=claw_motor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=self.ir_beacon_channel)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.dis = Screen()
        self.speaker = Sound()


    def sting_by_ir_beacon(self):
        while True:
            if self.beacon.beacon:
                self.sting_motor.run_to_rel_pos(
                    speed_sp=750,
                    position=-220,
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.sting_motor.wait_while(Motor.STATE_RUNNING)

                self.sting_motor.run_timed(
                    speed_sp=-1000,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.sting_motor.wait_while(Motor.STATE_RUNNING)

                self.sting_motor.run_timed(
                    speed_sp=1000,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.sting_motor.wait_while(Motor.STATE_RUNNING)

                while self.beacon.beacon:
                    pass


    def be_noisy_to_people(self):
        while True:
            if self.color_sensor.reflected_light_intensity > 30:
                for i in range(4):
                    self.speaker.play_song((
                        ('D4', 'e3'),      
                        ('D4', 'e3'),
                        ('D4', 'e3'),
                        ('G4', 'h'),       
                        ('D5', 'h'),
                        ('C5', 'e3'),      
                        ('B4', 'e3'),
                        ('A4', 'e3'),
                        ('G5', 'h'),
                        ('D5', 'q'),
                        ('C5', 'e3'),      
                        ('B4', 'e3'),
                        ('A4', 'e3'),
                        ('G5', 'h'),
                        ('D5', 'q'),
                        ('C5', 'e3'),      
                        ('B4', 'e3'),
                        ('C5', 'e3'),
                        ('A4', 'h.')
                    ))
                        

    def pinch_if_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                self.claw_motor.run_timed(
                    speed_sp=500,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.claw_motor.wait_while(Motor.STATE_RUNNING)

                self.claw_motor.run_timed(
                    speed_sp=-500,
                    time_sp=0.3 * 1000,
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.claw_motor.wait_while(Motor.STATE_RUNNING)


    def keep_driving_by_ir_beacon(self):
        while True:
            if self.beacon.red_up and self.beacon.blue_up:
                self.go_motor.run_forever(speed_sp=910)

            elif self.beacon.blue_up:
                self.go_motor.run_forever(speed_sp=-1000)

            else:
                self.go_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)


    def main(self):
        self.dis.image.paste(im=Image.open('/home/robot/image/Evil.bmp'))
        self.dis.update()

        # FIXME: ValueError: invalid literal for int() with base 10: '' or '9\n9'
        # when multiple threads access the same Sensor
        Thread(target=self.pinch_if_touched,
               daemon=True).start()

        Thread(target=self.be_noisy_to_people,
               daemon=True).start()

        Thread(target=self.sting_by_ir_beacon,
               daemon=True).start()
        
        self.keep_driving_by_ir_beacon() 


if __name__ == '__main__':
    SPIK3R = Spik3r()

    SPIK3R.main()
