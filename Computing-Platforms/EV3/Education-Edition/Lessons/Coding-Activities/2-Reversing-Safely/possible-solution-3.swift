ev3.move(leftPort: .b, rightPort: .c, leftPower: 50, rightPower: 50)
ev3.waitForTouch(on: .one)
ev3.stopMove(leftPort: .b, rightPort: .c)
ev3.brickLightOff()

while true
{
ev3.display(text: ".")
if ev3.measureTouch(on : .one)
{
ev3.brickLightOn(withColor: .orange, inMode: .on)
ev3.display(text: "Reverse" )
ev3.move(forSeconds: 2, leftPort: .b, rightPort: .c, leftPower: -50, rightPower: -50)
ev3.brickLightOff()
}
else if ev3.measureTouchCount(on: .two) == 1 
{
repeat 
{
ev3.brickLightOn(WithColor: .red, inMode: .on)
ev3.waitFor(seconds: 0.5)
ev3.brickLightOff()
ev3.waitFor(seconds : 0.5)
} while ev3.measureTouchCount(on : .two) < 2
ev3.resetTouchCount(on: .two)
}
else if ev3.measureUltrasonicCentimeters(on: .four) < 10
{
ev3.playSound(file: .errorAalarm, atVolume: 100, withStyle: .wait ForCompletion)
}
}
