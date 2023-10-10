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

def rotate_both_motors(robot, Langle, Rangle, wait=False, speed=250):
    rotate_both_attachment_motors(robot, speed, Langle, Rangle, wait)

def reset_attachment_motors(robot, angle=0, speed=250):
    reset_motors(robot, angle, speed)

def run_1(robot):
    robot.hub.imu.reset_heading(0)
    move_distance(robot, 450, 250)
    rotate_both_motors(robot, 120, 120)
    move_backwards_distance(robot, 450, 250)

def run_2(robot):
    robot.hub.imu.reset_heading(0)
    move_distance(robot, 300, 350)
    sensor_1_move_until_black_line(robot, 130, 7)
    move_distance(robot, 50, 350)
    turn_on_one_wheel(robot, 45, 150)
    move_distance(robot, 100, 350)
    move_backwards_distance(robot, 100, 350)
    # move_distance(robot, 37)
    # wait(750)
    # turn(robot, -45)
    # wait(750)
    # move_distance(robot, 50)
    # wait(750)
    # turn(robot, 45)
    # wait(750)
    # move_distance(robot, 75)

def run_3(robot):
    turn(robot, 45, 250)

def run_4(robot, Lreseting_angle, Rreseting_angle):
    rotate_both_motors(robot, Lreseting_angle, Rreseting_angle)

"""def run_2(robot):
    move_distance(robot, 50)
    turn(robot, -45)
    move_distance(robot, 100)
    turn(robot, 45)
    move_distance(robot, 100)"""

def mission_1(robot):
    move_distance(robot, 2000, 500, 10)

def mission_2(robot):
    move_distance(robot, 800)

def test_rotation(robot):
    rotate_left_attachment_motor(robot, 200, 120)
    rotate_right_attachment_motor(robot, 200, 120)
