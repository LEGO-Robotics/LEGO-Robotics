#!/usr/bin/env python3


from ev3dev2 import *

from multiprocessing import Process

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


