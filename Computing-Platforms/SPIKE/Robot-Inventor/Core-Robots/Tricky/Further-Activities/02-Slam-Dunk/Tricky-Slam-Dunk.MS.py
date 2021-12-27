from mindstorms.control import wait_for_seconds, wait_until
from mindstorms.operator import less_than

from tricky_basketball_ms import TrickyPlayingBasketball


TRICKY = TrickyPlayingBasketball()


TRICKY.hub.light_matrix.show_image(
    image='TARGET',
    brightness=100)

TRICKY.lower_arm()

# TRICKY.driving_motor_pair.move(
#    amount=100,
#    unit='cm',
#    steering=0,
#    speed=None)

wait_for_seconds(seconds=1)

TRICKY.distance_sensor.light_up_all(brightness=100)

# wait_until(
#    get_value_function=TRICKY.distance_sensor.get_distance_cm,
#    operator_function=less_than,
#    target_value=8)
distance_to_object = TRICKY.distance_sensor.get_distance_cm(short_range=False)
while (distance_to_object is None) or (distance_to_object >= 8):
    distance_to_object = TRICKY.distance_sensor.get_distance_cm(short_range=False)

TRICKY.sport_motor.run_for_degrees(
    degrees=-110,
    speed=25)

TRICKY.driving_motor_pair.stop()

TRICKY.hub.speaker.beep(
    note=70,
    seconds=1)

# On the way back, Tricky's speed is reduced to make it more accurate
# TRICKY.driving_motor_pair.move(
#     amount=100,
#     unit='cm',
#     steering=0,
#     speed=-40)

detected_color = TRICKY.color_sensor.get_color()
while (detected_color is None) or (detected_color != 'cyan'):
    TRICKY.driving_motor_pair.move(
        amount=1,
        unit='cm',
        steering=0,
        speed=-40)
    detected_color = TRICKY.color_sensor.get_color()

TRICKY.hub.status_light.on(color='cyan')

TRICKY.driving_motor_pair.stop()

TRICKY.sport_motor.run_for_seconds(
    seconds=0.4,
    speed=-75)

TRICKY.hub.light_matrix.show_image(
    image='SURPRISED',
    brightness=100)

TRICKY.hub.speaker.beep(
    note=60,
    seconds=1)

TRICKY.lower_arm()

wait_for_seconds(seconds=2)
