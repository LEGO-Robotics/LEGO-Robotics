while true {
    // https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/sensors.html#ev3dev2.sensor.lego.InfraredSensor.proximity
    // 100% is approximately 70cm/27in
    if ev3.measureIRProximity(on: .four) > 20.0 * 100 / 70 {
        ev3.motorOn(on: .b, withPower: -100)
        ev3.motorOn(on: .c, withPower: -100)
    } else {
        ev3.motorOn(on: .b, withPower: -50)
        ev3.motorOn(on: .c, withPower: -50)
    }
}
