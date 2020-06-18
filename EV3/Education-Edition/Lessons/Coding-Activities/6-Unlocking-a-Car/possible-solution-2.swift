/*
As of summer 2017, there is no way to use EV3 Brick’s buttons in Swift playground. 
In this example, EV3 Up button has been replaced with touch 2. 
Sound file used in this example are not the same has RobotC example 
*/

While true 
{
ev3.brickLightOn(WithColor: .green inMode: .on)
if ev3.measureUltrasonicCentimeters(on: .four) < 4 && ev3.measureTouch(on : .two)
{
ev3.playSound(file: .hello, atVolume : 100, withStyle: .WaitForCompletion)
}
}
