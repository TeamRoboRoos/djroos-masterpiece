from pybricks.tools import wait

from attachment_functions import *
from drive_functions import *


def run_1(robot: Robot):
    """Adapted version of 'run_1' using the jig we use for 'run_2' to make it more efficient and easier"""
    robot.reset_heading()
    move(robot, 180, 0)
    turn(robot, -44)
    move(robot, 250, -44)
    rotate_left_attachment_motor(robot, 130, wait=True)
    wait(250)
    move(robot, 30, -44)
    move(robot, -200, -44)
    turn(robot, -67)
    move(robot, 300, -67)


def run_2(robot: Robot):
    """Mission 6 and 7"""
    robot.reset_heading()
    move(robot, 680, 0)
    move(robot, 40, 0)
    turn(robot, 42)
    move(robot, 50, 42)
    move(robot, -90, 42)
    turn(robot, -45)
    move(robot, -650, 42)


def run_3(robot: Robot, Lreseting_angle=0, Rreseting_angle=0):
    """Mission 8 and rolling camara mission"""
    robot.reset_heading()
    move(robot, 455)
    rotate_left_attachment_motor(robot, 140, wait=True)
    wait(750)
    turn(robot, 12)
    move(robot, 390, 12)
    rotate_left_attachment_motor(robot, -120)
    rotate_right_attachment_motor(robot, -120, 1000)
    wait(100)
    turn(robot, 12)
    move(robot, 600, 12)
    turn(robot, 0)
    move(robot, 400, 0)
    rotate_right_attachment_motor(robot, 120, 1000)


def run_4(robot: Robot):
    """Robot driving from blue to red home base"""
    robot.reset_heading()
    move(robot, 400, 0)
    move(robot, 70, 0)
    rotate_left_attachment_motor(robot, -200, speed=500)
    move(robot, 20, 0)
    move(robot, -500, 0)
    rotate_left_attachment_motor(robot, 200)


def run_5(robot: Robot):
    robot.reset_heading()
    move(robot, 380, 0)
    turn(robot, 27)
    wait(250)
    turn(robot, 0)
    move(robot, -380, 0)


def run_6(robot: Robot):
    robot.reset_heading()
    move(robot, 330, 0, 200)
    turn(robot, -45)
    move(robot, 420, -45)
    turn(robot, -67)
    move(robot, 400, -67)
    rotate_left_attachment_motor(robot, -150, speed=1000)
    turn(robot, -78)
    wait(750)
    move(robot, -110, -78)
    turn(robot, -155)
    move(robot, 250, -155)
    rotate_right_attachment_motor(robot, 130, 100, wait=True)
    rotate_right_attachment_motor(robot, -130)
    move(robot, 190, -155, 200)
    wait(1000)
    move(robot, -40, -155, 200)
    move(robot, 40, -155, 200)
    wait(1000)
    move(robot, -40, -155, 200)
