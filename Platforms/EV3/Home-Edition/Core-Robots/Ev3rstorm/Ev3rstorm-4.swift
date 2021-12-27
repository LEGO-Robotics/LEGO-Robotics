while true {
    if ev3.measureIRProximity(on: .four) < 25 {
        ev3.stopMove(leftPort: .b, rightPort: .c, withBrake: true)
        ev3.brickLightOn(withColor: .red, inMode: .pulsating)
        ev3.playSound(file: .object, atVolume: 100, withStyle: .waitForCompletion)
        ev3.playSound(file: .fanfare, atVolume: 100, withStyle: .waitForCompletion)
        ev3.playSound(file: .errorAlarm, atVolume: 100, withStyle: .waitForCompletion)
        ev3.motorOn(on: .a, withPower: 100)
        ev3.move(forRotations: 1, leftPort: .b, rightPort: .c, leftPower: 100, rightPower: 80, brakeAtEnd: true)
        ev3.motorOn(on: .a, withPower: -100)
        ev3.move(forRotations: 1, leftPort: .b, rightPort: .c, leftPower: -100, rightPower: -80, brakeAtEnd: true)
        ev3.motorOff(on: .a, brakeAtEnd: true)
        ev3.move(forRotations: 2, leftPort: .b, rightPort: .c, leftPower: 100, rightPower: -100, brakeAtEnd: true)
        ev3.move(forRotations: 1, leftPort: .b, rightPort: .c, leftPower: 0, rightPower: 100, brakeAtEnd: true)
    } else {
        ev3.brickLightOn(withColor: .green, inMode: .pulsating)
        ev3.move(forSeconds: 1.5, leftPort: .b, rightPort: .c, leftPower: 50, rightPower: 100)
        ev3.move(forSeconds: 1.5, leftPort: .b, rightPort: .c, leftPower: 100, rightPower: 50)
    }
}
