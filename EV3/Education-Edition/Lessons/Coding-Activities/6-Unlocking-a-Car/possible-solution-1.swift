/*
As of summer 2017, there is no way to use EV3 Brick’s buttons in Swift playground. 
In this example, EV3 Up button has been replaced with touch sensor 2. 
*/
ev3.waitForUltrasonicCentimeters (on: .four, lessThanOrEqualTo: 5)
ev3.display(text: "Welcome")
ev3.waitFor(seconds: 3)
ev3.waitForTouch(on: .One)
ev3.display(text: "Ignition")
ev3.waitFor(seconds : 3)
