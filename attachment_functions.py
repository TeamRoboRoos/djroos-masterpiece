# Functions for attachments
from core import Robot
from pybricks.parameters import Stop

def rotate_right_attachment_motor(robot: Robot, angle, speed=250, holding_method=Stop.BRAKE, wait=False):
    robot.right_attachment_motor.run_angle(speed, angle, holding_method, wait=wait)

def rotate_left_attachment_motor(robot: Robot, angle, speed=250, holding_method=Stop.BRAKE, wait=False):
    robot.left_attachment_motor.run_angle(speed, angle, holding_method, wait=wait)

def rotate_both_attachment_motors(robot: Robot, left_angle, right_angle, speed=250, holding_method=Stop.BRAKE, wait=False):
    rotate_left_attachment_motor(robot, left_angle, speed, holding_method, wait=wait)
    rotate_right_attachment_motor(robot, right_angle, speed, holding_method)


def reset_motors(robot: Robot, angle=0, speed=250):
    
    robot.right_attachment_motor.reset_angle(0)
    robot.left_attachment_motor.reset_angle(0)

    robot.right_attachment_motor.run_angle(speed, angle)
    robot.left_attachment_motor.run_angle(speed, angle) 
    
