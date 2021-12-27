from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor, Motor
from pybricks.parameters import Port, Stop


hub = PrimeHub()
force_sensor = ForceSensor(port=Port.E)
motor = Motor(port=Port.A)


while True:
    if force_sensor.pressed(force=3):
        motor.run(speed=-1000)

    else:
        motor.run_until_stalled(
            speed=1000,
            then=Stop.COAST,
            duty_limit=None)
