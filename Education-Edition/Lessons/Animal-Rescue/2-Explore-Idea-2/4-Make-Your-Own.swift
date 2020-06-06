while true {
    if ev3.measureUltrasonicCentimeters(on: .one) > 20.0 {
        ev3.motorOn(
            on: .a,
            withPower: 100)
  } else {
        ev3.motorOn(
            on: .a,
            withPower: 50)
  }
}
