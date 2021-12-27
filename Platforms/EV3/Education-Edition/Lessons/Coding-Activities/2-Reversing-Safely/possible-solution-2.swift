ev3.move(leftPort: .b, rightPort: .c, leftPower: 50, rightPower: 50)
ev3.waitForTouch(on: .One)
ev3.stopMove(leftPort: .b, rightPort: .c)

while true
{
if ev3.measureTouch(on: .one)
{
ev3.brickLightOn(withColor: .orange, inMode: .flashing)
ev3.move(forSeconds : 2, leftPort: .b, rightPort: .c, leftPower: -50, rightPower: -50)
}
else 
{
ev3.stopMove(leftPort: .b, rightPort: .c)
ev3.brickLight Off()
}
}
