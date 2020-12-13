def ir_beacon_measurements_reliable(
        heading_angle: float,
        distance: float) -> bool:
    return (heading_angle is not None) and (-75 < heading_angle < 75) \
       and (distance is not None) and (0 < distance < 100)
