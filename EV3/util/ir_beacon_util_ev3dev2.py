def ir_beacon_measurements_reliable(
        heading_angle: float,
        distance: float) -> bool:
    return (heading_angle is not None) and (-25 < heading_angle < 25) \
       and (distance is not None) and (0 < distance < 100)
