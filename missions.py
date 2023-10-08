from drive_functions import (
    hold,
    move_distance,
    move_until_black_line,
    turn
)

from attachment_functions import (
    rotate_left_attachment_motor,
    rotate_right_attachment_motor
)

def mission_1(robot):
    move_distance(robot, 2000, 500, 10)

def mission_2(robot):
    move_until_black_line(robot, 150, 10)

def test_rotation(robot):
    rotate_right_attachment_motor(robot, 200, 120)
