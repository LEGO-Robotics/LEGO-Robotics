def ir_beacon_measurements_reliable(
        heading_angle: float,
        distance: float) -> bool:
    return (-25 < heading_angle < 25) and (0 < distance < 100)
