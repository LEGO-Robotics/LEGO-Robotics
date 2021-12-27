while true {
    ev3.brickLightOn(withColor: .orange, inMode: .pulsating)

    var headingDifference = ev3.measureIRSeek(on: .four) - (-3)

    if abs(headingDifference) < 5 {
        ev3.stopMove(leftPort: .b, rightPort: .c, withBrake: true)
        ev3.brickLightOn(withColor: .red, inMode: .pulsating)
        ev3.motorOn(forRotations: 3, on: .a, withPower: 100, brakeAtEnd: true)
        ev3.playSound(file: .fanfare, atVolume: 100, withStyle: .waitForCompletion)
    } else {
        // TODO: fix to make it work
        ev3.move(leftPort: .b, rightPort: .c, leftPower: 1, rightPower: 1)
    }
}
