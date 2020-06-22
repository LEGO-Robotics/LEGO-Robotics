while true {
    if ev3.measureLightAmbient(on: .three) < 5 {
        ev3.displayImage(named: .neutral)
        ev3.move(forSeconds: 1.5, leftPort: .b, rightPort: .c, leftPower: -80, rightPower: -100, brakeAtEnd: true)
        ev3.displayImage(named: .pinchRight)
        ev3.move(forSeconds: 1.5, leftPort: .b, rightPort: .c, leftPower: -100, rightPower: 100, brakeAtEnd: true)
    } else {
        ev3.move(forSeconds: 1.5, leftPort: .b, rightPort: .c, leftPower: 50, rightPower: 100, brakeAtEnd: true)
        ev3.move(forSeconds: 1.5, leftPort: .b, rightPort: .c, leftPower: 100, rightPower: 50, brakeAtEnd: true)
        ev3.displayImage(named: .awake)
    }
    if ev3.measureTouch(on: .one) {
        ev3.playSound(file: .ouch, atVolume: 100, withStyle: .waitForCompletion)
        ev3.motorOn(forRotations: 6, on: .a, withPower: 100, brakeAtEnd: true)
    }
}
