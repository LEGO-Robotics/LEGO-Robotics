/*
As of summer 2017, there is no way to use the EV3 Brick’s buttons in Swift playground. 
In this example, the EV3 up and down buttons have been replaced with touch sensor 1 and touch sensor 2. 
The Sound files used in this example are not the same as in the RobotC example 
*/

Var drive = 0
repeat 
{
ev3.waitFor(seconds: 0.1)
if ev3.measureTouchCount(on: .one) == 1
{
drive = 1
ev3.resetTouchCount(on: .one)
}
else if ev3.measureTouchCount(on : .two) == 1 
{
drive = 2
ev3.resetTouchCount(on: .two)
}
} While drive == 0

ev3.waitFor(seconds: 2)
ev3.playSound(file: .start, atVolume: 100, WithStyle: .WaitForCompletion)

if drive == 1 
{
ev3.motorOn(forDegrees: 360, on: .c, withPower: 50)
}
else if drive == 2
{
ev3.motorOn(forDegrees: 360, on: .b, withPower: 50)
}
ev3.playSound(file: .goodbye, atVolume: 100, WithStyle: .waitForCompletion)
