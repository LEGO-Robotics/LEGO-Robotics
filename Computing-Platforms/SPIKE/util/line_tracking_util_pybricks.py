"""Line-Tracking Utilities."""


from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Direction, Port


class DoubleLineTrackingDriveBase:
    """Drive Base with 2 Color Sensors in front for tracking 2 lines."""

    def __init__(self,  # pylint: disable=too-many-arguments
                 wheel_diameter: float, axle_track: float,  # both in mm
                 left_motor_port: Port = Port.A,
                 left_motor_pos_dir: Direction = Direction.COUNTERCLOCKWISE,
                 right_motor_port: Port = Port.B,
                 right_motor_pos_dir: Direction = Direction.CLOCKWISE,
                 left_color_sensor_port: Port = Port.C,
                 right_color_sensor_port: Port = Port.D):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=left_motor_pos_dir)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=right_motor_pos_dir)

        self.drive_base = DriveBase(left_motor=self.left_motor,
                                    right_motor=self.right_motor,
                                    wheel_diameter=wheel_diameter,
                                    axle_track=axle_track)

        self.left_color_sensor = ColorSensor(port=left_color_sensor_port)
        self.right_color_sensor = ColorSensor(port=right_color_sensor_port)

    def drive_forward(self):
        """Drive forward along 2 lines."""

    def drive_backward(self):
        """Drive backward along 2 lines."""


if __name__ == '__main__':
    double_line_tracking_drive_base = \
        DoubleLineTrackingDriveBase(
            wheel_diameter=44,
            axle_track=88,
            left_motor_port=Port.D,
            left_motor_pos_dir=Direction.COUNTERCLOCKWISE,
            right_motor_port=Port.D,
            right_motor_pos_dir=Direction.CLOCKWISE,
            left_color_sensor_port=Port.F,
            right_color_sensor_port=Port.E)

    double_line_tracking_drive_base.drive_base.straight(distance=100)
