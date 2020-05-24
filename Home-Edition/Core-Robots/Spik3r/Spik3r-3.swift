ev3.motorOn(forSeconds: 1, on: .a, withPower: 50)
ev3.motorOn(forSeconds: 0.3, on: .a, withPower: -50)
for i in 1 ... 2 {
    for k in 1 ... 3 {
        ev3.motorOn(forSeconds: 0.2, on: .a, withPower: 75)
        ev3.motorOn(forSeconds: 0.2, on: .a, withPower: -75)
    }
    ev3.motorOn(forRotations: 3, on: .b, withPower: 100)
    ev3.playSound(file: .blip, atVolume: 100, withStyle:.waitForCompletion)
    ev3.motorOn(forRotations: 2, on: .b, withPower: -100)
    ev3.playSound(file: .blip, atVolume: 100, withStyle:.waitForCompletion)
    ev3.motorOn(on: .b, withPower: 25)
    ev3.playSound(file: .blip, atVolume: 100, withStyle: .playOnce)
}
