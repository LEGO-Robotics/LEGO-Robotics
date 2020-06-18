while true {
    ev3.displayImage(named: .questionMark)
    ev3.brickLightOn(withColor: .orange, inMode: .on)
    while !ev3.measureTouch(on: .one) {
        ev3.playSound(file: .errorAlarm, atVolume: 100, withStyle: .waitForCompletion)
    }
    ev3.displayImage(named: .warning)
    ev3.playSound(file: .start, atVolume: 100, withStyle: .waitForCompletion)
    ev3.playSound(file: .hello, atVolume: 100, withStyle: .waitForCompletion)
    ev3.displayImage(named: .neutral)
    ev3.brickLightOn(withColor: .green, inMode: .pulsating)
    ev3.motorOn(forRotations: 1, on: .b, withPower: 75)
    ev3.motorOn(forRotations: 1, on: .c, withPower: 75)
    ev3.waitForTouch(on: .one)
    ev3.displayImage(named: .pinchRight)
    ev3.playSound(file: .goodbye, atVolume: 100, withStyle: .waitForCompletion)
}
