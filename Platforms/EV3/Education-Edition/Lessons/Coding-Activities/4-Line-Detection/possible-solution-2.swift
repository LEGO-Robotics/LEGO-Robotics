while true
{
ev3.move(leftPort: .b rightPort: .c, leftPower: 20, rightPower: 20)
ev3.waitForLightColor(on: .three, color: .red)
ev3.stopMove(leftPort : .b, rightPort : .c)
ev3.waitForLightColor(on : .three color: .green)
}
