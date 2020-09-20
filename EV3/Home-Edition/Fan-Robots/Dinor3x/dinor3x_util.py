def cyclic_position_offset(rotation_sensor: float, cyclic_degrees: float):
    return rotation_sensor \
        - (round(rotation_sensor / cyclic_degrees)
           * cyclic_degrees)
