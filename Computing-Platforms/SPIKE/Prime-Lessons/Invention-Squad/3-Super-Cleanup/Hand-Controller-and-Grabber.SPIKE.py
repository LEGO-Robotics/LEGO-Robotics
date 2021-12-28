from spike import PrimeHub, ForceSensor, Motor


hub = PrimeHub()
force_sensor = ForceSensor('E')
motor = Motor('A')


while True:
    force_sensor_pressed = force_sensor.is_pressed()

    motor.set_stall_detection(stop_when_stalled=not force_sensor_pressed)

    if force_sensor_pressed:
        motor.start(speed=-100)
    else:
        motor.start(speed=100)
