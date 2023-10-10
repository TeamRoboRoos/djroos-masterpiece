# Function for driving and turning

def hold(left_motor, right_motor):
#    left_motor.brake()
#    right_motor.brake()
    left_motor.hold()
    right_motor.hold()

def drive_straight(robot, speed=500, kp=10):
    heading = robot.hub.imu.heading()
    steering = -heading * kp
    robot.drive_base.drive(speed, steering)

def move_distance(robot, distance, speed=500, kp=10):
    robot.drive_base.reset()
    robot.hub.imu.reset_heading(0)
    while robot.drive_base.distance() < distance:
        drive_straight(robot, speed, kp)

    # hold(robot.left_motor, robot.right_motor)
    robot.drive_base.stop()

def move_backwards_distance(robot, distance, speed=500, kp=10):
    robot.drive_base.reset()
    robot.hub.imu.reset_heading(0)
    while -robot.drive_base.distance() < distance:
        drive_straight(robot, -speed, kp)

    # hold(robot.left_motor, robot.right_motor)
    robot.drive_base.stop()

def move_until_black_line(robot, speed=350, kp=7):
    robot.left_sensor.lights.off()
    robot.right_sensor.lights.off()
    robot.drive_base.reset()

    while True:
        reflection1 = robot.left_sensor.reflection()
        reflection2 = robot.right_sensor.reflection()

        print(f"Sensor1 - {reflection1}")
        print(f"Sensor2 - {reflection2}")

        # Check if black line detected
        white_line_detected = reflection1 > 90 and reflection2 > 90
        black_line_detected = reflection1 < 16 and reflection2 < 15

        if white_line_detected:
            break
        else:
            drive_straight(robot, speed, kp)

        if black_line_detected:
            break
        else:
            drive_straight(robot, speed, kp)

    hold(robot.left_motor, robot.right_motor)

def sensor_1_move_until_black_line(robot, speed=500, kp=10):
    robot.left_sensor.lights.off()
    robot.right_sensor.lights.off()
    robot.drive_base.reset()

    while True:
        reflection = robot.right_sensor.reflection()

        print(f"Right sensor - {reflection}")

        # Check if black line detected
        black_line_detected = reflection < 15

        if black_line_detected:
            break
        else:
            drive_straight(robot, speed, kp)

    hold(robot.left_motor, robot.right_motor)

def reset_angle(left_motor, right_motor, angle=0):
    # Resets both motors degree count to 0
    left_motor.reset_angle(angle)
    right_motor.reset_angle(angle)

def turn_on_one_wheel(robot, angle, speed=150):
    robot.hub.imu.reset_heading(0)
    right_turn = angle > 0

    if right_turn:
        while robot.hub.imu.heading() < angle:
            robot.left_motor.run(speed)
    
    else:
        while robot.hub.imu.heading() > angle:
            robot.right_motor.run(speed)

    hold(robot.left_motor, robot.right_motor)

def turn(robot, angle, speed=100):
    # Reseting both the angle and the heading variable of the robot
    robot.hub.imu.reset_heading(0)
    right_turn = angle > 0

    # Checks if the robot should turn right or left
    if right_turn:
        while robot.hub.imu.heading() < angle:
            robot.right_motor.run(-speed)
            robot.left_motor.run(speed)
    else:
        while hub.imu.heading() > angle:
            robot.right_motor.run(speed)
            robot.left_motor.run(-speed)

    hold(robot.left_motor, robot.right_motor)