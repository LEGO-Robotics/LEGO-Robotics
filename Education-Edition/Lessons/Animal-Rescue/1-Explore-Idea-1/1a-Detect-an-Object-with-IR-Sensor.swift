ev3.waitForUltrasonicCentimeters(
    on: .four,
    lessThanOrEqualTo: 30)

ev3.brickLightOn(
    withColor: .red,
    inMode: .flashing)

ev3.waitFor(seconds: 0.5)

ev3.brickLightOff()
