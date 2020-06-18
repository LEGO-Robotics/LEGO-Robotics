/*
As of summer 2017, there is no way to use the EV3 Brick’s buttons in Swift playground. 
In this example, the EV3 up button has been replaced with touch sensor 1. 
*/

Var speed = 0
While true 
{
ev3.waitForTouch(on: .one)
ev3.waitFor(seconds: 0.5)
if speed < 100
{
	speed = speed + 10
while ev3.measureTouch(on: .one) == true
	{
		ev3.waitFor(seconds: 0.1)
	}
ev3.move(leftPort: .b, rightPort: .c, leftPower: (Float(speed)), rightPower: (Float(speed)))
}
}
