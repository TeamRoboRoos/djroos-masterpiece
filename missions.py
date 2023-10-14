from core import Robot
from pybricks.tools import wait
from drive_functions import (
    hold,
    move_distance,
    move_backwards_distance,
    move_until_black_line,
    turn,
    sensor_1_move_until_black_line,
    turn_on_one_wheel
)

from attachment_functions import (
    rotate_left_attachment_motor,
    rotate_right_attachment_motor,
    reset_motors,
    rotate_both_attachment_motors
)

def reset_attachment_motors(robot: Robot, angle=0, speed=250):
    reset_motors(robot, angle, speed)

def run_1(robot: Robot): 
    """Mission 12 and 13"""
    robot.hub.imu.reset_heading(0)
    move_distance(robot, 560, 250, kp=7)
    rotate_left_attachment_motor(robot, 120)
    move_backwards_distance(robot, 550, 250, kp=7)
    rotate_left_attachment_motor(robot, -120)

def run_1B(robot: Robot):
    """Adapted version of 'run_1' using the jig we use for 'run_2' to make it more efficient and easier"""
    move_distance(robot, 70)
    turn(robot, -37)
    move_distance(robot, 460, 250)
    rotate_left_attachment_motor(robot, 120)
    move_backwards_distance(robot, 500)
    rotate_left_attachment_motor(robot, -120)

def run_2(robot: Robot):
    """Mission 6 and 7"""
    robot.hub.imu.reset_heading(0)
    move_distance(robot, 300, 350)
    sensor_1_move_until_black_line(robot, 130)
    move_distance(robot, 70, 390)
    turn_on_one_wheel(robot, 45, 150)
    move_distance(robot, 50)
    move_backwards_distance(robot, 50)
    turn(robot, -45)
    move_backwards_distance(robot, 700)

def run_3(robot: Robot, Lreseting_angle=0, Rreseting_angle=0):
    """Mission 8 and rolling camara mission"""
    move_distance(robot, 470)
    rotate_left_attachment_motor(robot, 70)
    wait(750)
    move_distance(robot, 350)
    rotate_left_attachment_motor(robot, -70)
    turn(robot, 45)
    wait(750)
    move_distance(robot, 100)
    rotate_right_attachment_motor(robot,-160, 1000)
    turn(robot, -45)
    move_distance(robot, 800)

def run_4(robot: Robot, Lreseting_angle=0, Rreseting_angle=0):
    """Robot driving from blue to red home base"""
    pass


def test_rotation(robot: Robot):
    rotate_left_attachment_motor(robot, 200, 120)
    rotate_right_attachment_motor(robot, 200, 120)
