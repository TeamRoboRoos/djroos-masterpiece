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
    move_distance(robot, 180, 100)
    turn(robot, -44)
    wait(100)
    move_distance(robot, 250, 150)
    rotate_left_attachment_motor(robot, 130, wait=True)
    wait(DEFAULT_WAIT_TIME)
    # # turn(robot, 2)
    move_distance(robot, 30)
    # move_distance(robot, 50)
    move_backwards_distance(robot, 200, 250)
    turn(robot, -23)
    move_backwards_distance(robot, 300, 500)
    # rotate_left_attachment_motor(robot, -130, 500)

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
    move_distance(robot, 50)
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
    move_distance(robot, 330, 200)
    print(f"Heading is - {robot.hub.imu.heading()}")
    turn(robot, -45)
    move_distance(robot, 400, 200)
    turn(robot, -24, 100)
    move_distance(robot, 460, 200)
    rotate_left_attachment_motor(robot, -150, wait=True)
    turn(robot, -5)
    wait(100)
    move_backwards_distance(robot, 110, speed=200)
    turn(robot, -75 )
    move_distance(robot, 300, 200)
    rotate_right_attachment_motor(robot, 120, 100, wait=True)
    wait(100)
    rotate_right_attachment_motor(robot, -45, 100)
    turn(robot, 2)
    move_distance(robot, 200, speed=150)
    wait(250)
    move_backwards_distance(robot, 40, 500)
    move_distance(robot, 40, 500)
    wait(250)
    move_backwards_distance(robot, 40, 500)
    raise KeyboardInterrupt
    # rotate_left_attachment_motor(robot, 180, 1000, wait=True)
    # wait(1000)
    # rotate_left_attachment_motor(robot, -180, 1000)
    

def test(robot: Robot):
    move_distance(robot, 100)
    turn(robot, -45)
