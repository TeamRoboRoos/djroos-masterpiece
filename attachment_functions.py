# Functions for attachments

def rotate_right_attachment_motor(robot, speed, angle, waita=False):
    robot.right_attachment_motor.run_angle(speed, angle, wait=wait)

def rotate_left_attachment_motor(robot, speed, angle, waita=False):
    robot.left_attachment_motor.run_angle(speed, angle, wait=waita)

def rotate_both_attachment_motors(robot, speed, Langle, Rangle, waitA=False):
    robot.left_attachment_motor.run_angle(speed, Langle, wait=waitA)
    robot.right_attachment_motor.run_angle(speed, Rangle)


def reset_motors(robot, angle=0, speed=250):
    
    robot.right_attachment_motor.reset_angle(0)
    robot.left_attachment_motor.reset_angle(0)

    robot.right_attachment_motor.run_angle(speed, angle)
    robot.left_attachment_motor.run_angle(speed, angle) 
    
