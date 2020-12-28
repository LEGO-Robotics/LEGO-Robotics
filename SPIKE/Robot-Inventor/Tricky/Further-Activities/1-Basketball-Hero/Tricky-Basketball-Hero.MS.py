from mindstorms import MSHub, Motor, MotorPair, DistanceSensor
from mindstorms.control import wait_for_seconds, wait_until
from mindstorms.operator import less_than


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


TRICKY = Tricky()

TRICKY.hub.light_matrix.show_image(
    image='TARGET',
    brightness=100)

TRICKY.lower_catapult()

# TRICKY.motor_pair.move_tank(
#    amount=100,
#    unit='cm',
#    left_speed=100,
#    right_speed=100)

wait_for_seconds(seconds=1)

TRICKY.distance_sensor.light_up_all(brightness=100)

# wait_until(
#     get_value_function=TRICKY.distance_sensor.get_distance_cm,
#     operator_function=less_than,
#     target_value=8)
distance_to_object = TRICKY.distance_sensor.get_distance_cm(short_range=False)
while (distance_to_object is None) or (distance_to_object >= 8):
    distance_to_object = TRICKY.distance_sensor.get_distance_cm(short_range=False)

TRICKY.catapult_motor.run_for_degrees(
    degrees=-110,
    speed=25)

TRICKY.motor_pair.move(
    amount=36,
    unit='cm',
    steering=100,
    speed=100)

TRICKY.catapult_motor.run_for_seconds(
    seconds=0.4,
    speed=-75)

TRICKY.hub.light_matrix.show_image(
    image='SURPRISED',
    brightness=100)

TRICKY.hub.speaker.beep(
    note=60,
    seconds=1)

TRICKY.lower_catapult()
