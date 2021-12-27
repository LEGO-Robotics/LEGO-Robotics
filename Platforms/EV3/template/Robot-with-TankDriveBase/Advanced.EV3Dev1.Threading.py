#!/usr/bin/env python3


from ev3dev.ev3 import *

from threading import Thread

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


