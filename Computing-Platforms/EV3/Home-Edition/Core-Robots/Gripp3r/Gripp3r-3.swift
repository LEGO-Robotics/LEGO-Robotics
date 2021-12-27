let leftWheelPort: OutputPort = .b
let rightWheelPort: OutputPort = .c

let leftRightBC = (leftWheelPort == .b)

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
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power)
    }
}

func left(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power,
            brakeAtEnd: brake)
    }
}

func startRight(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power)
    }
}

func right(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power,
            brakeAtEnd: brake)
    }
}

func startForwardLeft(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0)
    }
}

func forwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0,
            brakeAtEnd: brake)
    }
}

func startForwardRight(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power)
    }
}

func forwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power,
            brakeAtEnd: brake)
    }
}

func startBackwardLeft(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0)
    }
}

func backwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0,
            brakeAtEnd: brake)
    }
}

func startBackwardRight(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power)
    }
    
}

func backwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power,
            brakeAtEnd: brake)
    }
}


ev3.motorOn(forSeconds: 1, on: .a, withPower: -75)
startForward(power: 75)
ev3.waitForIRProximity(on: .four, lessThanOrEqualTo: 25)
ev3.stopMove(leftPort: leftWheelPort, rightPort: rightWheelPort, withBrake: true)
ev3.playSound(file: .stop, atVolume: 100, withStyle: .playOnce)
ev3.motorOn(forSeconds: 1, on: .a, withPower: 100)
right(nRotations: 2.5, power: 100, brake: true)
startForward(power: 75)
ev3.waitForIRProximity(on: .four, lessThanOrEqualTo: 25)
ev3.stopMove(leftPort: leftWheelPort, rightPort: rightWheelPort, withBrake: true)
ev3.motorOn(on: .a, withPower: -75)
ev3.playSound(file: .goodbye, atVolume: 100, withStyle: .playOnce)
