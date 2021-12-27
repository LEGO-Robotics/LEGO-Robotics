#!/usr/bin/env micropython


from mr_b3am_ev3dev2 import MrB3am


# FIXME: AttributeError: 'module' object has no attribute 'lseek'

MR_B3AM = MrB3am(fast=True)

MR_B3AM.main(debug=True)
