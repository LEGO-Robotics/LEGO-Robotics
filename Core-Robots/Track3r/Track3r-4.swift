let leftWheelPort: OutputPort = .c
let rightWheelPort: OutputPort = .b

func startForward(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: power)
}

func forward(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: power,
        brakeAtEnd: brake)
}

func startBackward(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: -power)
}

func backward(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: -power,
        brakeAtEnd: brake)
}

func startLeft(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: -power)
}

func left(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: -power,
        brakeAtEnd: brake)
}

func startRight(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: power)
}

func right(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: power,
        brakeAtEnd: brake)
}

func startForwardLeft(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: 0)
}

func forwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: 0,
        brakeAtEnd: brake)
}

func startForwardRight(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: power)
}

func forwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: power,
        brakeAtEnd: brake)
}

func startBackwardLeft(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: 0)
}

func backwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: 0,
        brakeAtEnd: brake)
}

func startBackwardRight(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: -power)
}

func backwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: -power,
        brakeAtEnd: brake)
}

ev3.motorOn(forSeconds: 1, on: .a, withPower: -20)
while true {
    ev3.motorOff(on: .a, brakeAtEnd: true)
    if ev3.measureIRProximity(on: .four) < 25 {
        ev3.displayImage(named: .pinchRight)
        right(nRotations: 6, power: 75, brake: true)
        ev3.displayImage(named: .hurt)
        ev3.motorOn(forSeconds: 0.8, on: .a, withPower: 100)
        ev3.playSound(file: .laser, atVolume: 100, withStyle: .waitForCompletion)
        ev3.motorOn(forSeconds: 1, on: .a, withPower: -20)
    } else {
        ev3.displayImage(named: .boom)
        startForward(power: 75)
        ev3.motorOn(forSeconds: 0.1, on: .a, withPower: 100)
        ev3.waitFor(seconds: 0.1)
        ev3.displayImage(named: .ev3Icon)
        startForwardRight(power: 75)
        ev3.motorOff(on: .a, brakeAtEnd: false)
        ev3.motorOn(forSeconds: 0.2, on: .a, withPower: -10)
    }
}
