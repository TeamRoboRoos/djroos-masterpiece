from pybricks.tools import wait

from attachment_functions import *
from drive_functions import *


def run_1(robot: Robot):
    """Adapted version of 'run_1' using the jig we use for 'run_2' to make it more efficient and easier"""
    robot.reset_heading()
    robot.left_attachment_motor.reset_angle(0)
    robot.right_attachment_motor.reset_angle(0)
    move(robot, 170, 0)
    turn(robot, -47)
    wait(250)
    move(robot, 150, -47, constant_speed=200)
    turn(robot, -35)
    rotate_left_attachment_motor(robot, 130, wait=True)
    turn(robot, -42)
    wait(250)
    move(robot, 100, -42, constant_speed=150, wait_after_move=False)
    # raise KeyboardInterrupt
    # turn(robot, -35)
    move(robot, -200, -42, constant_speed=150, wait_after_move=False)
    turn(robot, -60, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -400, -60, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)


def run_2(robot: Robot):
    """Mission 6 and 7"""
    robot.reset_heading()
    move(robot, 720, 0, max_speed=400)
    turn(robot, 37)
    move(robot, 50, 37, constant_speed=DRIVE_SPEED_STEADY)
    move(robot, -90, 37, constant_speed=DRIVE_SPEED_STEADY, wait_after_move=False)
    turn(robot, 0, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -200, 0, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    turn(robot, -60)
    move(robot, -450, -60)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 0)


def run_3(robot: Robot):
    """Mission 8 and rolling camara mission"""
    robot.reset_heading()
    move(robot, 460, 0)
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
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 17,then=Stop.COAST)


def run_4(robot: Robot):
    robot.reset_heading()
    move(robot, 350, 0)
    turn(robot, -10)
    move(robot, 15, -10)
    turn(robot, 22, max_turn_speed=1000)
    wait(250)
    move(robot, -300, 22)
    # turn(robot, -20, max_turn_speed=1000)
    # move(robot, -170, -20, constant_speed=DRIVE_SPEED_FAST)
    robot.left_attachment_motor.run_target(500, -7, then=Stop.COAST)


def run_5(robot: Robot):
    robot.reset_heading()
    move(robot, 400, 2)
    move(robot, 65, 2, constant_speed=100)
    wait(250)
    robot.left_attachment_motor.run_time(DEFAULT_ATTACHMENT_SPEED*-1, 1000, then=Stop.COAST)
    move(robot, -520, 2, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 32, then=Stop.COAST)


def run_6(robot: Robot, hit_twice = True):
    robot.reset_heading()
    move(robot, 100, 0)
    move(robot, 450, 30)
    move(robot, 490, -12)
    rotate_left_attachment_motor(robot, -200, wait=False)
    turn(robot, -20)
    move(robot, -100, -22)
    turn(robot, -105)
    move(robot, 250, -105)
    rotate_right_attachment_motor(robot, 200, speed=100)
    wait(750)
    rotate_right_attachment_motor(robot, -200, speed=100)
    move(robot, 180, -105, constant_speed=100)
    move(robot, -70, -105, constant_speed=100)

    if hit_twice:
        wait(1000)
        move(robot, 70, -105, constant_speed=100)
        move(robot, -70, -105, 100)

def run_6B(robot: Robot):
    run_6(robot, False)
