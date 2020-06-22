ev3.displayImage(named: .neutral)

ev3.move(forRotations: 5, leftPort: .b, rightPort: .c, leftPower: 75, rightPower: 75, brakeAtEnd: true)

ev3.displayImage(named: .decline)

ev3.motorOn(forRotations: 5, on: .b, withPower: 75, brakeAtEnd: true)

ev3.displayImage(named: .neutral)

ev3.move(forRotations: 5, leftPort: .b, rightPort: .c, leftPower: 75, rightPower: 75, brakeAtEnd: true)

ev3.displayImage(named: .pinchRight)

ev3.motorOn(forRotations: 5, on: .c, withPower: 75, brakeAtEnd: true)
