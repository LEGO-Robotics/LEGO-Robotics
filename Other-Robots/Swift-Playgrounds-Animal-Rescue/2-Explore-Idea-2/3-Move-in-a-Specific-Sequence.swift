func stepLeg() {
    ev3.motorOn(
        forDegrees: 90,
        on: .a,
        withPower: 100)

    ev3.waitFor(seconds: 1)

    ev3.motorOn(
        forDegrees: 360,
        on: .a,
        withPower: 50)
}

for i in 1 ... 3 {
    stepLeg()
}
