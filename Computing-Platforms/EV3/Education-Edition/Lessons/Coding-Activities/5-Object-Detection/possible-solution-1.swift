while true {
ev3.move (leftPort: .b, rightPort: .c, leftPower: 50, rightPower: 50)
while ev3.measureUltrasonicCentimeters (on : .four) < 20
{
ev3.stopMove (leftPort: .b, rightPort: .C)
}
}
