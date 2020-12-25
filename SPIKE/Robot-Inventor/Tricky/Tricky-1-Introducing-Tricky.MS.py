from mindstorms import MotorPair, DistanceSensor


class Tricky:
    def __init__(
            self,
            left_motor_port: str = 'A', right_motor_port: str = 'B',
            distance_sensor_port: str = 'D'):
        self.motor_pair = MotorPair(left_motor_port, right_motor_port)

        self.distance_sensor = DistanceSensor(distance_sensor_port)


TRICKY = Tricky()

TRICKY.distance_sensor.light_up_all(brightness=100)

while True:
    distance_in_cm = TRICKY.distance_sensor.get_distance_cm(short_range=False)

    # Tricky will begin when
    # the Distance Sensor detects something closer than 10 cm
    if (distance_in_cm is not None) and (distance_in_cm < 10):
        TRICKY.motor_pair.move_tank(
            amount=71,
            unit='cm',
            left_speed=100,
            right_speed=100)

        TRICKY.motor_pair.move_tank(
            amount=-71,
            unit='cm',
            left_speed=100,
            right_speed=100)
