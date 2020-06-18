/*
As of summer 2017, there is no way to use the EV3 Brick’s buttons in Swift playground. 
In this example, the EV3 up and down buttons have been replaced with touch sensor 1 and touch sensor 2. 
*/

Var speed = 0
func accelerate() 
{
if ev3.measureTouch (on : .One) 
{
speed = speed + 10
}
}
func decelerate() 
{
if ev3.measureTouch (on : .two) 
{
speed = speed - 10
}
}
While true 
{
accelerate()
decelerate()
ev3.move(leftPort: .b, rightPort: .c, leftPower: (Float(speed)),
rightPower: (Float(speed)))
}
