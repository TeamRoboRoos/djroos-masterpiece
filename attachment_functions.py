# Functions for attachments
from core import *


def rotate_right_attachment_motor(
    robot: Robot,
    angle,
    speed=DEFAULT_ATTACHMENT_SPEED,
    holding_method=DEFAULT_HOLD_METHOD,
    wait=False,
):
    """Rotate the right attachment motor to the target angle.

    :param robot: The robot instance.
    :param angle: The target angle.
    :param speed: The rotation speed.
    :param holding_method: The holding method once the target angle has been reached.
    :param wait: Whether to wait until target angle is reached before executing next instruction.
    """
    robot.right_attachment_motor.run_angle(speed, angle, holding_method, wait=wait)


def rotate_left_attachment_motor(
    robot: Robot,
    angle,
    speed=DEFAULT_ATTACHMENT_SPEED,
    holding_method=DEFAULT_HOLD_METHOD,
    wait=False,
):
    """Rotate the left attachment motor to the target angle.

    :param robot: The robot instance.
    :param angle: The target angle.
    :param speed: The rotation speed.
    :param holding_method: The holding method once the target angle has been reached.
    :param wait: Whether to wait until target angle is reached before executing next instruction.
    """
    robot.left_attachment_motor.run_angle(speed, angle, holding_method, wait=wait)


def rotate_both_attachment_motors(
    robot: Robot,
    left_angle,
    right_angle,
    speed=DEFAULT_ATTACHMENT_SPEED,
    holding_method=DEFAULT_HOLD_METHOD,
    wait=False,
):
    """Rotate the both attachment motors to the target angle.

    :param robot: The robot instance.
    :param left_angle: The target angle for the left attachment motor.
    :param right_angle: The target angle for the right attachment motor.
    :param speed: The rotation speed.
    :param holding_method: The holding method once the target angle has been reached.
    :param wait: Whether to wait until target angle is reached before executing next instruction.
    """
    rotate_left_attachment_motor(robot, left_angle, speed, holding_method, wait=wait)
    rotate_right_attachment_motor(robot, right_angle, speed, holding_method)


def reset_motors(robot: Robot):
    """Resets the angle of both attachment motors.

    :param robot: The robot instance.
    """
    robot.right_attachment_motor.reset_angle(0)
    robot.left_attachment_motor.reset_angle(0)
