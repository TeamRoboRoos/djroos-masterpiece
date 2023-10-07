# Function for driving and turning

def hold(left_motor, right_motor):
    left_motor.brake()
    right_motor.brake()
    left_motor.hold()
    right_motor.hold()

def move_distance(hub, drive_base, distance, speed=500, kp=10):
    drive_base.reset()
    while drive_base.distance() < distance:
        heading = hub.imu.heading()
        steering = -heading * kp
        drive_base.drive(speed, steering)

def reset_angle(left_motor, right_motor, angle=0):
    # Resets both motors degree count to 0
    left_motor.reset_angle(angle)
    right_motor.reset_angle(angle)

def turn(hub, left_motor, right_motor, angle, speed=100):
    # Reseting both the angle and the heading variable of the robot
    hub.imu.reset_heading(0)
    right_turn = angle > 0

    # Checks if the robot should turn right or left
    if right_turn:
        while hub.imu.heading() < angle:
            right_motor.run(-speed)
            left_motor.run(speed)
    else:
        while hub.imu.heading() > angle:
            right_motor.run(speed)
            left_motor.run(-speed)

    hold(left_motor, right_motor)