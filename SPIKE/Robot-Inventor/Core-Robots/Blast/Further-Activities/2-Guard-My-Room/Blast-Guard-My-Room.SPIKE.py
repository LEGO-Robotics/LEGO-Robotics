while BLAST.distance_sensor.distance() < 40:
        BLAST.hub.lights.on(100)

        BLAST.drive_base.turn(angle=60)

        BLAST.drive_base.turn(angle=-60)

    BLAST.drive_base.stop()

    BLAST.arm_movement_motor.run_angle(
        speed=-100,
        rotation_angle=3 * 360,
        then=Stop.HOLD,
        wait=True)

    BLAST.action_motor.run_time(
        speed=100,
        time=0.4,
        then=Stop.COAST,
        wait=False)

    BLAST.action_motor.run_angle(
        speed=100,
        rotation_angle=130,
        then=Stop.HOLD,
        wait=True)

    BLAST.action_motor.run_angle(
        speed=100,
        rotation_angle=60,
        then=Stop.HOLD,
        wait=True)

    BLAST.arm_movement_motor.run_angle(
        speed=100,
        rotation_angle=1.5 * 360,
        then=Stop.HOLD,
        wait=True)
