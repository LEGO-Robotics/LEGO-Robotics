ev3.motorOn(on: .b, withPower: 100)
for i in 1 ... 3 {
    ev3.motorOn(forSeconds: 1, on: .a, withPower: 10, brakeAtEnd: false)
    ev3.motorOn(forSeconds: 1, on: .a, withPower: -10, brakeAtEnd: false)
}
