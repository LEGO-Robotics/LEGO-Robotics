ev3.motorOn(forRotations: -0.25, on: .a, withPower: 100)
for i in 1 ... 2 {
    ev3.move(forRotations: 2, leftPort: .b, rightPort: .c, leftPower: 75, rightPower: 75)
    ev3.motorOn(forRotations: 0.25, on: .a, withPower: 100)
    ev3.playSound(file: .errorAlarm, atVolume: 100, withStyle: .waitForCompletion)
    ev3.waitFor(seconds: 0.5)
    ev3.move(forRotations: 0.35, leftPort: .b, rightPort: .c, leftPower: -75, rightPower: 75, brakeAtEnd: true)
    ev3.motorOn(forRotations: -0.25, on: .a, withPower: 100)
    ev3.playSound(file: .fanfare, atVolume: 100, withStyle: .waitForCompletion)
    ev3.waitFor(seconds: 0.5)
    ev3.move(forRotations: -0.35, leftPort: .b, rightPort: .c, leftPower: -75, rightPower: 75, brakeAtEnd: true)
}
ev3.move(forRotations: 4, leftPort: .b, rightPort: .c, leftPower: -75, rightPower: -75)
ev3.playSound(file: .ouch, atVolume: 100, withStyle: .waitForCompletion)
