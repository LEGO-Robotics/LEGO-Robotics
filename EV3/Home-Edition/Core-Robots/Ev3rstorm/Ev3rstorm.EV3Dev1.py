#!/usr/bin/env python3


"""
original: https://github.com/ev3dev/ev3dev-lang-python-demo/blob/jessie/robots/EV3RSTORM/ev3rstorm.py
"""


from ev3dev.ev3 import (
    Motor, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Leds, Screen
)


class Ev3rstorm:
    def __init__(
            self,
            left_foot_track_motor_port: str = OUTPUT_B, right_foot_track_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4,
            driving_ir_beacon_channel: int = 1, shooting_ir_beacon_channel: int = 2):
        self.left_foot_track_motor = LargeMotor(address=left_foot_track_motor_port)
        self.right_foot_track_motor = LargeMotor(address=right_foot_track_motor_port)

        self.shooting_motor = MediumMotor(address=shooting_motor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.driving_remote_control = RemoteControl(sensor=self.ir_sensor,
                                                    channel=driving_ir_beacon_channel)
        self.shooting_remote_control = RemoteControl(sensor=self.ir_sensor,
                                                     channel=shooting_ir_beacon_channel)

        self.touch_sensor = TouchSensor(address=INPUT_1)
        self.color_sensor = ColorSensor(address=INPUT_3)

        self.leds = Leds()
        self.screen = Screen()

        assert self.left_foot_track_motor.connected
        assert self.right_foot_track_motor.connected
        assert self.shooting_motor.connected

        assert self.ir_sensor.connected
        assert self.touch_sensor.connected
        assert self.color_sensor.connected

        # reset the motors
        for motor in (self.left_foot_track_motor, self.right_foot_track_motor, self.shooting_motor):
            motor.reset()
            motor.position = 0
            motor.stop_action = Motor.STOP_ACTION_BRAKE
        
        self.draw_face()
    

    def draw_face(self):
        w, h = self.screen.shape
        y = h // 2

        eye_xrad = 20
        eye_yrad = 30

        pup_xrad = 10
        pup_yrad = 10

        def draw_eye(x):
            self.screen.draw.ellipse(
                (x - eye_xrad, y - eye_yrad,
                 x + eye_xrad, y + eye_yrad))
            
            self.screen.draw.ellipse(
                (x - pup_xrad, y - pup_yrad,
                 x + pup_xrad, y + pup_yrad),
                fill='black')

        draw_eye(w // 3)
        draw_eye(2 * w // 3)
        self.screen.update()


    def shoot(self, direction='up'):
        """
        Shot a ball in the specified direction (valid choices are 'up' and 'down')
        """
        self.shooting_motor.run_to_rel_pos(
            speed_sp=900,   # degrees per second
            position_sp=-3 * 360 if direction == 'up' else 3 * 360,   # degrees
            stop_action=Motor.STOP_ACTION_BRAKE)
        self.shooting_motor.wait_while(Motor.STATE_RUNNING)


    def rc_loop(self,
                driving_speed: float = 1000   # degrees per second
               ):
        """
        Enter the remote control loop.
        RC buttons on channel 1 control the robot movement, channel 2 is for shooting things.
        The loop ends when the touch sensor is pressed.
        """

        def roll(motor: Motor, led_group: str, speed: float):
            """
            Generate remote control event handler.
            It rolls given motor into given direction (1 for forward, -1 for backward).
            When motor rolls forward, the given led group flashes green, when backward -- red.
            When motor stops, the leds are turned off.
            The on_press function has signature required by RemoteControl class.
            It takes boolean state parameter; True when button is pressed, False otherwise.
            """
            def on_press(state: int):
                if state:
                    # roll when button is pressed
                    motor.run_forever(speed_sp=speed)

                    self.leds.set_color(
                        group=led_group,
                        color=Leds.GREEN if speed > 0 else Leds.RED,
                        pct=1)
                    
                else:
                    # stop otherwise
                    motor.stop(stop_action=Motor.STOP_ACTION_COAST)

                    self.leds.set_color(
                        group=led_group,
                        color=Leds.BLACK,
                        pct=1)

            return on_press

        self.driving_remote_control.on_red_up = \
            roll(motor=self.right_foot_track_motor,
                 led_group=Leds.RIGHT,
                 speed=driving_speed)
            
        self.driving_remote_control.on_red_down = \
            roll(motor=self.right_foot_track_motor,
                 led_group=Leds.RIGHT,
                 speed=-driving_speed)
        
        self.driving_remote_control.on_blue_up = \
            roll(motor=self.left_foot_track_motor,
                 led_group=Leds.LEFT,
                 speed=driving_speed)
        
        self.driving_remote_control.on_blue_down = \
            roll(motor=self.left_foot_track_motor,
                 led_group=Leds.LEFT,
                 speed=-driving_speed)


        def shoot(direction: str):
            def on_press(state: int):
                if state: self.shoot(direction)

            return on_press

        self.shooting_remote_control.on_red_up    = shoot('up')
        self.shooting_remote_control.on_blue_up   = shoot('up')
        self.shooting_remote_control.on_red_down  = shoot('down')
        self.shooting_remote_control.on_blue_down = shoot('down')


        # now that the event handlers are assigned,
        # let's enter the processing loop:
        while not self.touch_sensor.is_pressed:
            self.driving_remote_control.process()

            self.shooting_remote_control.process()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.rc_loop()
