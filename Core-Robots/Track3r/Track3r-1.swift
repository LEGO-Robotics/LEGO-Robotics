let leftWheelPort: OutputPort = .b
let rightWheelPort: OutputPort = .c

func forward(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: power,
        brakeAtEnd: brake)
}

func backward(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: -power,
        brakeAtEnd: brake)
}

ev3.displayImage(named: .pinchRight)
forward(nRotations: 2, power: 75, brake: true)
ev3.motorOn(forRotations: 3, on: .a, withPower: 75)
backward(nRotations: 2, power: 75, brake: true)
ev3.playSound(file: .fanfare, atVolume: 60, withStyle: .waitForCompletion)
