ev3.displayImage(
    named: .hurt,
    atX: 0,
    atY: 0,
    clearScreen: true)

ev3.waitFor(seconds: 0.5)

ev3.displayImage(
    named: .neutral,
    atX: 0,
    atY: 0,
    clearScreen: true)

ev3.brickLightOn(
    withColor: .red,
    inMode: .flashing)
