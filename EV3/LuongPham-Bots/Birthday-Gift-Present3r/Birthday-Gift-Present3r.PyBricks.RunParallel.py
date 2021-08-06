#!/usr/bin/env pybricks-micropython


from pybricks.experimental import run_parallel

from birthday_gift_present3r_pybricks import BirthdayGiftPresent3r


GIFT_PRESENT3R = BirthdayGiftPresent3r()

run_parallel(
    GIFT_PRESENT3R.keep_driving_by_ir_beacon,
    GIFT_PRESENT3R.keep_controlling_arm_by_ir_beacon,
    GIFT_PRESENT3R.say_happy_birthday_whenever_touch_sensor_pressed,
    GIFT_PRESENT3R.sing_happy_birthday_whenever_ir_beacon_button_pressed)
