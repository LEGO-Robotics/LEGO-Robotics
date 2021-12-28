While true {
if ev3.measureUltraSonicCentimeters (on : .four) < 20
{
if ev3.measureUltrasonicCentimeters (on: .four) < 10 
{
ev3.stopMove(leftPort: .b, rightPort: .c)
else 
{
ev3.move(leftPort: .b, rightPort: .c, leftPower: 10,
rightPower: 10)
}
}
else 
{
ev3.move(leftPort: .b, rightPort: .c, leftPower: 50,
rightPower: 50)
}
}
