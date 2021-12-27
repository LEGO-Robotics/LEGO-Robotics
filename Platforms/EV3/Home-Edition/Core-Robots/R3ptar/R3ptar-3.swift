ev3.motorOn(forSeconds: 1, on: .d, withPower: -30)
while true {
    if ev3.measureIRProximity(on: .four) < 30 {
        ev3.brickLightOn(withColor: .red, inMode: .on)
        ev3.motorOff(on: .a, brakeAtEnd: true)
        ev3.motorOff(on: .b)
        ev3.playSound(file: .errorAlarm, atVolume: 100, withStyle: .playOnce)
        ev3.motorOn(forSeconds: 1, on: .d, withPower: 100)
        ev3.motorOn(on: .a, withPower: 100)
        ev3.motorOn(on: .b, withPower: -100)
        ev3.motorOn(forSeconds: 1, on: .d, withPower: -30)
        ev3.waitFor(seconds: 2)
        ev3.motorOn(forSeconds: 1, on: .a, withPower: -100)
        ev3.waitFor(seconds: 1)
    } else {
        ev3.brickLightOn(withColor: .orange, inMode: .pulsating)
        ev3.motorOn(on: .b, withPower: 100)
        ev3.motorOn(forSeconds: 0.2, on: .a, withPower: random(min: -30, max: 30), brakeAtEnd: false)
    }
}
