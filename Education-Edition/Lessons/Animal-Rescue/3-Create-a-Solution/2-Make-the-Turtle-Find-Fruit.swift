while true {
    if ev3.measureIRProximity(on: .four) > 30 {
        ev3.move(forRotations: 3, leftPort: .b, rightPort: .c, leftPower: -100, rightPower: -100)
    } else {
        ev3.stopMove(leftPort: .b, rightPort: .c)
        ev3.playSound(file: .fanfare, atVolume: 100, withStyle: .waitForCompletion)
    }
    
    if ev3.measureTouch(on: .one ) {
        ev3.stopMove(leftPort: .b, rightPort: .c)
        for i in 1 ... 4 {
            ev3.motorOn(on: .a, withPower: 99)
        }
        ev3.motorOff(on: .a)
    }
    
    if ev3.measureLightReflection(on: .two) > 10 {
        ev3.playSound(file: .object, atVolume: 100, withStyle: .waitForCompletion )
        ev3.playSound(file: .errorAlarm, atVolume: 100, withStyle: .waitForCompletion)
    }
}
