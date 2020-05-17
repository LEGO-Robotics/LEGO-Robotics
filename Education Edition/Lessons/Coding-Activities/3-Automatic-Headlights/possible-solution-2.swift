while true
{
ev3.waitForLightAmbient(on: .three, lessThanOrEqualTo: 15)
ev3.displayImage(named: .awake)
ev3.waitForLightAmbient(on: .three, greaterThanOrEdualTo: 15)
ev3.display(text: “.”)
}
