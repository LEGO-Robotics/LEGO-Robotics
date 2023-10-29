"""Line-Tracking Utilities."""


from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Color, Direction, Port


class DoubleLineTrackingDriveBase:
    """Drive Base with 2 Color Sensors in front for tracking 2 lines."""

    def __init__(  # pylint: disable=dangerous-default-value,too-many-arguments
            self,
            wheel_diameter: float, axle_track: float,  # both in mm
            left_motor_port: Port = Port.A,
            left_motor_pos_dir: Direction = Direction.COUNTERCLOCKWISE,
            right_motor_port: Port = Port.B,
            right_motor_pos_dir: Direction = Direction.CLOCKWISE,
            left_color_sensor_port: Port = Port.C,
            right_color_sensor_port: Port = Port.D,
            left_line_color: (Color |
                              list[Color] |
                              set[Color] |
                              tuple[Color]) = {Color.NONE, Color.BLACK},
            right_line_color: (Color |
                               list[Color] |
                               set[Color] |
                               tuple[Color]) = Color.WHITE) -> None:
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

        self.left_line_colors: list[Color] | set[Color] | tuple[Color] = \
            ({left_line_color}
             if isinstance(left_line_color, Color)
             else left_line_color)
        self.right_line_colors: list[Color] | set[Color] | tuple[Color] = \
            ({right_line_color}
             if isinstance(right_line_color, Color)
             else right_line_color)

    @property
    def left_color_sensor_detecting_left_line_color(self) -> bool:
        """Check if Left Color Sensor is detecting Left Line Color."""
        return self.left_color_sensor.color(surface=True) in self.left_line_colors  # noqa: E501

    @property
    def left_color_sensor_detecting_right_line_color(self) -> bool:
        """Check if Left Color Sensor is detecting Right Line Color."""
        return self.left_color_sensor.color(surface=True) in self.right_line_colors  # noqa: E501

    @property
    def right_color_sensor_detecting_left_line_color(self) -> bool:
        """Check if Right Color Sensor is detecting Left Line Color."""
        return self.right_color_sensor.color(surface=True) in self.left_line_colors  # noqa: E501

    @property
    def right_color_sensor_detecting_right_line_color(self) -> bool:
        """Check if Right Color Sensor is detecting Right Line Color."""
        return self.right_color_sensor.color(surface=True) in self.right_line_colors  # noqa: E501

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
            right_motor_port=Port.C,
            right_motor_pos_dir=Direction.CLOCKWISE,
            left_color_sensor_port=Port.F,
            right_color_sensor_port=Port.E,
            left_line_color={Color.NONE, Color.BLACK},
            right_line_color=Color.WHITE)

    double_line_tracking_drive_base.drive_base.straight(distance=100)
