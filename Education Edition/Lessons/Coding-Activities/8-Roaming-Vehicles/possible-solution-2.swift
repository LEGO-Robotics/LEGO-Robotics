/*
As of summer 2017, there is no way to use the EV3 Brick’s buttons in Swift playground. 
In this example, the EV3 up and down buttons have been replaced with touch sensor 1 and touch sensor 2. 
The Sound files used in this example are not the same as in the RobotC example 
*/

var drive = [0, 0, 0, 0, 0]
ev3.resetTouchCount(on: .One)
ev3.resetTouchCount(on: .two)

for i in 0 ... 4
{
	repeat
	{
		ev3.WaitFor(seconds: 0.1)
if ev3.measureTouchCount(on: .one) == 1 
{
drive[i] = 1
ev3.resetTouchCount(on : .one)
}
else if ev3.measureTouchCount(on : .two) == 1
{
drive[i] = 2
ev3.resetTouchCount(on: .two)
}
} while drive[i] == 0
ev3.playSound(file: .blip, atVolume: 50, WithStyle: .Wait ForCompletion)
}
ev3.WaitFor(seconds: 2)
ev3.playSound(file: .start, atVolume: 100, WithStyle: .WaitForCompletion)

for i in 0 ... 4 
{
if drive[i] == 1 
{
ev3.move(forDegrees: 360, leftPort: .b, rightPort: .c, leftPower: 50, rightPower: 50)
}
else if drive[i] == 2
{
ev3.move(forDegrees: 360, leftPort: .b, rightPort: .c, leftPower: -50, rightPower: -50)
}
}
ev3.playSound(file: .goodbye, atVolume: 100, WithStyle: .WaitForCompletion)
