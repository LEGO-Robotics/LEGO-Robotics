while true {
    ev3.motorOn(forSeconds: 1, on: .d, withPower: -30)
    ev3.waitForIRProximity(on: .four, lessThanOrEqualTo: 30)
    ev3.playSound(file: .errorAlarm, atVolume: 100, withStyle: .playOnce)
    ev3.motorOn(forSeconds: 1, on: .d, withPower: 100)

    // doing 2nd process SEQUENTIALLY for now
    // (don't know how to do Parallel processes in Swift yet)
    ev3.motorOn(forSeconds: 1, on: .a, withPower: 10, brakeAtEnd: false)
    ev3.playSound(file: .arm, atVolume: 100, withStyle: .waitForCompletion)
    ev3.motorOn(forSeconds: 1, on: .a, withPower: -10, brakeAtEnd: false)
    ev3.waitFor(seconds: 1)
}
