func stepLeg() {
    ev3.motorOn(forDegrees: 90, on: .b, withPower: 100)
    ev3.waitFor(seconds: 1)
    ev3.motorOn(forDegrees: 360, on: .b, withPower: 50)
}

for i in 1 ... 3 {
    stepLeg()
}
