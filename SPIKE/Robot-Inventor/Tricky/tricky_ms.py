from mindstorms import MotorPair, DistanceSensor


class Tricky:
    def __init__(
            self,
            left_motor_port: str = 'A', right_motor_port: str = 'B',
            distance_sensor_port: str = 'D'):
        self.motor_pair = MotorPair(left_motor_port, right_motor_port)

        self.distance_sensor = DistanceSensor(distance_sensor_port)
