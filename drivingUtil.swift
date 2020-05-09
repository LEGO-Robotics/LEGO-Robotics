let leftWheelPort: OutputPort = .c
let rightWheelPort: OutputPort = .b

func forward(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: power,
        brakeAtEnd: brake)
}

func backward(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: -power,
        brakeAtEnd: brake)
}

func left(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: power,
        brakeAtEnd: brake)
}

func right(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: -power,
        brakeAtEnd: brake)
}

func forwardLeft(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: power,
        brakeAtEnd: brake)
}

func forwardRight(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: 0,
        brakeAtEnd: brake)
}

func backwardLeft(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: -power,
        brakeAtEnd: brake)
}

func backwardRight(nRotations: Float, power: Float, brake: Bool) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: 0,
        brakeAtEnd: brake)
}
