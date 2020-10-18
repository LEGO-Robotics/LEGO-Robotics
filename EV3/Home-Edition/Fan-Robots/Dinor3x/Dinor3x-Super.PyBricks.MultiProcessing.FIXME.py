#!/usr/bin/env pybricks-micropython


from dinor3x_pybricks import Dinor3x

from multiprocessing import Process


DINOR3X = Dinor3x()

DINOR3X.close_mouth()

Process(target=DINOR3X.keep_changing_speed_by_color).start()
Process(target=DINOR3X.keep_roaring_by_ir_beacon).start()
DINOR3X.keep_walking_by_ir_beacon()

# FIXME: OSError: [Errno 5] EIO:
# Unexpected hardware input/output error with a motor or sensor:
# --> Try unplugging the sensor or motor and plug it back in again.
# --> To see which sensor or motor is causing the problem,
#     check the line in your script that matches
#     the line number given in the 'Traceback' above.
# --> Try rebooting the hub/brick if the problem persists.
