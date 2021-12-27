def mod(a: float, b: float) -> float:
    return a - round(a / b, ndigits=None) * b


def cyclic_position_offset(
        rotation_sensor: float,
        cyclic_degrees: float) -> float:
    return mod(rotation_sensor, cyclic_degrees)
