from tricky_ms import Tricky


TRICKY = Tricky()


TRICKY.distance_sensor.light_up_all(brightness=100)

while True:
    distance_in_cm = TRICKY.distance_sensor.get_distance_cm(short_range=False)

    # Tricky will begin when
    # the Distance Sensor detects something closer than 10 cm
    if (distance_in_cm is not None) and (distance_in_cm < 10):
        TRICKY.driving_motor_pair.move(
            amount=71,
            unit='cm',
            steering=100,
            speed=None)

        TRICKY.driving_motor_pair.move(
            amount=71,
            unit='cm',
            steering=-100,
            speed=None)
