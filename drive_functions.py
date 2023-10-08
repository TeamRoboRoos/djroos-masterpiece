# Function for driving and turning

def hold(left_motor, right_motor):
    left_motor.brake()
    right_motor.brake()
    left_motor.hold()
    right_motor.hold()

def drive_straight(robot, speed=500, kp=10):
    heading = robot.hub.imu.heading()
    steering = -heading * kp
    robot.drive_base.drive(speed, steering)

def move_distance(robot, distance, speed=500, kp=10):
    robot.drive_base.reset()
    while robot.drive_base.distance() < distance:
        drive_straight(robot, speed, kp)

    hold(robot.left_motor, robot.right_motor)

def move_backwards_distance(robot, distance, speed=500, kp=10):
    robot.drive_base.reset()
    while -robot.drive_base.distance() < distance:
        drive_straight(robot, -speed, kp)

    hold(robot.left_motor, robot.right_motor)

def move_until_black_line(robot, speed=500, kp=10):
    robot.left_sensor.lights.off()
    robot.right_sensor.lights.off()
    robot.drive_base.reset()

    while True:
        reflection1 = robot.left_sensor.reflection()
        reflection2 = robot.right_sensor.reflection()

        print(f"Sensor1 - {reflection1}")
        print(f"Sensor2 - {reflection2}")

        # Check if black line detected
        black_line_detected = reflection1 < 16 and reflection2 < 15

        if black_line_detected:
            break
        else:
            drive_straight(robot, speed, kp)

    hold(robot.left_motor, robot.right_motor)

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