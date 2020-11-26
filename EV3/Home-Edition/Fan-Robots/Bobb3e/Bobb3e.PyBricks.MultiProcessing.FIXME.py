#!/usr/bin/env pybricks-micropython


from bobb3e_pybricks import Bobb3e

from multiprocessing import Process


BOBB3E = Bobb3e()

BOBB3E.screen.print('BOBB3E')

Process(target=BOBB3E.sound_alarm_whenever_reversing).start()

BOBB3E.keep_driving_or_operating_forks_by_ir_beacon(speed=1000)

# FIXME: OSError: [Errno 5] EIO: 
#  Unexpected hardware input/output error with a motor or sensor:
# --> Try unplugging the sensor or motor and plug it back in again.
# --> To see which sensor or motor is causing the problem,
#     check the line in your script that matches
#     the line number given in the 'Traceback' above.
# --> Try rebooting the hub/brick if the problem persists.
