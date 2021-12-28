#!/usr/bin/env micropython


from ev3dev2 import *

from threading import Thread

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


