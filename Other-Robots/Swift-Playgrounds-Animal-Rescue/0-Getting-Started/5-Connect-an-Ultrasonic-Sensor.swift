ev3.waitForUltrasonicChange(on: .four)

ev3.motorOn(
    forSeconds: 3,
    on: .a,
    withPower: 100,
    brakeAtEnd: true)
