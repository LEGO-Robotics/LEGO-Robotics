let power = random(min: 0.0, max: 100.0)
let seconds = random(min: 1, max: 5)

ev3.motorOn(forSeconds: seconds, on: .b, withPower: power)
ev3.motorOn(forSeconds: seconds, on: .b, withPower: random(min: -100, max: 100.0))
