ev3.motorOn(forSeconds: 1, on: .a, withPower: -20)
while true {
    ev3.motorOff(on: .a, brakeAtEnd: true)
    if ev3.measureIRProximity(on: .four) < 25 {
        ev3.displayImage(named: .pinchRight)
        ev3.move(forDegrees: 1200, leftPort: .b, rightPort: .c, leftPower: -100, rightPower: 100)
        ev3.displayImage(named: .hurt)
        ev3.motorOn(forSeconds: 0.8, on: .a, withPower: 100)
        ev3.playSound(file: .laser, atVolume: 100, withStyle: .waitForCompletion)
        ev3.motorOn(forSeconds: 1, on: .a, withPower: -20)
    } else {
        ev3.displayImage(named: .boom)
        ev3.move(forSeconds: 0.8, leftPort: .b, rightPort: .c, leftPower: 100, rightPower: -100)
        ev3.motorOn(forSeconds: 0.1, on: .a, withPower: 100)
        ev3.waitFor(seconds: 0.1)
        ev3.displayImage(named: .ev3Icon)
        ev3.move(forSeconds: 0.2, leftPort: .b, rightPort: .c, leftPower: 100, rightPower: -100)
        ev3.motorOn(forSeconds: 0.2, on: .a, withPower: -10)
    }
}
