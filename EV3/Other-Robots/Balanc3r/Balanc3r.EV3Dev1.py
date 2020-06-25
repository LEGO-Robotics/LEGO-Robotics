#!/usr/bin/env python3


from ev3dev.GyroBalancer import GyroBalancer


BALANC3R = GyroBalancer(gainGyroAngle=1156,
                        gainGyroRate=146,
                        gainMotorAngle=7,
                        gainMotorAngularSpeed=9,
                        gainMotorAngleErrorAccumulated=3)

BALANC3R.main()
