# Functions for attachments

def rotate_right_attachment_motor(robot, speed, angle):
    robot.right_attachment_motor.run_angle(speed, angle)

def rotate_left_attachment_motor(robot, speed, angle):
    robot.left_attachment_motor.run_angle(speed, angle)

def reset_motors(robot, angle):
    if robot.right_attachment_motor.angle() < 0:
        while robot.right_attachment_motor.angle() != angle: 
            print(f"ight motor: {robot.right_attachment_motor.angle()}, left motor angle: {robot.left_attachment_motor.angle()}")
            robot.right_attachment_motor.run(-100)
    elif robot.right_attachment_motor.angle() > 0:
        while robot.right_attachment_motor.angle() != angle:
            print(f"ight motor: {robot.right_attachment_motor.angle()}, left motor angle: {robot.left_attachment_motor.angle()}")
            robot.right_attachment_motor.run(100)
    if robot.left_attachment_motor.angle() < 0:
        while robot.left_attachment_motor.angle() != angle:
            print(f"ight motor: {robot.right_attachment_motor.angle()}, left motor angle: {robot.left_attachment_motor.angle()}")
            robot.left_attachment_motor.run(100)
    elif robot.left_attachment_motor.angle() > 0:
        while robot.left_attachment_motor.angle() != angle:
            print(f"ight motor: {robot.right_attachment_motor.angle()}, left motor angle: {robot.left_attachment_motor.angle()}")
            robot.left_attachment_motor.run(-100)
