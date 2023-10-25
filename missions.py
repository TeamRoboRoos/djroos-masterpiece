from pybricks.tools import wait

from attachment_functions import *
from drive_functions import *


def run_1(robot: Robot):
    """Adapted version of 'run_1' using the jig we use for 'run_2' to make it more efficient and easier"""
    robot.reset_heading()
    move(robot, 160, 0)
    turn(robot, -47)
    wait(250)
    move(robot, 255, -47, constant_speed=200)
    rotate_left_attachment_motor(robot, 130, wait=True)
    wait(250)
    move(robot, 65, -47, constant_speed=150, wait_after_move=False)
    # raise KeybardInterrupt
    turn(robot, -43)
    move(robot, -200, -47, constant_speed=150, wait_after_move=False)
    turn(robot, -67, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -300, -67, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    rotate_left_attachment_motor(robot, -130)


def run_2(robot: Robot):
    """Mission 6 and 7"""
    robot.reset_heading()
    move(robot, 800, 0, max_speed=400)
    turn(robot, 32)
    move(robot, 50, 37, constant_speed=DRIVE_SPEED_STEADY)
    move(robot, -90, 37, constant_speed=DRIVE_SPEED_STEADY, wait_after_move=False)
    turn(robot, 0, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -350, 0, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    turn(robot, -8)
    move(robot, 350)

def run_3(robot: Robot):
    """Mission 8 and rolling camara mission"""
    robot.reset_heading()
    move(robot, 485, 0)
    rotate_left_attachment_motor(robot, 150, wait=True)
    # wait(500)
    turn(robot, 12)
    move(robot, 390, 10, constant_speed=400)
    # wait(500)
    rotate_left_attachment_motor(robot, -150)
    turn(robot, 16)
    rotate_right_attachment_motor(robot, -120, 1000)
    wait(500)
    move(robot, 400, 12, constant_speed=400, wait_after_move=False)
    turn(robot, -30, max_turn_speed=800)
    move(robot, 400, -20, constant_speed=400, wait_after_move=False)
    rotate_right_attachment_motor(robot, 120, 1000)


def run_4(robot: Robot):
    robot.reset_heading()
    move(robot, 345, 0)
    turn(robot, -10)
    move(robot, 15, -10)
    turn(robot, 22, max_turn_speed=1000)
    wait(250)
    move(robot, -100, 22)
    turn(robot, -20, max_turn_speed=1000)
    move(robot, -150, -20, constant_speed=DRIVE_SPEED_FAST)
    robot.left_attachment_motor.run_target(500, -7, then=Stop.BRAKE)


def run_5(robot: Robot):
    robot.reset_heading()
    move(robot, 400, 2)
    move(robot, 65, 2, constant_speed=100)
    wait(250)
    rotate_left_attachment_motor(robot, -200, speed=500, wait=True)
    move(robot, -520, 2, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    rotate_left_attachment_motor(robot, 205, holding_method=Stop.COAST)


def run_6(robot: Robot):
    robot.reset_heading()
    move(robot, 100, 0)
    move(robot, 450, 30)
    move(robot, 490, -12)
    rotate_left_attachment_motor(robot, -200, wait=False)
    turn(robot, -20)
    move(robot, -100, -22)
    turn(robot, -105)
    move(robot, 200, -105)
    rotate_right_attachment_motor(robot, 200, speed=150)
    wait(750)
    rotate_right_attachment_motor(robot, -200, speed=150)
    move(robot, 220, -105)
    move(robot, -70, -105)
    wait(1000)
    move(robot, 70, -105)
    move(robot, -70, -105)
    # turn(robot, -10)

def _run_6(robot: Robot):
    robot.reset_heading()
    # move(robot, 330, 0)
    # turn(robot, -45)
    # move(robot, 420, -45)
    # turn(robot, -71)
    # move(robot, 410, -67)
    # rotate_left_attachment_motor(robot, -150, speed=1000)
    # wait(250)
    # turn(robot, -73)
    # wait(250)
    # turn(robot, -67)
    # move(robot, -110, -67)
    # turn(robot, -151)
    # move(robot, 260, -155)
    # rotate_right_attachment_motor(robot, 130, 100, wait=True)
    # rotate_right_attachment_motor(robot, -130)
    # move(robot, 170, -155, constant_speed=DRIVE_SPEED_STEADY)
    # wait(750)
    # move(robot, -30, -155, constant_speed=DRIVE_SPEED_STEADY)
    # move(robot, 30, -155, constant_speed=DRIVE_SPEED_STEADY)
    # wait(1000)
    # move(robot, -30, -155, constant_speed=DRIVE_SPEED_STEADY)
    # wait(1000)
