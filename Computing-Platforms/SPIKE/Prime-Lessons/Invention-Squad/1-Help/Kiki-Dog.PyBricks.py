from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Color, Icon, Port


# Configure the Hub and the Color Sensor
hub = PrimeHub()
color_sensor = ColorSensor(port=Port.B)


# Kiki walks around and sees things
while True:
    # if he sees blue, he thinks it's the sky above
    if color_sensor.color(surface=True) == Color.BLUE:
        hub.display.image(image=[[100, 100, 100, 100, 100],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0]])

    # if he sees yellow, he thinks it's a house
    elif color_sensor.color(surface=True) == Color.YELLOW:
        hub.display.image(image=Icon.UP)

    # if he sees green, he thinks it's the grass below
    elif color_sensor.color(surface=True) == Color.GREEN:
        hub.display.image(image=[[0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [100, 100, 100, 100, 100]])

    else:
        hub.display.off()
