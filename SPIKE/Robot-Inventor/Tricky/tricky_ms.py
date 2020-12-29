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


# EOF


import os
import sys


TARGET_FILE_NAME = 'tricky_ms.py'


# save current file to target file
print('SAVING {} AS {}...'.format(__file__, TARGET_FILE_NAME))
os.rename(__file__, TARGET_FILE_NAME)

# remove file content after "# EOF"
with open(TARGET_FILE_NAME, 'r') as f:
    file_content = f.read()
file_content = file_content.split('# EOF')[0]
with open(TARGET_FILE_NAME, 'w') as f:
    f.write(file_content)

# list projects/ directory and print file content before exiting
print(os.listdir())
print('{} SAVED:\n```\n{}\n```'.format(TARGET_FILE_NAME, file_content))
sys.exit()
