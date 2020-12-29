from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor


class Tricky:
    def __init__(
            self,
            left_wheel_motor_port: str = 'A', right_wheel_motor_port: str = 'B',
            sport_motor_port: str = 'C',
            distance_sensor_port: str = 'D',
            color_sensor_port: str = 'E'):
        self.hub = MSHub()

        self.driving_motor_pair = MotorPair(left_wheel_motor_port, right_wheel_motor_port)

        self.sport_motor = Motor(sport_motor_port)

        self.color_sensor = ColorSensor(color_sensor_port)

        self.distance_sensor = DistanceSensor(distance_sensor_port)


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
print('{} SAVED!'.format(TARGET_FILE_NAME))
sys.exit()
