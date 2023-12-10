from pybricks.tools import wait

from attachment_functions import *
from drive_functions import *

def run_1(robot: Robot):
    """Adapted version of 'run_1' using the jig we use for 'run_2' to make it more efficient and easier"""
    robot.reset_heading()
    move(robot, 170, 0)
    turn(robot, -47)
    move(robot, 150, -47, constant_speed=200)
    rotate_left_attachment_motor(robot, 130, wait=True)
    move(robot, 100, -42, constant_speed=150, wait_after_move=False)
    # raise KeyboardInterrupt
    # turn(robot, -35)
    move(robot, -200, -42, constant_speed=150, wait_after_move=False)
    turn(robot, -60, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -400, -60, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 0, then=Stop.COAST, wait=False)
    robot.right_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 0, then=Stop.COAST, wait=False)


def run_2(robot: Robot):
    """Mission 6 and 7"""
    robot.reset_heading()
    move(robot, 720, 0, max_speed=400)
    turn(robot, 37)
    move(robot, 50, 37, constant_speed=DRIVE_SPEED_STEADY)
    move(robot, -90, 37, constant_speed=DRIVE_SPEED_STEADY, wait_after_move=False)
    turn(robot, 0, max_turn_speed=TURN_SPEED_FAST)
    move(robot, -200, 0, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    move(robot, -450, -60, constant_speed=DRIVE_SPEED_FAST)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 0, then=Stop.COAST)


def run_3(robot: Robot):
    """Mission 8 and rolling camara mission"""
    robot.reset_heading()
    move(robot, 460, 0)
    rotate_left_attachment_motor(robot, 155, wait=True)
    # wait(500)
    # turn(robot, 12)
    move(robot, 100, 8, constant_speed=100)
    move(robot, 290, 8, constant_speed=250)
    # wait(500)
    rotate_left_attachment_motor(robot, -155)
    turn(robot, 30)
    rotate_right_attachment_motor(robot, -120, 1000)
    # wait(500)
    move(robot, 310, 30)
    turn(robot, -20, max_turn_speed=800)
    move(robot, 490, -20, constant_speed=400, wait_after_move=False)
    rotate_right_attachment_motor(robot, 120, 1000)
    # robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 40, then=Stop.COAST, wait=False)


def run_4(robot: Robot):
    robot.reset_heading()
    move(robot, 350, 0)
    turn(robot, -10)
    move(robot, 15, -10)
    turn_timed(robot, 700, 22, max_turn_speed=1000)
    # turn(robot, 22, max_turn_speed=1000)
    wait(250)
    move(robot, -300, 22)
    # turn(robot, -20, max_turn_speed=1000)
    # move(robot, -170, -20, constant_speed=DRIVE_SPEED_FAST)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, -42, then=Stop.COAST, wait=False)
    

def run_5(robot: Robot):
    robot.reset_heading()
    move(robot, 400, 0)
    move(robot, 65, 0, constant_speed=100)
    wait(250)
    robot.left_attachment_motor.run_time(DEFAULT_ATTACHMENT_SPEED*-1, 1000, then=Stop.COAST)
    move(robot, -520, 0, constant_speed=DRIVE_SPEED_FAST, wait_after_move=False)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, 32, then=Stop.COAST)


def run_6(robot: Robot, hit_twice=True):
    robot.reset_heading()
    move(robot, 100, 0)
    move(robot, 450, 30)
    move(robot, 485, -13)
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
        wait(200)
        move(robot, 70, -105, constant_speed=100)
        move(robot, -70, -105, 100)

    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, -34, then=Stop.COAST, wait=False)

def run_6B(robot: Robot):
    run_6(robot, False)

def run_7(robot: Robot):
    robot.reset_heading()
    move(robot, 100, 0)
    move(robot, 450, 30)
    move(robot, 670, 2)
    turn(robot, 58)
    move(robot, 30, 58)
    turn_timed(robot, 800, 28)
    turn(robot, 58)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, -6, then=Stop.COAST, wait=False)
    move(robot, 120, 58)
    # turn_timed(robot, 800, 20)
    move(robot, 300, 38)
    # turn(robot, 23)
    # move(robot, 60, 23)
    robot.left_attachment_motor.run_time(-1000, 1000, then=Stop.COAST, wait=True)
    turn(robot, 28)
    robot.left_attachment_motor.run_time(1000, 1000, then=Stop.COAST, wait=True)
    robot.left_attachment_motor.run_time(-1000, 1000, then=Stop.COAST)
    # # rotate_left_attachment_motor(robot, -200, wait=True)
    move(robot, 40, 25)
    robot.left_attachment_motor.run_target(DEFAULT_ATTACHMENT_SPEED, -34, then=Stop.COAST, wait=False)


