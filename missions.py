from pybricks.tools import wait

from core import (
    DEFAULT_WAIT_TIME,
    DEFAULT_DRIVE_SPEED
)

from attachment_functions import *
from core import Robot
from drive_functions import *


def run_1(robot: Robot):
    """Mission 12 and 13"""
    robot.hub.imu.reset_heading(0)
    move_distance(robot, 560, 250)
    rotate_left_attachment_motor(robot, 120)
    move_backwards_distance(robot, 550, 250)
    rotate_left_attachment_motor(robot, -120)


def run_1B(robot: Robot):
    """Adapted version of 'run_1' using the jig we use for 'run_2' to make it more efficient and easier"""
    move_distance(robot, 150, 100)
    turn(robot, -42)
    wait(100)
    move_distance(robot, 280, 150)
    rotate_left_attachment_motor(robot, 120, wait=True)
    wait(DEFAULT_WAIT_TIME)
    # # turn(robot, 2)
    move_distance(robot, 50)
    # move_distance(robot, 50)
    move_backwards_distance(robot, 200, 250)
    turn(robot, -27)
    move_backwards_distance(robot, 250, 500)
    # rotate_left_attachment_motor(robot, -120, 500)

def run_2(robot: Robot):
    """Mission 6 and 7"""
    robot.hub.imu.reset_heading(0)
    move_distance(robot, 680, 250)
    wait(DEFAULT_WAIT_TIME)
    # turn(robot, -1)
    move_distance(robot, 40, 150)
    # wait(DEFAULT_WAIT_TIME) 
    turn(robot, 42)
    wait(100)
    move_distance(robot, 35)
    wait(100)
    move_backwards_distance(robot, 90)
    turn(robot, -45)
    move_backwards_distance(robot, 650, 500)

def run_3(robot: Robot, Lreseting_angle=0, Rreseting_angle=0):
    """Mission 8 and rolling camara mission"""
    move_distance(robot, 455)
    rotate_left_attachment_motor(robot, 140)
    wait(750)
    turn_speed(robot, 12, speed=200)
    wait(200)
    move_distance(robot, 390, 700)
    rotate_left_attachment_motor(robot, -120)
    rotate_right_attachment_motor(robot, -120, 1000, wait=False)
    wait(100)
    turn_speed(robot, 12, speed=200)
    move_distance(robot, 600)
    turn_speed(robot, -12, speed=200)
    move_distance(robot, 400)
    rotate_right_attachment_motor(robot, 120, 1000)

def run_4(robot: Robot):
    """Robot driving from blue to red home base"""
    move_distance(robot, 400, DEFAULT_DRIVE_SPEED)
    wait(DEFAULT_WAIT_TIME)
    drive_timed(robot, .75, 100)
    wait(DEFAULT_WAIT_TIME)
    rotate_left_attachment_motor(robot, -180, speed=500)
    move_distance(robot, 50)
    wait(DEFAULT_WAIT_TIME)
    move_backwards_distance(robot, 550, 250)
    rotate_left_attachment_motor(robot, 182)

def run_5(robot: Robot):
    move_distance(robot, 380, 200)
    wait(DEFAULT_WAIT_TIME)
    turn_speed(robot, 27, 350)
    wait(DEFAULT_WAIT_TIME)
    turn(robot, -27)
    move_backwards_distance(robot, 380, 200)

def run_6(robot: Robot):
    move_distance(robot, 297)
    turn(robot, -67)
    move_distance(robot, 600)
