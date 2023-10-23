from pybricks.tools import wait

from attachment_functions import *
from drive_functions import *


def run_1(robot: Robot):
    """Adapted version of 'run_1' using the jig we use for 'run_2' to make it more efficient and easier"""
    robot.reset_heading()
    move(robot, 180, 0)
    turn(robot, -44)
    move(robot, 250, -44, constant_speed=DRIVE_SPEED_STEADY)
    rotate_left_attachment_motor(robot, 130, wait=True)
    wait(250)
    move(robot, 30, -44, constant_speed=DRIVE_SPEED_STEADY, wait_after_move=False)
    move(robot, -200, -44, constant_speed=DRIVE_SPEED_STEADY, wait_after_move=False)
    turn(robot, -67, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -300, -67, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)


def run_2(robot: Robot):
    """Mission 6 and 7"""
    robot.reset_heading()
    move(robot, 720, 0)
    turn(robot, 42)
    move(robot, 50, 42, constant_speed=DRIVE_SPEED_STEADY)
    move(robot, -90, 42, constant_speed=DRIVE_SPEED_STEADY, wait_after_move=False)
    turn(robot, 0, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -650, 0, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)


def run_3(robot: Robot):
    """Mission 8 and rolling camara mission"""
    robot.reset_heading()
    move(robot, 455, 0)
    rotate_left_attachment_motor(robot, 140, wait=True)
    wait(500)
    turn(robot, 12)
    move(robot, 390, 12)
    rotate_left_attachment_motor(robot, -120)
    rotate_right_attachment_motor(robot, -120, 1000)
    wait(500)
    turn(robot, 12)
    move(robot, 600, 12, constant_speed=400, wait_after_move=False)
    turn(robot, -20, max_turn_speed=800)
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
    turn(robot, -20, max_turn_speed=600)
    move(robot, -150, -20, constant_speed=DRIVE_SPEED_FAST)
    robot.left_attachment_motor.run_target(500, -7)


def run_5(robot: Robot):
    robot.reset_heading()
    move(robot, 400, 0)
    move(robot, 73, 0, constant_speed=150)
    wait(250)
    rotate_left_attachment_motor(robot, -200, speed=500)
    move(robot, -520, 0, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    rotate_left_attachment_motor(robot, 205, holding_method=Stop.COAST)


def run_6(robot: Robot):
    robot.reset_heading()
    move(robot, 330, 0)
    turn(robot, -45)
    move(robot, 420, -45)
    turn(robot, -71)
    move(robot, 400, -67)
    rotate_left_attachment_motor(robot, -150, speed=1000)
    wait(250)
    turn(robot, -78)
    wait(250)
    move(robot, -110, -78)
    turn(robot, -155)
    move(robot, 260, -160)
    rotate_right_attachment_motor(robot, 130, 100, wait=True)
    rotate_right_attachment_motor(robot, -130)
    move(robot, 190, -155, constant_speed=DRIVE_SPEED_STEADY)
    wait(750)
    move(robot, -40, -155, constant_speed=DRIVE_SPEED_STEADY)
    move(robot, 50, -155, constant_speed=DRIVE_SPEED_STEADY)
    wait(1000)
    move(robot, -50, -155, constant_speed=DRIVE_SPEED_STEADY)
    wait(1000)
