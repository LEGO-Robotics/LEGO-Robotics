#!/usr/bin/env python3

"""
from https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/MINDCUB3R/mindcuber.py
"""

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedDPS
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor
from pprint import pformat
from rubikscolorresolver import RubiksColorSolverGeneric
from subprocess import check_output
from time import sleep
import json
import logging
import os
import signal
import sys
import time

log = logging.getLogger(__name__)


class ScanError(Exception):
    pass


class MindCuber(object):
    scan_order = [
        5, 9, 6, 3, 2, 1, 4, 7, 8,
        23, 27, 24, 21, 20, 19, 22, 25, 26,
        50, 54, 51, 48, 47, 46, 49, 52, 53,
        14, 10, 13, 16, 17, 18, 15, 12, 11,
        41, 43, 44, 45, 42, 39, 38, 37, 40,
        32, 34, 35, 36, 33, 30, 29, 28, 31]

    hold_cube_pos = 85
    rotate_speed = 400
    flip_speed = 300
    flip_speed_push = 400

    def __init__(self):
        self.shutdown = False
        self.flipper = LargeMotor(OUTPUT_A)
        self.turntable = LargeMotor(OUTPUT_B)
        self.colorarm = MediumMotor(OUTPUT_C)
        self.color_sensor = ColorSensor()
        self.color_sensor.mode = self.color_sensor.MODE_RGB_RAW
        self.infrared_sensor = InfraredSensor()
        self.init_motors()
        self.state = ['U', 'D', 'F', 'L', 'B', 'R']
        self.rgb_solver = None
        signal.signal(signal.SIGTERM, self.signal_term_handler)
        signal.signal(signal.SIGINT, self.signal_int_handler)

        filename_max_rgb = 'max_rgb.txt'

        if os.path.exists(filename_max_rgb):
            with open(filename_max_rgb, 'r') as fh:
                for line in fh:
                    (color, value) = line.strip().split()

                    if color == 'red':
                        self.color_sensor.red_max = int(value)
                        log.info("red max is %d" % self.color_sensor.red_max)
                    elif color == 'green':
                        self.color_sensor.green_max = int(value)
                        log.info("green max is %d" % self.color_sensor.green_max)
                    elif color == 'blue':
                        self.color_sensor.blue_max = int(value)
                        log.info("blue max is %d" % self.color_sensor.blue_max)

    def init_motors(self):

        for x in (self.flipper, self.turntable, self.colorarm):
            x.reset()

        log.info("Initialize flipper %s" % self.flipper)
        self.flipper.on(SpeedDPS(-50), block=True)
        self.flipper.off()
        self.flipper.reset()

        log.info("Initialize colorarm %s" % self.colorarm)
        self.colorarm.on(SpeedDPS(500), block=True)
        self.colorarm.off()
        self.colorarm.reset()

        log.info("Initialize turntable %s" % self.turntable)
        self.turntable.off()
        self.turntable.reset()

    def shutdown_robot(self):
        log.info('Shutting down')
        self.shutdown = True

        if self.rgb_solver:
            self.rgb_solver.shutdown = True

        for x in (self.flipper, self.turntable, self.colorarm):
            # We are shutting down so do not 'hold' the motors
            x.stop_action = 'brake'
            x.off(False)

    def signal_term_handler(self, signal, frame):
        log.error('Caught SIGTERM')
        self.shutdown_robot()

    def signal_int_handler(self, signal, frame):
        log.error('Caught SIGINT')
        self.shutdown_robot()

    def apply_transformation(self, transformation):
        self.state = [self.state[t] for t in transformation]

    def rotate_cube(self, direction, nb):
        current_pos = self.turntable.position
        final_pos = 135 * round((self.turntable.position + (270 * direction * nb)) / 135.0)
        log.info("rotate_cube() direction %s, nb %s, current_pos %d, final_pos %d" % (direction, nb, current_pos, final_pos))

        if self.flipper.position > 35:
            self.flipper_away()

        self.turntable.on_to_position(SpeedDPS(MindCuber.rotate_speed), final_pos)

        if nb >= 1:
            for i in range(nb):
                if direction > 0:
                    transformation = [0, 1, 5, 2, 3, 4]
                else:
                    transformation = [0, 1, 3, 4, 5, 2]
                self.apply_transformation(transformation)

    def rotate_cube_1(self):
        self.rotate_cube(1, 1)

    def rotate_cube_2(self):
        self.rotate_cube(1, 2)

    def rotate_cube_3(self):
        self.rotate_cube(-1, 1)

    def rotate_cube_blocked(self, direction, nb):

        # Move the arm down to hold the cube in place
        self.flipper_hold_cube()

        # OVERROTATE depends on lot on MindCuber.rotate_speed
        current_pos = self.turntable.position
        OVERROTATE = 18
        final_pos = int(135 * round((current_pos + (270 * direction * nb)) / 135.0))
        temp_pos = int(final_pos + (OVERROTATE * direction))

        log.info("rotate_cube_blocked() direction %s nb %s, current pos %s, temp pos %s, final pos %s" %
                 (direction, nb, current_pos, temp_pos, final_pos))

        self.turntable.on_to_position(SpeedDPS(MindCuber.rotate_speed), temp_pos)
        self.turntable.on_to_position(SpeedDPS(MindCuber.rotate_speed/4), final_pos)

    def rotate_cube_blocked_1(self):
        self.rotate_cube_blocked(1, 1)

    def rotate_cube_blocked_2(self):
        self.rotate_cube_blocked(1, 2)

    def rotate_cube_blocked_3(self):
        self.rotate_cube_blocked(-1, 1)

    def flipper_hold_cube(self, speed=300):
        current_position = self.flipper.position

        # Push it forward so the cube is always in the same position
        # when we start the flip
        if (current_position <= MindCuber.hold_cube_pos - 10 or
            current_position >= MindCuber.hold_cube_pos + 10):

            self.flipper.ramp_down_sp=400
            self.flipper.on_to_position(SpeedDPS(speed), MindCuber.hold_cube_pos)
            sleep(0.05)

    def flipper_away(self, speed=300):
        """
        Move the flipper arm out of the way
        """
        log.info("flipper_away()")
        self.flipper.ramp_down_sp = 400
        self.flipper.on_to_position(SpeedDPS(speed), 0)

    def flip(self):
        """
        Motors will sometimes stall if you call on_to_position() multiple
        times back to back on the same motor. To avoid this we call a 50ms
        sleep in flipper_hold_cube() and after each on_to_position() below.
        We have to sleep after the 2nd on_to_position() because sometimes
        flip() is called back to back.
        """
        log.info("flip()")

        if self.shutdown:
            return

        # Move the arm down to hold the cube in place
        self.flipper_hold_cube()

        # Grab the cube and pull back
        self.flipper.ramp_up_sp = 200
        self.flipper.ramp_down_sp = 0
        self.flipper.on_to_position(SpeedDPS(self.flip_speed), 190)
        sleep(0.05)

        # At this point the cube is at an angle, push it forward to
        # drop it back down in the turntable
        self.flipper.ramp_up_sp = 200
        self.flipper.ramp_down_sp = 400
        self.flipper.on_to_position(SpeedDPS(self.flip_speed_push), MindCuber.hold_cube_pos)
        sleep(0.05)

        transformation = [2, 4, 1, 3, 0, 5]
        self.apply_transformation(transformation)

    def colorarm_middle(self):
        log.info("colorarm_middle()")
        self.colorarm.on_to_position(SpeedDPS(600), -750)

    def colorarm_corner(self, square_index):
        """
        The lower the number the closer to the center
        """
        log.info("colorarm_corner(%d)" % square_index)
        position_target = -580

        if square_index == 1:
            position_target -= 10

        elif square_index == 3:
            position_target -= 30

        elif square_index == 5:
            position_target -= 20

        elif square_index == 7:
            pass

        else:
            raise ScanError("colorarm_corner was given unsupported square_index %d" % square_index)

        self.colorarm.on_to_position(SpeedDPS(600), position_target)

    def colorarm_edge(self, square_index):
        """
        The lower the number the closer to the center
        """
        log.info("colorarm_edge(%d)" % square_index)
        position_target = -640

        if square_index == 2:
            position_target -= 20

        elif square_index == 4:
            position_target -= 40

        elif square_index == 6:
            position_target -= 20

        elif square_index == 8:
            pass

        else:
            raise ScanError("colorarm_edge was given unsupported square_index %d" % square_index)

        self.colorarm.on_to_position(SpeedDPS(600), position_target)

    def colorarm_remove(self):
        log.info("colorarm_remove()")
        self.colorarm.on_to_position(SpeedDPS(600), 0)

    def colorarm_remove_halfway(self):
        log.info("colorarm_remove_halfway()")
        self.colorarm.on_to_position(SpeedDPS(600), -400)

    def scan_face(self, face_number):
        log.info("scan_face() %d/6" % face_number)

        if self.shutdown:
            return

        if self.flipper.position > 35:
            self.flipper_away(100)

        self.colorarm_middle()
        self.colors[int(MindCuber.scan_order[self.k])] = self.color_sensor.rgb

        self.k += 1
        i = 1
        target_pos = 115
        self.colorarm_corner(i)

        # The gear ratio is 3:1 so 1080 is one full rotation
        self.turntable.reset()
        self.turntable.on_to_position(SpeedDPS(MindCuber.rotate_speed), 1080, block=False)
        self.turntable.wait_until('running')

        while True:

            # 135 is 1/8 of full rotation
            if self.turntable.position >= target_pos:
                current_color = self.color_sensor.rgb
                self.colors[int(MindCuber.scan_order[self.k])] = current_color

                i += 1
                self.k += 1

                if i == 9:
                    # Last face, move the color arm all the way out of the way
                    if face_number == 6:
                        self.colorarm_remove()

                    # Move the color arm far enough away so that the flipper
                    # arm doesn't hit it
                    else:
                        self.colorarm_remove_halfway()

                    break

                elif i % 2:
                    self.colorarm_corner(i)

                    if i == 1:
                        target_pos = 115
                    elif i == 3:
                        target_pos = 380
                    else:
                        target_pos = i * 135

                else:
                    self.colorarm_edge(i)

                    if i == 2:
                        target_pos = 220
                    elif i == 8:
                        target_pos = 1060
                    else:
                        target_pos = i * 135

            if self.shutdown:
                return

        if i < 9:
            raise ScanError('i is %d..should be 9' % i)

        self.turntable.wait_until_not_moving()
        self.turntable.off()
        self.turntable.reset()
        log.info("\n")

    def scan(self):
        log.info("scan()")
        self.colors = {}
        self.k = 0
        self.scan_face(1)

        self.flip()
        self.scan_face(2)

        self.flip()
        self.scan_face(3)

        self.rotate_cube(-1, 1)
        self.flip()
        self.scan_face(4)

        self.rotate_cube(1, 1)
        self.flip()
        self.scan_face(5)

        self.flip()
        self.scan_face(6)

        if self.shutdown:
            return

        log.info("RGB json:\n%s\n" % json.dumps(self.colors))
        self.rgb_solver = RubiksColorSolverGeneric(3)
        self.rgb_solver.enter_scan_data(self.colors)
        self.rgb_solver.crunch_colors()
        self.cube_kociemba = self.rgb_solver.cube_for_kociemba_strict()
        log.info("Final Colors (kociemba): %s" % ''.join(self.cube_kociemba))

        # This is only used if you want to rotate the cube so U is on top, F is
        # in the front, etc. You would do this if you were troubleshooting color
        # detection and you want to pause to compare the color pattern on the
        # cube vs. what we think the color pattern is.
        '''
        log.info("Position the cube so that U is on top, F is in the front, etc...to make debugging easier")
        self.rotate_cube(-1, 1)
        self.flip()
        self.flipper_away()
        self.rotate_cube(1, 1)
        input('Paused')
        '''

    def move(self, face_down):
        log.info("move() face_down %s" % face_down)

        position = self.state.index(face_down)
        actions = {
            0: ["flip", "flip"],
            1: [],
            2: ["rotate_cube_2", "flip"],
            3: ["rotate_cube_1", "flip"],
            4: ["flip"],
            5: ["rotate_cube_3", "flip"]
        }.get(position, None)

        for a in actions:

            if self.shutdown:
                break

            getattr(self, a)()

    def run_kociemba_actions(self, actions):
        log.info('Action (kociemba): %s' % ' '.join(actions))
        total_actions = len(actions)

        for (i, a) in enumerate(actions):

            if self.shutdown:
                break

            if a.endswith("'"):
                face_down = list(a)[0]
                rotation_dir = 1
            elif a.endswith("2"):
                face_down = list(a)[0]
                rotation_dir = 2
            else:
                face_down = a
                rotation_dir = 3

            log.info("Move %d/%d: %s%s (a %s)" % (i, total_actions, face_down, rotation_dir, pformat(a)))
            self.move(face_down)

            if rotation_dir == 1:
                self.rotate_cube_blocked_1()
            elif rotation_dir == 2:
                self.rotate_cube_blocked_2()
            elif rotation_dir == 3:
                self.rotate_cube_blocked_3()
            log.info("\n")

    def resolve(self):

        if self.shutdown:
            return

        cmd = ['kociemba', ''.join(map(str, self.cube_kociemba))]
        output = check_output(cmd).decode('ascii')

        if 'ERROR' in output:
            msg = "'%s' returned the following error\n%s\n" % (' '.join(cmd), output)
            log.error(msg)
            print(msg)
            sys.exit(1)

        actions = output.strip().split()
        self.run_kociemba_actions(actions)
        self.cube_done()

    def cube_done(self):
        self.flipper_away()

    def wait_for_cube_insert(self):
        rubiks_present = 0
        rubiks_present_target = 10
        log.info('wait for cube...to be inserted')

        while True:

            if self.shutdown:
                break

            dist = self.infrared_sensor.proximity

            # It is odd but sometimes when the cube is inserted
            # the IR sensor returns a value of 100...most of the
            # time it is just a value less than 50
            if dist < 50 or dist == 100:
                rubiks_present += 1
                log.info("wait for cube...distance %d, present for %d/%d" %
                         (dist, rubiks_present, rubiks_present_target))
            else:
                if rubiks_present:
                    log.info('wait for cube...cube removed (%d)' % dist)
                rubiks_present = 0

            if rubiks_present >= rubiks_present_target:
                log.info('wait for cube...cube found and stable')
                break

            time.sleep(0.1)


if __name__ == '__main__':

    # logging.basicConfig(filename='rubiks.log',
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    mcube = MindCuber()

    try:
        mcube.wait_for_cube_insert()

        # Push the cube to the right so that it is in the expected
        # position when we begin scanning
        mcube.flipper_hold_cube(100)
        mcube.flipper_away(100)

        mcube.scan()
        mcube.resolve()
        mcube.shutdown_robot()

    except Exception as e:
        log.exception(e)
        mcube.shutdown_robot()
        sys.exit(1)
