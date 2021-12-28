#!/usr/bin/env pybricks-micropython


from multiprocessing import Process

from kraz3_pybricks import Kraz3


KRAZ3 = Kraz3()

Process(target=KRAZ3.kungfu_manoeuvre_whenever_touched_or_remote_controlled) \
    .start()

Process(target=KRAZ3.react_to_color).start()

KRAZ3.keep_driving_by_ir_beacon()

# FIXME: OSError: [Errno 5] EIO: 
# Unexpected hardware input/output error with a motor or sensor:
# --> Try unplugging the sensor or motor and plug it back in again.
# --> To see which sensor or motor is causing the problem,
#     check the line in your script that matches
#     the line number given in the 'Traceback' above.
# --> Try rebooting the hub/brick if the problem persists.
