from mindstorms import MSHub, Motor, MotorPair, DistanceSensor


class Tricky:
    def __init__(
            self,
            left_motor_port: str = 'A', right_motor_port: str = 'B',
            catapult_motor_port: str = 'C',
            distance_sensor_port: str = 'D'):
        self.hub = MSHub()

        self.motor_pair = MotorPair(left_motor_port, right_motor_port)

        self.catapult_motor = Motor(catapult_motor_port)

        self.distance_sensor = DistanceSensor(distance_sensor_port)

    def lower_catapult(self):
        self.catapult_motor.run_for_seconds(
            seconds=1,
            speed=25)
