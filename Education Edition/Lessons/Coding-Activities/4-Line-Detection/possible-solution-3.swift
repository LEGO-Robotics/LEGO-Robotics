while true
{
ev3.move(leftPort: .b, rightPort: .c, leftPower: 20, rightPower: 5)
ev3.waitForLightColor(on: .three, color: .black)
ev3.playSound(file: .errorAlarm, atVolume : 100, withStyle: .)
ev3.move(leftPort: .b, rightPort: .c, leftPower: 5, rightPower: 20)
ev3.waitForLightColor(on: .three, color: .white)
}
